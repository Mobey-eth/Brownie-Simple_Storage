from brownie import accounts, config, simpleStorage, network


def get_account():
    # account = accounts[0]
    # account = accounts.load("garou")
    # account = accounts.add(os.getenv("private_key"))
    # account = accounts.add(config["wallets"]["from_key"])
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_simple_storage():

    account = get_account()
    # Brownie's smart enough to know if its a transact or a call
    simple_storage = simpleStorage.deploy({"from": account})

    # To make a call to the function in SC
    stored_value = simple_storage.retrieve()
    print(stored_value)

    # To make a state change and store numbr on chain
    transaction = simple_storage.store(19, {"from": account})
    transaction.wait(1)

    # To view our change
    print(simple_storage.retrieve())


def main():
    deploy_simple_storage()
