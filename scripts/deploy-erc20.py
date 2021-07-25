from brownie import ERC20Basic, config, accounts, network
from scripts.helpful_scripts import get_account

def deployContract():
    # account = accounts.add(config["wallets"]["from_key"])
    print(f"The active network is {network.show_active()}")
    account = get_account()
    ERC20Basic.deploy(1000000,{'from': account})

def main():
    deployContract()