import pandas as pd
import plotly.express as px
# data= [1,2,3,4,5,6]
# df= pd.DataFrame(data)
# df= pd.read_csv("line_chart.csv")
# fig = px.line(df, x="Year", y="Per capita income", color="Country", title="Per Capita Income")
df= pd.read_csv("data.csv")
fig = px.bar(df, x="Country", y="InternetUsers")
# df= pd.read_csv("data.csv")
# fig = px.scatter(df, x="Population", y="Per capita", size= "Percentage", color="Country", size_max=60)
fig.show()
# print(df)