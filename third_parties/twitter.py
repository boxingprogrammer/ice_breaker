##################################
# twitter.py
# 000, 20230803, cliff: original coding
##################################
# this is howw we scrape twitter data
##################################

import os
from datetime import datetime, timezone
import logging
import tweepy

logger = logging.getLogger('twitter')

auth = tweepy.OAuth1UserHandler(os.environ.get('TWITTER_API_KEY'), os.environ.get('TWITTER_API_SECRET'))

auth.set_access_token(os.environ.get('TWITTER_ACCESS_TOKEN'), os.environ.get('TWITTER_ACCESS_SECRET'))

api = tweepy.API(auth)
                                