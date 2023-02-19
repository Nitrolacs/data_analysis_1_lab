"""Основные функции для построения графиков"""
import pandas as pd
import matplotlib.pyplot as plt


def build_bar_and_pie_chart(dataframe: "pd.DataFrame", column_name: str,
                            variable_name: str) -> None:
    """
    Построение столбчатой и круговой диаграммы.
    :param dataframe:
    :param column_name:
    :param variable_name:
    :return:
    """
    count = dataframe[column_name].value_counts()
    fig = plt.figure(figsize=(15, 5))
    # Adds subplot on position 1
    ax = fig.add_subplot(121)
    # Adds subplot on position 2
    ax2 = fig.add_subplot(122)
    ax.bar(x=count.index, height=count.values)
    ax.set_title("Столбчатая диаграмма распределения " + variable_name +
                 " в выборке")
    ax2.pie(count.values, labels=count.index)
    ax2.legend(bbox_to_anchor=(0.9, 1))
    ax2.set_title("Круговая диаграмма распределения " + variable_name +
                  " в выборке")

    plt.setp([ax], xlabel='значения выборки', ylabel='частота')
    plt.show()


def build_histogram_density_diagram(dataframe: "pd.DataFrame", column_name: str,
                                    number: int):
    """
    Построение гистограммы, оценки плотности распределения и диаграммы
    "ящик с усами".
    :param dataframe:
    :param column_name:
    :param number:
    :return:
    """
    # dropna временно удаляет пустые значения, чтобы
    # избежать ошибки при построении
    num1 = dataframe[column_name].dropna()
    fig = plt.figure(figsize=(17, 5))
    ax = fig.add_subplot(131)
    ax2 = fig.add_subplot(133)
    ax3 = fig.add_subplot(132)
    ax.hist(num1, bins=100)
    ax.set_title("Гистограмма " + str(number) + " числового параметра")
    ax2.boxplot(x=num1)
    ax3.set_title(
        "Оценка функции плотности " + str(number) + " числового параметра")
    ax2.set_title("Диаграмма 'ящик с усами' " + str(number) +
                  " числового параметра")
    dataframe[column_name].plot.kde()
    plt.setp([ax, ax3], xlabel='значения выборки')
    plt.setp([ax2], xlabel='номер выборки', ylabel='разброс значений')
    plt.setp([ax], ylabel='частота')
    plt.setp([ax3], ylabel='вероятность')
    plt.show()


def build_histogram(dataframe: "pd.DataFrame", first_column: str,
                    second_column: str, third_column: str):
    fig = plt.figure(figsize=(17, 5))
    ax = fig.add_subplot(131)
    ax2 = fig.add_subplot(133)
    ax3 = fig.add_subplot(132)
    ax.hist(dataframe[first_column], bins=100)
    ax2.hist(dataframe[second_column], bins=100)
    ax3.hist(dataframe[third_column], bins=100)
    ax.set_title("Гистограмма 1 числового параметра")
    ax3.set_title("Гистограмма 2 числового параметра")
    ax2.set_title("Гистограмма 3 числового параметра")
    plt.setp([ax, ax2, ax3], xlabel='значения выборки', ylabel='частота')
    plt.show()