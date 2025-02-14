# import streamlit as st
# import face_recognition,ocr,plant_leaf_disease,suduko

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
#     # st.markdown("""<h1 style='font-size:36px;'>Plant Leaf Diesease Detection</h1>""", unsafe_allow_html=True)
#     # st.write("Details about Project.")
#     plant_leaf_disease.app()
# elif st.session_state.page == "Face Recognition":
#     st.markdown("""<h1 style='font-size:36px;'>Face Recognition</h1>""", unsafe_allow_html=True)
#     st.write("Details about Project.")
# elif st.session_state.page == "OCR":
#     st.markdown("""<h1 style='font-size:36px;'>OCR</h1>""", unsafe_allow_html=True)
#     st.write("Details about Project.")
# elif st.session_state.page == "Suduko":
#     st.markdown("""<h1 style='font-size:36px;'>Suduko</h1>""", unsafe_allow_html=True)
#     st.write("Details about Project.")


# # import streamlit as st

# # def home_page():
# #     st.title("Hi")
# #     st.write("Welcome")

# # if "page" not in st.session_state:
# #     st.session_state.page = "home"

# # # Sidebar navigation with Home button
# # st.sidebar.title("Content")

# # if st.sidebar.button("Home Page"):
# #     st.session_state.page = "home"
# #     st.rerun()

# # app_mode = st.sidebar.selectbox("Choose a project", 
# #     ["Select a project", "Plant Leaf Disease Detection", "Face Recognition", "OCR", "Sudoku"], index=0)

# # if app_mode != "Select a project":
# #     st.session_state.page = app_mode

# #     if app_mode == "Plant Leaf Disease Detection":
# #         st.switch_page("/pages/plant_lead_disease.py")
# #     elif app_mode == "Face Recognition":
# #         st.switch_page("/pages/plant_lead_disease.py")
# #     elif app_mode == "OCR":
# #         st.switch_page("/pages/plant_lead_disease.py")
# #     elif app_mode == "Sudoku":
# #         st.switch_page("/pages/plant_lead_disease.py")

# # # Display home page
# # if st.session_state.page == "home":
# #     home_page()


import streamlit as st

from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv
load_dotenv()

import face_recognition,ocr,plant_leaf_disease,suduko
st.set_page_config(
        page_title="Pondering",
)


st.markdown(
    """
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src=f"https://www.googletagmanager.com/gtag/js?id={os.getenv('analytics_tag')}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', os.getenv('analytics_tag'));
        </script>
    """, unsafe_allow_html=True)
print(os.getenv('analytics_tag'))


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Pondering ',
                options=['plant_leaf_diseaes','ocr','face_recognition','suduko'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "plant_leaf_disease":
            plant_leaf_disease.app()
        if app == "ocr":
            ocr.app()    
        if app == "face_recognition":
            face_recognition.app()        
        if app == "suduko":
            suduko.app()   
             
          
             
    run()            
         