import requests
import environ


env = environ.Env()
environ.Env.read_env()

class SendRequest:
    def post_order(self, data):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': "Bearer " + env('STORE_TOKEN')

        }
        response = requests.post(f"{env('WAREHOUSE_URL')}/warehouse/api/create/order/", headers=headers, data=data)
        return response.status_code
