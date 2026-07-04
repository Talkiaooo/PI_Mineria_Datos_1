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