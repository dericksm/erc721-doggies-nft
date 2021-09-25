from brownie import AdvancedCollectible, accounts, network, config, interface

OPENSEA_FORMAT = "https://testnets.opensea.io/assets/{}/{}"

def fund_advanced_collectible(nft_contract):
    dev = accounts.add(config['wallets']['from_key'])
    print(dev.balance())
    link_token = interface.LinkTokenInterface(
        config['networks'][network.show_active()]['link_token']
    )
    link_token.transfer(nft_contract, 0.1*10**18, {"from": dev})

def get_breed(breed_number):
    switch = {0: 'PUG', 1: "SHINA_INU", 2: 'ST_BERNARD'}
    return switch[breed_number]