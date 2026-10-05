"""PERSON 3 owns this. Merge gps_features + address_features -> candidates -> LightGBM ranker."""
from src.data.loaders import OUT, check_contract
from src.gps.build_gps_features import GPS_COLUMNS
from src.address.build_address_features import ADDR_COLUMNS
# TODO: candidates A baseline, B GPS cluster, C locality centroid, D landmark, E 2nd cluster
