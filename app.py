# CODIGO DE MODELO DE PREDICCION DEL NIVEL DE URGENCIA DE UN PACIENTE.#
# 10/05/2025#
# AUTOR : A.T#
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from menu_custom.menu_custom import render_menu
from datetime import datetime
import streamlit as st
import seaborn as sns

st.set_page_config(page_title="App Urgencias Médicas", layout="wide")

# Hora actual
ahora = datetime.now().strftime("%d/%m/%Y · %H:%M")

# Logo + título + hora
st.markdown(
    f"""
    <div style='display: flex; justify-content: space-between; align-items: center; padding: 0.5rem 1rem 1rem 1rem; border-bottom: 1px solid #991b1b;'>
        <div style='display: flex; align-items: center;'>
            <img src='https://loghi-famosi.com/wp-content/uploads/2020/04/UPV-Logo.png' style='height: 40px; margin-right: 12px;' />
            <span style='font-size: 1.4rem; font-weight: bold;'>ESTRELLA COJA</span>
        </div>
        <div style='color: gray; font-size: 0.9rem;'> {ahora}</div>
    </div>
    """,
    unsafe_allow_html=True
)





# Mostrar menú personalizado
seccion = render_menu()


# --- SECCIÓN EQUIPO ---
def seccion_equipo():
    st.markdown("<h3 style='text-align: center;'> Informacion del Grupo</h3>", unsafe_allow_html=True)
    st.write('Somos un grupo de estudiantes de la universidad politecnica de Valencia, del grado de Ciencia de datos, y este es nuestro proyecto. Es innegable que el proceso de urgencias hoy en dia es un proceso lento, tedioso y sobresaturado; de aqui salío nuestra motivacion para llevar al cabo este proyecto, que se centraria en hacer una app que evalue el nivel de urgencias de los pacientes. Para ello hemos llevado a cabo un largo proceso de informacion y aprendizaje.')
    st.write('Comenzamos haciendo referencia al articulo .... del cual extraímos la base de datos con la que mas tarde trabajariamos. Esta base de datos recoje todo tipo de datos de triaje en las urgencias de 3 hospitales durante el periodo de un año, alcanzando la cantidad de mas de 260.000 casos y mas de 900 variables.')
    st.write('Sobre ella llevamos a cabo una limpieza de los datos, eliminando aquellas variables que no aportaban casi informacion y obteniendo un dataset cuya relacion carga-informacion era perfecta para nuestro cometido. Sobre esto aplicamos un PCA para reducir mas el número de variables y hallar aquellas que tuvieran mas informacion. Con esto, y con la ayuda de un algoritmo de Random Forest, conseguimos un modelo que alcanzaba una precision de 0.75 en el testeo.')
    st.write('A partir de aqui, decidimos crear una app que pudiera ser util para la gente, y que pudiera ayudar a los medicos a decidir si un paciente es urgente o no. Para ello, creamos una app en streamlit, donde el usuario puede subir un archivo CSV con los sintomas del paciente y la app le devuelve su nivel de urgencia en segundos.')
    st.markdown("<h3 style='text-align: center;'> Integrantes</h3>", unsafe_allow_html=True)
    st.markdown("""
    - **Adrián Tierno** -  [@adriitiernooo_](https://www.instagram.com/adriitiernooo_/)
    - **Jaime planells** -  [@jaimeplanellss](https://www.instagram.com/jaimeplanellss/)
    - **Raúl Benitez** - [@rauul.benitezz](https://www.instagram.com/rauul.benitezz/)
    - **Carlos San José**  - [@carlossanjosee_](https://www.instagram.com/carlossanjosee_/)
    - **Juan Pascual**  - [@juan.pascuaal](https://www.instagram.com/juan.pascuaal/)
    """)
# --- SECCIÓN DATASET ---
    import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def seccion_dataset():
    st.markdown("<h3 style='text-align: center;'> Analisis del dataset</h3>", unsafe_allow_html=True)

    # Cargar el CSV
    urgencias = pd.read_csv('./output.csv', sep=',')

    # --- Análisis por género ---
    st.markdown("### Distribución del Nivel de Urgencia (ESI) por Género")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.countplot(data=urgencias, x='esi', hue='gender', palette='viridis', ax=ax1)
    ax1.set_title('Nivel de Urgencia (ESI) por Género')
    ax1.set_xlabel('Nivel de Urgencia (ESI)')
    ax1.set_ylabel('Cantidad')
    st.pyplot(fig1)

    # Porcentaje por género
    mujeres = urgencias[urgencias['gender'] == 'Female']
    hombres = urgencias[urgencias['gender'] == 'Male']
    M1 = mujeres['esi'].value_counts(normalize=True).sort_index() * 100
    H1 = hombres['esi'].value_counts(normalize=True).sort_index() * 100

    st.markdown("### Porcentaje de Hombres y Mujeres por Nivel de Urgencia")
    fig2, ax2 = plt.subplots()
    ax2.bar(M1.index - 0.2, M1.values, width=0.4, label="Mujeres")
    ax2.bar(H1.index + 0.2, H1.values, width=0.4, label="Hombres")
    ax2.set_title("Porcentaje de Hombres y Mujeres por Nivel de Urgencia")
    ax2.set_xlabel("Nivel de Urgencia (ESI)")
    ax2.set_ylabel("Porcentaje (%)")
    ax2.legend()
    st.pyplot(fig2)

    # --- Urgencias por edad ---
    st.markdown("### Total de Urgencias por Edad")
    fig3, ax3 = plt.subplots(figsize=(25, 10))
    sns.countplot(data=urgencias, x='age', palette='viridis', ax=ax3)
    ax3.set_title('Total de Urgencias por Edad')
    ax3.set_xlabel('Edad')
    ax3.set_ylabel('Cantidad')
    ax3.tick_params(axis='x', rotation=45)
    st.pyplot(fig3)

    # --- Urgencias por intervalos de edad ---
    st.markdown("### Total de Urgencias por Intervalos de Edad")
    bins = np.arange(18, 108, 10)
    labels = [f"{i}-{i+9}" for i in bins[:-1]]
    urgencias['age_group'] = pd.cut(urgencias['age'], bins=bins, labels=labels, right=False)
    urgencias['age_group'] = urgencias['age_group'].cat.add_categories('107+').fillna('107+')

    fig4, ax4 = plt.subplots(figsize=(15, 6))
    sns.countplot(data=urgencias, x='age_group', palette='viridis', ax=ax4)
    ax4.set_title('Total de Urgencias por Intervalos de Edad')
    ax4.set_xlabel('Intervalos de Edad')
    ax4.set_ylabel('Cantidad')
    ax4.tick_params(axis='x', rotation=45)
    st.pyplot(fig4)

    # --- ESI por intervalos de edad ---
    st.markdown("### Total de Urgencias por Intervalos de Edad y Nivel de Urgencia (ESI)")
    fig5, ax5 = plt.subplots(figsize=(15, 6))
    sns.countplot(data=urgencias, x='age_group', hue='esi', palette='viridis', ax=ax5)
    ax5.set_title('Urgencias por Intervalos de Edad y ESI')
    ax5.set_xlabel('Intervalos de Edad')
    ax5.set_ylabel('Cantidad')
    ax5.legend(title='Nivel de Urgencia (ESI)')
    ax5.tick_params(axis='x', rotation=45)
    st.pyplot(fig5)

    # --- Estadísticas descriptivas ---
    st.markdown("### Estadísticas descriptivas del nivel de urgencia (ESI)")
    st.dataframe(urgencias['esi'].describe())

    # --- Distribución por meses ordenados (si existe columna 'arrivalmonth') ---
    # ...existing code...
    # --- Distribución por meses ordenados (si existe columna 'arrivalmonth') ---
    if 'arrivalmonth' in urgencias.columns:
        st.markdown("### Total de Pacientes por Mes de Llegada")
        # Asegura que los meses estén en orden correcto
        meses_ordenados = [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ]
        # Si los meses están en español, usa esta lista:
        # meses_ordenados = [
        #     'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        #     'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
        # ]
        urgencias['arrivalmonth'] = pd.Categorical(
            urgencias['arrivalmonth'],
            categories=meses_ordenados,
            ordered=True
        )
        conteo_meses = urgencias['arrivalmonth'].value_counts().reindex(meses_ordenados)
        fig6, ax6 = plt.subplots(figsize=(10, 6))
        sns.barplot(x=conteo_meses.index, y=conteo_meses.values, palette='viridis', ax=ax6)
        ax6.set_title('Total de Pacientes por Mes de Llegada')
        ax6.set_xlabel('Mes de Llegada')
        ax6.set_ylabel('Cantidad de Pacientes')
        ax6.tick_params(axis='x', rotation=45)
        st.pyplot(fig6)
# ...existing code...


# --- SECCIÓN CALCULADOR ---
def seccion_calculador():
    st.markdown("<h3 style='text-align: center;'> Clasificador de urgencias</h3>", unsafe_allow_html=True)
    try:
        modelo = joblib.load("modelo.pkl")
    except FileNotFoundError:
        st.error("No se encontró el archivo 'modelo.pkl'.")
        return

    archivo = st.file_uploader("📤Suba el archivo en formato CSV con los sintomas requeridos", type=["csv"])
    if archivo:
        df = pd.read_csv(archivo)
        pred = modelo.predict(df)
        df["Nivel de urgencia"] = pred
        for i, row in df.iterrows():
            st.write(f"**Paciente {i+1}** — {row['Nivel de urgencia']}")
            if row['Nivel de urgencia'] == "poco urgente":
                st.write(f'Se recomienda encarecidamente al paciente que no acuda al servicio de urgencias')
                st.write(f'RECOMENCACIONES:')
                st.write(f'1. Derivar al paciente a atencion primaria')
                st.write(f'2. Tratamiento sintomático básico')
                st.write(f'3. Proporcionar informacion sobre otras opciones de atencion (Telefono, webs ...)')
            elif row['Nivel de urgencia'] == "urgencia moderada":
                st.write(f'Se recomienda al paciente que no acuda al servicio de urgencias salvo que su estado empeore')
                st.write(f'RECOMENDACIONES:')
                st.write(f'1. Pedir cita con su medico de cabezera')
                st.write(f'2. Proporcionar tratamiento sintomatico')
                st.write(f'3. Si el paciente empeora o el medico de cabezera se lo indica, acudir al servicio de urgencias')
            else:
                st.write(f'Se avisa al paciente de la necesidad imperiosa de acudir al servicio de urgencias')
                st.write(f'RECOMENDACIONES:')
                st.write(f'1. Acudir lo antes posible, su integridad fisica y su vida pueden estar en peligro')
                st.write(f'2. Si el paciente no puede acudir por sus propios medios, avisar a algun conocido') 
                st.write(f'3. Tras el diagnostico de urgencias, acuda periodicamente a su medico de cabezera para facilitar el seguimiento de la enfermedad')
            st.write(row.drop("Nivel de urgencia"))

# --- MOSTRAR SECCIÓN SEGÚN OPCIÓN ELEGIDA ---
if seccion == "equipo":
    seccion_equipo()
elif seccion == "dataset":
    seccion_dataset()
elif seccion == "calculador":
    seccion_calculador()

st.markdown(
    """
    <hr style="margin-top: 3rem;">

    <div style='text-align: center; font-size: 0.85rem; color: gray;'>
        ⚠Esta app es meramente informativa y no puede ser sustituta de una consulta médica <br> 
        *Esta app ha sido desarrollada a partir de un modelo de machine learning y entrenada con un dataset de mas de 260.000 urgencias medicas, alcanzando una precision proxima al 75%   
        <br><br>
        Versión de la app: <strong>1.0.2</strong>
    </div>
    """,
    unsafe_allow_html=True
)





































