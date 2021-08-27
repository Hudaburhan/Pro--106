import plotly_express as px
import csv
# with open("./data/Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv") as csv_file:
#     df= csv.DictReader(csv_file)
#     fig = px.scatter(df,x="Temperature",y="Ice-cream Sales")
#     fig.show()
# with open("./data/cups of coffee vs hours of sleep.csv") as csv_file:
#     df= csv.DictReader(csv_file)
#     fig = px.scatter(df,x="Coffee in ml",y="sleep in hours",color="week")
#     fig.show()
with open("./data/Student Marks vs Days Present.csv") as csv_file:
    df= csv.DictReader(csv_file)
    fig = px.scatter(df,x="Days Present",y="Marks In Percentage")
    fig.show()