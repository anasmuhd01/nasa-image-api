import requests
import streamlit as st


url = "https://api.nasa.gov/planetary/apod?api_key=gnoCmPes81gIQ7NhVkSq8EVHp9xNx5qoMhgqLqFb"
content = requests.get(url)
file = content.json()

st.title("testing")

# print(file)