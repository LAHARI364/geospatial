"""PERSON 2 owns this. Output: outputs/address_features.csv, ONE ROW PER address_id."""
ADDR_COLUMNS = ["address_id", "town_match", "locality_match", "locality_score", "pincode_match",
                "landmark_match", "landmark_score", "landmark_x", "landmark_y", "baseline_x", "baseline_y",
                "baseline_quality", "normalized_address"]
# Suggested extras: group_key (town|locality|landmark|road) so one visit helps many accounts;
#                   remark_is_correction / remark_offset_lanes (parsed from field_visits.remark)
# TODO: normalize -> transliterate (unidecode) -> RapidFuzz vs localities & landmarks_poi -> write CSV
