import pandas as pd
from sklearn.feature_extraction.text import ____
pd.set_option('display.expand_frame_repr', False)

tweets_csv = pd.read_csv("exercises/tweets.csv")
tweets_df = pd.DataFrame(tweets_csv)

vectorizer = ____
X = ____(____.values)
Y = ____.values