import os

path = 'C:\\txtfiles'  # Путь до папки с файлами


def update_files(path_to_file):
    counter = 1  # Счетчик строк
    file_count = 1  # Счетчик файлов
    files = os.listdir(path_to_file)
    file_list = [file for file in files if file.endswith('.txt')]  # Получения списка файлов txt в папке
    for file_ in file_list[::-1]:  # Пробежка по списку файлов с конца
        with open('C:\\txtfiles\\' + file_, encoding='utf-8') as f:  # Открытие файлов для чтения
            with open('C:\\txtfiles\\' + 'result_file.txt', 'a',
                      encoding='utf-8') as f1:  # Дозапись результирующего файла
                f1.write(file_ + '\n')
                f1.write(str(file_count) + '\n')
                for line in f:
                    f1.write(f'Строка номер {counter} {line.strip()} '
                             f'файла номер {file_list[file_list.index(file_)].rstrip(".txt")}' + '\n')
                    counter += 1
                counter = 1
                file_count += 1


update_files(path)  # Вызов функции и создание нового файла
