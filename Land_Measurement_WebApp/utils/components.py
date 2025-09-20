# utils.py
import streamlit as st
import pandas as pd
from PIL import Image
def process_data(data):
    """Simulasi proses data"""
    with st.spinner("Process data..."):
        import time
        time.sleep(2)
    return data * 2

def show_toast(message, icon="ℹ️"):
    """Menampilkan toast message"""
    st.toast(message, icon=icon)

def markdown(text):
    st.markdown(text, unsafe_allow_html=True)

def image( image_name):
        st.image(Image.open(image_name))

def info(message):
    st.info(message)

def warning(message):
    st.warning(message)

def error(message):
    st.error(message)

def success(message):
    st.success(message)

def write(text):
    st.write(text)

def button(label, key=None, type="primary", use_container_width=False):
    return st.button(label, key=key, type=type, use_container_width=use_container_width)

def number_input(label, min_value=None, max_value=None, value=0.0, step=0.001, format=None, help=None,key=None):
    return st.number_input(label, min_value=min_value, max_value=max_value, value=value, step=step, format=format, help=help,key=key)

def text_input(label, value="", help=None):
    return st.text_input(label, value=value, help=help)

def columns(spec):
    return st.columns(spec)

def download_button(label, data, file_name):
    return st.download_button(label=label, data=data, file_name=file_name)

def line_chart(data, x, y, height=400):
    return st.line_chart(data=data, x=x, y=y, height=height)

def bar_chart(data, x, y, height=400):
    return st.bar_chart(data=data, x=x, y=y, height=height)

def scatter_chart(data, x, y, height=400):
    return st.scatter_chart(data=data, x=x, y=y, height=height)

def dataframe(data, use_container_width=True):
    return st.dataframe(data, use_container_width=use_container_width)

def tabs(tabs):
    return st.tabs(tabs)  

def text(text):
    return st.text(text)

def spinner(text):
    return st.spinner(text)

def subheader(text):
    return st.subheader(text)

def get_state(key, default=None):
    return st.session_state.get(key, default)

def set_state(key, value):
    st.session_state[key] = value

def del_state(key):
    if key in st.session_state:
        del st.session_state[key]

def session_state():
    return st.session_state

def expander(label, expanded=False):
    return st.expander(label, expanded=expanded)

def container():
    return st.container()

def secrets(key):
    return st.secrets.get(key, None)

def rerun():
    st.rerun()

def code(text, language="python"):
    return st.code(text, language=language)

def header(text):
    return st.header(text)
    
def link_button(label, url, key=None):
    return st.link_button(f"{label}",f"{url}",use_container_width=True)


@st.dialog("Confirm your input")
def confirm_and_process(value, result_name="confirm_result"):
    st.write(value)
    col = st.columns([1,2,1,2,1])
    with col[3]:
        if st.button("Next", key="submit_dialog"):
            st.session_state[result_name] = True
            st.rerun()
    with col[1]:
        if st.button("Cancel", key="cancel_dialog"):
            st.session_state[result_name] = False
            st.rerun()
            

        
    