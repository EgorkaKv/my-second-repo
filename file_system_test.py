"""лабораторна 6"""
#тест внесення
#змін

class File:
    """Клас для определения файлов"""

    def __init__(self, name, extension, size, place='Desktop/'):
        self.name = name
        self.extension = extension
        self.size = size
        self.place = place

    def replace(self, new):
        """метод для перезаписи положения файла"""
        self.place = new

    def __str__(self):
        return f'class: File, name: {self.name}, ext: {self.extension}'


class Folder:
    """Клас для определения папок"""

    def __init__(self, name, fold_list='', file_list='', place='Desktop/'):
        self.name = name
        self.folders = fold_list
        self.files = file_list
        self.place = place
        self.replace()

    def replace(self, new='Desktop/'):
        """перезапись положения положения папки и всех вложенностей"""
        self.place = new
        for i in self.folders:
            i.replace(self.place + self.name + '/')
        for i in self.files:
            i.replace(self.place + self.name)

    def __str__(self):
        return f'class: File, name: {self.name}, place: {self.place}'


def path(top=''):
    """функция для вывода дерева файловой системы"""
    s = '    '
    tab = len(top.place.split('/')) - 2
    print(s * tab + top.name + ':')
    for i in top.folders:
        path(top=i)
    for i in top.files:
        print(s * (tab + 1) + i.name)


def test_replace_files():
    """тест класа files"""
    test = File('test', '.', 100)
    temp = 'new_pl'
    test.replace(temp)
    assert test.place == temp


def test_replace_folders():
    """test of class folders"""
    test = Folder('test')
    temp = 'new_pl'
    test.replace(temp)
    assert test.place == temp
