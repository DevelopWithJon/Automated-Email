# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 18:13:09 2020

@author: joeyb
"""

class Student:
    
    def __init__(self):
        # this is an instance v
        self.name = None
    
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def __str__(self):
        return "This is a student"
    
def main():
    mike = Student()
    mike.set_name("Mike")
    print(mike.get_name())
    print(hex(id(mike)))
    print(mike)    

#if __name__ == '__main__':
#    main()
    
one_day_of_hourly_temperatures = [
67, 67, 68, 69, 71, 73, 75, 76,
79, 81, 81, 80, 82, 81, 81, 80,
78, 75, 72, 70, 67, 65, 66, 66
]

one_day_of_hourly_humidity = [
    60, 65, 65, 70, 70, 70, 70, 75,
    75, 75, 75, 80, 80, 85, 85, 85,
    85, 80, 80, 80, 80, 80, 80, 80
]

one_day_of_hourly_rainfall = [
    0, 0, 0, 0.1, 0.1, 0.05, 0.1, 0.15,
    0.2, 0.3, 0.3, 0.5, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0
]

number_of_years_of_data = 10
times_it_has_rained = 0

class Forecast:
    """
    Forecast class
    """
   
    
    def __init__(self, location, data):
        self.location = location
        self.data = data
        
    def get_daily_high(self):
        return max(self.data)
    def get_daily_low(self):
        return min(self.data)
    def get_daily_chance_of_rain(self):
        number_of_years_of_data = 10
        times_it_has_rained = 0
        sum_of_rain = sum(one_day_of_hourly_rainfall)
        if sum_of_rain > 0:
            times_it_has_rained += 1
        percent_of_times_it_has_rained = (times_it_has_rained / number_of_years_of_data) * 100
        return percent_of_times_it_has_rained
        

        
#test = Forecast("Austin, TX", one_day_of_hourly_temperatures)
#print("high:", test.get_daily_high())
#print("low:", test.get_daily_low())
#print("Chance of Rain:", test.get_daily_chance_of_rain(), '%')

grade_i = 22
grade_s = grade_i.__str__()
print(type(grade_s))
