### Processed Data

#### observations_clean.csv

This file has one row per visit. It has the same columns as `Updated_Dataset.csv`, with the available counts and percentages recalculated, plus these new columns:

| Column | Meaning |

| `chair_occupancy_pct` | Percent of chairs occupied |
| `table_occupancy_pct` | Percent of tables occupied |
| `location_label` | Lounge name |
| `space_type` | Indoor or outdoor |
| `session_id` | Which walk-through the visit belongs to (date / time) |
| `table_chair_gap` | Table percent minus chair percent |
| `people_per_table` | Average number of people at each occupied table |
| `has_open_table` | 1 if at least one table was open, 0 if not |

#### Summary Tables

| File | What it shows |

| `q1_by_time_of_day.csv` | Average occupancy for each lounge at each time of day (Question 1) |
| `q2_rain_vs_sun.csv` | Rainy vs. sunny visits at the same lounge, day, and time of day (Question 2) |
| `q4_by_location.csv` | Open seats, open tables, and people per table for each lounge (Question 4 and our new question) |
| `coverage.csv` | Number of visits for each day and time of day |