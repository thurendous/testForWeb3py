
from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

DECIMALS = 18
STARTING_PRICE = 3000


def get_account():
    if(network.show_active() == "development"):
        return accounts[0]
    if(network.show_active() == "rinkeby"):
        return accounts.add(config["wallets"]["from_key"])
    if(network.show_active() == "ganache-local"):
        return accounts.add(config["wallets"]["from_local_key"])
    

def deploy_mocks():
    print("Deploy Mocks.....")
    if len(MockV3Aggregator) <= 0:
            MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()})
    print("Mocks deployed! Here we go!")

