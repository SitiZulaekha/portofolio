
import streamlit as st



st.set_page_config(
    page_title="Portfolio | Zulaikha",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("SELAMAT DATANG DI PORTFOLIO SAYA 👨‍🎓")

st.sidebar.success("SILAHKAN PILIH MENU DI ATAS")

import streamlit as st

col1, col2 = st.columns(2)

with col1:
   st.header("About Me")
   st.image("zule.jpg", width= 390)

with col2:
   st.header("My Biodata")
   st.subheader("NAMA : Siti Zulaekha")
   st.caption("NIM : 0402201083")
   st.write(
            """
            - Tempat Tanggal Lahir : Brebes 1 September 2002 
            - Alamat               : Sengon Tanjung Brebes
            - Hobi                 : Reading book
            - Cita-cita            : Guru mulia
            - Hal yang disukai     : Kumpul bareng keluarga
            - Kesan         : Senang bisa belajar di Al-bukhori dan Tetap jaga kepercanyaan
        
            """
        )
st.header("*Call Me If You Want*")