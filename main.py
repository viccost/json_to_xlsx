from pandas import read_json
from pandas import json_normalize
from os import path
from salvar_ajustar.salvar_ajustar import escolher_arquivo
from salvar_ajustar.salvar_ajustar import salvar_arquivo_planilha
import json
from pprint import pprint
import xlsxwriter


def transform():
    """useful when the json data from an scraper/extraction contains \n (10) \r (13) ASCIICODE and amount of line breaks,
    then the text is splitted and this problem is solved
    https://stackoverflow.com/questions/1761051/difference-between-n-and-r/1761086"""

    file_local = escolher_arquivo()
    file_name = path.basename(file_local)
    json_file = read_json(file_local)
    local_save = path.dirname(file_local)
    column_name = 'div'  # column's data to manipulate

    for i in json_file.index:
        to_manipulating = json_file.at[i, column_name]
        to_manipulating = ' '.join(to_manipulating.replace("\n", "#").split())
        json_file.at[i, column_name] = to_manipulating

    json_file.to_excel(f'{local_save}/{file_name}.xlsx', index=False)
    print(f'Arquivo salvo em {local_save}')


def read_json_extra_data_problem():
    """this was used when I tried to read a json file that was reporting me a Extra Data file, what means that there are
    two json data in the file"""
    test = []
    for line in open(escolher_arquivo(), 'r'):
        test.append(json.loads(line))
    df = json_normalize(test)
    salvar_arquivo_planilha(df, 'dutra', 'xlsx')


if __name__ == '__main__':
    read_json_extra_data_problem()
