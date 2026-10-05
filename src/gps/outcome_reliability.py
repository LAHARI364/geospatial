"""PERSON 1, step 0: how close is each outcome's check-in to surveyed truth, and how far is the
check-in from the end of the GPS trail? Use this to SET the outcome weights from data."""
from src.data.loaders import load_all
from src.evaluation.metrics import dist

d = load_all()
v = d["field_visits"].merge(d["surveyed_addresses"], on="address_id")
v["checkin_err"] = dist(v.checkin_x, v.checkin_y, v.surveyed_x, v.surveyed_y)
last = d["visit_gps_points"].sort_values(["visit_id", "seq"]).groupby("visit_id").tail(1).set_index("visit_id")
v = v.join(last[["x", "y"]], on="visit_id")
v["checkin_to_trail_end"] = dist(v.checkin_x, v.checkin_y, v.x, v.y)
v["trail_end_err"] = dist(v.x, v.y, v.surveyed_x, v.surveyed_y)
print(v.groupby("outcome")[["checkin_err", "trail_end_err", "checkin_to_trail_end", "dwell_s"]]
        .agg(["count", "median"]).round(0).to_string())
