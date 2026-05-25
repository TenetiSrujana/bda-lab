bash

nano weather.txt
#2022 35 20
2021 33 18
2020 38 22
2019 36 21
2018 37 19
2017 34 18
2016 32 17

nano cleaner.py
#import re
import sys
for i in sys.stdin:
    print(re.sub(r'\s+', ' ', i))
cat weather.txt | python3 cleaner.py > weather_cleaned.txt

pig -x local

weather_data = LOAD 'weather.txt' USING PigStorage(' ') AS (year:int, maxtemp:int, mintemp:int);

DUMP weather_data;

filtered_weather = FILTER weather_data BY maxtemp > 35;

DUMP filtered_weather;

grouped_weather = GROUP weather_data BY year;

DUMP grouped_weather;

grouped_weather_count = FOREACH grouped_weather GENERATE group AS year, COUNT(weather_data) AS record_count;

DUMP grouped_weather_count;
