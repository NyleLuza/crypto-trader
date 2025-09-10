import kagglehub
import pandas as pd


def combined_set(data):
    after_drop = data.drop(columns = ["SNo", "Symbol", "Name", "Date"], axis=1)
    filter = after_drop[after_drop["Volume"]!=0]
    dropped_index = filter.reset_index(drop=True)
    return dropped_index


# Download latest version
path = kagglehub.dataset_download("sudalairajkumar/cryptocurrencypricehistory")
# initalize datasets
bit_dataset = pd.read_csv(f"{path}/coin_Bitcoin.csv")
eth_dataset = pd.read_csv(f"{path}/coin_Ethereum.csv")
ada_dataset = pd.read_csv(f"{path}/coin_Cardano.csv")
sol_dataset = pd.read_csv(f"{path}/coin_Solana.csv")
doge_dataset = pd.read_csv(f"{path}/coin_Dogecoin.csv")



df = combined_set(bit_dataset)

print(df.head())