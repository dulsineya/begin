# encoding=utf8

import os
import psutil
import shutil
import sys
import random
g=8
def rand_dupl(dirname):
    file_list = os.listdir(dirname)
    b = len(file_list)
    a = random.randrange(0,b)
    f = file_list[a]
    fullname = os.path.join(dirname, f)
    if os.path.isfile(fullname):
        newfile = fullname + ".dupl"
        shutil.copy(fullname, newfile)
    return os.path.exists(newfile)
    #     print ("файл", newfile, "создан")
    #     return True
    # else:
    #     print ("ошибка копирования")
    #     return False


def rand_delete(dirname):
    file_list = os.listdir(dirname)
    b = len(file_list)
    a = random.randrange(0, b)
    f = file_list[a]
    filename = os.path.join(dirname, f)
    if os.path.isfile(filename):
        os.remove(filename)
    return not os.path.exists(filename)


def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + ".dupl"
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print ("файл", newfile, "создан")
            return True
        else:
            print ("ошибка копирования")
            return False


def dupl_delete(dirname):

    file_list = os.listdir(dirname)
    dupl_count = 0
    for f in file_list:
        fullname = os.path.join(dirname, f)
        if fullname.endswith(".dupl"):
            os.remove(fullname)
            if not os.path.exists(fullname):
                print ("файл", fullname, "удален")
                dupl_count += 1
    return dupl_count


def sys_info():
    print ("количество процессов:", psutil.cpu_count())
    print("платформа:", sys.platform)
    print("кодировка файловой системы:", sys.getfilesystemencoding())
    print ("текуая директория:", os.getcwd())
    print ("текущий пользователь:", os.getlogin())


def main():



    print ("привет")
    name = input("ваше имя: ")
    print(name, ",добро пожаловать в наш справочник, идиот!")
    answer = ' '
    while answer != "q":
        answer = input("вы хотели что-то узнать?[да/нет/q]")
        if answer == 'да':
            print ("[1]-посмотреть список файлов")
            print ("[2]-узнать информацию о системе")
            print ("[3]-вывести список процессов")
            print ("[4]-продублировать файлы")
            print ("[5]-дублировать указанный файл")
            print ("[6]-удалить дубликаты из выбранной директории")
            print ("7 - delete random file")
            print ("8 - dublicate random file")
            do = int(input("выберите из списка"))
            if do == 1:
                print(os.listdir())
            if do == 2:
                 sys_info()
            if do == 3:
                print (psutil.pids())
            if do == 4:
                print ("дублироване файлов")
                file_list = os.listdir()
                i = 0
                while i < len(file_list):
                    duplicate_file(file_list[i])
                    i += 1

            if do == 5:
                filename=input("укажите имя файла:")
                duplicate_file(filename)
            if do == 6:
                dirname = input("укажите директорию")
                count = dupl_delete(dirname)
                print ("удалено", count, "файлов")
            if do == 7:     #удаление случайного файла
                if rand_delete("/Applications/test"):
                    print ("файл удален")
                else:
                    print ("ошибка удаления")
            if do == 8:
                x = rand_dupl("/Applications/test")
                if x:
                    print ("файл создан")
                else:
                    print ("ошибка копирования")

                # if random_dupl("/Applications/test"):
                #     print ("ok")
                # else:
                #     print ("false")




            else:
                pass
        elif answer == "нет":
            print ("до свидания")


if __name__ == "__main__":
    main()
