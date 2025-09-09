import kagglehub
import pandas as pd


def combined_set(df, data):
    for i in range(len(data)):
        after_drop = data[i].drop(columns = ["SNo"], axis=1)
        df = pd.concat([df, after_drop.head(n = after_drop.size)])
    print(df.shape)
    return df


# Download latest version
path = kagglehub.dataset_download("sudalairajkumar/cryptocurrencypricehistory")
# initalize datasets
bit_dataset = pd.read_csv(f"{path}/coin_Bitcoin.csv")
eth_dataset = pd.read_csv(f"{path}/coin_Ethereum.csv")
ada_dataset = pd.read_csv(f"{path}/coin_Cardano.csv")
sol_dataset = pd.read_csv(f"{path}/coin_Solana.csv")
doge_dataset = pd.read_csv(f"{path}/coin_Dogecoin.csv")
dataset_array = [bit_dataset, eth_dataset,
                 ada_dataset, sol_dataset, doge_dataset]
main_dataset = pd.DataFrame()

df = combined_set(main_dataset, dataset_array)
print(df.tail(5))