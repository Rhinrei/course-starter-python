def test():
    assert "sklearn.metrics " in __solution__, "Вы правильно импортируете библиотеку accuracy_score?"
    assert "accuracy_score" in __solution__, "Вы используете метод accuracy_score?"
    assert "y_test" in __solution__, "Вы сравниваете тестовые значения целевой переменной?"
    assert "predicted" in __solution__, "Вы сравниваете предсказанные значения целевой переменной?"
    __msg__.good("Well done!")