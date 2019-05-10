import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
pd.set_option('display.expand_frame_repr', False)

tweets_csv = pd.read_csv("exercises/tweets.csv")
tweets_df = pd.DataFrame(tweets_csv)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(tweets_df['ttext'].values)
Y = tweets_df['class'].values