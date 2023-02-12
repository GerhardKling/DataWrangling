"""
Main file to execute application
"""
from psaw import PushshiftAPI
import datetime as dt

#Creates the API instance
api = PushshiftAPI()

#Converts start date into integer
start = int(dt.datetime(2021, 2, 23).timestamp())

#Goes into subreddit wallstreetbets
#Provides a list: generator object
#NOTE: selftext is the main body of a message; body refers to comments
posts = list(api.search_submissions(after = start,
                            subreddit = 'wallstreetbets',
                            filter = ['url','author', 'title', 'subreddit', 'selftext'],
                            limit = 10))

#Print first post
print('\nThis is the first post to see the structure of the output\n')
print(posts[0])

#Print authors of 10 posts
print('\nThese are the first ten authors\n')
for post in posts:
    print(post[0])

