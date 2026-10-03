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

#### Jake Jimenez Collection Times:

| Monday             | Tuesday           | Wednesday          | Thursday          | Friday    |
| ------------------ | ----------------- | ------------------ | ----------------- | --------- |
| 10:00 – 11:00 AM   | 12:30 – 2:00 PM   | 10:00 – 11:00 AM   | 12:30 – 2:00 PM   |           |
| 12:30 – 1:00 PM    |                   | 12:30 – 2:00 PM    |                   |           |



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

After our team completed the pilot collection, we felt as though some attributes were easier to collect than others. For instance, the weather observation and total chairs and tables were able to be converted fairly quickly within our dataset by counting all the tables and chairs in each section once and checking the weather app. One aspect of our data collection that was more difficult was the number of tables used, as different students may either be sitting alone at one table or sitting in a group, which made us manually check each table at a given time to make sure that our data was accurate.

Different group members interpreted data differently because they went at different times throughout the day, which caused different results to appear for the weather and the number of tables used per location. There were no important attributes missing within any observation, as all locations were open throughout building hours, which allowed us to collect data seamlessly without any issues. One unnecessary aspect was our available chair count, as our chair occupancy rate already provided the ratio between the chairs used compared to the total number of chairs. The only reason we kept this there was due to Excel formatting for dividing the two rows together per column, but this was unnecessary. 

The pilot did change the types of questions we answered, as it made us focus more on how specific weather patterns and times of day fluctuate student activities, rather than simply just the day of the week. We also diverted from our original hypothesis of seeing if students would rather be in groups or by themselves throughout the day, as we felt as though it was too small of an idea to capture throughout many different study areas, and we were able to collect more unique data to provide a more genuine problem to solve.

During our pilot run, our team mainly focused on the morning time on Monday, September 28th. After our pilot run, we decided to run 3 separate times throughout the week for morning, midday, and afternoon. This made sure that we would be able to see the patterns between student activity more clearly. We also assigned each team member a specific time to make sure that schedules wouldn’t cause us to miss our collection sections. Lastly, we revised the process of data collection so each team member would write the time and location on the Google Sheet each time to avoid errors or missing data.
	
## Task Three

We collected 73 observations of study space availability between seven study lounges throughout the UIC Student Center East Building during week 6 of the semester. Each observation included the time of the observation, location, and the number of tables and chairs used compared with the total. We also captured temporal data regarding the time of day and weather conditions. Our spatial coverage includes the seven lounges, with 17 variables per observation, which are in Data_Collection.csv.

Our data collection revealed that chair occupancy rates differed by time of day and weather conditions. For instance, chair occupancy rates ranged from 3.13% to 77.78%, with morning times showing lower occupancy rates compared to midday periods, where they were almost full. Weather conditions also showed large discrepancies, with rain being at around 52% on average, sunny at 38%, and cloudy at 10%. Different locations, such as the west terrace, also had much lower occupancy rates during rain, even with cover, at 1.56% compared to 62.5% during sunny weather.

Some constraints we had were that our data only captured one week within this semester and not on weekends due to our team not being on campus. We also weren’t able to capture every location at the exact minute because we had to count the number of open chairs and tables, so our observations looked over a section of time rather than exactly on the hour.

For data collection, we focused on seats positioned at study tables and excluded seats and corner areas without tables. We also ignored data regarding student count, as students could also be entering a study lounge to talk with a friend or get food rather than studying, which would disrupt our data accuracy. 

One domain question our team would like to investigate is whether occupancy changes throughout the day. We chose this question because our data shows a consistent trend with morning observations lower than midday observations, ranging from 3.13% to 61.11%. Our second domain question is whether weather affects the occupancy of students in different types of spaces. This question works with our data because outdoor spaces such as the west terrace drop significantly in total chair use count from 62% in the sun to 1.56% in the rain. This could mean that the space itself is not protective against the rain, or that students just avoid outdoor spaces in general. Our third domain question would be whether there is a specific temperature boundary where more students study indoors. This is also a great question because our data collects weather from between 59℉ and 75℉, and other study areas can anticipate incoming students if our data predicts a sudden increase in table usage. Our fourth domain question is whether spaces are most open throughout the day depending on location. This question works within our dataset because we noticed that some locations, such as the Commuter Center, showed far greater usage compared to the inner circle, which shows that some areas are more popular for studying or possibly used differently compared to other study lounges, such as for events.

## Task Four

## Task Five

## Task Six

## Task Seven
