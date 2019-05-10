import pandas as pd
pd.set_option('display.expand_frame_repr', False)

tweets_csv = pd.read_csv("na.csv")
tweets_df = pd.DataFrame(tweets_csv)
print(tweets_df.iloc[1:3,4])
tweets_df = tweets_df.dropna(axis=0)
print(tweets_df.iloc[1:3,4])
test = len(tweets_df)