import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import ____
pd.set_option('display.expand_frame_repr', False)

tweets_csv = pd.read_csv("exercises/tweets.csv")
tweets_df = pd.DataFrame(tweets_csv)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(tweets_df['ttext'].astype('U'))
y = tweets_df['class'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
model = ____
model.____
predicted = ____
