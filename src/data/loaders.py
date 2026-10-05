"""Shared loaders. Expects data in data/raw/shared and data/raw/ps3_geocoder.
All coordinates are LOCAL METRES (x, y) - distance is plain Euclidean."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "outputs"

def _r(folder, name, **kw):
    return pd.read_csv(RAW / folder / f"{name}.csv", **kw)

def load_all():
    d = {n: _r("shared", n) for n in ["accounts", "addresses", "field_visits", "splits", "agents"]}
    for n in ["towns", "localities", "landmarks_poi", "baseline_geocodes", "visit_gps_points", "surveyed_addresses"]:
        d[n] = _r("ps3_geocoder", n)
    # every address inherits its account's split
    d["addr_split"] = d["addresses"][["address_id", "account_id", "town_id"]].merge(d["splits"], on="account_id")
    return d

def check_contract(df, cols, name):
    missing = [c for c in cols if c not in df.columns]
    assert not missing, f"{name} is missing columns: {missing}"
    assert df["address_id"].is_unique, f"{name}: address_id must be unique (one row per address)"
    return df
