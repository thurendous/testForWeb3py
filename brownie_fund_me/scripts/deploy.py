from brownie import accounts, config, FundMe, MockV3Aggregator, network
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENT,BLOCKCHAIN_ENVIRONMENT
from web3 import Web3
from brownie.network import priority_fee




def deploy_fund_me():
    # network.connect("ganache-local2")
    account = get_account()
    # since here we are making a change to the blockchain we need this "from"

    # if we are on a persistent network like rinkeby, use the associated address
    # otherwise, deploy mocks
    # price_feed = config["networks"]["rinkeby"]["eth_usd_price_feed"]
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT or network.show_active() in BLOCKCHAIN_ENVIRONMENT:
        # priority_fee("1.15 gwei")
        print(f"The active netowork is {network.show_active()}")
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else: 
        print(f"The active network is {network.show_active()}")
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        
    fund_me = FundMe.deploy(price_feed_address, {"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"Contract deployed to {fund_me.address}")
    return fund_me




def main():
    deploy_fund_me()
