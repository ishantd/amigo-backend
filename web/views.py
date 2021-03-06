from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import uuid
import requests

from accounts.models import ShopifyAccessToken
from accounts.orders import Shopify

def index(request):
    
    return render(request, 'web/index.html')

@login_required(login_url='/login/')
def dashboard(request):
    shop_name = request.GET.get('shop_name', False)
    context = {}
    if shop_name:
        nonce = str(uuid.uuid4())
        context['login_url'] = f'https://{shop_name}.myshopify.com/admin/oauth/authorize?client_id={settings.SHOPIFY_API_KEY}&scope={settings.SHOPIFY_API_SCOPES}&redirect_uri={settings.SHOPIFY_REDIRECT_URI}&state={nonce}'
    return render(request, 'web/dashboard.html', context)

@login_required(login_url='/login/')
def shopify_callback(request):
    authorization_code = request.GET.get('code', False)
    hmac = request.GET.get('hmac', False)
    host = request.GET.get('host', False)
    shop = request.GET.get('shop', False)
    state = request.GET.get('state', False)
    timestamp = request.GET.get('timestamp', False)
    print(request.GET) 
    access_token_url = 'https://{shop}/admin/oauth/access_token'.format(shop=shop)
    print(access_token_url)
    data = {
        "client_id": settings.SHOPIFY_API_KEY,
        "client_secret": settings.SHOPIFY_API_SECRET_KEY,
        "code": authorization_code,
    }
    
    resp = requests.post(access_token_url, data=data)
    resp_data = resp.json()
    print(resp_data)
    
    at = ShopifyAccessToken.objects.create(user=request.user, access_token=resp_data['access_token'], shop_name=shop, connection='Shopify', scope=resp_data['scope'])
        
    
    
    return render(request, 'web/shopify_callback.html')

def shopify_orders(request):
    user = request.user
    shopify_token = ShopifyAccessToken.objects.filter(user=user).first()
    s = Shopify(shopify_token)
    data = s.all_orders()
    print(data)
    return render(request, 'web/shopify_orders.html')