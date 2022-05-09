import json
import requests

rpc_user = 'me'
rpc_pass = 'secret'

url = 'http://%s:%s@localhost:8332' % (rpc_user, rpc_pass)
headers = {'content-type': 'application/json'}

"""
For making the requests. 
"""


def makerequest(payload):
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    return response


"""
The method can only take one tx as input and send to one address as output. 
@return: hex string of the transaction
"""


def create(txid_input, output_nr, to_address, amount):
    payload = {
        "method": "createrawtransaction",
        "params": [[{"txid": txid_input, "vout": output_nr}],
                   [{to_address: amount}]]
    }
    response = makerequest(payload)
    return response['result']


"""
The second argument is an json array of base58-encoded private
keys that will be the only keys used to sign the transaction.
"""


def sign(tx_to_sign, privKey):
    payload = {
        "method": "signrawtransactionwithkey",
        "params": [tx_to_sign, privKey]
    }
    response = makerequest(payload)
    return response['result']['hex']


"""
Submits raw transaction (serialized, hex-encoded) to local node and network.
"""


def send(signedhex):
    payload = {
        "method": "sendrawtransaction",
        "params": [signedhex, 0]
    }
    response = makerequest(payload)
    return response['result']
