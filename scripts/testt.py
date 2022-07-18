from brownie import accounts, network


def deploy_simple_storage():
    account = accounts[0]
    netwerk = network.show_active()
    print(account)
    print(netwerk)


def main():
    deploy_simple_storage()
