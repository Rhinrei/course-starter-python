def test():
    assert "pandas" in __solution__, "Вы импортируете pandas?"
    assert "pd.read_csv" in __solution__, "Вы загружаете csv-файл?"
    assert "pd.DataFrame(tweets_csv)" in __solution__, "Вы приводите csv к dataframe?"
    assert ".iloc[:, 1:4]" in __solution__, "Вы печатаете только некоторые строки?"

    __msg__.good("Отлично!")