
from datetime import datetime
import re
import math
import matplotlib.pyplot as plt
from datetime import datetime


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# RainData Class for loading and computing rain statistics...
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class RainData():
    def __init__(self, data_path):
        self.path = data_path
        self.data = ""
        self.row_tuple_list_data = []
        self.num_of_daily_totals = 0
        self.sum_of_daily_rain_totals = 0
        self.sum_of_all_rain_varaince_totals = 0
        self.variance = 0
        self.mean = 0
        self.largest_daily_tuple = None
        self.lab_19_version_1() # Load the data
        self.lab_19_version_2() # Process the data 
        self.lab_19_version_3() # Process the data 

    def lab_19_version_1(self):
        self.read_data_from_absolute_path()  # read the data from a absolute path

    # read data from an absolute path in an instance variable 
    def read_data_from_absolute_path(self):
        with open(self.path, 'r') as file:
            self.data = file.read()
        #print(self.data)

    def lab_19_version_2(self):
        self.parse_text_into_row_data()
        self.num_of_daily_totals = len(self.row_tuple_list_data)
        print(f'Number of rows: {self.num_of_daily_totals}')
        print(f'Rain sum of all rain totals: {self.compute_sum_of_daily_totals()}')
        self.mean = self.sum_of_daily_rain_totals / self.num_of_daily_totals        
        print(f'Rain sum of all rain variance totals: {self.compute_sum_of_daily_variance()}')
        self.variance = self.sum_of_all_rain_varaince_totals / self.num_of_daily_totals
        print(f'Rain Variance: {self.variance}')
        print(f'Std Deviation: { math.sqrt(self.variance) }')
        print(f'Most Rain Fall in 1 day: { self.largest_daily_tuple[0] } was { (int(self.largest_daily_tuple[1]) * .01) }" ')
        #print(self.row_tuple_list_data)

    def lab_19_version_3(self):
        self.draw_specific_year_plot('2018') # plot the data for the year of 2018

    # Class Method - break the text in to a sepcified regx pattern then saves them into a list of tuples
    def parse_text_into_row_data(self):
        regex = r'(\d+[-]\w+[-]\d+)\s+(\d+)'
        self.row_tuple_list_data=re.findall(regex, self.data)

    # Class Method - compute the sum of the daily totals
    def compute_sum_of_daily_totals(self):
        rain_total_tuple_index = 1
        sum_of_all_rain_totals = 0
        largest_daily_rainfall = 0
        for row in self.row_tuple_list_data:
            sum_of_all_rain_totals += int(row[rain_total_tuple_index])
            if int(row[rain_total_tuple_index]) > largest_daily_rainfall:
                largest_daily_rainfall = int(row[rain_total_tuple_index])
                self.largest_daily_tuple = row
        self.sum_of_daily_rain_totals = sum_of_all_rain_totals
        return sum_of_all_rain_totals

    # Class Method - compute the sum of the daily variances
    def compute_sum_of_daily_variance(self):
        rain_total_tuple_index = 1
        sum_of_all_rain_varaince_totals = 0
        for row in self.row_tuple_list_data:
            daily_total = int(row[rain_total_tuple_index])
            sum_of_all_rain_varaince_totals +=  (daily_total - self.mean)**2
            #print(f'daily variance: {(daily_total - self.mean)**2}')
        self.sum_of_all_rain_varaince_totals = sum_of_all_rain_varaince_totals
        return sum_of_all_rain_varaince_totals

    # Class Method - Draw the data for a specific year to a MatPlotLib view
    def draw_specific_year_plot(self, year):
        year_data = None
        x_values = []
        y_values = []

        for row in self.row_tuple_list_data:
            row_year_str = row[0] # get the date from the tuple for each row
            if year in row_year_str: # Note this is in Day Month Year format
                date = datetime.strptime(row_year_str, '%d-%b-%Y')
                x_values.append(date.strftime('%d-%b-%Y'))
                y_values.append(int(row[1]))
        plt.plot(x_values, y_values)
        plt.show()       





#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Runtime code
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

absolute_path = r'/Users/pparks/Desktop/PDX-Code-Guild-Assigments/Python/hayden_island.clean.txt'
prd = RainData(absolute_path)
prd.read_data_from_absolute_path()
