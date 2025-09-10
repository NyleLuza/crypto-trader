import kagglehub
import pandas as pd


def filter_cols(data):
    after_drop = data.drop(columns = ["SNo", "Symbol", "Name", "Date", "Open"], axis=1)
    filter = after_drop[after_drop["Volume"]!=0]
    dropped_index = filter.reset_index(drop=True)
    return dropped_index

def final_frame(data):
    data["Mean"] = data[["High", "Low", "Close"]].mean(axis=1) # calc mean across columns
    new_cols = data[["Mean", "High", "Low", "Close", "Volume", "Marketcap"]]
    return new_cols
    
# Download latest version
path = kagglehub.dataset_download("sudalairajkumar/cryptocurrencypricehistory")
# initalize datasets
bit_dataset = pd.read_csv(f"{path}/coin_Bitcoin.csv")
eth_dataset = pd.read_csv(f"{path}/coin_Ethereum.csv")
ada_dataset = pd.read_csv(f"{path}/coin_Cardano.csv")
sol_dataset = pd.read_csv(f"{path}/coin_Solana.csv")
doge_dataset = pd.read_csv(f"{path}/coin_Dogecoin.csv")



df = filter_cols(bit_dataset)
final_df = final_frame(df)
print(final_df.head(20))