import streamlit
streamlit.title("First Streamlit App")
streamlit.text("try adding some more text")
streamlit.text("It is wonderful!")
streamlit.text("Make a great day!")


streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# include drop down list to choose fruit 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# put a pick list 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# display the table on streamlit web(app) page
streamlit.dataframe(my_fruit_list)
