import streamlit as st
import pandas as pd
import numpy as np
import folium
import plotly.express as px
import requests

api_key = "ae27f4e8-6047-4c7d-b1cc-bcf768b9c451"
gmap_api_key = "AIzaSyD0mWLeD6eekVTM9DRfUdUPwZ-VZnzbMOs"

st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"]::before {
            content: "Fitness Buddy API";
            margin-left: 20px;
            margin-top: 20px;
            font-size: 30px;
            position: relative;
            top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)



st.title("Find nearby Parks or Gyms")


user_zip = st.text_input('Insert your ZIP code:')

if user_zip:
    location = st.selectbox('Select an option:', options= [" ", "gym", "park"])

    if location is not " ":
        url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={location}+in+{user_zip}&key=AIzaSyD0mWLeD6eekVTM9DRfUdUPwZ-VZnzbMOs'
        json_data = requests.get(url).json()
        # st.json(json_data)
        # st.write("bruh:")

        latitude = []
        longitude = []
        address = []
        name = []
        for i in json_data['results']:
            latitude.append(i["geometry"]["location"]["lat"])
            longitude.append(i["geometry"]["location"]["lng"])
            address.append(i['formatted_address'])
            name.append(i['name'])

        df = pd.DataFrame({"Address": address, "Name": name, "Latitude": latitude, "Longitude": longitude})

        st.write(df)

        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",
                                zoom =11,
                                size_max=100,
                                hover_name="Name",
                                )
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_traces(marker=dict(size=15, color="blue", opacity=0.8))
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

        st.plotly_chart(fig)

























