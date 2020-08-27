from typing import List
import collections
import matplotlib.pyplot as plt
import os.path as path
import pandas as pd
import seaborn as sb


def export_each_column_to_csv(file_read_path: str, colums_names: List[str], sep=';'):
    df = pd.read_csv(file_read_path, sep)
    dirname = path.dirname(file_read_path) + path.sep

    for col in colums_names:
        df[col].to_csv(f"{dirname}{col}.csv", sep, index=False, header=True)


def main():
    dirname = '../data/microdados_enade_2018/2018/3.DADOS/'
    dirname_file_full = f'{dirname}/microdados_enade_2018.csv'
    df = pd.read_csv(dirname + 'CO_RS_I1.csv', sep=';')
    # cols = ['CO_RS_I1', 'CO_RS_I3', 'NT_GER', 'QE_I01', 'QE_I02', 'QE_I08']
    cont_pontos = {k: v for k, v in sorted(collections.Counter(df['CO_RS_I1']).items(), key=lambda item: item[1])}
    print(cont_pontos)

    # Obs: dados NaN ou NA é sinônimo de sem resposta
    sb.set_style('darkgrid')
    sb.countplot(data=df, x='CO_RS_I1', palette=sb.color_palette('YlOrRd'))
    plt.show()
    return 0


main()
