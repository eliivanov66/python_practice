#класс ввода-вывода данных
import os
class UserInterface:
    def outlet(arg_msgtext):
        print(arg_msgtext)
        return 0
    
    def inlet(arg_msgtext):
        return input(arg_msgtext)
    
    def clean():
        if os.name == "nt":
            os.system('cls')
        elif os.name == "posix":
            os.system('clear')
        
