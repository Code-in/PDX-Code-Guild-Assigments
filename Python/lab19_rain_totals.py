
from datetime import datetime
import re
import math
import matplotlib.pyplot as plt
from datetime import datetime


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# RainData Class for loading and computing rain statistics...
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class DailyRainData():
    def __init__(self, date, rain_total):
        self.date = datetime.strptime(date, '%d-%b-%Y')
        self.rain_total_in_tips = rain_total
        self.inch_converter = .01

    def get_rain_in_tips(self):
        return self.rain_total_in_tips

    def get_rain_in_inches(self):
        return self.rain_total_in_tips * self.inch_converter

    def get_date(self):
        return self.date.strftime("%Y/%m/%d")

    def get_year(self):
        return self.date.strftime("%Y")

    def get_month(self):
        return self.date.strftime("%m")

    def get_month_and_day(self):
        return self.date.strftime("%m/%d")

    def __str__(self):
        return f'Date:{self.date.strftime("%Y/%m/%d")} in:{self.rain_total_in_tips*self.inch_converter}'

    def __repr__(self):
        return self.__str__()


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# RainData Class for loading and computing rain statistics...
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class RainData():
    def __init__(self, data_path):
        self.path = data_path
        self.data = None
        self.days = []
        self.lab_19_version_1() # Load the data
        self.lab_19_version_2() # Process the data 
        self.lab_19_version_3() # Process the data 

    def lab_19_version_1(self):
        self.data = self.read_data_from_absolute_path()  # read the data from a absolute path

    def lab_19_version_2(self):
        if self.data is not None:
            self.parse_text_into_row_data(self.data)


        print(f'Number of rows: {self.compute_num_of_daily_totals(self.days)}')
        print(f'Rain sum of all rain totals: {self.compute_sum_of_daily_totals(self.days)}')

        mean = self.compute_mean()       
        print(f'Compute the mean of rain totals: {mean}')

        varaince = self.compute_variance()
        print(f'Rain Variance: {varaince}')
        print(f'Std Deviation: { math.sqrt(varaince) }')
        
        day = self.find_largest_daily_rainfall_amount(self.days)
        print(f'Most Rain Fall in 1 day: { day.get_date() } was { day.get_rain_in_inches() }" ')


    def lab_19_version_3(self):
        self.draw_specific_year_plot('2006', self.days) # plot the data for the year of 2018

    # read data from an absolute path in an instance variable 
    def read_data_from_absolute_path(self):
        data = ''
        with open(self.path, 'r') as file:
            data = file.read()
        #print(self.data)
        return data

    # Class Method - break the text in to a sepcified regx pattern then saves them into a list of tuples
    def parse_text_into_row_data(self, data):
        regex = r'(\d+[-]\w+[-]\d+)\s+(\d+)'
        row_tuple_list_data=re.findall(regex, data)
        self.convert_tuple_list_into_dailyraindata(row_tuple_list_data)
        #print(self.row_tuple_list_data)

    def convert_tuple_list_into_dailyraindata(self, list_tuples_dates_rain):
        for daily in list_tuples_dates_rain:
            date = daily[0] # Get string date from the tuple from the regex output list
            rain_fall = int(daily[1])  # Get rainfall from the tuple from the regex output list
            drd = DailyRainData(date, rain_fall)
            self.days.append(drd)
        #print(self.days)

    # Class Method - to return the number of days in rain data
    def compute_num_of_daily_totals(self, days):
        return len(days)

    # Class Method - to compute the mean of rain data
    def compute_mean(self):
        mean = self.compute_sum_of_daily_totals(self.days) / self.compute_num_of_daily_totals(self.days)
        return round(mean, 8)      
    
    # Class Method - to compute the vaiance of rain data
    def compute_variance(self):
        sum_of_all_rain_varaince_totals = 0
        mean = self.compute_mean()
        for day in self.days:
            sum_of_all_rain_varaince_totals += (day.get_rain_in_inches() - mean)**2
        variance = sum_of_all_rain_varaince_totals / self.compute_num_of_daily_totals(self.days)
        return variance


    # Class Method - compute the sum of the daily totals
    def compute_sum_of_variance_totals(self, days):
        sum_of_daily_rain_totals = 0
        for day in days:
            sum_of_daily_rain_totals  += day.get_rain_in_inches()
        return round(sum_of_daily_rain_totals, 2)

    # Class Method - compute the sum of the daily totals
    def compute_sum_of_daily_totals(self, days):
        sum_of_daily_rain_totals = 0
        for day in days:
            sum_of_daily_rain_totals  += day.get_rain_in_inches()
        return round(sum_of_daily_rain_totals, 2)

    # Class Method - finds the largest single daily total of rain in the rain data
    def find_largest_daily_rainfall_amount(self, days):
        largest_daily_rainfall = 0
        largest_daily_rainfall_object = None
        for day in days:
            rainfall = day.get_rain_in_inches()
            if rainfall > largest_daily_rainfall:
                largest_daily_rainfall = rainfall
                largest_daily_rainfall_object = day
        print(largest_daily_rainfall_object)
        return largest_daily_rainfall_object

    # Class Method - compute the sum of the daily variances
    def compute_sum_of_daily_variance(self, days):
        sum_of_all_rain_varaince_totals = 0
        mean = self.compute_mean()
        for day in days:
            daily_total = day.get_rain_in_inches()
            sum_of_all_rain_varaince_totals +=  (daily_total - mean)**2
            #print(f'daily variance: {(daily_total - self.mean)**2}')
        self.sum_of_all_rain_varaince_totals = sum_of_all_rain_varaince_totals
        return sum_of_all_rain_varaince_totals

    

    # Class Method - Draw the data for a specific year to a MatPlotLib view
    def draw_specific_year_plot(self, year, days):
        year_data = None
        x_values_list = []
        y_values_list = []

        for day in days:
            year_of_day = day.get_year() # get the date from the tuple for each row
            if year in year_of_day:
                x_values_list.append(day.get_month_and_day())
                y_values_list.append(day.get_rain_in_inches())
        plt.plot(x_values_list, y_values_list)
        plt.show()       





#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Runtime code
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

absolute_path = r'/Users/pparks/Desktop/PDX-Code-Guild-Assigments/Python/hayden_island.clean.txt'
prd = RainData(absolute_path)
prd.read_data_from_absolute_path()
