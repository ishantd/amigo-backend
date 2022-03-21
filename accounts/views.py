from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.http.response import JsonResponse
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from accounts.models import ShopifyAccessToken
from accounts.orders import Shopify

import os

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = os.environ.get('GOOGLE_CALLBACK_URL')
    client_class = OAuth2Client
    
class GetAllOrder(APIView):
    permission_classes = [AllowAny]
    def get(self ,request, *args, **kwargs):
        
        email = request.query_params.get('email', False)
        if not email:
            return JsonResponse({'error': 'email is required'}, status=400)
        
        user = User.objects.get(email=email)
        access_token = ShopifyAccessToken.objects.filter(user=user).first()
        s = Shopify(access_token)
        return JsonResponse(s.all_orders(), status=200)