import streamlit as st
import pandas as pd
import plotly.express as px
import openpyxl
import requests
import json

from PIL import Image
from datetime import datetime
from streamlit_lottie import st_lottie 

st.set_page_config(layout="wide", page_title="CDT")
#para importar imagen desde el archivo
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

#para importar imagen con url
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None

    return r.json()

st.write("<h1 style='font-size:60px'>Cambio de Turno - Service Desk</h1>", unsafe_allow_html=True)

# Dividir la pantalla en dos columnas
col1, col2, col3 = st.columns(3)

# SIDEBAR

#Lector de archivo CSV
archivo_cdt = st.sidebar.file_uploader('Choose a CSV file', type='csv')
# Horarios
turno_m = st.sidebar.checkbox('Turno Mañana')
turno_t = st.sidebar.checkbox('Turno Tarde')
turno_n = st.sidebar.checkbox('Turno Noche')

# Actividades
st.sidebar.subheader('Actividades Service Desk 💻')
acti_cenam = st.sidebar.checkbox('Actividad Cenam')
acti_aup = st.sidebar.checkbox('Actividad AUP')
acti_ecuador = st.sidebar.checkbox('Actividad Ecuador')

# PANTALLA PRINCIPAL
# Mostrar los participantes
with col1:
    option1 = st.selectbox(
    ' Participante 1 🧑‍💻',
    ('','Novoa Carlos', 'Gonzales Ivan', 'Pacciarioni Gastón', 'Barrionuevo Matías','LLanos Brian','Godoy Emiliano','Fernandez Diego' ,'Aviles Paula','Gimenez Rodrigo')
)

with col2:
    option2 = st.selectbox(
    ' Participante 2 👩‍💻',
    ('','Novoa Carlos', 'Gonzales Ivan', 'Pacciarioni Gastón', 'Barrionuevo Matías','LLanos Brian','Godoy Emiliano','Fernandez Diego' ,'Aviles Paula','Gimenez Rodrigo')
    )

with col3:
    option4 = st.selectbox(
    ' Participante 3 🧑‍💻',
    ('','Novoa Carlos', 'Gonzales Ivan', 'Pacciarioni Gastón', 'Barrionuevo Matías','LLanos Brian','Godoy Emiliano','Fernandez Diego' ,'Aviles Paula','Gimenez Rodrigo')
    )

# Comentarios    
def add_note():
 # Aquí puedes agregar el código para guardar la nota en una base de datos.
 #   st.subheader('-')
    st.subheader(f"🗒️Comentarios del Turno:")
    st.write(f" {note}")
    st.write(f" {note2}")
    st.write(f" {note3}")
    st.write(f" {note4}")    
 #   st.subheader('-')
 #  st.write(f" {note3}")

#if not acti_aup or acti_cenam or acti_ecuador:
 #   st.subheader(f"🗓️Comentarios de la Actividad:")
 #   st.write(f" {note4}")
  #  st.write(f" {note5}")
  #  st.subheader('-')
  #  st.write(f" {note6}")
    
# Imagen    
with col1:
    st_lottie_animation2 = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_m9zragkd.json")
    st_lottie(st_lottie_animation2,
              speed=0.9,
              reverse=False,
              loop=True,
              quality="low",
              height=None,
              width=None,
              key=None) 
# Mostrar el campo de entrada de texto para agregar notas
with col2:
    st.subheader('Comentarios  del Turno  ')
    note = st.text_input('Comentario 1', key='new_note')
    note2 = st.text_input('Comentario 2', key='new_note2')
with col3:
    st.subheader('✏️🗒️')
    note3 = st.text_input('Comentario 3', key='new_note3')
    note4 = st.text_input('Comentario 4', key='new_note4')
  

  #  st.subheader('-----------------------------------------------')
 #Imagen    
#with col2:
 #  st_lottie_animation = load_lottiefile("coding.json")
 #  st_lottie(st_lottie_animation,
 #             speed=0.9,
 #             reverse=False,
 #             loop=True,
 #             quality="low",
 #             height=None,
 #             width=None,
 #             key=None)   
    
# Comentarios Actividad
#if acti_cenam or acti_aup or acti_ecuador:
 #  with col3:
   #     st.subheader('Comentarios de Actividad 🗓️')
   #     note4 = st.text_input('', key='new_note4')
   #     note5 = st.text_input('', key='new_note5')
       #note6 = st.text_input('', key='new_note6')
    


#Mostrar Imagen TN3
st.subheader('-')
st.subheader('-')
image = Image.open('tn3.jpg')
st.image(image, caption='',use_column_width=False)

# Obtener la fecha actual
today = datetime.today().strftime('%d/%m/%y')

# Mostrar la fecha actual en Streamlit
if turno_m:
    st.title(f'Service Desk - Cambio de Turno - {today} - 8:00 a 16:00hs')
if turno_t:
    st.title(f'Service Desk - Cambio de Turno - {today} - 16:00 a 00:00hs')
if turno_n:
    st.title(f'Service Desk - Cambio de Turno - {today} - 00:00 a 8:00hs')
    
# Mostrar Participantes
# st.subheader('-')
st.subheader(f"🧑‍💻Participantes: {option1} - {option2} - {option4}")

add_note()

if acti_cenam:
    with col1:
        encargado = st.sidebar.selectbox(
        'Encargado:',
        ('-','Novoa Carlos', 'Gonzales Ivan', 'Pacciarioni Gastón', 'Barrionuevo Matías','LLanos Brian','Godoy Emiliano','Fernandez Diego' ,'Aviles Paula','Gimenez Rodrigo')
        )
        horario = st.sidebar.radio("Inicio Actividad CENAM",('','22:00','23:00','00:00','1:00','2:00'))

    st.subheader(f'➡️Actividad CENAM: {encargado} - Comienza a las {horario}hs')
                 
if acti_aup:
    with col1:
        encargado2 = st.sidebar.selectbox(
        'Encargado 2:',
        ('-','Novoa Carlos', 'Gonzales Ivan', 'Pacciarioni Gastón', 'Barrionuevo Matías','LLanos Brian','Godoy Emiliano','Fernandez Diego' ,'Aviles Paula','Gimenez Rodrigo')
        )
        horario2 = st.sidebar.radio("Inicio Actividad AUP",('','22:00','23:00','00:00','1:00','2:00'))

    st.subheader(f'➡️Actividad AUP: {encargado2} - Comienza a las {horario2}hs')
    

if acti_ecuador:
    with col1:
        encargado3 = st.sidebar.selectbox(
        'Encargado 3:',
        ('-','Novoa Carlos', 'Gonzales Ivan', 'Pacciarioni Gastón', 'Barrionuevo Matías','LLanos Brian','Godoy Emiliano','Fernandez Diego' ,'Aviles Paula','Gimenez Rodrigo')
        )
        horario3 = st.sidebar.radio("Inicio Actividad ECUADOR",('','22:00','23:00','00:00','1:00','2:00'))
    
    st.subheader(f'➡️Actividad ECUADOR: {encargado3} - Comienza a las {horario3} hs')
    

st.subheader('-')

# Leer el excel
if archivo_cdt:
    df = pd.read_csv(archivo_cdt, engine='python')
    #Tarjeta de Total de Casos
    num_filas = df.shape[0]
    if num_filas == 0:
        st.subheader('No se reportaron nuevos casos en este turno')
    else:
        st.subheader(f'Total de Casos: {num_filas}')
        # Convertir el DataFrame a una tabla HTML
        tabla_html = df.to_html(index=False)
        st.write(tabla_html, unsafe_allow_html=True)
    
    #Tarjeta de casos Asignados:
    #asignado = (df['Estado'] == 'Asignado').sum()
    #st.subheader(f'Casos en Asignados: {asignado}')
    #Tarjeta de casos Cerrados:
    #cerrado = (df['Estado'] == 'Closed').sum()
    #st.subheader(f'Casos Solucionados: {cerrado}')
    #Tarjeta de casos en Investigacion:
    #investigacion = (df['Estado'] == 'En investigacion').sum()
    #st.subheader(f'Casos en Investigación: {investigacion}')


    
    
    
