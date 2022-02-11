from pandas import read_json
from os import path


def transform():
    from salvar_ajustar.salvar_ajustar import escolher_arquivo
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


if __name__ == '__main__':
    transform()
