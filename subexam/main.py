
from Data import Data
from Controller import Controller

notes = Data("Notes.base") # файл с базой заметок, любого расширения, если не существует, то будет создан пустой
navigation = Controller(notes) # логика работы программы

navigation.menu()
