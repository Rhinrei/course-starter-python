def test():
    assert "sklearn.model_selection" in __solution__, "Вы правильно импортируете библиотеку train_test_split?"
    assert "X_train, X_test, y_train, y_test " in __solution__, "Вы создаете все необходимые обучающие и тестовые переменные?"
    assert "X, y, test_size=0.33, random_state=42" in __solution__, "Вы используете все упомянутые аргументы функции train_test_split?"

    __msg__.good("Отлично!")