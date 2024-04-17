import streamlit as st
import pandas as pd
import plotly.express as px
import requests

api_key = "ae27f4e8-6047-4c7d-b1cc-bcf768b9c451"
gmap_api_key = "AIzaSyD0mWLeD6eekVTM9DRfUdUPwZ-VZnzbMOs"
selectColor = "blue"
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
st.markdown("This page will find nearby gym and/or parks that you can go to get a workout in.")

user_zip = st.text_input('Insert your ZIP code:')

if user_zip:
    location = st.selectbox('Select an option:', options= [" ", "gym", "park"])

    if location is not " ":
        st.subheader(f"Here's your result for all the {location}s based on the zip code: {user_zip}")
        st.text(f"Closest {location} is the first, farthest is the last")
        url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={location}+in+{user_zip}&key=AIzaSyD0mWLeD6eekVTM9DRfUdUPwZ-VZnzbMOs'
        json_data = requests.get(url).json()
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
        color = st.checkbox('Do you want to change the color of the locations on the map')
        if color:
            selectColor = st.color_picker('Pick A Color', '#00f900')

        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",
                                zoom =11,
                                size_max=100,
                                hover_name="Name",
                                )
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_traces(marker=dict(size=15, color=selectColor, opacity=0.8))
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

        st.plotly_chart(fig)



























