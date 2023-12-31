import requests
import environ


env = environ.Env()


class SendRequest:
    def put_order(self, data):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': "Token " + env('WAREHOUSE_TOKEN')

        }
        response = requests.put(f"{env('STORE_URL')}/store/api/update/order/", headers=headers, data=data)
        return response.status_code
