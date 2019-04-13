# tarMerger
# v.: 0.9
# Intervision ©

import glob, os, sys


print('Укажите путь до директории с архивами или пропустите этот шаг, если операция выполняется в текущей директории')
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
    print('ERR: #010: Указанная директория отсутствует или задана неверно.')
    sys.exit("Остановка выполнения")
print('====================')
if glob.glob("*.tgz"):
    print('Обнаружены следующие архивы:')
    for file in glob.glob("*.tgz"):
        print(file)
else:
    print('ERR: #310: Архивы отсутствуют')
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
#else if yesNo == "n":

#else if yesNo == "y":
    
#else:
