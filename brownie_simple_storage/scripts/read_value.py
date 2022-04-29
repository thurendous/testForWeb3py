from brownie import SimpleStorage, accounts, config

def read_contract():
    # print(len(SimpleStorage))
    for i in SimpleStorage:
        print(i.retrieve())
        # simple_storage = SimpleStorage[-1] 
    # this make sure you always work with most recent deployment
    # go take the index thats one less than the length
    # brownie already knows ABI, so no need to deploy
    # address
        # print(simple_storage.retrieve())


def main():
    read_contract()


