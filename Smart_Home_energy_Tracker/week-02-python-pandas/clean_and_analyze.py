import os
import pandas as pd
import numpy as np

def run_pipeline(file_path: str):
    print("=" * 60)
    print("SMART HOME ENERGY DATA PROCESSING PIPELINE")
    print("=" * 60)

    # 1. Load Data
    df = pd.read_csv(file_path)
    initial_count = len(df)
    print(f"[1] Raw data loaded: {initial_count} records")

    # 2. Type Casting & Datetime Normalization
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df['energy_kwh'] = pd.to_numeric(df['energy_kwh'], errors='coerce')

    # 3. Clean Corrupt/Missing Data
    # Drop records with bad timestamp or missing IDs
    df = df.dropna(subset=['timestamp', 'device_id', 'room_id']).copy()

    # Drop negative energy readings (sensor errors)
    df = df[df['energy_kwh'].isna() | (df['energy_kwh'] >= 0)]

    # Impute missing energy_kwh with device-level median
    df['energy_kwh'] = df.groupby('device_id')['energy_kwh'].transform(
        lambda grp: grp.fillna(grp.median() if not np.isnan(grp.median()) else 0.0)
    )

    print(f"[2] Data cleaned: {len(df)} records retained ({initial_count - len(df)} discarded)")

    # 4. NumPy Vectorized Metric Calculations (Device Level)
    print("\n[3] Calculating Device Statistics via NumPy...")
    device_records = []
    for dev_id, group in df.groupby('device_id'):
        values = group['energy_kwh'].to_numpy(dtype=np.float64)
        device_records.append({
            'device_id': dev_id,
            'total_kwh': np.round(np.sum(values), 4),
            'avg_kwh': np.round(np.mean(values), 4),
            'std_kwh': np.round(np.std(values), 4),
            'peak_kwh': np.round(np.max(values), 4)
        })

    device_summary_df = pd.DataFrame(device_records)

    # 5. Pandas Room-Level Aggregation
    print("[4] Generating Room-Level Summaries via Pandas...")
    room_summary_df = (
        df.groupby(['room_id', 'room_name'])
        .agg(
            total_room_kwh=('energy_kwh', 'sum'),
            avg_reading_kwh=('energy_kwh', 'mean'),
            reading_count=('energy_kwh', 'count')
        )
        .reset_index()
        .sort_values(by='total_room_kwh', ascending=False)
    )

    return df, device_summary_df, room_summary_df

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(base_dir, '..', 'data', 'energy_usage.csv')

    cleaned_df, dev_summary, rm_summary = run_pipeline(csv_file)

    print("\n" + "-" * 50)
    print("DEVICE-LEVEL SUMMARY (NumPy Aggregations)")
    print("-" * 50)
    print(dev_summary.to_string(index=False))

    print("\n" + "-" * 50)
    print("ROOM-LEVEL SUMMARY (Pandas Aggregations)")
    print("-" * 50)
    print(rm_summary.to_string(index=False))