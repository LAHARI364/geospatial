"""python -m src.evaluation.run_baseline  ->  the number every model must beat."""
from src.data.loaders import load_all
from src.evaluation.metrics import evaluate

d = load_all()
pred = d["baseline_geocodes"].rename(columns={"geocoder_x": "pred_x", "geocoder_y": "pred_y"})
table, m = evaluate(pred, d)
print(table.to_string())
print("\nBy baseline precision:")
print(m.groupby("precision").err.agg(["count", "median"]).round(1))
