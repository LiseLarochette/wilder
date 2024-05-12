import streamlit as st
import pandas as pd
import numpy as np

st.title("Analyse d'une base de données")
st.write("Lise LAROCHETTE")

st.write("Base de données")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_voitures = pd.read_csv(link)


your-repository/
├── pages/
│   ├── page_1.py
│   └── page_2.py
└── your_app.py

  import streamlit as st

st.https://wilder.streamlit.app/("your_app.py", label="Home", icon="🏠")
st.https://wilder.streamlit.app/("pages/page_1.py", label="Page 1", icon="1️⃣")
st.https://wilder.streamlit.app/("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
st.https://wilder.streamlit.app/("http://www.google.com", label="Google", icon="🌎")

#afficher la DF
df_voitures


#créer un filtre
import streamlit as st

# Sélectionnez la colonne 'continent'
selected_continent = st.selectbox("Sélectionnez un continent :", df_voitures['continent'].unique())

# Filtrer le DataFrame en fonction du continent sélectionné
df_filtered = df_voitures[df_voitures['continent'] == selected_continent]

# Afficher le DataFrame filtré
st.write("Votre sélection :")
st.write(df_filtered)

#afficher un graphique en bar
st.title("Puissance des voitures (cylindres) par nationalité")
st.bar_chart(data=df_voitures, x='continent', y='cylinders')
st.write("On remarque que les voitures américaines sont les plus puissantes.")

#afficher un graphique en courbe
st.title("Consommation des voitures en fonction de la puissance (cylindres)")
st.line_chart(data=df_voitures, x= 'weightlbs', y='mpg')
st.write("On remarque que les voitures qui ont un poids entre 2000 et 2800 lbs consomment le plus.")
