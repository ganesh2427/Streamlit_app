import streamlit as st
import importlib
import sys

def home_page():
    st.title("Hi")
    st.write("Welcome!")

if "page" not in st.session_state:
    st.session_state.page = "home"

st.sidebar.title("Content")
if st.sidebar.button("Home Page"):
    st.session_state.page = "home"
    st.rerun()

app_mode = st.sidebar.selectbox(
    "Choose a project",
    ["Select a project", "Plant Leaf Disease", "Face Recognition", "OCR", "Suduko","kjad"],
    index=0
)
if st.session_state.page == "home":
    home_page()

if app_mode != "Select a project":
    if st.session_state.page != app_mode:
        st.session_state.page = app_mode
        st.rerun()

    module_name = app_mode.lower().replace(" ", "_")  # Convert to match filename

    try:
        if module_name in sys.modules:
            del sys.modules[module_name]  # Force reload of the module

        project_module = importlib.import_module(module_name)  # Import dynamically
        importlib.reload(project_module)  # Reload module to reflect changes

        if hasattr(project_module, "app"):
            project_module.app()  # Run app function ONCE
        else:
            st.error(f"Module '{module_name}.py' does not have an 'app()' function!")
    except ModuleNotFoundError:
        st.error(f"Module '{module_name}.py' not found!")
        
 


