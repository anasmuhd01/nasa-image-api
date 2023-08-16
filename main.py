import requests
import streamlit as st


with st.form(key="nasa"):
    date = st.text_input("enter date:")
    btn = st.form_submit_button("submit")
    if btn:
        print(date)
        url = f"https://api.nasa.gov/planetary/apod?api_key=gnoCmPes81gIQ7NhVkSq8EVHp9xNx5qoMhgqLqFb&date={date}"
        content = requests.get(url)
        file = content.json()

        st.title(file["title"])
        st.image(file["url"])
        st.caption(file["explanation"])
