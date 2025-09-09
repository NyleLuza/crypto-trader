import kagglehub
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("sudalairajkumar/cryptocurrencypricehistory")

# initalize datasets
bit_dataset = pd.read_csv(f"{path}/coin_Bitcoin.csv")
eth_dataset = pd.read_csv(f"{path}/coin_Ethereum.csv")
ada_dataset = pd.read_csv(f"{path}/coin_Cardano.csv")
sol_dataset = pd.read_csv(f"{path}/coin_Solana.csv")
doge_dataset = pd.read_csv(f"{path}/coin_Dogecoin.csv")
print(doge_dataset.head())