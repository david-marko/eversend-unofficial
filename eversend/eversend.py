import requests

class Eversend:
    def __init__(self, clientId, clientSecret):
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.base_url = 'https://api.eversend.com/v1'
        self.token = None
        self.headers = {
            'clientId': self.clientId,
            'clientSecret': self.clientSecret
        }
        self.get_token()
        if self.token:
            self.token_header = {
                'Bearer '+self.token
            }

    def get_token(self):
        r = requests.get(self.base_url, headers=self.headers)
        resp = r.json()
        if resp['status'] == 200:
            self.token = resp['token']

    def get_wallets(self):
        url = self.base_url + '/wallets'
        r = requests.get(url, headers=self.token_header)
        return r.json()

    def get_wallet(self, walletId):
        url = self.base_url + '/wallets?walledId='+walletId
        r = requests.get(url, headers=self.token_header)
        return r.json()

    def activate_wallet(self, wallet):
        url = self.base_url + '/wallets/activate'
        payload = {
            'wallet': wallet
        }
        r = requests.post(url, json=payload, headers=self.token_header)
        return r.json()

    def activate_wallet(self, wallet):
        url = self.base_url + '/wallets/deactivate'
        payload = {
            'wallet': wallet
        }
        r = requests.post(url, json=payload, headers=self.token_header)
        return r.json()

    def account_profile(self):
        url = self.base_url + "/account"
        r = requests.get(url, headers=self.token_header)
        return r.json()

    def create_quotation(self, _from, amount, _to):
        url = self.base_url + '/exchanges/quotation'
        payload = {
            'from': _from,
            'Amount': amount,
            'To': _to
        }
        r = requests.post(url, json=payload, headers=self.token_header)
        return r.json()

    def create_exchange(self, quote_token):
        url = self.base_url + '/exchanges'
        payload = {
            'token': quote_token
        }
        r = requests.post(url, json=payload, headers=self.token_header)
        return r.json()

    def get_transaction(self, transactionId):
        url = self.base_url + "/transactions?transactionId="+transactionId
        r = requests.get(url, headers=self.token_header)
        return r.json()
    
    def transactions(self, search,range,limit, page, _from, _to, _type, currency, status):
        url = self.base_url + "/transactions"
        parameters = {
            'search': search,
            'range': range,
            'limit': limit,
            'page': page,
            'from': _from,
            'to': _to,
            'type': _type,
            'currency': currency,
            'status': status
        }
        r = requests.get(url, params=parameters, headers=self.token_header)
        return r.json()

    def collection_fees(self, method, currency, amount):
        url = self.base_url + "/collection/fees"
        payload = {
            "method": method,
            "currency": currency,
            "amount": amount
        }
        r = requests.post(url, json=payload, headers=self.token_header)
        return r.json()

    def collection_otp(self, phone):
        url = self.base_url + "/collection/otp"
        payload = {
            "phone": phone
        }
        r = requests.post(url, json=payload, headers=self.token_header)
        return r.json()

    def mobile_money_collection(self, phone, amount, country, currency, transactionRef, customer=None, otp=None):
        url = self.base_url + "/collection/momo"
        payload = {
            "phone": phone,
            "amount": amount,
            "country": country,
            "currency": currency,
            "transactionRef": transactionRef,
            "customer": customer,
            "otp": otp
        }
        r = requests.post(url, json=payload, headers=self.token_header)
        return r.json()

    