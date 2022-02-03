from twitter import Twitter
from twitterUserInfo import username,password


twitter = Twitter(username,password)
twitter.singIn()
twitter.searchWithHashtag('python')
twitter.findTweet()

