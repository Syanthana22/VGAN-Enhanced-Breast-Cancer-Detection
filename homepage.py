import streamlit as st
import home
import about

# Set page background
page_bg_img = """
    <style>
    .sidebar .sidebar-content {
        width: 120px;
    }
    [data-testid="stAppSidebar"] {
        width: 120px !important;
    }
    [data-testid="stSideBar"] {
        width: 120px !important;
    }
    [data-testid="stAppViewContainer"] > .main {
        background-image: url("https://www.nikkisplate.com/wp-content/uploads/2023/01/Blush-Pink-Wallpaper-for-Desktop-13.png");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
        background-attachment: local;
        padding: 20px;
    }

    .title {
        font-size: 32px; /* Change this value to adjust the title size */
    }

    .container {
        background-color: rgba(0, 0, 0, 0.5); /* Adjust the transparency here */
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: justify; /* Justify the text within the container */
    }
    
    </style>
    """
st.markdown(page_bg_img, unsafe_allow_html=True)

# Add navigation with the name "My Pages"
nav_selection = st.sidebar.radio("My Pages", ["Home", "About Us", "Upload Image"])

# Content based on user's selection
if nav_selection == "About Us":
    about.about()

elif nav_selection == "Upload Image":
    home.home()

else:
    st.markdown("""
    <html>
    <head>
        <title>Welcome to our Website</title>
        <style>
            .container {
                text-align: center;
                margin-top: 100px;
            }
            .container p {
                color: white;
                font-size: 18px;
                margin-bottom: 10px;
            }
        </style>
    </head>
    <body>
        <h1 style='text-align: center; color: white;'>Welcome to our Website</h1>
        <div class='container'>
            <p>Add an MRI breast image and detect your Tumor</p>
            <p>To know about Breast cancer click on About us</p>
            <p>To upload image click on Upload Image</p>
        </div>
    </body>
    </html>
    """, unsafe_allow_html=True)