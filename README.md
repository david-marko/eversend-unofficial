# eversend-unofficial
Unofficial SDK for Eversend Business Platform
# EverSend API
A tiny library to connect and use the Eversend Business API

### Installation
```
pip install eversend-api
```

### Get started
Sign up to Eversend and access your API keys from the Dashboard
https://business.eversend.co/signup

```Python
from eversend-sdk import Eversend

# Use your API Keys. Alternatively, you can set them up as environment variables.
client_id = '123qwe456rty789yui'
client_secret = '123qwe456rty789yui123qwe456rty789yui'
version = '1'

# Initiate Eversend Class
client = Eversend(clientId=client_id, clientSecret=client_secret, version=version)
```

### Account and Wallet Information
Get your account details and manage wallets
```Python

# Initiate Eversend Class
wallets = client.get_wallets()

# Get Single Wallet
wallet_id = ''
wallet = client.get_wallet(wallet_id)

# Activate a Wallet
cur_wallet = 'UGX' # UGX, USD, KES, NGN
print(client.activate_wallet(cur_wallet))

# Deactivate a Wallet
cur_wallet = 'UGX' # UGX, USD, KES, NGN
print(client.deactivate_wallet(cur_wallet))

# Get Account Profile
print(client.account_profile())
```

### Exchanges
Manage Currency Exchanges by creating quotations, checking fees and converting currencies
```Python

# Create a quotation
_from = 'USD'
amount = 1000
_to = 'UGX'
quote = client.create_quotation(_from, amount, _to)

# Exchange money in your wallet using the quotation ID
quote_id = ''
exchange = client.create_exchange(quote_id)
```

### Transactions
Get transactions information and statuses
```Python

# Fetch a single transaction
transactionID = ''
transaction = client.get_transaction(transactionId)

# Search Transactions
search = '' # Transaction ID
_range = 'day'
limit = 10
page = 1
_from = '2022-11-11'
_to = '2022-11-15'
_type = 'collection' # collection, exchange, payout
currency = 'UGX'
status = 'pending' # pending, successful, failed
quote = client.transactions(search, _range, limit, page, _from, _to, _type, currency, status)
```

### Collections
Collection endpoints for initiating transactions and managing OTP requests
```Python
import uuid

# Check collection Fees
method = 'momo' # momo, bank
currency = 'UGX'
amount = 50000
fees = client.collection_fees(method, currency, amount)

# Get Collection OTP
phone = '+256781234567'
otp_req = client.collection_otp(phone)

# Mobile Money Collection
phone = '256712345678' # International Format
amount = 1000
country = 'UG'
currency = 'UGX'
customer = {
    "email": "jdoe@gmail.com"
}
transactionRef = uuid.uuid4().hex
otp = {
    'pinId': '32466gdfsfsrey1535',
    'pin': '123456'
}
coll_req = client.mobile_money_collection(phone, amount, country, currency, customer, transactionRef, otp)
```

### Todo
Sections i will be adding in the coming weeks or months
- Beneficiary Management
- Payouts Management
- Support for Environment Variables for Authentication
- Parameter Validation for Better Error Handling