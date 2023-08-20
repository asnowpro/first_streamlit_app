import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError



streamlit.title("First Streamlit App")
streamlit.text("try adding some more text")
streamlit.text("It is wonderful!")
streamlit.text("Make a great day!")


streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')

# import pandas

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

# fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# streamlit.write('The user entered ', fruit_choice)

# adding try-except with nested if-else
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('please select a fruit to get information.')
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    # normalize the json reponse 
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    # Print it as a table in the UI
    streamlit.dataframe(fruityvice_normalized)

except URLError as e:
  streamlit.error()


# import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# streamlit.text(fruityvice_response)
# streamlit.text(fruityvice_response.json())

# normalize the json reponse 
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Print it as a table in the UI
# streamlit.dataframe(fruityvice_normalized)

#do not run anything past here while we troubleshoot
# streamlit.stop()

#import snowflake.connector

# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_cur.execute("SELECT * from fruit_load_list")
#fetches one record
# my_data_row = my_cur.fetchone()
#fetch all the records
# my_data_rows = my_cur.fetchall()
# streamlit.text("Hello from Snowflake:")
# streamlit.header("The fruit load list contains:")
# streamlit.dataframe(my_data_rows)

#allow user to add fruit to the list
# add_my_fruit = streamlit.text_input('What fruit would you like to add?')
# streamlit.write('Thanks for adding ', add_my_fruit)

# We took 6 lines of above code and re-distributed them so that we now have 
# 1) a function that queries the table and 
# 2) a button that calls our function and loads the data onto the page. 

streamlit.header('The fruit load list contains:')
#snowflake related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute('select * from fruit_load_list')
    return my_cur.fetchall()

# add a button to load the fruit list
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets['snowflake'])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)


# Allow user to add a fruit to the list
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from streamlit')")
    return "Thanks for adding " + new_fruit

add_my_fruit = streamlit.text('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets['snowflake'])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)



