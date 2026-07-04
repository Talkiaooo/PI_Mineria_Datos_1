import streamlit as st
import pandas as pd
from pathlib import Path

def load_data():
    # .parent.parent sube dos niveles desde 'app/utils.py' hasta la raíz
    # Esto funcionará sin importar cómo se llame tu carpeta raíz
    ruta_csv = Path(__file__).resolve().parent.parent / "data" / "processed" / "straming_users_clean.csv"
    return pd.read_csv(ruta_csv)
    
    # Esto cargará el archivo sin importar desde dónde ejecutes la terminal
    return pd.read_csv(ruta_csv)

import os
from datetime import datetime

def log_transformacion(paso, descripcion, df, log_path='logs/pipeline_log.csv'):
    
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    filas = len(df)
    nulos = df.isnull().sum().sum()
    
   
    data = {
        'Timestamp': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        'Paso': [paso],
        'Descripción': [descripcion],
        'Filas': [filas],
        'Nulos': [nulos]
    }
    
    df_log = pd.DataFrame(data)
    
    if not os.path.exists(log_path):
        df_log.to_csv(log_path, index=False)
    else:
        df_log.to_csv(log_path, mode='a', header=False, index=False)