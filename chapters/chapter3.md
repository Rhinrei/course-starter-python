---
title: 'Глава 3: Наивная Байесовская модель'
description:
  'Основная модель для предсказания тональности.'
prev: /chapter2
next: /chapter1
type: chapter
id: 3
---

<exercise id="1" title="Как работает модель" type="slides">

<slides source="chapter3_01_theory">
</slides>

</exercise>

<exercise id="2" title="Для чего нужна модель?">
В каком случае пригодится мультиномиальная байесовская модель?
<choice>
<opt text="если все признаки принимают значения 0 или 1">

Увы.

</opt>

<opt text="если признаки нормально распределены" correct="true">

И это правильный ответ!

</opt>
<opt text="если признаки принимают разные значения, и выборка сбалансирована">

Не угадал.

</opt>
</choice>
</exercise>

<exercise id="3" title="Разделение выборки на тестовую и обучающую">
Импортируйте необходимую библиотеку и разделите выборку.
<codeblock id="03_01">

...

</codeblock>

</exercise>

<exercise id="4" title="Предсказание значений">
Создайте модель, обучите ее на тренировочных данных и предскажите значения целевой переменной на тестовых.
<codeblock id="03_02">

...

</codeblock>

</exercise>

<exercise id="5" title="Точность предсказания">
Вычислите точность предсказания модели из прошлого задания.
<codeblock id="03_03">

...

</codeblock>

</exercise>

<exercise id="6" title="Точность предсказания: подсчет">
Чему равна accuracy из предыдущего задания?
<choice>
<opt text="0,6">

Увы.

</opt>

<opt text="0,75" correct="true">

И это правильный ответ!

</opt>
<opt text="0,43">

Не угадал.

</opt>
</choice>
</exercise>
