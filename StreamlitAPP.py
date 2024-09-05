# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize your Smoothie! :cup_with_straw:")
st.write(
#    """Replace this example with your own code!
#    **And if you're new to Streamlit,** check
#    out our easy-to-follow guides at
#    [docs.streamlit.io](https://docs.streamlit.io).
    """Choose the fruits you want in your custom **Smoothie**!
    """
)

