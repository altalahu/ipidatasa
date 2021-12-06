import streamlit as st
import pandas as pd
import pyodbc

st.title("My First Web App")

st.header("Temperatura de Cocinas")
conn = pyodbc.connect('DRIVER={SQL Server};'
                     'SERVER=192.168.31.207;'
                     'Database=TASA;'
                     'UID=rmUser;'
                     'PWD=rmUser;'
                     'Authentication=ActiveDirectoryPassword'
                     'Trusted_Connection=yes;'
                     )
sqlquery2 = ''' select top 600 *
from remotedb r
where id >919536641 and [_NAME] like '%Cocinas Prensas.TT2%'
and [_NAME] like '%P11%' '''

ft_temperaturas = pd.read_sql(sqlquery2,conn)
st.write(ft_temperaturas)
