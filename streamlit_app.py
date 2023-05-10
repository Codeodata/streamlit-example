import streamlit as st
import pandas as pd
import plotly.express as px
import openpyxl
import requests
import json
import time
import smtplib
import pickle

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

# Crea una barra de navegación para cambiar de pestaña
menu = ["Página 1", "Página 2"]
choice = st.sidebar.selectbox("Seleccione una página", menu)

# Crea una sección para cada página
if choice == "Página 1":
        st.write("<h1 style='font-size:60px'>Cambio de Turno - Service Desk</h1>", unsafe_allow_html=True)

        # Dividir la pantalla en dos columnas
        col1, col2, col3 = st.columns(3)

        # SIDEBAR
        #Lector de archivo CSV
        archivo_cdt = st.sidebar.file_uploader('Choose a CSV file', type='csv')

        # Define the radio button for selecting the turno
        st.sidebar.subheader('Turno⌚')
        options = st.sidebar.radio('', options=['Turno Mañana', 'Turno Tarde','Turno Noche'])

        # Use the selected option to set the corresponding value of horario
        if options == 'Turno Mañana':
            hora = '8:00 a 16:00hs'
        elif options == 'Turno Tarde':
            hora = '16:00 a 00:00hs'
        elif options == 'Turno Noche':
            hora = '00:00 a 8:00hs'
                
        # Actividades
        st.sidebar.subheader('Actividades Service Desk 💻')
        acti_cenam = st.sidebar.checkbox('Actividad Cenam')
        acti_aup = st.sidebar.checkbox('Actividad AUP')
        acti_ecuador = st.sidebar.checkbox('Actividad Ecuador')
        # PANTALLA PRINCIPAL
        # Mostrar los participantes
        with col1:
            option1 = st.selectbox(' Participante 1 🧑‍💻',
                    ('','Novoa Carlos', 'Gonzales Ivan', 'Pacciaroni Gastón', 'Barrionuevo Matías','LLanos Brian','Godoy Emiliano','Fernandez Diego' ,'Aviles Paula','Gimenez Rodrigo')
                )

        with col2:
            option2 = st.selectbox(' Participante 2 👩‍💻',
                ('','Novoa Carlos', 'Gonzales Ivan', 'Pacciaroni Gastón', 'Barrionuevo Matías','LLanos Brian','Godoy Emiliano','Fernandez Diego' ,'Aviles Paula','Gimenez Rodrigo')
                )

        with col3:
            option4 = st.selectbox(' Participante 3 🧑‍💻',
                ('','Novoa Carlos', 'Gonzales Ivan', 'Pacciaroni Gastón', 'Barrionuevo Matías','LLanos Brian','Godoy Emiliano','Fernandez Diego' ,'Aviles Paula','Gimenez Rodrigo')
                )
            
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
         st_lottie_animation = load_lottiefile("coding.json")
         st_lottie(st_lottie_animation,
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
            note3 = st.text_input('Comentario 3', key='new_note3')
        with col3:
            st.subheader('✏️🗒️')
            note4 = st.text_input('Comentario 4', key='new_note4')
            note5 = st.text_input('Comentario 5', key='new_note5')
            note6 = st.text_input('Comentario 6', key='new_note6')

            
        # Cargar las notas desde el archivo si existe
        try:
            with open('notas.pickle', 'rb') as f:
                notas = pickle.load(f)
        except FileNotFoundError:
            notas = []

        # Agregar una nueva nota
        def agregar_nota(nota):
            notas.append(nota)
            guardar_notas()

        # Eliminar una nota existente
        def eliminar_nota(nota):
            notas.remove(nota)
            guardar_notas()

        # Guardar las notas en el archivo
        def guardar_notas():
            with open('notas.pickle', 'wb') as f:
                pickle.dump(notas, f)

        # Formulario para agregar una nueva nota
        nueva_nota = st.text_input('Backlog')
        if st.button('Agregar'):
            agregar_nota(nueva_nota)

        # Formulario para eliminar una nota existente
        nota_eliminar = st.selectbox('Eliminar Backlog', notas)
        if st.button('Eliminar'):
            eliminar_nota(nota_eliminar)

                # Comentarios    
        def add_note():
        # Aquí puedes agregar el código para guardar la nota en una base de datos.
        #   st.subheader('-')         
            # Mostrar la lista de notas
            st.subheader(f"🔙Backlog:")
            for i, nota in enumerate(notas):
            st.warning(f'{i+1}. {nota}')

            st.subheader(f"🗒️Comentarios del Turno:")
            st.write(f" {note}")
            st.write(f" {note2}")
            st.write(f" {note3}")
            st.write(f" {note4}")  
            st.write(f" {note5}")
            st.write(f" {note6}")
                       
        # Comentarios Actividad
        #if acti_cenam or acti_aup or acti_ecuador:
        #  with col3:
        #     st.subheader('Comentarios de Actividad 🗓️')
        #     note4 = st.text_input('', key='new_note4')
        #     note5 = st.text_input('', key='new_note5')
            #note6 = st.text_input('', key='new_note6')
            


        #Mostrar Imagen TN3
        image = Image.open('tn3.jpg')
        st.image(image, caption='',use_column_width=False)

        # Obtener la fecha actual
        today = datetime.today().strftime('%d/%m/%y')

        # Mostrar la fecha actual en Streamlit
        st.title(f'Service Desk - Cambio de Turno - {today} - {hora}')

        # Mostrar Participantes
        # st.subheader('-')
        st.subheader(f"🧑‍💻Participantes: {option1} - {option2} - {option4}")



        add_note()

        if acti_cenam:
            with col1:
                encargado = st.sidebar.selectbox(
                'Encargado:',
                ('-','Novoa Carlos', 'Gonzales Ivan', 'Pacciaroni Gastón', 'Barrionuevo Matías','LLanos Brian','Godoy Emiliano','Fernandez Diego' ,'Aviles Paula','Gimenez Rodrigo')
                )
                horario = st.sidebar.radio("Inicio Actividad CENAM",('','22:00','23:00','00:00','1:00','2:00'))

            st.info(f'➡️Actividad CENAM: {encargado} - Comienza a las {horario}hs')
                        
        if acti_aup:
            with col1:
                encargado2 = st.sidebar.selectbox(
                'Encargado 2:',
                ('-','Novoa Carlos', 'Gonzales Ivan', 'Pacciaroni Gastón', 'Barrionuevo Matías','LLanos Brian','Godoy Emiliano','Fernandez Diego' ,'Aviles Paula','Gimenez Rodrigo')
                )
                horario2 = st.sidebar.radio("Inicio Actividad AUP",('','22:00','23:00','00:00','1:00','2:00'))

            st.info(f'➡️Actividad AUP: {encargado2} - Comienza a las {horario2}hs')
            time.sleep(3)
            

        if acti_ecuador:
            with col1:
                encargado3 = st.sidebar.selectbox(
                'Encargado 3:',
                ('-','Novoa Carlos', 'Gonzales Ivan', 'Pacciaroni Gastón', 'Barrionuevo Matías','LLanos Brian','Godoy Emiliano','Fernandez Diego' ,'Aviles Paula','Gimenez Rodrigo')
                )
                horario3 = st.sidebar.radio("Inicio Actividad ECUADOR",('','22:00','23:00','00:00','1:00','2:00'))

            st.info(f'➡️Actividad ECUADOR: {encargado3} - Comienza a las {horario3} hs')
            

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

            # Agrega contenido a la segunda sección

#else:
