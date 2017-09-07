import requests
import praw

username = 'Nose_to_the_Wind'
password = open('..\PyPass\PyKey\pyRedditAPI_Pass.txt', 'r').read()
user_id = open('..\PyPass\PyUser\pyRedditAPI_User.txt', 'r').read()
token = open('..\PyPass\PyKey\pyRedditAPI_Key.txt', 'r').read()

reddit = praw.Reddit(client_id = user_id,
                     client_secret = token,
                     password = password,
                     user_agent = r"python:pyRedditAPI:v1.0(by \u\Nose_to_the_Wind)",
                     username = username
                     )

for submission in reddit.subreddit('dataisbeautiful').hot(limit = 10):
    print(submission.title)
