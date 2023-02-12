"""
Main file to execute application
"""
import datetime as dt
from pmaw import PushshiftAPI

#Creates the API instance
api = PushshiftAPI()

#Converts start date into integer
start = int(dt.datetime(2023, 2, 9).timestamp())

#Goes into subreddit wallstreetbets
#Provides a list: generator object
#NOTE: selftext is the main body of a message; body refers to comments
posts = list(api.search_submissions(after = start,
                            subreddit = 'wallstreetbets',
                            filter = ['author', 'title', 'selftext'],
                            limit = 10))

#Print first post
print('\nThis is the first post to see the structure of the output\n')
print(posts[0])

#Print authors of 10 posts
print('\nThese are the first ten authors\n')
for post in posts:
    print(post['author'])

