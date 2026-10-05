"""PERSON 1 owns this. Output: outputs/gps_features.csv, ONE ROW PER address_id."""
GPS_COLUMNS = ["address_id", "visit_count", "productive_visit_count", "weighted_visit_score",
               "cluster_x", "cluster_y", "cluster_radius", "cluster_density", "median_gps_accuracy",
               "number_of_clusters", "baseline_to_cluster_distance"]
# Suggested extras: integrity_flag_share, agent_integrity (down-weight fake/outlier agents)
# TODO: join visits+trail+addresses -> outcome weight x accuracy x dwell -> DBSCAN per address -> write CSV
