import pandas as pd
import altair as alt
import streamlit as st
import snowflake
#import snowflake.col
#from snowflake.snowpark.functions import col
#import snowflake.snowpark.functions
#from snowflake import col

# Write directly to the app
st.title(":cup_with_straw: Customize your Smoothie! :cup_with_straw:")
st.write("""Choose the fruits you want in your custom **Smoothie**!"""
        )

# Client Name
name_order = st.text_input("Name on Smoothie: ")
st.write("The current movie title is", name_order)

#Box fruit option

st.connections.SnowflakeConnection(account = "JHLSWFL-TD25150",
user = "Andrea",
password = "SNOW24gl##$",
role = "SYSADMIN",
warehouse = "COMPUTE_WH",
database = "SMOOTHIES",
schema = "PUBLIC",
client_session_keep_alive = "true", type="snowflake")

#session = get_active_session()
cnx = st.connection("snowflake")
session = cnx.sesion()
