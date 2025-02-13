import streamlit as st

def home_page():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

if "page" not in st.session_state:
    st.session_state.page = "home"

# Sidebar navigation with Home button
st.sidebar.title("Navigation")
if st.sidebar.button("Home"):
    st.session_state.page = "home"
    st.rerun()

app_mode = st.sidebar.selectbox("Choose a page", ["Select a project", "Project 1", "Project 2", "Project 3", "Project 4"], index=0)

if app_mode != "Select a project":
    st.session_state.page = app_mode

# Display content based on selection
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "Project 1":
    st.markdown("""<h1 style='font-size:36px;'>Project 1</h1>""", unsafe_allow_html=True)
    st.write("Details about Project 1.")
elif st.session_state.page == "Project 2":
    st.markdown("""<h1 style='font-size:36px;'>Project 2</h1>""", unsafe_allow_html=True)
    st.write("Details about Project 2.")
elif st.session_state.page == "Project 3":
    st.markdown("""<h1 style='font-size:36px;'>Project 3</h1>""", unsafe_allow_html=True)
    st.write("Details about Project 3.")
elif st.session_state.page == "Project 4":
    st.markdown("""<h1 style='font-size:36px;'>Project 4</h1>""", unsafe_allow_html=True)
    st.write("Details about Project 4.")
