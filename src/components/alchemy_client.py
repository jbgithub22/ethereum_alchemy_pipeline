from web3 import Web3

def get_alchemy_client(api_key: str) -> Web3:
    alchemy_url = f"https://eth-mainnet.alchemyapi.io/v2/{api_key}"
    return Web3(Web3.HTTPProvider(alchemy_url))