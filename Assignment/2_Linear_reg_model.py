import pandas as pd 
import numpy as np
import matplotlib.pyplot as Plt
from sklearn import linear_model
import matplotlib.pyplot as plt
# import csv

# with open("Housing.csv", 'r' )as csv_file:

#     csv_reader = csv.reader(csv_file)

#     for line in csv_reader:
#         print(line)

data = pd.read_csv('Housing.csv')

plt.scatter(data.Avg_price, data.Price)
plt.show()
