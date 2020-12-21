# Reddit-Datascience
## Data Collection (collect.py, collect_hottest.py)
#### Newest:
Used the Reddit API to download posts and put them into two files via collect.py 
- Sample 1: the 1000 newest posts from the 10 most popular subreddits by subscribers:
funny, AskReddit, gaming, aww, pics, Music, science, worldnews, videos, todayilearned.
- Sample 2: Collect the 1000 newest posts from the 10 most popular subreddits by # of posts by day:
AskReddit, memes, politics, nfl, nba, wallstreetbets, teenagers, PublicFreakout, leagueoflegends,
unpopularopinion
#### Hottest:
Collected 500 per day posts over the course of Nov. 3-5 from the Politics subreddit. This was happening during the 2020 election period, so the subreddit was quite popular 
## Data Cleaning (clean.py)
Self explanatory, just made sure that every post had a title and the proper datetime format, where input is a json with one dictionary per line.
## compute_title_length.py
Again, this is just a short code bit to compute average post title length (measured as # of characters/post text).
