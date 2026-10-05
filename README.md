# CN PS3 - Address Geocoder That Learns from Field Visits
Run from repo root. Coordinates are local metres (x, y).

    pip install -r requirements.txt
    python -m src.evaluation.run_baseline        # baseline numbers
    python -m src.gps.outcome_reliability        # P1: outcome weights from data

Owners: P1 src/gps  |  P2 src/address  |  P3 src/model, src/evaluation, app
Contracts: outputs/gps_features.csv (P1), outputs/address_features.csv (P2), outputs/predictions.csv (P3)
Branches: person1/gps, person2/address, person3/model -> PR into main.
