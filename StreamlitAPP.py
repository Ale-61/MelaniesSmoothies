import pandas as pd
import altair as alt
import streamlit as st
#import snowflake.snowpark.functions
import snowflake.snowpark.DataFrameReader as snowflake

#from snowflake.snowpark.functions import col
#pip install snowflake-snowpark-python

# Write directly to the app
st.title(":cup_with_straw: Customize your Smoothie! :cup_with_straw:")
st.write("""Choose the fruits you want in your custom **Smoothie**!"""
        )

# Client Name
name_order = st.text_input("Name on Smoothie: ")
st.write("The current movie title is", name_order)

#Box fruit option

#session = get_active_session()
cnx = st.connection("snowflake")
session = cnx.sesion()
