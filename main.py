import streamlit as st

def home_page():
    st.title("Hi")
    st.write("Welcome ")

if "page" not in st.session_state:
    st.session_state.page = "home"



# Sidebar navigation with Home button
st.sidebar.title("Content")
if st.sidebar.button("Home Page"):
    st.session_state.page = "home"
    st.rerun()

app_mode = st.sidebar.selectbox("Choose a project", ["Select a project", "Plant Leaf Diesease Detection", "Face Recognition", "OCR", "Suduko"], index=0)

if app_mode != "Select a project":
    st.session_state.page = app_mode

# Display content based on selection
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "Plant Leaf Diesease Detection":
    st.markdown("""<h1 style='font-size:36px;'>Plant Leaf Diesease Detection</h1>""", unsafe_allow_html=True)
    st.write("Details about Project.")
elif st.session_state.page == "Face Recognition":
    st.markdown("""<h1 style='font-size:36px;'>Face Recognition</h1>""", unsafe_allow_html=True)
    st.write("Details about Project.")
elif st.session_state.page == "OCR":
    st.markdown("""<h1 style='font-size:36px;'>OCR</h1>""", unsafe_allow_html=True)
    st.write("Details about Project.")
elif st.session_state.page == "Suduko":
    st.markdown("""<h1 style='font-size:36px;'>Suduko</h1>""", unsafe_allow_html=True)
    st.write("Details about Project.")


# import streamlit as st

# def home_page():
#     st.title("Hi")
#     st.write("Welcome")

# if "page" not in st.session_state:
#     st.session_state.page = "home"

# # Sidebar navigation with Home button
# st.sidebar.title("Content")

# if st.sidebar.button("Home Page"):
#     st.session_state.page = "home"
#     st.rerun()

# app_mode = st.sidebar.selectbox("Choose a project", 
#     ["Select a project", "Plant Leaf Disease Detection", "Face Recognition", "OCR", "Sudoku"], index=0)

# if app_mode != "Select a project":
#     st.session_state.page = app_mode

#     if app_mode == "Plant Leaf Disease Detection":
#         st.switch_page("/pages/plant_lead_disease.py")
#     elif app_mode == "Face Recognition":
#         st.switch_page("/pages/plant_lead_disease.py")
#     elif app_mode == "OCR":
#         st.switch_page("/pages/plant_lead_disease.py")
#     elif app_mode == "Sudoku":
#         st.switch_page("/pages/plant_lead_disease.py")

# # Display home page
# if st.session_state.page == "home":
#     home_page()