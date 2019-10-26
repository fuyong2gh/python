cars =100# 车有10辆
space_in_a_car = 4 #每一辆车有4个空位置
drivers=30 #一共30个司机
passengers=90#乘客一共90人
cars_not_driven = cars-drivers#根据司机人数计算出不能开的车
cars_driven=drivers#能开出去的车数量等于人数
carpool_capacity=cars_driven*space_in_a_car#能够容纳的人总数
average_passengers_per_car=passengers/cars_driven#平均每一辆车是多少人


print('There are',cars,'cars available.')
print('There are only',drivers,'drivers available.')
print('There will be',cars_not_driven,'empty cars today.')
print('We can transport',carpool_capacity,'to carpool today.')
print('We need to put about',average_passengers_per_car,'in each car.')
