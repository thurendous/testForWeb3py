# import accounts to manage accounts
from brownie import accounts, config, SimpleStorage, network
import os


def deploy_simple_storage():
    # ---get original account from ganache-cli
    # account = accounts[0]
    # ---get account from the brownie encrypted account
    # account = accounts.load("freecodecamp-account")
    # ---get account from .env
    account = get_account()
    print(account)
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    if stored_value == 0:
        transaction = simple_storage.store(155, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)
    print(network.gas_price())


def get_account():
    if(network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

# brownie do the sutff behind the scene
# 1. compile the contract
# 2. dump the file into a fiel
# 3. get the bytecode and abi for us
# 4. add a local blockchain for us
# * we need to add our private key and address


def main():
    deploy_simple_storage()