# DROP TABLES

tweets_table_drop = "DROP TABLE IF EXISTS tweets"
user_table_drop = "DROP TABLE IF EXISTS users"
time_table_drop = "DROP TABLE IF EXISTS time"
value_table_drop = "DROP TABLE IF EXISTS value"
company_table_drop = "DROP TABLE IF EXISTS company"

fact_tweet_table_create = ("""
    CREATE TABLE IF NOT EXISTS tweets
    (tweet_id bigint PRIMARY KEY, date_time TIMESTAMP, writer_id bigint,
     ticker_symbol_id bigint,
     body text NOT NULL,
     comment_num int,
     retweet_num int,
     like_num int)
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users
    (writer_id bigint PRIMARY KEY,
     writer text)
""")

company_table_create = ("""
    CREATE TABLE IF NOT EXISTS company
    (ticker_symbol_id bigint PRIMARY KEY,
     ticker_symbol text)
""")

value_table_create = ("""
    CREATE TABLE IF NOT EXISTS value
    (day_date TIMESTAMP NOT NULL,
     volume int,
     open_value float,
     high_value float,
     low_value float,
     ticker_symbol_id bigint NOT NULL,
     PRIMARY KEY (day_date, ticker_symbol_id))
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time
    (date_time TIMESTAMP PRIMARY KEY, hour int, day int,
    week int, month int, year int, weekday text)
""")

# INSERT RECORDS

fact_tweet_table_insert = ("""
    INSERT INTO tweets
    (tweet_id, date_time, writer_id, ticker_symbol_id, body, comment_num, retweet_num, like_num)
    VALUES (%s,%s,%s,%s,%s, %s, %s, %s)
    ON CONFLICT (tweet_id) DO NOTHING;
""")

user_table_insert = ("""
    INSERT INTO users
    (writer_id, writer)
    VALUES (%s,%s)
    ON CONFLICT (writer_id) DO NOTHING;
""")

company_table_insert = ("""
    INSERT INTO company (ticker_symbol_id, ticker_symbol)
    VALUES (%s, %s)
    ON CONFLICT (ticker_symbol_id) DO NOTHING;
""")

value_table_insert = ("""
    INSERT INTO value
    (day_date, volume, open_value, high_value, low_value, ticker_symbol_id)
    VALUES (%s, %s, %s, %s, %s, %s);
""")

time_table_insert = ("""
    INSERT INTO time (date_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (date_time) DO NOTHING;
""")

# QUERY LISTS

create_table_queries = [fact_tweet_table_create, user_table_create, company_table_create, value_table_create,
                        time_table_create]
drop_table_queries = [tweets_table_drop, user_table_drop, time_table_drop, value_table_drop, company_table_drop]
