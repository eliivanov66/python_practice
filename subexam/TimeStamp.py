from datetime import datetime
class TimeStamp:
    def __init__(self) -> None:
        pass
    @staticmethod
    def time():
        return f"{datetime.now().year}/{datetime.now().month}/{datetime.now().day} {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
