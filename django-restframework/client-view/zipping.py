import zipfile


# with open('test file.txt', 'w') as f:
#     f.write('hello world we are rocking')
#

with zipfile.ZipFile('files.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write('test file.txt')
    my_zip.write('oop.py')
