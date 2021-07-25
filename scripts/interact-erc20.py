from brownie import ERC20Basic, accounts, config, network
from scripts.helpful_scripts import get_account

def main():
    # account = accounts.add(config["wallets"]["from_key"])
    print(f"The active network is {network.show_active()}")
    account = get_account()

    erc20 = ERC20Basic[-1]
    tx = erc20.transfer('0x5fe94DCBd28C501051b16d1f5E62e1C6E82c7F6b', 1000, {'from': account})
    tx.wait(1)
    print(f"Number is {erc20.balanceOf('0x5fe94DCBd28C501051b16d1f5E62e1C6E82c7F6b')}")

