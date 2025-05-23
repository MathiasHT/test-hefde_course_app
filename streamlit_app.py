# import streamlit as st
# import pandas as pd
# import mag4 as mg
# import matplotlib.pyplot as plt
# # st.title("🎈 My new app hello")
# # st.write(
# #     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# # )

# st.title("Hello World")
# st.write("Hello World")

# # mg.available_datasets('bastcrat')

# #st.write(mg.available_datasets())
# df = mg.get_data('bastcrat')





# elements = df.columns.tolist()[20:]
# xEl = st.selectbox("select xAxis", elements)
# yEl = st.selectbox("select yAxis", elements)

# fig, ax = plt.subplots()
# ax.scatter(xEl,yEl)
# st.pyplot(fig)


# # df['Si']

import streamlit as st
import requests

api_key = 'a5df94b0065c318ee195e630b94ad050'

st.title("🌦️ Aktuelles Wetter")

# Eingabe: Stadtname
city = st.text_input("Stadt eingeben", "Berlin")

# API-Key (eigene OpenWeatherMap API verwenden)
#api_key = "DEIN_API_KEY_HIER"  # Hier deinen gültigen API-Key eintragen

if st.button("Wetter anzeigen"):
    # Schritt 1: Geodaten abrufen
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    geo_response = requests.get(geo_url)

    if geo_response.status_code == 200 and geo_response.json():
        lat = geo_response.json()[0]['lat']
        lon = geo_response.json()[0]['lon']

        # Schritt 2: Wetterdaten abrufen
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        weather_response = requests.get(weather_url)

        if weather_response.status_code == 200:
            data = weather_response.json()
            st.subheader(f"Wetter in {city}")
            st.metric("🌡 Temperatur", f"{data['main']['temp']} °C")
            st.write(f"💧 Luftfeuchtigkeit: {data['main']['humidity']} %")
            st.write(f"🌬 Windgeschwindigkeit: {data['wind']['speed']} m/s")
            st.write(f"📝 Beschreibung: {data['weather'][0]['description'].capitalize()}")
        else:
            st.error("Fehler beim Abrufen der Wetterdaten.")
    else:
        st.error("Stadt nicht gefunden oder Fehler beim Abrufen der Koordinaten.")
