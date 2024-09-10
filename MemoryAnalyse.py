import os


class MemoryAnalyse:

    def __init__(self, big_size, dir):
        self.found_files = {}
        self.size = big_size
        if dir == '':
            dir = os.getcwd()
        self.path = dir

    def finder(self):
        self.walker(self.path)
        if self.found_files != {}:
            with open('found_big_files.txt', 'w') as file:
                for key, value in self.found_files.items():
                    file.write(f'Путь: {str(key)}\tРазмер, Гб:  {value} \n')
        return self.found_files

    def walker(self, path):

        try:
            self.size = float(self.size)
            for name in os.listdir(path):
                abs_name = os.path.join(path, name)
                if os.path.isfile(abs_name):
                    file_size = os.path.getsize(abs_name)
                    if file_size > self.size * (1024 ** 3):
                        file_size = round(file_size / 1024 ** 3, 2)
                        print("Найден файл: ", abs_name, ", Его размер:", file_size, " Гбайт")
                        self.found_files[abs_name] = file_size
                elif os.path.isdir(abs_name):
                    self.walker(abs_name)

        except PermissionError:
            print("Нет прав доступа к папке")

        except FileNotFoundError:
            print("Такого пути не существует")

        except OSError:
            print("Недопустимое значение пути")

        except ValueError:
            print("Недопустимое значение размера")
