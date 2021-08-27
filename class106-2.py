import plotly_express as px
import csv
import numpy as np

def getDataSource(data_path):
    ice_cream_sales =[]
    cold_drink_sales=[]
    with open(data_path) as csv_file:
        csv_reader= csv.DictReader(csv_file)
        for row in csv_reader:
            # ice_cream_sales.append(float(row["Temperature"]))
            # cold_drink_sales.append(float(row["Ice-cream Sales"]))
            # ice_cream_sales.append(float(row["Size of TV"]))
            # cold_drink_sales.append(float(row["\tAverage time spent watching TV in a week"]))
            ice_cream_sales.append(float(row["Days Present"]))
            cold_drink_sales.append(float(row["Marks In Percentage"]))
    return {"x":ice_cream_sales,"y":cold_drink_sales}

def find_correlation(datasource):
    correlation= np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])

def setup():
    data_path="./data/Student Marks vs Days Present.csv"
    datasource= getDataSource(data_path)
    find_correlation(datasource)
setup()