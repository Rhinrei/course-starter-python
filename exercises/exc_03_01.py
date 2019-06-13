import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from ____ import train_test_split
pd.set_option('display.expand_frame_repr', False)

tweets_csv = pd.read_csv("exercises/tweets.csv")
tweets_df = pd.DataFrame(tweets_csv)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(tweets_df['ttext'].astype('U'))
y = tweets_df['class'].values
____ = train_test_split(____)
