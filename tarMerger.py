
softName = 'TarMerger'
ver = '1.1.5'
author = 'Intervision'

about = [softName, author, ver]
delimiter = '===================='

import glob, os, sys, crayons, colorama

colorama.init()
print(crayons.cyan('{} by {}\nVesion:{}', bold=True).format(*about))
print(delimiter)

print('Укажите путь до директории с архивами или пропустите этот шаг,\nесли операция выполняется в текущей директории')
tarDir = input()
if tarDir == "":
      tarDir = os.getcwd()
      print('Не указан путь. Используется текущая директория:')
      print(tarDir)
else:
    print('Попытка использовать указанный путь:')
    print(tarDir)

try:
    os.chdir(tarDir)
except FileNotFoundError:
    print(crayons.red('ERR: #010:', bold=True) + ' Указанная директория отсутствует или задана неверно.')
    sys.exit("Остановка выполнения")
print(delimiter)
if glob.glob("*.tgz"):
    print('Обнаружены следующие архивы:')
    for file in glob.glob("*.tgz"):
        print(file)
else:
    print(crayons.yellow('ERR: #310:', bold=True) + ' Архивы отсутствуют')
    print('Нажмите любую клавишу для завершения')
    exitKey = input()
    sys.exit("Остановка выполнения")

print(delimiter)
print('Обнаружены следующие тома архивов:')
from natsort import natsorted
files = natsorted(glob.glob("*.tgz.part*"))
for file in files:
    print (file)

print(delimiter)
print('Будет произведена попытка склейки всех имеющихся томов в данной директории!')
print('Продолжить? [Y/n]')
yesNo = input()
if yesNo == "Y":      
    print('Получено подтверждение.')
    print(delimiter)
    print('Укажите название готового файла (Без расширения)')
    finalArc = input() or "MergedArchive"
    print(crayons.white('Целевой файл: ') + crayons.white(finalArc + '.tgz', bold=True))
    print('Выполняется склейка томов архивов...')
    mergedParts = ' + '.join(files)
    commandMerge = 'copy /B ' + mergedParts + ' ' + finalArc + '.tgz'
    #os.system(commandMerge)
    print('Тома архива объединены')
    print (delimiter)
    print ('Использована команда')
    print(commandMerge)
    print(delimiter)
    print('Нажмите любую клавишу для выхода')
    exitKey = input()
elif yesNo == "n":
      print('ERR: #301: Получена команда отмены')
      sys.exit('Остановка выполнения')

elif yesNo == "y":
      print(crayons.yellow('ERR: #302:', bold=True) + ' Для подтверждения используйте букву Y (регистр имеет значение!)')
      exitKey =input()
      sys.exit('Регистр ответа неверен')
else:
      print(crayons.yellow('ERR: #303:', bold=True) + ' Команда не распознана')
      print('Нажмите любую клавишу для завершения')
      exitKey = input()
      sys.exit('Команда не распознана')
