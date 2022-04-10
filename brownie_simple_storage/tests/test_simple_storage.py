from brownie import accounts, SimpleStorage

def test_deploy():
    # arrange 
    account = accounts[0]
    # act 
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # assert
    assert starting_value == expected

def test_update_storage():
    # arrange 
    account = accounts[0]
    # act 
    simple_storage = SimpleStorage.deploy({"from": account})
    transaction = simple_storage.store(15, {"from": account})
    print(transaction)
    starting_value = simple_storage.retrieve()
    expected = 15
    # assert
    assert starting_value == expected




