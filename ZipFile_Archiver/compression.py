import os
from zipfile import ZipFile, ZIP_DEFLATED

def compressing(d_name, c_lev):
    z = ZipFile(f'{d_name}.zip', 'w',
                compression=ZIP_DEFLATED,
                allowZip64=True,
                compresslevel=c_lev)
    print('Compressing...')
    for root, dirs, files in os.walk(d_name):  # Список всех файлов и папок в директории folder
        for file in files:
            z.write(os.path.join(root, file))  # Создание относительных путей и запись файлов в архив

    z.close()
    print('Complete!')

def unpacking(z_name):
    print('Unpacking...')
    with ZipFile(f"{z_name}.zip", "r") as myzip:
        myzip.extractall(path=f"{z_name}-unpack")
    print('Complete!')

def printcommands():
    print('Choose command:',
          '1 - Compressing files in Directory',
          '2 - Unpacking files from ZIP',
          '3 - View commands',
          '0 - exit', sep='\n')

printcommands()
while True:
    command = int(input())
    if command == 1:
        print('Enter directory name:', end=' ')
        directory_name = input()
        print('Enter compress Level (0-9):', end=' ')
        compress_lev = int(input())
        compressing(directory_name, compress_lev)
    elif command == 2:
        print('Enter ZIP name:', end=' ')
        zip_name = input()
        os.mkdir(f"{zip_name}-unpack")
        unpacking(zip_name)
    elif command == 3:
        printcommands()
    elif command == 0:
        break
    else:
        print('Wrong command. Print <3> to view commands')
