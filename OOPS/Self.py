class Car():
    car_id = 0
    car_brand = None
    car_color = None
    car_speed = 0
    car_hybrid = True

    def showDetails(self):
        print(self.car_id,self.car_brand,self.car_color,self.car_speed)

car_1 = Car()
car_1.car_id = 101
car_1.car_brand = 'Tata'
car_1.car_color = 'White'
car_1.car_speed = 200

car_1.showDetails()

car_2 = Car()
car_2.car_id = 102
car_2.car_brand = 'BMW'
car_2.car_color = 'BLACK'
car_2.car_speed = 400

car_2.showDetails()