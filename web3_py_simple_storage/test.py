from solcx import compile_standard, install_solc
import json
from web3 import Web3
import setting
import os
import binascii
import time 


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


w3 = Web3(Web3.HTTPProvider(setting.URL))
chain_id = 4


newestBlock = w3.eth.get_block_number()
print(newestBlock)
newestBlock2 = w3.eth.block_number
print(newestBlock2)

while True: 
    print(w3.eth.gas_price)
    time.sleep(2)

