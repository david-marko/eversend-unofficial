import requests

class Eversend:
    def __init__(self, clientId, clientSecret, version):
        """"
        Initialize Eversend Class by providing the ClientID and ClientSecret from your Business Account Settings
        """
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.version = version
        self.base_url = 'https://api.eversend.com/v'+self.version
        self.token = None
        self.headers = {
            'clientId': self.clientId,
            'clientSecret': self.clientSecret
        }
        self.get_token()
        if self.token:
            self.token_header = {
                "Authorization": 'Bearer '+self.token
            }

    def get_token(self):
        r = requests.get(self.base_url, headers=self.headers)
        resp = r.json()
        if resp['status'] == 200:
            self.token = resp['token']

    def get_wallets(self):
        """
        Get All available Wallets 
        """
        url = self.base_url + '/wallets'
        r = requests.get(url, headers=self.token_header)
        return r.json()

    def get_wallet(self, walletId):
        """
        Get a specifi Wallet using WalletID or Currency
        """
        url = self.base_url + '/wallets?walledId='+walletId
        r = requests.get(url, headers=self.token_header)
        return r.json()

    def activate_wallet(self, wallet):
        """
        Activate a specific wallet by the currency
        :param wallet: UGX, KES, USD, NGN
        """
        url = self.base_url + '/wallets/activate'
        payload = {
            'wallet': wallet
        }
        r = requests.post(url, json=payload, headers=self.token_header)
        return r.json()

    def deactivate_wallet(self, wallet):
        """
        Deactivate a specific wallet by the currency
        :param wallet: UGX, KES, USD, NGN
        """
        url = self.base_url + '/wallets/deactivate'
        payload = {
            'wallet': wallet
        }
        r = requests.post(url, json=payload, headers=self.token_header)
        return r.json()

    def account_profile(self):
        """
        Get your complete account profile
        """
        url = self.base_url + "/account"
        r = requests.get(url, headers=self.token_header)
        return r.json()

    def create_quotation(self, _from, amount, _to):
        """
        Activate a quotation for currency conversion
        :param _from: UGX, KES, USD, NGN
        :param amount: Amount as a float
        :param _to: UGX, KES, NGN, USD
        """
        url = self.base_url + '/exchanges/quotation'
        payload = {
            'from': _from,
            'Amount': amount,
            'To': _to
        }
        r = requests.post(url, json=payload, headers=self.token_header)
        return r.json()

    def create_exchange(self, quote_token):
        """
        Exchange 
        :param quote_token: Quotation reference to make a currency exchange
        """
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
        """
        View All Transactions
        :param search: Transaction ID or detail
        :param range: Options are day, week, month, year
        :param limit: Number of items returned, Integer Starts from 1 Default value is 10
        :param page: Number of Pages, Integer Default value is 1
        :param _from: String Date as YYYY-MM-dd
        :param _to: String Date as YYYY-MM-dd
        :param _type: Options are payout, exchange, collection
        :param currency: Options are UGX, USD, NGN, GHS, KES ...
        :param status: Options are pending, successful, failed
        """
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
        """
        Check collection fees
        :param method: Options are momo, bank
        :param currency: Options are UGX, KES, NGN, USD, GHS ..
        :param amount: Amount as a number
        """
        url = self.base_url + "/collection/fees"
        payload = {
            "method": method,
            "currency": currency,
            "amount": amount
        }
        r = requests.post(url, json=payload, headers=self.token_header)
        return r.json()

    def collection_otp(self, phone):
        """
        Send an OTP before collection
        :param phone: phone number in internation format
        """
        url = self.base_url + "/collection/otp"
        payload = {
            "phone": phone
        }
        r = requests.post(url, json=payload, headers=self.token_header)
        return r.json()

    def mobile_money_collection(self, phone, amount, country, currency, transactionRef, customer=None, otp=None):
        """
        Initiate Mobile Money Collection Request
        :param phone: Phone Number in international format
        :param amount: Amount as a number
        :param country: Options are UG, KE, GH, RW
        :param currency: Options are UGX, KES, GHS, RWF
        :param customer: JSON Object for customer information e.g. '{"email":"john@example.com"}'
        :param transactionRef: Unique alphanumeric string set by the client
        :param otp: A JSON object with pinId from Get Collection OTP and pin from customer e.g {"pinId":"132466gdfsfsrey1535", "pin":"123456"}
        """
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

    