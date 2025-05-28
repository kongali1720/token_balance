from web3 import Web3
import json

RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
TOKEN_ADDRESS = "0xYourERC20TokenAddress"

erc20_abi = json.loads('[{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"type":"function"}]')

def check_token_balance(wallet_address):
    web3 = Web3(Web3.HTTPProvider(RPC_URL))
    token_contract = web3.eth.contract(address=web3.toChecksumAddress(TOKEN_ADDRESS), abi=erc20_abi)
    balance = token_contract.functions.balanceOf(web3.toChecksumAddress(wallet_address)).call()
    decimals = token_contract.functions.decimals().call()
    return balance / (10 ** decimals)

if __name__ == "__main__":
    wallet = input("Masukkan alamat wallet: ")
    balance = check_token_balance(wallet)
    print(f"Saldo token di wallet {wallet}: {balance}")
