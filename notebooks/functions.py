"""Основные функции для построения графиков"""
import pandas as pd
import matplotlib.pyplot as plt


def build_bar_and_pie_chart(dataframe: "pd.DataFrame", column_name: str,
                            variable_name: str) -> None:
    """
    Построение столбчатой и круговой диаграммы.
    :param dataframe: датафрейм
    :param column_name: колонка
    :param variable_name: текстовое название колонки
    :return: None
    """
    count = dataframe[column_name].value_counts()
    fig = plt.figure(figsize=(15, 5))
    # Добавляет subplot на позицию 1
    ax = fig.add_subplot(121) # 121 - это первая строка, второй столбец и первая
                              # ячейка на сетке figure.
    # Добавляет subplot на позицию 2
    ax2 = fig.add_subplot(122)

    ax.bar(x=count.index, height=count.values)
    ax.set_title("Столбчатая диаграмма распределения " + variable_name)

    ax2.pie(count.values, labels=count.index, autopct="%1.1f%%")
    ax2.legend(bbox_to_anchor=(0.9, 1))
    ax2.set_title("Круговая диаграмма распределения " + variable_name)

    plt.setp([ax], xlabel='значения выборки', ylabel='частота')
    plt.show()


def build_histogram_density_diagram(dataframe: "pd.DataFrame", column_name: str,
                                    number: str) -> None:
    """
    Построение гистограммы, оценки плотности распределения и диаграммы
    "ящик с усами".
    :param dataframe: датафрейм
    :param column_name: колонка
    :param number: текстовое название колонки
    :return: None
    """
    # dropna временно удаляет пустые значения, чтобы
    # избежать ошибки при построении
    num1 = dataframe[column_name].dropna()
    fig = plt.figure(figsize=(19, 5))

    ax = fig.add_subplot(131)
    ax2 = fig.add_subplot(133)
    ax3 = fig.add_subplot(132)

    ax.hist(num1, bins="auto", edgecolor="black")
    ax.set_title("Гистограмма параметра " + number)

    ax2.boxplot(x=num1)
    ax3.set_title(
        "Оценка функции плотности параметра " + number)
    ax2.set_title("Диаграмма 'ящик с усами' параметра " + number)
    dataframe[column_name].plot.kde()
    plt.setp([ax, ax3], xlabel='значения выборки')
    plt.setp([ax2], xlabel='номер выборки', ylabel='разброс значений')
    plt.setp([ax], ylabel='частота')
    plt.setp([ax3], ylabel='вероятность')
    plt.show()


def build_histogram(dataframe: "pd.DataFrame", first_column: str,
                    second_column: str, third_column: str) -> None:
    """
    Построение гистограмм для всех количественных признаков.
    :param dataframe: датафрейм
    :param first_column: первая колонка
    :param second_column: вторая колонка
    :param third_column: третья колонка
    :return: None
    """
    fig = plt.figure(figsize=(17, 5))

    ax = fig.add_subplot(131)
    ax2 = fig.add_subplot(133)
    ax3 = fig.add_subplot(132)

    ax.hist(dataframe[first_column], bins="auto", edgecolor="black")
    ax2.hist(dataframe[second_column], bins="auto", edgecolor="black")
    ax3.hist(dataframe[third_column], bins="auto", edgecolor="black")

    ax.set_title("Гистограмма 1 числового параметра")
    ax3.set_title("Гистограмма 2 числового параметра")
    ax2.set_title("Гистограмма 3 числового параметра")

    plt.setp([ax, ax2, ax3], xlabel='значения выборки', ylabel='частота')
    plt.show()
