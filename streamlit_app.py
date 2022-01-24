from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
# import matplotlib.pyplot as plt
"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


# nba_dataFrame = pd.read_csv('Seasons_Stats.csv')

# nba_df_2001=nba_dataFrame[nba_dataFrame['Year']==2001]
# nba_df_2001_ind = nba_df_2001.set_index(['Tm','PER'])
# st.table(nba_df_2001_ind.sort_index(level=["Tm","PER"],ascending=[True,False]))







sales_df = pd.read_csv("5000 Sales Records.csv")
europe_sales_df = sales_df[sales_df['Region']=='Europe'].set_index(["Region","Country"])

asia_sales_df = sales_df[sales_df['Region']=='Asia']
Africa_sales_df = sales_df[sales_df['Region']=='Sub-Saharan Africa']
Middle_East_sales_df = sales_df[sales_df['Region']=='Middle East and North Africa']
Central_America_sales_df = sales_df[sales_df['Region']=='Central America and the Caribbean']
Aussie_sales_df = sales_df[sales_df['Region']=='Australia and Oceania']
NorthAmerica_sales_df = sales_df[sales_df['Region']=='North America']
st.button('BEGIN')
st.checkbox('I agree')
st.radio('Pick one', ['Asia', 'Africa','Middle East','Central America','Australia and Oceania', 'North America'])
st.selectbox('Pick one', ['Asia', 'Africa','Middle East','Central America','Australia and Oceania', 'North America'])
st.header("Sales Data")

st.header("North American Sales")
st.table(NorthAmerica_sales_df.head())
avg_NA_sales = NorthAmerica_sales_df.groupby("Country")["Total Profit"].mean()
st.bar_chart(avg_NA_sales)



st.header("European Sales")
st.table(europe_sales_df.head().sort_values("Country").head())
avg_sales_by_country = europe_sales_df.groupby("Country")["Total Profit"].mean()
st.table(avg_sales_by_country.head())
st.bar_chart(avg_sales_by_country)

st.header("Asian Sales")
# st.table(asia_sales_df)
st.table(europe_sales_df[europe_sales_df["Order Date"] > "2017"].head())

avg_asia_sales = asia_sales_df.groupby("Country")["Total Profit"].mean()
st.bar_chart(avg_asia_sales)







with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
