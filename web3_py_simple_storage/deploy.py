from solcx import compile_standard, install_solc
import json
from web3 import Web3
import setting
import os
import binascii


# create a /.env file to loadenv
from dotenv import load_dotenv
load_dotenv() # load env file 

# get addresses from the setting.py
my_address = setting.my_address
private_key = setting.private_key

# write the info into the variable
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    # print(simple_storage_file)

install_solc("0.6.0")

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode"]},
            }
        },
    },
    solc_version="0.6.0",
)

# print(compiled_sol)
 
with open("compiled_code.json", "w") as file: 
    json.dump(compiled_sol, file)


# get bytecode 
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# print("ABIIII",abi)
print(my_address)

# connect to blockchain
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 1337


# create the contract in python 
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
print(SimpleStorage)


# get ehtereum nonce increases 1 by 1
nonce = w3.eth.getTransactionCount(setting.my_address)
print(nonce)

# build a transaction -> sign a transaction -> send a transaction
transaction = SimpleStorage.constructor().buildTransaction({"chainId": chain_id, "gasPrice": w3.eth.gas_price, "from": my_address, "nonce": nonce})

print(transaction)

signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
print(signed_txn)

private_key = os.getenv("PRIVATE_KEY")
private_key2 = os.getenv("SOME_OTHER_VAR")
print(private_key)
print(private_key2)

# send the signed transaction
print("deploying contracts")
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
print("deployed")

# use this to decode
print(binascii.b2a_hex(tx_hash).decode("utf-8"))
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# working with the contract
# contract Address and contract ABI
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
# call: simulate making the call and getting a return value -> call
# you can always call a function without worrying about any state change
# transaction: make a state change to the blockchain -> transact
# you can always make a transact to a function to attempt to make a state change
print(simple_storage.functions.retrieve().call())
print(simple_storage.functions.store(16).call())
print(simple_storage.functions.retrieve().call())
# calling is just a simulation so the 16 is not updated on blockchain 

# send a transaction to change the blockchain state 
# 1st, we build the transaction
# 2nd, we sign the transaction
# 3rd, we send the transaction and wait for it to finish
print("updating the state!")
store_transaction = simple_storage.functions.store(161).buildTransaction(
    {"chainId": chain_id, "from": my_address, "gasPrice":w3.eth.gas_price, "nonce": nonce+1 }
)
signed_store_txn = w3.eth.account.sign_transaction(store_transaction, private_key=private_key)
tx_hash = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
print("updated the state!")


print(simple_storage.functions.retrieve().call())

