import random
import pandas as pd
import plotly.express as px
import plotly.figure_factory as pff
import csv

df= pd.read_csv("data.csv")

fig=pff.create_distplot([df["Avg Rating"].tolist()],["Average Rate"],show_hist=False)
fig.show()