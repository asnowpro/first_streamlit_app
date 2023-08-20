import streamlit
streamlit.title("First Streamlit App")
streamlit.text("try adding some more text")
streamlit.text("It is wonderful!")
streamlit.text("Make a great day!")


streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# include drop down list to choose fruit 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.header('Build Your Own Fruit Smoothie')
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

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response)
#streamlit.text(fruityvice_response.json())

# normalize the json reponse 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Print it as a table in the UI
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)


