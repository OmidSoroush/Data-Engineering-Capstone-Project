# Capstone Project

This project aims to build a database for market value data and Twitter data posted about Amazon, Apple, Google, Microsoft, and Tesla that will be optimized to query and analyze. An ETL pipeline is going to be built to create the database.

## Data Sources

#### Twitter Data

This dataset as a part of the paper published in the 2020 IEEE International Conference on Big Data under the 6th Special Session on Intelligent Data Mining track. The dataset contains over 3 million unique tweets with their information such as tweet id, author of the tweet, post date, the text body of the tweet, and the number of comments, likes, and retweets of tweets matched with the related company.

#### Company Value Data
This dataset contains daily OPEN, CLOSE, VOLUME, HIGH, and LOW values of Amazon, Apple, Google, Microsoft, and Tesla companies as tagged by dates. Values are fetched from the official NASDAQ website.

## Database Design

A star schema design is chosen for the database. This schema has one Fact Table having twitter data, and four supporting Dimension Tables. A star schema Database design allows for flexible queries by separating dimensions into specific tables in a clean way.

##### Fact table

contains twitter data:

- tweet_id int PRIMARY KEY
- date_time TIMESTAMP
- writer_id bigint
- ticker_symbol_id bigint
- body text NOT NULL
- comment_num int
- retweet_num int
- like_num int


##### User Dimension Table

- writer_id bigint PRIMARY KEY
- writer text

##### Company Dimension Table

- ticker_symbol_id bigint PRIMARY KEY
- ticker_symbol text

##### Value Dimension Table

- day_date TIMESTAMP PRIMARY KEY
- volume int
- open_value float
- high_value float
- low_value float
- ticker_symbol_id bigint

##### Time Dimension Table

- date_time TIMESTAMP PRIMARY KEY
- hour int, day int
- week int
- month int
- year int
- weekday text

### Choice of tools and technologies

Pandas is used to preprocess and clean up the data. It is a very efficient tool for this purpose. I have used Python to realize this project because Python is the language I am comfortable with, and it is one of the most used languages for these purposes
A monthly update of the data is recommended. 

### What if?
1. The data was increased by 100x.

    * Spark can be used to process the data in an efficient and distributed way. Amazon Redshift is also helpful in such a scenario since         it is an optimized analytical database tool for such heavy work-loads.
    
2. The data populates a dashboard that must be updated on a daily basis by 7am every day.

    * Airflow can be used in this scenario. In case of failures, use Dag retries and send failure emails.

3. The database needed to be accessed by 100+ people.
    * Redshift is the right tool in this case because it has auto-scaling capabilities and high read performance