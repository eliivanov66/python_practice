#класс хранилища
from UserInterface  import UserInterface as HMI

class Data():
    dbFile = ""
    def __init__(self, datafile):
        try:
            with open(datafile, "r", encoding="utf-8") as file:
                lines = file.readlines()
                self.dbFile = datafile
        except FileNotFoundError:
            HMI.outlet("Внимание!!! Файл данных не существует")
            key = ""
            while not key.lower().__eq__("y") and not key.lower().__eq__("n"):
                key = HMI.inlet("Создать новый файл данных Y/N?\n")
            if key.lower().__eq__("y"):
                with open(datafile, "w", encoding="utf-8") as file:
                    self.dbFile = datafile
    
    def info(self):
        with open(self.dbFile, "r", encoding="utf-8") as file:
            lines = file.readlines()
            retList = []
            #return len(lines)
            for line in lines:
                # разбиение строки на отдельные стролбцы
                lineData = str(line.replace(";\n", "")).split(";")
                retList.append(lineData[0])
            return retList
    
    def read(self, id):
        with open(self.dbFile, "r", encoding="utf-8") as file:
            lines = file.readlines()
        # поиск нужной нам строки в файле
        for line in lines:
            # разбиение строки на отдельные стролбцы
            lineData = str(line.replace(";\n", "")).split(";")
            if lineData[0].lower().__eq__(id.lower()):
                return lineData
        HMI.outlet("Чтение. Данные отсувуют в таблице")
        return -1
    
    def write(self, id, values):
        with open(self.dbFile, "r", encoding="utf-8") as file:
            lines = file.readlines()
            # проверка данных
            if len(values) == 0:
                HMI.outlet("Запись. Входные данные нулевого размера")
                return -1
            # проверка совпадает ли данные для вставки с данными в таблице
            if len(lines) > 0:
                lineData = str(lines[0].replace(";\n", "")).split(";")
                if (len(values) + 1) != (len(lineData)):
                    HMI.outlet("Запись. Размер входных данных и данных в таблице не совпадают")
                    return -1
        # строка для вставки в таблицу
        lineDataInsert = f"{id};"
        for i in values:
            lineDataInsert = f"{lineDataInsert}{i};"

        # проверка, существует ли запись уже в таблице
        for line in lines:
            lineData = str(line.replace(";\n", "")).split(";")
            # присутсвует
            if lineData[0].lower().__eq__(id.lower()):
                lineTarget = line
                lineDataOld = ""
                for i in lineData:
                    lineDataOld = f"{lineDataOld}{i};"
                # запрос на перезапись       
                key = ""
                while not key.lower().__eq__("y") and not key.lower().__eq__("n"):
                    HMI.outlet(f"В таблице присутсвует запись ({lineDataOld})")
                    HMI.outlet(f"В заменить её на ({lineDataInsert})")
                    key = HMI.inlet("Заменить Y/N?\n")
                if key.lower().__eq__("n"):
                    return 0  # пользователь не заменил запись
                if key.lower().__eq__("y"):
                    with open(self.dbFile, "w", encoding="utf-8") as file:
                        for i in lines:
                            if i != lineTarget:
                                file.write(i)
                            else:
                                file.write(f"{lineDataInsert}\n")
                        return 0  # пользователь заменил запись
        # запись отсуствует в таблице, просто создаём новую запись
        with open(self.dbFile, "a", encoding="utf-8") as file:
            file.write(f"{lineDataInsert}\n")
            return 0
        
    def remove(self, id):
        with open(self.dbFile, "r", encoding="utf-8") as file:
                lines = file.readlines()
        # поиск записи в таблице
        for line in lines:
            # запись найдена
            lineData = str(line.replace(";\n", "")).split(";")

            if lineData[0].lower().__eq__(id.lower()):
                key = ""
                while not key.lower().__eq__("y") and not key.lower().__eq__("n"):
                    HMI.outlet(f"В таблице присутсвует запись ({lineData})")
                    key = HMI.inlet("Удалить Y/N?\n")
                if key.lower().__eq__("n"):
                    return 0  # пользователь не удалил запись
                if key.lower().__eq__("y"):
                    with open(self.dbFile, "w", encoding="utf-8") as file:
                        # запись всех строк, кроме той что должна быть удалена
                        for i in lines:
                            if i != line:
                                file.write(i)
                        return 0
        HMI.outlet("Удаление. Данные отсувуют в таблице")
        return -1
    
    def find(self, critery):
        retList = []
        with open(self.dbFile, "r", encoding="utf-8") as file:
            lines = file.readlines()
        # поиск нужной нам строки в файле
        for line in lines:
            # разбиение строки на отдельные стролбцы
            lineData = str(line.replace(";\n", "")).split(";")
            for elementData in lineData:
                if str(critery).lower() in elementData.lower():
                    retList.append(lineData)
        if len(retList) != 0:
            return retList
        HMI.outlet("Поиск. Данные отсувуют в таблице")
        return -1