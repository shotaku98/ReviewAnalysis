import re
from textblob import TextBlob
import tweepy

class Review(object):
    def __init(self):
        print("Object Created")


    
    
    def clean_review(self,reviews):
        REPLACE_NO_SPACE = re.compile("(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])")
        REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
        reviews = [REPLACE_NO_SPACE.sub("", line.lower()) for line in reviews]
        reviews = [REPLACE_WITH_SPACE.sub(" ", line) for line in reviews]
        """reviews.split(".")"""

    def get_sentiment(self,reviews):
         

        analysis = TextBlob(self.clean_review(reviews))
        
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'
        

def main():
    api=Review()
    print(api.get_sentiment("Good food"))
    
