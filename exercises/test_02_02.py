def test():
    assert "pandas" in __solution__, "Вы импортируете pandas?"
    assert "pd.read_csv" in __solution__, "Вы загружаете csv-файл?"
    assert tweets_df == pd.DataFrame(tweets_csv), "Вы приводите csv к dataframe?"
    assert "head(10)" in __solution__, "Вы печатаете первые десять записей?"

    __msg__.good("Well done!")