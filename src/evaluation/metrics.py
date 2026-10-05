import numpy as np, pandas as pd
from src.data.loaders import load_all

def dist(x1, y1, x2, y2):
    return np.hypot(np.asarray(x1) - np.asarray(x2), np.asarray(y1) - np.asarray(y2))

def summarize(err, radius=None):
    err = np.asarray(err, float)
    out = {"n": len(err), "median": np.median(err), "p90": np.quantile(err, .9), "mean": err.mean(),
           "within_50": (err <= 50).mean(), "within_100": (err <= 100).mean(), "within_250": (err <= 250).mean()}
    if radius is not None:
        out["coverage"] = (err <= np.asarray(radius, float)).mean()  # should match the confidence level you claim
        out["mean_radius"] = float(np.mean(radius))
    return out

def evaluate(pred, data=None, by="split"):
    """pred: DataFrame[address_id, pred_x, pred_y, (radius_m)]. Scored on the 100 surveyed addresses only."""
    data = data or load_all()
    m = (data["surveyed_addresses"].merge(pred, on="address_id")
         .merge(data["addr_split"][["address_id", "split", "town_id"]], on="address_id"))
    m["err"] = dist(m.pred_x, m.pred_y, m.surveyed_x, m.surveyed_y)
    rad = "radius_m" in m
    rows = {k: summarize(g.err, g.radius_m if rad else None) for k, g in m.groupby(by)}
    rows["ALL"] = summarize(m.err, m.radius_m if rad else None)
    return pd.DataFrame(rows).T.round(3), m
