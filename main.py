# import streamlit as st
# import os

# def home_page():
#     st.title("Hi")
#     st.write("Welcome ")

# if "page" not in st.session_state:
#     st.session_state.page = "home"


# # Sidebar navigation with Home button
# st.sidebar.title("Content")
# if st.sidebar.button("Home Page"):
#     st.session_state.page = "home"
#     st.rerun()

# app_mode = st.sidebar.selectbox("Choose a project", ["Select a project", "Plant Leaf Diesease Detection", "Face Recognition", "OCR", "Suduko"], index=0)

# if app_mode != "Select a project":
#     st.session_state.page = app_mode

# # Display content based on selection
# if st.session_state.page == "home":
#     home_page()
# elif st.session_state.page == "Plant Leaf Diesease Detection":
#     st.markdown("""<h1 style='font-size:36px;'>Plant Leaf Diesease Detection</h1>""", unsafe_allow_html=True)
#     st.write("Details about Project.")
# elif st.session_state.page == "Face Recognition":
#     st.markdown("""<h1 style='font-size:36px;'>Face Recognition</h1>""", unsafe_allow_html=True)
#     st.write("Details about Project.")
# elif st.session_state.page == "OCR":
#     st.markdown("""<h1 style='font-size:36px;'>OCR</h1>""", unsafe_allow_html=True)
#     st.write("Details about Project.")
# elif st.session_state.page == "Suduko":
#     st.markdown("""<h1 style='font-size:36px;'>Suduko</h1>""", unsafe_allow_html=True)
#     st.write("Details about Project.")
     
import streamlit as st
import importlib

# Function for the home page
def home_page():
    st.title("Hi")
    st.write("Welcome!")

# Ensure session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

# Sidebar navigation
st.sidebar.title("Content")
if st.sidebar.button("Home Page"):
    st.session_state.page = "home"
    st.rerun()

# Project selection
app_mode = st.sidebar.selectbox(
    "Choose a project",
    ["Select a project", "Plant Leaf Disease", "Face Recognition", "OCR", "Suduko"],
    index=0
)

# Run the selected project
if app_mode != "Select a project":
    st.session_state.page = app_mode
    module_name = app_mode.lower().replace(" ", "_")  # Convert name to match filename

    try:
        project_module = importlib.import_module(module_name)  # Import from the same folder
        # project_module.app()  # Call the app function inside the module
    except ModuleNotFoundError:
        st.error(f"Module '{module_name}.py' not found!")

# Display home page if no project selected
if st.session_state.page == "home":
    home_page()