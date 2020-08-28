import os.path as path
from typing import List, Dict

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
from pandas import DataFrame


def export_each_column_to_csv(file_read_path: str, colums_names: List[str], sep=';'):
    df = pd.read_csv(file_read_path, sep)
    dirname = path.dirname(file_read_path) + path.sep

    for col in colums_names:
        df[col].to_csv(f"{dirname}{col}.csv", sep, index=False, header=True)


def plot_bar_graph(df: DataFrame, column_x_name: str):
    sb.countplot(data=df, x=column_x_name, palette=sb.color_palette('YlOrRd'))
    plt.show()


def plot_histogram(df: DataFrame):
    sb.distplot(df, kde=False)
    plt.show()


def str_num_to_float(num_str: str) -> float:
    return float(num_str.split()[0].replace(',', '.'))


def plot_pie_graph(labels: List[str], values: List[int]):
    explode = [0 for i in range(len(labels))]
    fig1, ax1 = plt.subplots()
    ax1.axis('equal')
    ax1.pie(values, explode, labels, autopct='%1.1f%%', startangle=30, labeldistance=1.05)
    plt.show()


def main():
    sb.set_style('darkgrid')
    dirname = '../data/microdados_enade_2018/2018/3.DADOS'
    sep = ';'
    # dirname_file_full = f'{dirname}/microdados_enade_2018.csv'
    cols = ['CO_RS_I1', 'CO_RS_I3', 'NT_GER', 'QE_I01', 'QE_I02', 'QE_I08']

    # Gráficos de barras
    # for i in range(2):
    #     plot_bar_graph(pd.read_csv(f"{dirname}/{cols[i]}.csv", sep), cols[i])

    # Histograma
    # plot_histogram(pd.read_csv(f"{dirname}/{cols[2]}.csv", sep).apply(str_num_to_float))

    # Gráficos de pizza
    ans_labels = [
        {
            'A': 'Solteiro(a)', 'B': 'Casado(a)', 'C': 'Separado(a) judicialmente/divorciado(a)',
            'D': 'Viúvo(a)', 'E': 'Outro'
        },
        {
            'A': 'Branca', 'B': 'Preta', 'C': 'Amarela', 'D': 'Parda',
            'E': 'Indígena', 'F': 'Não quero declarar'
        }
    ]

    for i in range(2):
        col_name = cols[i + 3]
        df = pd.read_csv(f"{dirname}/{col_name}.csv", sep)
        count: Dict[str, int] = df[col_name].value_counts()
        values = [count[ans] for ans in ans_labels[i]]
        labels = [ans_labels[i][ans] for ans in ans_labels[i]]
        plot_pie_graph(labels, values)

    # Obs: dados NaN ou NA é sinônimo de sem resposta
    return 0


main()
