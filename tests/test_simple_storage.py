from brownie import accounts, simpleStorage


def test_depl_contract():
    # Arrange
    account = accounts[0]
    # Act
    depl_contract = simpleStorage.deploy({"from": account})
    starting_Value = depl_contract.retrieve()
    expected = 0

    # Assert
    assert expected == starting_Value


def test_update_contract():
    # Arrange
    account = accounts[0]
    depl_contract = simpleStorage.deploy({"from": account})

    # Act
    expected = 19
    depl_contract.store(expected, {"from": account})
    updated_value = depl_contract.retrieve()

    # Assert
    assert expected == updated_value
