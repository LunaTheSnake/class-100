class Car(object):
    def __init__(self,price,modul,company,commoncolor):
        self.price=price
        self.modul=modul
        self.company=company
        self.commoncolor=commoncolor
    def start(self):
        print("car started")

    def stop(self):
        print("car stopped")

    def vroom(self):
        print(self.company,"has power")

kia=Car(25000,"kia1001","kia","silver")
kia.start()
kia.stop()
kia.vroom()

