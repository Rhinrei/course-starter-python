import pandas as pd
pd.set_option('display.expand_frame_repr', False)

tweets_csv = pd.read_csv("exercises/tweets.csv")
tweets_df = pd.DataFrame(tweets_csv)
tweets_df = ____(axis=0)
