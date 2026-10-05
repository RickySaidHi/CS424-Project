# CS 424 UIC Study Space Availability

## Task One

### Project Observation

For our project, we will observe study space availability in UIC’s Student Center East (SCE). Our collection will focus on seven areas identified on UIC’s website as designated study lounges: the first-floor Circle Lounge, Montgomery Lounge, Pier Room, East Terrace, West Terrace, Inner Circle, and the Commuter Center.

Our initial domain question is: How does study-space availability vary across the seven lounges in Student Center East? To find this out we will compare table and seat availability across these areas at different times and on different days. By recording factors such as weather and semester week, we also hope to explore conditions associated with changes in availability. Our goal is to understand when and where students are most likely to find an available place to study.

### Observation Definitions

One observation will represent one visit to a specific study area at a recorded date and time.

We will count only seats positioned at a table that provides space for studying. Standalone seats without an accompanying table and chairs with small attached folding tables will be excluded. These rules establish a consistent definition of a study seat across all seven areas.

For booth seating, we will use visible seat divisions or seams to determine capacity when those divisions represent individual seating spaces. For booths without clear divisions, we will establish and document a fixed seating capacity based on the space available. We will use that same capacity during subsequent visits to keep our counts consistent.

Tables with people or personal belongings will count as occupied. Each backpack on an otherwise unoccupied seat or at an unoccupied place at a table will count as one occupied seat. A backpack belonging to someone already counted will not add another occupied seat. These counts represent places that appear taken, rather than an exact count of people present.

### Initial Domain Questions

We started with these five domain questions before collecting any data, with Task 3 describing how they changed specifically.

1. Which SCE study lounges are most likely to have open seats, and which are usually full?

2. Does seat availability change throughout the week?

3. Do students study alone or in groups, and does that change over the day?

4. Does weather affect how many students use the study lounges?

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

### Sample Collection Table

| Attribute          | Type          | Description                               | Example              |
| ------------------ | ------------- | ----------------------------------------  | -------------------- |
| `visit_id`         | Identifier    | Unique ID for each location visit         | `001`                |
| `location`         | Categorical   | Building and specific study area          | `West Terrace` |
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

### Final Revised Data Dictionary

| Attribute | Type | Description | Example |
| --- | --- | --- | --- |
| `visit_id` | Identifier | Unique ID for each location visit | `7` |
| `location` | Categorical | Study area observed | `commuter_center` |
| `date` | Temporal | Date of observation | `9/28/2026` |
| `day` | Categorical | Day of the week | `Monday` |
| `time` | Temporal | Recorded local observation time | `17:20` |
| `time_of_day` | Ordinal | Observation period: Morning, Midday, or Afternoon | `Afternoon` |
| `semester_week` | Ordinal | Week within the 16-week semester | `6` |
| `temperature` | Quantitative | Outdoor temperature in degrees Fahrenheit | `66` |
| `temp_bucket` | Ordinal | Lower bound of the 10°F temperature interval; 60 represents 60–69°F | `60` |
| `weather` | Categorical | Recorded weather condition: Sunny, Rain, or Cloudy | `Sunny` |
| `total_chairs` | Quantitative | Total eligible study seats in the observation area | `54` |
| `total_tables` | Quantitative | Total eligible study tables in the observation area | `23` |
| `occupied_chairs` | Quantitative | Seats counted as taken by people or belongings | `37` |
| `available_chairs` | Quantitative | Total chairs minus occupied chairs | `17` |
| `chair_occupancy_rate` | Quantitative | Occupied chairs divided by total chairs, expressed as a percentage | `68.52%` |
| `occupied_tables` | Quantitative | Tables with people or belongings, counted once per table | `23` |
| `available_tables` | Quantitative | Total tables minus occupied tables | `0` |
| `table_occupancy_rate` | Quantitative | Occupied tables divided by total tables, expressed as a percentage | `100.00%` |

## Task Two

After our team completed the pilot collection, we felt as though some attributes were easier to collect than others. For instance, the weather observation and total chairs and tables were able to be converted fairly quickly within our dataset by counting all the tables and chairs in each section once and checking the weather app. One aspect of our data collection that was more difficult was the number of tables used, as different students may either be sitting alone at one table or sitting in a group, which made us manually check each table at a given time to make sure that our data was accurate.

Different group members interpreted data differently because they went at different times throughout the day, which caused different results to appear for the weather and the number of tables used per location. There were no important attributes missing within any observation, as all locations were open throughout building hours, which allowed us to collect data seamlessly without any issues. One unnecessary aspect was our available chair count, as our chair occupancy rate already provided the ratio between the chairs used compared to the total number of chairs. The only reason we kept this there was due to Excel formatting for dividing the two rows together per column, but this was unnecessary. 

The pilot did change the types of questions we answered, as it made us focus more on how specific weather patterns and times of day fluctuate student activities, rather than simply just the day of the week. We also diverted from our original hypothesis of seeing if students would rather be in groups or by themselves throughout the day, as we felt as though it was too small of an idea to capture throughout many different study areas, and we were able to collect more unique data to provide a more genuine problem to solve.

During our pilot run, our team mainly focused on the morning time on Monday, September 28th. After our pilot run, we decided to run 3 separate times throughout the week for morning, midday, and afternoon. This made sure that we would be able to see the patterns between student activity more clearly. We also assigned each team member a specific time to make sure that schedules wouldn’t cause us to miss our collection sections. Lastly, we revised the process of data collection so each team member would write the time and location on the Google Sheet each time to avoid errors or missing data.
	
## Task Three

Task3: 

We collected 73 observations of study space availability between seven different study lounges throughout the UIC Student Center East Building during week 6 of the semester. Each observation included the time of the observation, location, and the number of tables and chairs used compared with the total. Each group member was assigned time slots to count the number of tables and chairs in all seven locations and enter the data in a shared Google Sheet. We also captured temporal data regarding the time of day and weather conditions. Our spatial coverage includes the seven lounges, with 17 variables per observation, which are in Data_Collection.csv.

Our data collection revealed that chair occupancy rates differed immensely depending on the time of day and weather conditions. For instance, chair occupancy rates ranged from 1.56% to 88.89%, with morning times showing lower occupancy rates compared to midday periods, which averaged 49% compared with 22% in the morning. Weather conditions also showed large discrepancies, with rain being at around 33% on average, sunny at 37%, and cloudy at 27%. Different locations, such as the west terrace, also had much lower occupancy rates during rain, even with cover, at 1.56% compared to 62.5% during sunny weather.

Some constraints we had were that our data only captured one week within this semester and not on weekends due to our team not being on campus. We also weren’t able to capture every location at the exact minute because we had to count the number of open chairs and tables, so our observations looked over a section of time rather than exactly on the hour.

For data collection, we focused on collecting seats positioned at study tables and excluding seats and corner areas without tables. We also ignored data regarding student count, as students could also be entering a study lounge to talk with a friend or get food rather than studying, which would disrupt our data accuracy. Lastly, since a pass through each location and counting the number of chairs took time, the first and last locations were counted at different times. There could also be slight bias in the data, as it’s hard to perfectly count the exact number of open chairs when one or a few students could also be entering and sitting down while you are counting.

One domain question our team would like to investigate is whether occupancy changes throughout the day. We chose this question because our data shows a consistent trend, with morning observations lower than midday observations, averaging 22% in the morning and 49% at midday. Our second domain question is whether weather affects the occupancy of students in different types of spaces. This question works with our data because outdoor spaces such as the west terrace drop significantly in total chair use count from 62% in the sun to 1.56% in the rain. This could mean that the space itself is not protective against the rain, or that students just avoid outdoor spaces in general. Our third domain question would be whether there is a specific temperature boundary where more students study indoors. This is also a great question because our data collects weather from between 59℉ and 75℉, but every reading in the 70s came at midday, so we need to separate temperature from time of day. Our fourth domain question is whether spaces are most open throughout the day depending on location. This question works within our dataset because we noticed that some locations, such as the Commuter Center, showed far greater usage compared to the inner circle, which shows that some areas are more popular for studying or possibly used differently compared to other study lounges, such as for events.

## Task Four

Question 1 (does occupancy change throughout the day)

Task abstraction - discover the trend in occupancy rate across the ordered times of day.
At first we thought of this as just comparing occupancy rates across the times of day (morning, midday, and afternoon). But time of day has a natural order, so the real goal isn't only seeing which time block is highest, but it's seeing whether occupancy increases or falls as the day goes on. We already noticed mornings ran lower than midday, so the task is checking if that pattern holds consistently across locations and days instead of being a one time thing.

Question 2 (does weather affect occupancy in different types of spaces)

Task abstraction - compare how occupancy rate depends on weather for indoor vs outdoor spaces.
Weather is a categorical attribute (sunny, cloudy, rainy, and snow as we keep collecting more data), and we want to see how occupancy depends on it. The west terrace dropping from 62% in the sun to 1.56% in the rain made us realize the question isn't just "does weather matter," it's whether weather matters differently for outdoor spaces than indoor ones. That's why we're comparing across both weather and space type instead of weather alone.

Question 3 (is there a temperature boundary where more students study indoors)

Task abstraction - locate the temperature threshold where indoor occupancy starts to change.
Temperature is quantitative, so this is about the relationship between two numeric attributes, not comparing categories. We know what we're looking for, a cutoff point, but we don't know where it is, so the goal is finding where in the temperature range the pattern shifts. One thing this made us notice is that our max temperature is 75℉ because of when we started collecting data, and given the time of year we don't expect it to go any higher. Since 75℉ is still nice enough for people to be outdoors, we probably won't see a boundary where it gets too hot and students move inside. If a boundary exists outside our range, we won't be able to find it.

Question 4 (are spaces more open at certain times depending on location)

Task abstraction - identify which locations are most and least likely to have open seating at different times of the day.
The goal is to find which spaces a student is most likely to find a spot in, and whether that changes depending on when they show up. For example, the Commuter Center showed far greater usage than the inner circle, so the inner circle tends to be the better bet for an open seat. Since locations have very different chair counts, we compare the percentage of open seats instead of raw counts so a big lounge doesn't look more open just because it's bigger. We also want to look for outliers, since unusual spikes in usage could be from events rather than normal studying.

Reflection

When we first wrote our questions, almost every one came down to "compare occupancy across something." Turning them into abstract tasks showed us they're asking different kinds of things. Question 1 is about change over an ordered variable, Question 3 is about a relationship and a threshold, and Question 4 is about which locations are most likely to have open seats. This also changed how we think about our data. We realized we need to use occupancy rates instead of counts, that our temperature range limits what Question 3 can answer, and that Question 2 is really about how weather and space type interact, not weather on its own.

## Task Five

### Ramon's Sketches

![alt text](<visualizations/Ramon/CS 424 Task 5 Sketch Ramon_1.jpeg>)

This first sketch (Q1) was motivated by our pilot testing, which showed that morning counts were lower than midday counts. The domain question being asked here is whether occupancy changes throughout the day. Our abstract task here is to discover the trend in occupancy across the ordered times of day. The attributes are study lounge location (categorical), time of day (ordinal), and mean chair occupancy percentage (quantitative). We used a heatmap, where the marks are area marks, one cell for each lounge and time block. For channels, vertical position is the location and horizontal position is the time of day, with the density of the markings showing the occupancy level (blank, dots, lines). What worked well was that the busiest cells stand out using the different markings for each percentage bracket. What didn’t work well within this graph was that it summarized the times into 3 different sections rather than many different sections to show a more cohesive increase, but the graph still points out the conclusion that midday times contain a greater increase in chair and table usage. This sketch is different because it's the only graph that has location and time together. It is also the only one that uses marking density instead of position or length to show occupancy. 

![alt text](<visualizations/Ramon/CS 424 Task 5 Sketch Ramon_2.jpeg>)

The second sketch (Q2) here was motivated by our drop in the West Terrace, which dropped significantly when it rained. The domain question being asked here is if weather affects occupancy in different types of spaces. The abstract task is to compare how occupancy depends on weather within indoor and outdoor spaces. The attributes here are location (categorical), weather (categorical), and occupancy percentage (quantitative). The marks shown here are points being connected by lines. The channels here are horizontal position for occupancy percentage, vertical position for location, and the shape for the difference between rainy (square) vs. sunny (triangle) weather. What worked well was that the difference between weather conditions was easy to see for the reader, and how certain locations, such as the commuter center, changed far more compared to places such as the inner circle. What didn’t work the best was that the shapes almost overlap with each other when the values are close. This graph differs from the others because it is the only graph that shows the difference between two conditions as a length using a horizontal visualization rather than vertical.

![alt text](<visualizations/Ramon/CS 424 Task 5 Sketch Ramon_3.jpeg>)

The third sketch (Q3) here was motivated by our method of data collection, as our data covers a range of temperatures between 59-75°F, so we wanted to see if the temperature changes where students would study. The domain question being asked here is whether there is a temperature boundary where more students study indoors. The abstract task here is to locate the temperature at which these occupancy patterns shift. The attributes were the temperature range (ordinal), space type (categorical), and the mean chair occupancy percentage (quantitative). The marks here were the bars, and the channels were the bar height for mean occupancy, the horizontal position for temperature range, and the shape for indoor(triangle) vs. outdoor (square). What worked well with this graph was that it was visually simple to see the difference in occupancy between indoor and outdoor per temperature range. There is also a closer threshold at around the 71-75°F range, where both areas contain similar amounts of usage. What didn’t work as well was that the graph shows a wide range for temperature and not the exact degree at which the equalization happens (such as collecting data for every degree). The confusing part about this graph is that every observation within the 71-75°F range was also at midday, when more students are within these study areas as well. What differs from the other graphs is that this is the only bar chart that groups temperature into ranges and groups into indoor vs. outdoor.

---

### Ricky's Sketches

![alt text](<visualizations/Ricky/Sketch01CS424.jpg>)

This first sketch (Q3) explores whether temperature is associated with chair occupancy at West Terrace. It relates to our domain question about whether there is a temperature boundary where more students study indoors, providing an outdoor perspective on that question. The abstract task is to identify relationships between two quantitative attributes. The attributes are outdoor temperature in degrees Fahrenheit (quantitative) and chair occupancy percentage (quantitative), with location held constant at West Terrace. The marks are points, with each point representing one observation. The channels are horizontal position for temperature and vertical position for chair occupancy. I labeled each point with its occupancy percentage because I considered that value more important to emphasize than the temperature. This sketch differs from the others because it shows individual observations rather than grouped averages. It can reveal possible temperature related patterns at West Terrace, but it doesn't yet show any corrilation to students moving indoors due to harsh tempeture drops.

![alt text](<visualizations/Ricky/Sketch02CS424.jpg>)

The second sketch (Q1) compares average table and chair occupancy across weekdays. It relates to our domain question about occupancy changing over time, extending the comparison from time of day to Monday through Friday. The abstract tasks are to compare values across ordered time categories and identify patterns in the two occupancy measures. The attributes are weekday (ordinal), occupancy type (categorical), and mean occupancy percentage (quantitative). The marks are points connected by lines, with triangles representing table occupancy and squares representing chair occupancy. The channels are horizontal position for weekday, vertical position for mean occupancy, and shape for occupancy type. Separate lines connect each occupancy measure across the week, while dotted lines between the two markers on each day emphasize their difference. This sketch differs from the others because it shows weekday patterns and the gap between table and chair occupancy over time. The averages summarize the visits collected on each day, so differences in collection times and locations may also contribute to the patterns.

![alt text](<visualizations/Ricky/Sketch03CS424.jpg>)

The third sketch (Q4) compares average table and chair occupancy across the seven study locations. The domain question is which locations offer the most availability. The abstract tasks are to compare locations and identify differences between their table and chair occupancy rates. The attributes are study lounge location (categorical), occupancy type (categorical), and mean occupancy percentage (quantitative). The marks are side-by-side bars, with shaded bars representing table occupancy and unshaded bars representing chair occupancy. The channels are horizontal position for location, bar height for mean occupancy, and shading for occupancy type. A dotted line extends from the height of the chair occupancy bar to the top of the table occupancy bar, with the difference labeled in percentage. This highlights locations where a higher proportion of tables is taken than chairs. This sketch differs from the others because it emphasizes comparisons between locations and explicitly labels the gap between the two measures, although the overall averages do not show how consistently a location remains available throughout the day.

---

### Jake's Sketches

![alt text](<visualizations/Jake/IMG_7005.png>)

This first sketch (Q1) is a clock face, motivated by the limitation of our heatmap, which grouped time into only three blocks. It addresses the domain question of whether occupancy changes throughout the day, with the abstract task of discovering the trend in occupancy across time. The attributes are time of observation (quantitative), chair occupancy percentage (quantitative), and location (categorical). The marks are points, one for each of our 73 observations, and the channels are angle for time, distance from the center for occupancy, and shape for location. What worked well is that every observation sits at its actual time, so the midday cluster sitting much farther from the center makes the morning to midday increase easy to see. What didn't work as well is that the morning observations crowd near the center since their occupancy is low, which makes the location shapes hard to tell apart there. Radial distance is also harder to judge than a regular vertical axis, and the dots form clusters around our collection windows, so the gaps between them don't show whether occupancy rises gradually or jumps suddenly. This sketch differs from the others because it's the only radial layout and the only one showing every observation at its exact time across all locations.

![alt text](<visualizations/Jake/IMG_7006.png>)

The second sketch (Q4) is a floor map of Student Center East, motivated by the idea that someone looking for a seat cares about where a space is and how big it is, not just its occupancy rate. It addresses the domain question of whether spaces are more open depending on location, with the abstract task of identifying which locations are most and least likely to have open seating. The attributes are study lounge location (categorical), total chairs (quantitative), and mean chair occupancy percentage (quantitative). The marks are circles, one for each lounge, and the channels are spatial position for location, circle size for total chairs, and the area of an inner filled circle for occupancy. What worked well is that it shows something a bar chart can't, which is that the inner circle has the most open chairs overall even though its occupancy rate (19%) is close to the 1st floor lounge (16%), simply because it's so much bigger. The Commuter Center also stands out as the busiest at 59%. What didn't work as well is that area is hard to judge by eye, so the Commuter Center looks almost completely full even though it's only a little over half. The averages also hide how availability changes throughout the day, and the positions are only a rough version of the real building layout. This sketch differs from the others because it's the only one that uses physical space and shows each location's capacity.

![alt text](<visualizations/Jake/IMG_7007.png>)

The third sketch (Q3) combines bars and a line, motivated by a problem we found in our temperature bar chart, where every observation in the 71 to 75°F range was also at midday, so we couldn't tell whether temperature or time of day was driving occupancy. It addresses the domain question of whether there's a temperature boundary where more students study indoors, and also touches on Q1 and Q2, with the abstract task of identifying whether occupancy follows temperature or time of day. The attributes are collection session (ordinal), mean chair occupancy percentage (quantitative), temperature (quantitative), and weather (categorical). The marks are bars, points connected by a line, and weather icons, and the channels are horizontal position for session, bar height for occupancy, vertical position on a second axis for temperature, and icon shape for weather. What worked well is that the two tallest bars, Tuesday midday (58.6%) and Thursday midday (53.8%), were also the two warmest sessions at 75°F and 72°F, while Friday midday stayed low at 29.8% when it was only 64°F. Thursday midday was rainy and still busy, which suggests rain pushes students indoors rather than keeping them away. What didn't work as well is that dual axes can be misleading, since how well the bars and line seem to match depends on how the two axes are scaled. Also left out Wednesday midday because it was only one observation, and with only one week of data, each type of session only happens once or twice. This sketch differs from the others because it's the only one using two axes, and the only one that puts temperature, time of day, and weather together in the order they happened.

---

### Refined Sketches

![alt text](<visualizations/Refined/Refined_Sketch_One.jpg>)

The first refined sketch (Q4) develops the original bar chart comparing average table and chair occupancy at each location. It addresses which study areas offer greater availability, with the abstract tasks of comparing locations and identifying differences between two occupancy measures. The attributes are location (categorical), occupancy type (categorical), and mean occupancy percentage (quantitative). The marks are bars, with horizontal position identifying location and bar height representing occupancy. Compared with the outlined version, the refinement introduces a different color for each location and uses darker shades for table occupancy and lighter shades for chair occupancy. It retains the numerical labels and dashed connectors showing the percentage-point gaps. We expect viewers to identify locations with greater average availability and recognize where table occupancy substantially exceeds chair occupancy.

![alt text](<visualizations/Refined/Refined_Sketch_Two.jpg>)

The second refined sketch (Q1) develops the original patterned heatmap showing chair occupancy by location and time of day. It addresses whether occupancy changes throughout the day, with the abstract tasks of identifying temporal patterns and comparing those patterns across locations. The attributes are study lounge location (categorical), time of day (ordinal), and mean chair occupancy percentage (quantitative). The marks are rectangular cells, with vertical position representing location and horizontal position representing morning, midday, and afternoon. Compared with the outlined version’s blank spaces, the refinement uses shades of blue to represent occupancy brackets. We expect viewers to identify each location’s busiest observation period and determine whether similar daily occupancy patterns occur across the seven lounges.

## Task Six

Our sketches explored bars, lines, points, a heatmap, a clock, and a floor map. Bar charts and point comparisons made percentages easy to compare. The clock and floor map offered more unusual ways to show time and location, but radial distances and circle sizes were harder to read accurately.

For Question 1, the weekday line graph showed changes across the week, but it did not directly show how occupancy changed throughout a day. The clock showed exact observation times but became crowded where points overlapped. We chose to refine the heatmap because it made morning, midday, and afternoon patterns easier to compare across all seven locations. Its main limitation was grouping observations into three periods, which could potentially hide changes within those periods.

For Questions 2 and 3, the weather comparison clearly showed differences between sunny and rainy observations, while the temperature bars compared indoor and outdoor spaces. Grouping temperatures made the chart simpler but hid individual differences. The scatterplot kept those differences visible but covered only West Terrace. Though, we could expand it into an interactive visualization where users click an observation to see details such as its date, time, weather, and chair and table counts. The combined chart included weather, temperature, and time, although its two axes made it harder to interpret. So far, we have not confirmed a temperature threshold or established whether students moved indoors.

For Question 4, the location bar chart clearly compared table and chair occupancy, while the floor map added seating capacity and physical location. We refined the bar chart because it made the gaps between table and chair occupancy easy to see at each location. Color helps distinguish the bars, while labels show the percentages. More locations would make this chart crowded, whereas the heatmap could grow by adding rows.

Our data covers only one week, with uneven collection times and weather conditions. This limits the comparisons, especially because warmer observations often occurred at midday. Collecting at consistent times over more weeks would help. Exploring different layouts showed us what averages leave out. We are also looking foward to collecting data during weeks like midterms and campus events to explore conditions our first week may have missed.

## Task Seven

A lot of our collaboration happened in short bursts, usually the 10 minutes before class and the 10 to 15 minutes after. Those quick conversations ended up being where most of our ideas came from, including deciding between train and bus data or study room data. We went with study rooms, and having those regular check-ins meant we could keep making decisions without needing to schedule separate meetings. Our iMessage group chat filled in the gaps between classes, so we were never really out of the loop with each other.

The way we split up data collection shaped what our data ended up looking like. Since we each collected around our own times and the places we already go to study, it fit naturally into our days, but it also means our collection times partly reflect our own routines, even though we visited every location each time. To keep everything in one place, we shared a Google Sheet so all of us could access and add to the same file. We also automated most of the sheet so our entries would stay consistent no matter who was collecting. Location was a dropdown so nobody could misspell it, and picking one automatically filled in the total tables and chairs for that spot. Clicking the date filled in the day of the week, typing the time in 24-hour format filled in the time of day, and entering the temperature gave us the temperature bucket. Weather was also a dropdown, and once we put in the occupied seats and tables, the sheet automatically calculated how many were open and the occupancy ratio. Because three different people were collecting, this setup is a big reason our data came out clean and consistent, and it also gave us ready-made categories like time of day and temperature bucket that we could build our visualizations around.

Our process also shaped our visualization designs. We brainstormed together in the group chat to make sure we each planned different visualizations, then each of us took on three sketches and sent pictures once we finished. Since we each sketched on our own first, we ended up with a lot of different approaches, which gave us more to compare and build from when we worked on Task 5 together. We split the written tasks in a similar way, with me taking Tasks 4 and 7, Ramon taking 2 and 3, Ricky taking 1 and 6, and all of us working on Task 5 together.

We didn't run into any major challenges, but time was definitely the biggest one. Ricky and I are both commuters, so we aren't on campus later in the day, and neither of us has classes on Fridays. On the other hand, Ramon lives in the dorms, so he was able to cover times we couldn't. We also focused on daytime hours since the Commuter Center closes around 6pm, so our data doesn't capture evening use in the other spaces. That meant we had to be intentional about spreading our collection times out between the three of us so we could cover as much of the day as possible. Even so, our data stops around 6pm, so it doesn't capture how busy these spaces get in the evening, which is something we'll have to keep in mind when looking at how occupancy changes throughout the day. Looking back, our communication is really what made it work, since staying in constant contact made it easy to plan around each other's schedules.
