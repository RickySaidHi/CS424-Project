# CS 424 UIC Study Space Availability

## Task One

### Project Observation

For our project, we will observe study space availability in UIC’s Student Center East (SCE). Our collection will focus on seven areas identified on UIC’s website as designated study lounges: the first-floor Circle Lounge, Montgomery Lounge, Pier Room, East Terrace, West Terrace, Inner Circle, and the Commuter Center.

We will compare table and seat availability across these areas at different times and on different days. By recording factors such as weather and semester week, we also hope to explore conditions associated with changes in availability. Our goal is to understand when and where students are most likely to find an available place to study.

### Observation Definitions

One observation will represent one visit to a specific study area at a recorded date and time.

We will count only seats positioned at a table that provides space for studying. Standalone seats without an accompanying table and chairs with small attached folding tables will be excluded. These rules establish a consistent definition of a study seat across all seven areas.

For booth seating, we will use visible seat divisions or seams to determine capacity when those divisions represent individual seating spaces. For booths without clear divisions, we will establish and document a fixed seating capacity based on the space available. We will use that same capacity during subsequent visits to keep our counts consistent.

Tables with people or personal belongings will count as occupied. Each backpack on an otherwise unoccupied seat or at an unoccupied place at a table will count as one occupied seat. A backpack belonging to someone already counted will not add another occupied seat. These counts represent places that appear taken, rather than an exact count of people present.

Example images will illustrate which tables and seats are included or excluded from our observations.

### Collection Method

We will collect data through in-person visits to each study area, recording the total, occupied, and available tables and seats. Before repeated collection begins, we will establish baseline table and seating counts for each area using the definitions above.

Collection will take place at scheduled times throughout the week, covering morning, midday, afternoon, and evening periods. Repeated visits will allow us to compare availability across both locations and times rather than relying on a single snapshot.

We will divide collection approximately to the schedules below. Because visiting all seven areas takes time, we will record the actual observation time for each area rather than assign the scheduled start time to every observation. 

#### Ricky Ardisana Collection Times:

| Monday     | Tuesday    | Wednesday  | Thursday   | Friday     |
| ---------- | ---------- | ---------- | ---------- | ---------- |
| 8:30 AM    | 8:30 AM    | 8:30 AM    |            |            |
| 12:30 PM   | 12:30 PM   | 12:30 PM   | 12:30 PM   |            |
|            |            | 3:30 PM    |            |            |

#### Ramon Vazquez Collection Times:

| Monday    | Tuesday   | Wednesday | Thursday  | Friday    |
| --------- | --------- | --------- | --------- | --------- |
| 5:00 PM   |           | 6:00 PM   | 8:00 AM   | 8:00 AM   |
|           |           |           | 4:00 PM   | 1:00 PM   |
|           |           |           |           | 5:00 PM   |




### Collection Table

| Attribute          | Type          | Description                               | Example              |
| ------------------ | ------------- | ----------------------------------------  | -------------------- |
| `visit_id`         | Identifier    | Unique ID for each location visit         | `001`                |
| `location`         | Categorical   | Building and specific study area          | `Library, second-floor` |
| `date`             | Temporal      | Date of observation                       | `2026-09-24`         |
| `time`             | Temporal      | Time of observation                       | `14:35`              |
| `semester_week`    | Temporal      | Week within the 16-week semester          | `5`                  |
| `temperature`      | Quantitative  | Outdoor temperature in degrees Fahrenheit | `62`                 |
| `weather`          | Categorical   | Weather at the observation time           | `Rain`               |
| `total_chairs`     | Quantitative  | Total chairs in the area                  | `40`                 |
| `total_tables`     | Quantitative  | Total study tables in the area            | `10`                 |
| `occupied_chairs`  | Quantitative  | Chairs with people                        | `25`                 |
| `available_chairs` | Quantitative  | Total chairs minus occupied               | `15`                 |
| `occupied_tables`  | Quantitative  | Tables with people                        | `5`                  |
| `available_tables` | Quantitative  | Total tables minus occupied               | `5`                  |

## Task Two

## Task Three

## Task Four

## Task Five

## Task Six

## Task Seven
