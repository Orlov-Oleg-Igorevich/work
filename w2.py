import os


def reading(way):
    files = os.listdir(way)
    file_list = []
    for file in files:
        with open(f'{way}/{file}', 'r', encoding="utf-8") as f:
            file_list.append((file, f.read().strip() + "\n"))
    file_list.sort(key=lambda x: len(x[1]))        
    return file_list


def write(way, file_list):
    with open(f'{way}/Результат.txt', "w") as t:
        for file in file_list:
            t.write(file[0] + "\n")
            t.write(str((file[1].count("\n"))) + "\n")
            t.write(file[1])


def main(way = 'C:/Users/Oleg/Desktop/Новая папка'):
    file_list = reading(way)
    write(way, file_list)
    print("Файл записан")


main()