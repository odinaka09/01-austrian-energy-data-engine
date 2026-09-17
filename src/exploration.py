import pandas as pd
from pathlib import Path



# -------------------------
# 1. Load data
# -------------------------

root_dir = Path(__file__).parent.parent

print(root_dir)
print(root_dir / "data" / "raw" / "time_series_60min_singleindex.csv")


df = pd.read_csv(root_dir / "data" / "raw" / "time_series_60min_singleindex.csv")


# -------------------------
# 2. Basic inspection
# -------------------------

print("Shape:", df.shape)
print("Columns:", df.columns)
print("Data types:", df.dtypes)
# print()


# -------------------------
# 3. Austrian columns
# -------------------------

austrian_columns = [
   f for f in df.columns if f.startswith("AT_")
]

print("\nAustrian columns:")
print(len(austrian_columns))


# -------------------------
# 4. Missing values
# -------------------------

austrian_data = df[austrian_columns]
data_sum = austrian_data.isna().sum()
missing_percentage = data_sum/len(df) * 100

print("\nMissing values (%):")
print(missing_percentage.round(2))


# -------------------------
# 5. Timestamp analysis
# -------------------------

timestamps = df["utc_timestamp"]
timestamps =  pd.to_datetime(timestamps)

print("\nEarliest timestamp:",timestamps.min())
print("Latest timestamp:", timestamps.max())


# -------------------------
# 6. Load analysis
# -------------------------

load = df["AT_load_actual_entsoe_transparency"]

print("\nElectricity load statistics:")
print(load.describe())

## 17-09
#find timestamp of missing load value

missing_load_val = load.isna()
missing_load_val_timestamp = df.loc[missing_load_val, "utc_timestamp"]
print(missing_load_val_timestamp)

#price split date
price = df["AT_price_day_ahead"].notna()
price_timestamp = df.loc[price, "utc_timestamp"].min()
print("Price data starts at :", price_timestamp)

# Inspect the 664MW drop
min_load_idx = load.idxmin()
five_hr_win = df.iloc[min_load_idx - 2 : min_load_idx + 3][["utc_timestamp", "AT_load_actual_entsoe_transparency"]]
print("Window around 664 MW drop: \n", five_hr_win)

#get prices
# 1. Check when price reporting ends
print("Last valid price timestamp:", df.loc[price, "utc_timestamp"].max())

# 2. Check missing price percentage by year
df["year"] = pd.to_datetime(df["utc_timestamp"]).dt.year
print("\nMissing price % by year:\n", df.groupby("year")["AT_price_day_ahead"].apply(lambda s: s.isna().mean() * 100).round(2))