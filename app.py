# Importing necessary libraries
import streamlit as st
import requests
from bs4 import BeautifulSoup

# Title of the app
st.title("Weather App")

# Input for city name
city = st.text_input("Enter City Name:")

if city:
    # Create URL for weather data
    url = "https://www.google.com/search?q=" + "weather " + city

    # Requests instance
    html = requests.get(url).content

    # Getting raw data
    soup = BeautifulSoup(html, 'html.parser')

    # Get the temperature
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

    # This contains time and sky description
    str_ = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # Format the data
    data = str_.split('\n')
    time = data[0]
    sky = data[1]

    # List having all div tags having particular class name
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

    # Particular list with required data
    strd = listdiv[5].text

    # Formatting the string
    pos = strd.find('Wind')
    other_data = strd[pos:]

    # Displaying the data
    st.write("### Weather Information")
    st.write(f"**Temperature:** {temp}")
    st.write(f"**Time:** {time}")
    st.write(f"**Sky Description:** {sky}")
    st.write(f"**Other Data:** {other_data}")

    st.write("### Current Location Weather Information")


    # Optional: Get current location weather
    res = requests.get('https://ipinfo.io/')
    data = res.json()  # Receiving the response in JSON format
    citydata = data['city']
    st.write(f"**Current Location:** {citydata}")


    url = "https://www.google.com/search?q=" + "weather " + citydata

    # Requests instance
    html = requests.get(url).content

    # Getting raw data
    soup = BeautifulSoup(html, 'html.parser')

    # Get the temperature
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

    # This contains time and sky description
    str_ = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # Format the data
    data = str_.split('\n')
    time = data[0]
    sky = data[1]

    # List having all div tags having particular class name
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

    # Particular list with required data
    strd = listdiv[5].text

    # Formatting the string
    pos = strd.find('Wind')
    other_data = strd[pos:]

    # Displaying the data
    st.write(f"**Temperature:** {temp}")
    st.write(f"**Time:** {time}")
    st.write(f"**Sky Description:** {sky}")
    st.write(f"**Other Data:** {other_data}")






