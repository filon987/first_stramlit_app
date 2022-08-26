import streamlit
import pandas as pd

streamlit.title('Myparents New Healthy Diner')

streamlit.header('Brekfast Menu')
streamlit.text('🥣 Omega 3 & Bluberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

streamlit.multiselect('Pick some fruits:', list(my_fruits_list.index))

streamlit.dataframe(my_fruit_list)
