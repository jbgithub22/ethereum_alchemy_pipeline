# https://chatgpt.com/c/a893b474-5787-4509-9b4d-07aac9cf4f88

import os
from ethereum_alchemy_csv import get_alchemy_client, fetch_data, write_to_csv

def main():
    api_key = os.getenv("ALCHEMY_API_KEY")
    if not api_key:
        raise ValueError("Please set the ALCHEMY_API_KEY environment variable.")
    
    web3 = get_alchemy_client(api_key)
    start_block = 14000000
    end_block = 14000010
    
    data = fetch_data(web3, start_block, end_block)
    write_to_csv(data, "block_data.csv")

if __name__ == "__main__":
    main()