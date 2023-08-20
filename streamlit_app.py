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
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# put a pick list and filter selected fruits
selected_fruits = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[selected_fruits]

# display the table on streamlit web(app) page
# streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)


# new section to display fruityvice api repsonse
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response)
streamlit.text(fruityvice_response.json())


