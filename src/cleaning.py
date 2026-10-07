import pandas as pd
from pathlib import Path

def load_raw_data():
    
    root_dir = Path(__file__).parent.parent

    df = pd.read_csv(root_dir / "data" / "raw" / "time_series_60min_singleindex.csv")
    print(df.head())
    target_cols = [f for f in df.columns if f.startswith(("AT_", "utc"))]
    return df[target_cols]

def clean_column_names(df):
    mapping_dict = {
        "utc_timestamp": "timestamp_utc",
        "AT_load_actual_entsoe_transparency":"actual_load_mw",
        "AT_load_forecast_entsoe_transparency": "forecast_load_mw",
        "AT_price_day_ahead": "day_ahead_price_eur",
        "AT_solar_generation_actual":"solar_actual_mw",
        "AT_wind_onshore_generation_actual": "wind_actual_mw"
    }
    return df.rename(columns=mapping_dict)


def process_timestamps(df):
    df["timestamp_utc"] = pd.to_datetime(df["timestamp_utc"], utc=True)

    df = df.iloc[1:].reset_index(drop=True)
    return df

if __name__ == "__main__":
    df_raw = load_raw_data()
    print("Loaded shape:", df_raw.shape)
    
    df_clean = clean_column_names(df_raw)
    print("Cleaned columns:\n", df_clean.columns.tolist())

    df_timestamps = process_timestamps(df_clean)
    print("new shape: ", df_timestamps.shape)