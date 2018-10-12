class Car():
    car_id = 0
    car_brand = None
    car_color = None
    car_speed = 0
    car_hybrid = True

car_1 = Car()
car_1.car_id = 101
car_1.car_brand = 'Tata'
car_1.car_color = 'White'
car_1.car_speed = 200

car_2 = Car()
car_2.car_id = 102
car_2.car_brand = 'BMW'
car_2.car_color = 'BLACK'
car_2.car_speed = 400

# print("Car Features : {}, {}, {}, {}".format(car_1.car_id,car_1.car_brand,car_1.car_color,car_1.car_speed))
# print("Car Features : {}, {}, {}, {}".format(car_2.car_id,car_2.car_brand,car_2.car_color,car_2.car_speed))

# print("Car_1 Hybrid".format(car_1.car_hybrid))

car_1.gear = False
print(car_1.__dict__)
print(car_2.__dict__)
