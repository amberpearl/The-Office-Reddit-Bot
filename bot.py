import praw
import time
def botlogin():
    reddit = praw.Reddit(client_id='F8zBnyfLOXaT0A',
            client_secret='BLmnHdkrAXFQZiGytx44IuKJjO4',
            user_agent='<console:first_bot:0.0.1 (by /u/curlyfries___)>',
            username='curlyfries___',
            password='redditpassword') 
    return reddit 

def botrun(reddit):
    for comment in reddit.subreddit('RedditWritesTheOffice').comments(limit=25):
        if "Bears. Beets. Battlestar Galactica" in comment.body:
            print ("found")
            comment.reply("[Hello](http://www.pilkipedia.co.uk/wiki/images/c/cd/Dwight_Schrute.jpg)")

    time.sleep(8)
    
while True:
    reddit = botlogin()
    botrun(reddit)



