# Proyecto Integrador - Minería de Datos I


## Información general

Este proyecto corresponde al trabajo integrador de la materia Minería de Datos I.

Se analiza un dataset de usuarios de una plataforma de streaming mediante un proceso de inspección inicial, limpieza, análisis exploratorio, reducción de dimensionalidad y comunicación de resultados.

El trabajo conserva el dataset original sin modificaciones y genera una versión procesada para el análisis.

Repositorio GitHub: https://github.com/rapazxc/PI_Mineria_Datos_1
Aplicación Streamlit: https://pimineriadatos1-tqsw3bdv3lqgxtqkwaqpti.streamlit.app/
Informe final: `reports/informe_final.pdf`
Log ETL: `logs/pipeline_log.csv`

## Objetivo del proyecto

Aplicar un proceso de minería de datos sobre un dataset de usuarios de streaming.

El objetivo es inspeccionar la calidad inicial de los datos, preparar una versión limpia y analizar patrones de comportamiento de visualización.

También se busca aplicar PCA sobre variables numéricas para evaluar si la información puede representarse en menos dimensiones.

## Dataset

El dataset contiene registros de usuarios de una plataforma de streaming.

Cada fila representa un usuario.

Las variables incluyen edad, plan de suscripción, país, género favorito, tiempo mensual de visualización, fecha de último inicio de sesión y tickets de soporte.

El archivo original se conserva en `data/raw`.

La versión procesada utilizada para el análisis se guarda en `data/processed`.

## Estructura del repositorio

```text
PI_Mineria_Datos_1/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_inspeccion_inicial.ipynb
│   ├── 02_calidad_y_limpieza.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_pca.ipynb
│   └── 05_conclusiones.ipynb
├── app/
│   ├── Home.py
│   └── pages/
│       ├── 01_Dataset.py
│       ├── 02_EDA.py
│       ├── 03_PCA.py
│       └── 04_Conclusiones.py
├── reports/
│   └── informe_final.pdf
└── logs/
    └── pipeline_log.csv
```

## Preparación y calidad de datos

La inspección inicial se desarrolló en `notebooks/01_inspeccion_inicial.ipynb`.

La limpieza y preparación se realizó en `notebooks/02_calidad_y_limpieza.ipynb`.

Se detectaron duplicados completos, `user_id` repetidos, valores faltantes, categorías inconsistentes, fechas problemáticas y valores numéricos fuera de rango.

El dataset original fue preservado en `data/raw`.

El dataset limpio fue guardado en `data/processed`.

Las transformaciones relevantes fueron registradas en `logs/pipeline_log.csv`.

## Resumen del análisis exploratorio

El análisis exploratorio se desarrolló en `notebooks/03_eda.ipynb`.

Se analizaron distribuciones y relaciones vinculadas al comportamiento de visualización de los usuarios.

El EDA incluyó dos visualizaciones univariadas, dos bivariadas y una multivariada.

Cada visualización fue acompañada por una interpretación vinculada al objetivo del análisis.

Las interpretaciones completas se encuentran en el notebook y en la aplicación Streamlit.

## Reducción de dimensionalidad

La reducción de dimensionalidad se desarrolló en `notebooks/04_pca.ipynb`.

Se aplicó PCA sobre variables numéricas del dataset limpio.

Antes de PCA se aplicó escalamiento con `StandardScaler`.

Se analizaron la varianza explicada, la proyección en componentes principales y los loadings.

Los resultados indicaron que la varianza se distribuye de manera similar entre las componentes principales.

## Visualización interactiva

La aplicación interactiva fue desarrollada con Streamlit.

Incluye secciones para presentar el dataset, el análisis exploratorio, PCA y conclusiones.

La aplicación comunica los resultados principales para público general y no reemplaza la evidencia técnica del repositorio.

Aplicación Streamlit: https://pimineriadatos1-tqsw3bdv3lqgxtqkwaqpti.streamlit.app/
Repositorio GitHub: https://github.com/rapazxc/PI_Mineria_Datos_1

## Cómo ejecutar localmente

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación Streamlit:

```bash
streamlit run app/Home.py
```

Los notebooks deben ejecutarse desde la carpeta `notebooks`.

## Conclusiones

El proyecto permitió preparar y analizar un dataset de usuarios de streaming mediante un proceso reproducible.

La limpieza mejoró la consistencia del dataset sin modificar el archivo original.

El análisis exploratorio mostró patrones asociados al tiempo mensual de visualización.

PCA permitió visualizar la información numérica en componentes principales, aunque sin una separación clara por plan de suscripción.

Las conclusiones completas se encuentran en `notebooks/05_conclusiones.ipynb` y en `reports/informe_final.pdf`.
