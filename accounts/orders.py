import requests



class Shopify():
    
    def __init__(self, accessToken):
        self.headers = {
            'X-Shopify-Access-Token': accessToken.access_token,
        }
        self.shop = accessToken.shop_name
        print(self.shop)
    
    def all_orders(self):
        params = {
            'status': 'any',
        }
        response = requests.get(f'https://{self.shop}/admin/api/2021-10/orders.json', headers=self.headers, params=params)
        return response.json()