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

#session = get_active_session()
cnx = st.connections.SnowflakeConnection("snowflake")
#cnx = st.connection("snowflake")
session = cnx.sesion()

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    "Choose up to 5 ingredients",
    my_dataframe,
    max_selections=5
)

if ingredients_list:
    ingredients_string = ' '

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
    #st.write(ingredients_string)
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + " ""','""" + name_order + " ""')"""

    #st.write(my_insert_stmt)
    #st.stop()
    
    time_to_insert = st.button('Submit Order')
    #st.write(my_insert_stmt)
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered,' " "+ name_order + " "'!', icon="✅")
