softName = 'TarMerger'
ver = '1.1.6'
author = 'Intervision'

about = [softName, author, ver]
delimiter = '===================='

import glob, os, sys, crayons, colorama, datetime

colorama.init()
print(crayons.cyan('{} by {}\nVesion:{}', bold=True).format(*about))
print(delimiter)


nowDate = (datetime.datetime.today().strftime("%d-%m-%y_%H-%M"))
nowDateLog = (datetime.datetime.today().strftime("%d/%m/%y %H:%M:%S"))
logfile = open(nowDate + ".log", "w")
logfile.write(nowDateLog + " >> Начало работы скрипта\n")
logfile.write(nowDateLog + " >> " + softName + " " + ver + "\n\n")
print('Укажите путь до директории с архивами или пропустите этот шаг,\nесли операция выполняется в текущей директории')
tarDir = input()
if tarDir == "":
      tarDir = os.getcwd()
      print('Не указан путь. Используется текущая директория:')
      print(tarDir)
      logfile.write(nowDateLog + " >> Директория не указана. Используемая дриектория: " + tarDir + "\n")
else:
    print('Попытка использовать указанный путь:')
    print(tarDir)

try:
    os.chdir(tarDir)
except FileNotFoundError:
    print(crayons.red('ERR: #010:', bold=True) + ' Указанная директория отсутствует или задана неверно.')
    logfile.write(nowDateLog + " >> ERR: #010: Директория отсутствует или задана неверно: " + tarDir + "\n")
    logfile.exit()
    sys.exit("Остановка выполнения")
print(delimiter)
if glob.glob("*.tgz"):
    print('Обнаружены следующие архивы:')
    logfile.write(nowDateLog + " >> Обнаруженные архивы:\n\n")
    for file in glob.glob("*.tgz"):
        print(file)
        logfile.write(file + "\n")
else:
    print(crayons.yellow('ERR: #310:', bold=True) + ' Архивы отсутствуют')
    logfile.write(nowDateLog + " >> ERR: #310: Архивы отсутствуют\n")
    print('Нажмите любую клавишу для завершения')
    exitKey = input()
    logfile.close()
    sys.exit("Остановка выполнения")

print(delimiter)
print('Обнаружены следующие тома архивов:')
logfile.write(nowDateLog + " >> Обнаружены тома архивов:\n\n")
from natsort import natsorted
files = natsorted(glob.glob("*.tgz.part*"))
for file in files:
    print (file)
    logfile.write(file + "\n")

print(delimiter)
print('Будет произведена попытка склейки всех имеющихся томов в данной директории!')
print('Продолжить? [Y/n]')
yesNo = input()
if yesNo == "Y":      
    print('Получено подтверждение.')
    logfile.write(nowDateLog + " >> Получено подтверждение на запуск склейки. Попытка собрать архив...\n")
    print(delimiter)
    print('Укажите название готового файла (Без расширения)')
    finalArc = input() or "MergedArchive"
    print(crayons.white('Целевой файл: ') + crayons.white(finalArc + '.tgz', bold=True))
    logfile.write(nowDateLog + " >> Имя целевого архива: " + finalArc + ".tgz\n")
    print('Выполняется склейка томов архивов...')
    mergedParts = ' + '.join(files)
    commandMerge = 'copy /B ' + mergedParts + ' ' + finalArc + '.tgz'
    os.system(commandMerge)
    print('Тома архива объединены')
    logfile.write(nowDateLog + " >> Тома объединены в архив\n")
    print (delimiter)
    print ('Использована команда')
    print(commandMerge)
    logfile.write(nowDateLog + " >> Использована команда:\n\n")
    logfile.write(commandMerge + "\n\n")
    print(delimiter)
    print('Нажмите любую клавишу для выхода')
    exitKey = input()
elif yesNo == "n":
      print('ERR: #301: Получена команда отмены операции')
      logfile.write(nowDateLog + " >> ERR: #301: Получена команда отмены операции\n")
      logile.close()
      sys.exit('Остановка выполнения')

elif yesNo == "y":
      print(crayons.yellow('ERR: #302:', bold=True) + ' Для подтверждения используйте букву Y (регистр имеет значение!)')
      exitKey =input()
      logwile.write(nowDateLog + " >> ERR: #302: Неверный регистр ответа\n")
      logfile.close()
      sys.exit('Регистр ответа неверен')
else:
      print(crayons.yellow('ERR: #303:', bold=True) + ' Команда не распознана')
      logfile.write(nowDateLog + " >> ERR: #303: Неверная команда\n")
      print('Нажмите любую клавишу для завершения')
      exitKey = input()
      logile.close()
      sys.exit('Команда не распознана')

logfile.close()
