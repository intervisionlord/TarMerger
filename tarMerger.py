
softName = 'TarMerger'
ver = '1.1.4'
author = 'Intervision'

about = [softName, author, ver]

import glob, os, sys, crayons, colorama

colorama.init()
print(crayons.cyan('{} by {}\nVesion:{}', bold=True).format(*about))
print('====================')

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
print('====================')
if glob.glob("*.tgz"):
    print('Обнаружены следующие архивы:')
    for file in glob.glob("*.tgz"):
        print(file)
else:
    print(crayons.yellow('ERR: #310:', bold=True) + ' Архивы отсутствуют')
    print('Нажмите любую клавишу для завершения')
    exitKey = input()
    sys.exit("Остановка выполнения")

print('====================')
print('Обнаружены следующие тома архивов:')
from natsort import natsorted
files = natsorted(glob.glob("*.tgz.part*"))
for file in files:
    print (file)

print('====================')
print('Будет произведена попытка склейки всех имеющихся томов в данной директории!')
print('Продолжить? [Y/n]')
yesNo = input()
if yesNo == "Y":
    print('Получено подтверждение.')
    print('Выполняется склейка томов архивов...')
    mergedParts = ' + '.join(files)
    commandMerge = 'copy /B {} merged.tgz'.format(mergedParts)
    os.system(commandMerge)
    print('Тома архива объединены')
    print ('====================')
    print ('Использована команда')
    print(commandMerge)
elif yesNo == "n":
      print('ERR: #301: Получена команда отмены')
      sys.exit('Остановка выполнения')

elif yesNo == "y":
      print(crayons.yellow('ERR: #302:', bold=True) + ' Для подтверждения используйте букву Y (регистр имеет значение!)')
      sys.exit('Регистр ответа неверен')
else:
      print(crayons.yellow('ERR: #303:', bold=True) + ' Команда не распознана')
      print('Нажмите любую клавишу для завершения')
      sys.exit('Команда не распознана')
