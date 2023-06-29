import requests
import environ


env = environ.Env()


class SendRequest:
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Authorization': "Token " + env('STORE_TOKEN')

    }

    def post_order(self, data):
        response = requests.post(f"{env('WAREHOUSE_URL')}/warehouse/api/create/order/", headers=self.headers, data=data)
        return response.status_code

    def put_order(self, data):
        response = requests.put(f"{env('WAREHOUSE_URL')}/warehouse/api/update/order/", headers=self.headers, data=data)
        return response.status_code
