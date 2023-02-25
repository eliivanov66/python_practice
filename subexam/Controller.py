from UserInterface  import UserInterface as HMI
from Data import Data
from TimeStamp import TimeStamp

class Controller:
    DB: Data

    def __init__(self, dataBase: Data):
        self.DB = dataBase

    def menu(self):
        HMI.clean()
        key = ""
        while key.lower() != "q":
            HMI.outlet("(========= /root/ =======)")
            HMI.outlet("1 - список")
            HMI.outlet("2 - создание")
            HMI.outlet("3 - редактирование")
            HMI.outlet("4 - удаление")
            HMI.outlet("q - выйти из приложения")
            key = HMI.inlet("Ваш выбор: ")
            match key:
                case "1":
                    HMI.clean()
                    HMI.outlet("(========= /root/list/ =======)")
                    self.list()
                case "2":
                    HMI.clean()
                    HMI.outlet("(========= /root/create/ =======)")
                    self.list()
                    self.create()
                case "3":
                    HMI.clean()
                    HMI.outlet("(========= /root/edit/ =======)")
                    self.list()
                    self.edit()
                case "4":
                    HMI.clean()
                    HMI.outlet("(========= /root/delete/ =======)")
                    self.list()
                    self.delete()

    def list(self):
        for i in self.DB.info():
            HMI.outlet(f"{i} - {self.DB.read(str(i))}")
    
    def create(self):
        header = HMI.inlet("Введите заголовок заметки: ")
        body = HMI.inlet("Введите текст заметки: ")
        if len(self.DB.info()) != 0:
            self.DB.write(str(int(self.DB.info()[len(self.DB.info()) - 1]) + 1), [header, TimeStamp.time(), body])
        else:
            self.DB.write(str(0), [header, TimeStamp.time(), body])
    
    def edit(self):
        localKey = ""
        while not (localKey.isnumeric() and localKey in self.DB.info()) and not (localKey.lower().__eq__("w")):
            localKey = HMI.inlet("Выберите заметку для редактирования, W - назад: ")
            if localKey.isnumeric():
                if localKey in self.DB.info():
                    HMI.outlet(f"Редактирование записи: {self.DB.read(localKey)}")
                    header = HMI.inlet("Введите заголовок заметки: ")
                    body = HMI.inlet("Введите текст заметки: ")
                    self.DB.write(localKey, [header, TimeStamp.time(), body])
                    localKey = "w"
    def delete(self):
        localKey = ""
        while not (localKey.isnumeric() and localKey in self.DB.info()) and not (localKey.lower().__eq__("w")):
            localKey = HMI.inlet("Выберите заметку для удаления, W - назад: ")
            if localKey.isnumeric():
                if localKey in self.DB.info():
                    self.DB.remove(localKey)
                    localKey = "w"