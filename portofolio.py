import streamlit as st
import webbrowser
import base64

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("FOTO.jpeg")

# page_bg_img = f"""
# <style>

# [data-testid="stAppViewContainer"] {{
# background-image: url("data:image/png;base64,{img}");
# background-position: center; 
# background-repeat: no-repeat;
# background-attachment: fixed;
# }}

# </style>
# """



col1, col2 = st.columns(2)

with col1:
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown(
        f"""
        <style>
        .circular-image {{
            width: 250px; /* Ukuran gambar */
            height: 250px; /* Ukuran gambar */
            border-radius: 50%; /* Membuat gambar menjadi bulat */
            object-fit: cover; /* Menjaga proporsi gambar */
            border: 2px solid #4CAF50; /* Opsional: Tambahkan border */
        }}
        </style>
        <div style="text-align: center;">
            <img src="data:image/jpeg;base64,{img}" alt="Circular Image" class="circular-image"/>
        </div>
        """,
        unsafe_allow_html=True
    )
    

with col2:
    
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')

    st.markdown(
        """
        <a href="https://proyekdataanalysisreksa.streamlit.app/" target="_blank">
            <button style="
                background-color: #4CAF50; /* Hijau */
                border: none;
                color: white;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 8px;">
                Data Analysis Project
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

    st.markdown('')
    st.markdown('')

    st.markdown(
        """
        <a href="https://proyekdataanalysisreksa.streamlit.app/" target="_blank">
            <button style="
                background-color: #4CAF50; /* Hijau */
                border: none;
                color: white;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 8px;">
                Go to Example.com
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )    

    st.markdown('')
    st.markdown('')
    
    st.markdown(
        """
        <a href="https://proyekdataanalysisreksa.streamlit.app/" target="_blank">
            <button style="
                background-color: #4CAF50; /* Hijau */
                border: none;
                color: white;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 8px;">
                GitHub Repository
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )