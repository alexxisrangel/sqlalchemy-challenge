# sqlalchemy-challenge

## Instructions 
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

## Tool Used 
- matplotlib
- numpy
- pandas
- sqlalchemy

  ## Analyzing and Exploring Cliimate Data


First steps was to create a sqlite engine that allowed me to get my climate data from hawaii.sqlite

<img width="777" alt="Screenshot 2023-10-04 at 11 30 41 AM" src="https://github.com/alexxisrangel/sqlalchemy-challenge/assets/129305054/3b6a0aa7-d4c5-4a99-ba9b-3c052a5d3f1a">

Next steps was to explore the data I was working with and pull data from the last 12 months.  I used Datetime in order use my current date as the starting point for my one year ago. After getting this data I created a DataFrame 

<img width="824" alt="Screenshot 2023-10-04 at 11 35 00 AM" src="https://github.com/alexxisrangel/sqlalchemy-challenge/assets/129305054/0358a3fb-3ded-46c7-8af5-63a459f29ba8">


After sorting my data by date I able to create this graph that displayed Hawaii's precipitation from the last year
<img width="1118" alt="Screenshot 2023-10-04 at 11 35 25 AM" src="https://github.com/alexxisrangel/sqlalchemy-challenge/assets/129305054/a4749060-1bd1-4669-b609-52a275883607">


## Exploratory Station Analysis 

I proceeded to explore the Hawaii stations to see which stations were the most active. For this step I used value_counts to get a count for each station
<img width="905" alt="Screenshot 2023-10-04 at 11 40 54 AM" src="https://github.com/alexxisrangel/sqlalchemy-challenge/assets/129305054/1e644170-e434-4b4a-aae6-02b753245dbf">

With the most active station I decided to calculate the lowest, highest and average temperature for this station 
<img width="1058" alt="Screenshot 2023-10-04 at 11 43 15 AM" src="https://github.com/alexxisrangel/sqlalchemy-challenge/assets/129305054/9e3fd755-6cc2-4f31-bcf7-77439e662e34">


I created a Histogram with this data and we can see that station USC00519281 (most active) see most of its days between 75 - 80 degrees. 
<img width="758" alt="Screenshot 2023-10-04 at 11 47 37 AM" src="https://github.com/alexxisrangel/sqlalchemy-challenge/assets/129305054/15b26f27-5ca5-4522-8bda-330ba2fdd805">


## Flask App 

In order to have my results in a web app I created a Flask app to centralize everything. In my first route I have all posible routes a user can select. 

These options are:

Precipitation from th past year
<img width="775" alt="Screenshot 2023-10-04 at 11 58 10 AM" src="https://github.com/alexxisrangel/sqlalchemy-challenge/assets/129305054/5c7c9dea-3ffd-4a6c-9106-06d3720f2e23">


All active stations with weather data
<img width="846" alt="Screenshot 2023-10-04 at 11 58 32 AM" src="https://github.com/alexxisrangel/sqlalchemy-challenge/assets/129305054/cce749a6-2a53-47e1-8de6-c31757d2c240">


The most active station with its weather data 
<img width="721" alt="Screenshot 2023-10-04 at 11 59 17 AM" src="https://github.com/alexxisrangel/sqlalchemy-challenge/assets/129305054/29719cb8-6bc3-46ba-95d4-9d24b09bad57">



The option to select a specified data range that returns mimimun, maximum and avergage temperatures for that data range in a json file. 

<img width="745" alt="Screenshot 2023-10-04 at 11 59 33 AM" src="https://github.com/alexxisrangel/sqlalchemy-challenge/assets/129305054/42e80cff-30cf-404c-a866-be3fdafaea35">


