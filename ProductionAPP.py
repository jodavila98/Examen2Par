import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from PIL import Image
from io import StringIO
#Icono
icon=Image.open("resources/produccion.jpg")

st.set_page_config(page_title="Produccion Volve App", page_icon=icon)

#Titulo
st.title("Historial de producción del campo Volve")
st.write("El campo Volve es un campo offshore perteneciente a Noruega, localizado en el Mar del Norte, empezó sus  "
         "operaciones en 2008")


with st.sidebar:
    options = option_menu(
        menu_title="Main Menu",
        options=["Home", "Data ", "plots"])
