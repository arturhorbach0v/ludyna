class Человек:
    color = "white"

    def __init__(self,Фамилия,Имя,Отчество):
        self.Фамилия = Фамилия
        self.Имя = Имя
        self.Отчество = Отчество


    def show_info(self):
        print("Фамилия:", self.Фамилия)
        print("Имя:", self.Имя)
        print("Отчество:", self.Отчество)

    def set_Фамилия(self, newФамилия):
        self.Фамилия = newФамилия

    def set_Имя(self, newИмя):
        self.Имя = newИмя

    def set_Отчество(self, newОтчество):
        self.Отчество = newОтчество

myЧеловек = Человек("Горбачев", "Артур", "Денисович")
myЧеловек.show_info()
