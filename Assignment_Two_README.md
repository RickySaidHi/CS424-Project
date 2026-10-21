# CS 424 Assignment Two

## Task One

### Revisiting Data and Questions

So far, we have added 90 rows to our data set, bringing our total to 163 observations across weeks 6 through 9. We included this data to see how the patterns we noticed within week 6 repeat throughout the semester.

We still believe Questions 1 (does occupancy change throughout the day?), 2 (does weather affect occupancy in different types of spaces?), and 4 (are spaces more open at certain times depending on location?) are worth investigating. This is because our data showed that our occupancy averages were 20 percent in the morning, 51 percent at midday, and 31 percent in the afternoon, with every lounge being the busiest at midday. For question 4, we noticed that the Commuter Center was the busiest out of all of the other locations, with the Inner Circle and the West Terrace being the most open.

We will rewrite question 2 as well to focus on when looking at specific areas around the Student Center East building, does rain affect occupancy just within outdoor spaces or both within outdoor and indoor spaces, rather than just weather in general. This is because we were comparing different times of day with weather conditions, so we just want to focus on weather conditions instead.

We are also removing question 3 regarding whether there is a temperature boundary because almost every warm reading happened at midday, so we can’t visually separate temperature from time of day in this scenario.

We also added a new question about whether students study alone or in groups because tables fill up faster than chairs. For instance, Montgomery Lounge averages 36% of its chairs but 90% of its tables.

Some inconsistencies we have found within our dataset are that in a few visits, the counts were off, such as there being more occupied tables than chairs. The commuter center was also accidentally counted twice in a few instances within our dataset. There were also a few typos in some instances where there were 27 occupied tables, but instead there were only 7 occupied tables from our initial data collection. Lastly, we noticed a visit recorded with 27 occupied tables that should have been 7, a #REF! error, and 230 available chairs in a 54-chair room.

We fixed this by manually editing our spreadsheet and deleting duplicate visits, as well as rewriting any typos or broken formulas within our dataset. This included lines 81, 105, 116, and 143.

Some limits within our data are that we only collected on weekdays between about 8 AM and 6 PM, and weeks 8 and 9 only have mornings so far. Going forward, we plan to collect more midday and afternoon walk-throughs, including at least one more rainy day.