import os.path as path

import pandas as pd

from graph import *


def export_each_column_to_csv(file_read_path: str, colums_names: List[str], sep=';'):
    df = pd.read_csv(file_read_path, sep)
    dirname = path.dirname(file_read_path)

    for col in colums_names:
        df[col].to_csv(f"{path.join(dirname, col)}.csv", sep, index=False, header=True)


def main():
    sb.set_style('darkgrid')
    dirname = '../data/microdados_enade_2018/2018/3.DADOS'
    dirname_file_full = f'{dirname}/microdados_enade_2018_edit.csv'
    df = pd.read_csv(dirname_file_full, sep=';', decimal=',')
    bar_graphs: List[Graph2D] = [
        Graph2D(
            'CO_RS_I1', None, 'Percepção de dificuldade da prova', 'Nível de dificuldade', 'Número de votos',
            {
                'A': 'Muito fácil', 'B': 'Fácil', 'C': 'Médio', 'D': 'Difícil',
                'E': 'Muito difícil', '.': 'S/ resp.', '*': 'Anulada'
            }
        ),
        Graph2D(
            'CO_RS_I3', None, 'Percepção de duração da prova', 'Percepção de duração', 'Número de votos',
            {
                'A': 'Muito longa', 'B': 'Longa', 'C': 'Adequada', 'D': 'Curta',
                'E': 'Muito curta', '.': 'S/ resp.', '*': 'Anulada'
            }
        ),
    ]
    histograms: List[Graph2D] = [
        Graph2D(
            'NT_GER', None, 'Histograma de notas', 'Nota bruta da prova', 'Quantidade de notas'
        )
    ]
    pie_graphs: List[Graph2D] = [
        Graph2D(
            'QE_I01', None, 'Distribuição por estado civil', 'Estado civil', 'Número de candidatos',
            {'A': 'Solteiro', 'B': 'Casado', 'C': 'Separado / divorciado', 'D': 'Viúvo', 'E': 'Outro'}
        ),
        Graph2D(
            'QE_I02', None, 'Distribuição por cor/raça', 'Cor / raça', 'Número de candidatos',
            {'A': 'Branca', 'B': 'Preta', 'C': 'Amarela', 'D': 'Parda', 'E': 'Indígena', 'F': 'Não declarada'}
        ),
    ]
    boxplot_graphs: List[Graph2D] = [
        Graph2D(
            'QE_I08', 'NT_GER', 'Nota bruta por rendimento familiar', 'Rendimento familiar (Em salário mínimo)',
            'Nota bruta',
            {
                'A': 'Até 1.5', 'B': '1.5 a 3', 'C': '3 a 4.5', 'D': '4.5 a 6',
                'E': '6 a 10', 'F': '10 a 30', 'G': 'Mais de 30'
            }
        ),
        Graph2D(
            'QE_I04', 'NT_GER', 'Nota bruta por escolaridade do pai', 'Escolaridade do pai', 'Nota bruta',
            {
                'A': 'Nenhuma', 'B': '1ª a 4ª série', 'C': '5ª a 8ª série',
                'D': 'Ensino médio', 'E': 'Graduação', 'F': 'Pós-graduação'
            }
        ),
    ]
    graphs_bonus: List[Graph2D] = [
        Graph2D(
            'QE_I15', 'NT_GER', 'Nota bruta por ação afirmativa', 'Ação afirmativa', 'Nota bruta média',
            {
                'A': 'Não', 'B': 'Étnico-racial', 'C': 'Renda', 'D': 'E. pública ou bolsa',
                'E': 'Múltip. critérios', 'F': 'Sistema diferente'
            }
        ),
        Graph2D(
            'QE_I17', 'NT_GER', 'Nota bruta por escola (ensino médio)', 'Tipo de escola', 'Nota bruta média',
            {
                'A': 'Pública', 'B': 'Particular', 'C': 'Exterior',
                'D': 'Púb. (majorit.)', 'E': 'Part. (majorit.)',
                'F': 'Brasil e exterior'
            }
        ),
        Graph2D(
            'QE_I23', 'NT_GER', 'Nota bruta por horas de estudo semanal', 'Horas de estudo', 'Nota bruta média',
            {'A': '0 - só vê às aulas', 'B': '1 a 3', 'C': '4 a 7', 'D': '8 a 12', 'E': '+12'}
        )
    ]

    # Gráficos de barras
    for g in bar_graphs:
        plot_bar_graph(df, g.x_col, g.title, g.xlabel, g.ylabel, g.label_categories)

    # Histograma
    for h in histograms:
        plot_histogram(df[h.x_col], h.title, h.xlabel, h.ylabel)

    # Gráficos de pizza
    for g in pie_graphs:
        count: Dict[str, int] = df[g.x_col].value_counts()
        values = [count[ans] for ans in g.label_categories]
        labels = list(g.label_categories.values())
        plot_pie_graph(labels, values, g.title)

    # Gráficos boxplot
    for g in boxplot_graphs:
        plot_boxplot(df, g.x_col, g.y_col, g.title, g.xlabel, g.ylabel, g.label_categories)

    # Gráficos boxplot (extras)
    for g in graphs_bonus:
        plot_boxplot(df, g.x_col, g.y_col, g.title, g.xlabel, g.ylabel, g.label_categories)

    return 0


main()
