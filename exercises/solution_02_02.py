import pandas as pd
pd.set_option('display.expand_frame_repr', False)

tweets_csv = pd.read_csv("tweets.csv")
tweets_df = pd.DataFrame(tweets_csv)
print(tweets_df.head(10))