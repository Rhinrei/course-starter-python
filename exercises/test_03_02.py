def test():
    assert "ComplementNB" in __solution__, "Вы правильно импортируете библиотеку ComplementNB?"
    assert "ComplementNB()" in __solution__, "Вы создаете комплементарную модель Байеса при объявлении модели?"
    assert "fit(X_train, y_train)" in __solution__, "Вы обучаете модель на тренировочных данных?"
    assert "model.predict(X_test)" in __solution__, "Вы получаете предсказанные значения на тестовой выборке?"
    __msg__.good("Отлично!")