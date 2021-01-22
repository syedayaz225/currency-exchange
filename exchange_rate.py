import json
from datetime import datetime
import requests

class CurrencyConverter:
    base_url = 'http://api.currencylayer.com/live'

    def __init__(self, API_KEY):
        self.API_KEY = API_KEY

    def requestCurrency(self):
        params = {'access_key': self.API_KEY}
        response = requests.get(CurrencyConverter.base_url, params=params)
        response_json = json.loads(response.content)
        if response.status_code != 200:
            print('Failed to import currencies')
            print(response.reason)
            return None
        elif not response_json['success']:
            print('Failed to import currencies')
            print(response_json['error']['info'])
            return None
        else:
            timestamp = datetime.fromtimestamp(response_json['timestamp']).strftime('%m-%d-%Y')  
            base_currency = response_json['source']
            quotes = response_json['quotes']
            return {'base': base_currency, 'timestamp': timestamp, 'quotes': quotes}


c1 = CurrencyConverter('ffb05d85592ed51d1220fcb3aafff91e')
print(c1.requestCurrency())