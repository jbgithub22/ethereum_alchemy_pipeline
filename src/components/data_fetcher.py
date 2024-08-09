from web3 import Web3
import pandas as pd

def fetch_block_data(web3: Web3, block_number: int) -> dict:
    block = web3.eth.getBlock(block_number)
    return {
        "blockNumber": block.number,
        "timestamp": block.timestamp,
        "transactions": len(block.transactions),
        "miner": block.miner,
    }

def fetch_data(web3: Web3, start_block: int, end_block: int) -> pd.DataFrame:
    data = []
    for block_number in range(start_block, end_block + 1):
        block_data = fetch_block_data(web3, block_number)
        data.append(block_data)
    return pd.DataFrame(data)