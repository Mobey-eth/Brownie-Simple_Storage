from brownie import simpleStorage, config, accounts


def read_contract():
    # simpleStorage is an array of addresses print(simpleStorage[0])
    # arr[-1] to get latest item
    simple_storage = simpleStorage[-1]
    # To work with SC , I need ABI, ADDRESS.
    print(simple_storage.retrieve())


def main():
    read_contract()
