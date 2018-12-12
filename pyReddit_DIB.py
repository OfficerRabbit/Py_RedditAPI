import requests
import praw
from matplotlib import pyplot as plt
from pprint import pprint

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

submission_json = {
    "Submissions": []
    }

for submission in reddit.subreddit('dataisbeautiful').hot(limit = 10):
    print(submission.title)
    print("Total Comments:", submission.num_comments,
          "Upvote Ratio:", submission.upvote_ratio)
    submission_json['Submissions'].append({
        "Title": submission.title,
        "Total_Comments": submission.num_comments,
        "Upvote_Ratio": submission.upvote_ratio
        }
        )
    
x_axis = []
y_axis = []

for index, submission in enumerate(submission_json['Submissions']):
    x_axis.append(submission['Total_Comments'])
    y_axis.append(submission['Upvote_Ratio'])

x_axis.sort()
y_axis.sort()
plt.figure()
# Set x-axis range
plt.xlim((1,9))
# Set y-axis range
plt.ylim((1,9))
# Draw lines to split quadrants
plt.plot([5,5],[1,9], linewidth=4, color='red' )
plt.plot([1,9],[5,5], linewidth=4, color='red' )
plt.title('Quadrant plot')
# Draw some sub-regions in upper left quadrant
plt.plot([3,3],[5,9], linewidth=2, color='blue')
plt.plot([1,5],[7,7], linewidth=2, color='blue')
plt.plot(x_axis, y_axis)
plt.show()
