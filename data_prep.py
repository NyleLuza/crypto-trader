import kagglehub
import pandas as pd


def combined_set(df, data):
    for i in range(len(data)):
        after_drop = data[i].drop(columns = ["SNo", "Symbol"], axis=1)
        filter = after_drop[after_drop["Volume"]!=0]
        print(filter)
        df = pd.concat([df, after_drop.head(n = after_drop.size)])
    #print(df.shape)
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
pd.set_option("display.max_columns", 9)
#print(df.head())