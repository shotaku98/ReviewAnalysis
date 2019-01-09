import re
import tweepy
from textblob import TextBlob

class Review(object):
    def __init(self):


    REPLACE_NO_SPACE = re.compile("(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])")
    REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
    
    def clean_review(self,reviews):
         reviews = [REPLACE_NO_SPACE.sub("", line.lower()) for line in reviews]
         reviews = [REPLACE_WITH_SPACE.sub(" ", line) for line in reviews]
         reviews.split(".")

    def get_sentiment(self,)
         """
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'
        """
"""
this comment is added by PS
Sabki gaand me danda de denge
ML ki gaand faad denge
"""
def main():
    
    
