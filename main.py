import requests
import streamlit as st

st.title("APOD - Astronomy Picture of the Day")
caption = """
One of the most popular websites at NASA is the Astronomy 
Picture of the Day. In fact, this website is one of the 
most popular websites across all federal agencies.
"""
st.caption(caption)

with st.form(key="nasa"):
    date = st.text_input("enter date : format - YYYY-MM-DD ",placeholder="YYYY-MM-DD")
    btn = st.form_submit_button("submit")
    if btn:
        # print(date)
        api = st.secrets["API_KEY"]
        url = f"https://api.nasa.gov/planetary/apod?api_key={api}&date={date}"
        content = requests.get(url)
        file = content.json()

        st.title(file["title"])
        st.image(file["url"])
        st.caption(file["explanation"])
