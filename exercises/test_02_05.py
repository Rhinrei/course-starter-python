def test():
    assert "TfidfVectorizer" in __solution__, "Вы импортируете библиотеку TfidfVectorizer?"
    assert "TfidfVectorizer()" in __solution__, "Вы создаете векторизатор?"
    assert "vectorizer.fit_transform" in __solution__, "Вы используете векторизатор, чтобы привести значения независимой переменной к числовому виду?"
    assert "tweets_df['ttext']" in __solution__, "Вы выбираете независимую переменную в качестве Х?"
    assert "tweets_df['class']" in __solution__, "Вы выбираете зависимую переменную в качестве Y?"

    __msg__.good("Отлично!")