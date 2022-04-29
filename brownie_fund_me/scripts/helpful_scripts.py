
from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENT = ["ganache-local","development"]
BLOCKCHAIN_ENVIRONMENT = ["mainnet-fork-dev"]

DECIMALS = 8
STARTING_PRICE = 3000000000000


def get_account():
    # for i in accounts:
    #     print(i)
    if(network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT or network.show_active() in BLOCKCHAIN_ENVIRONMENT):
        print(f"yes this is {network.show_active()}")
        return accounts[0]
    if(network.show_active() == "rinkeby"):
        return accounts.add(config["wallets"]["from_key"])
    if(network.show_active() == "ganache-local"):
        return accounts.add(config["wallets"]["from_local_key"])


def deploy_mocks():
    print("Deploy Mocks.....")
    if len(MockV3Aggregator) <= 0:
            MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mocks deployed! Here we go!")

