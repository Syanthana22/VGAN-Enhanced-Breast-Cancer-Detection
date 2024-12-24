import streamlit as st
import home

def set_page_bg():
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: url("https://www.nikkisplate.com/wp-content/uploads/2023/01/Blush-Pink-Wallpaper-for-Desktop-13.png");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
        background-attachment: local;
    }

    .title {
        font-size: 32px; /* Change this value to adjust the title size */
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

def signup():
    set_page_bg()
    st.markdown("<h2 style='text-align: center;color: black;'>Sign Up</h2>", unsafe_allow_html=True)
    
    # Retrieve or initialize values for the input fields
    username = st.session_state.get("signup_username", "")
    password = st.session_state.get("signup_password", "")
    email = st.session_state.get("signup_email", "")

    # Render input fields
    username = st.text_input("Username", value=username, key="signup_username")
    password = st.text_input("Password", type="password", value=password, key="signup_password")
    email = st.text_input("Email", value=email, key="signup_email")

    col1, col2 = st.columns([2, 1])
    
    with col1:
        if st.button("Submit", key="signup_submit_button"):
            if username and password and email:  # Check if all fields are filled
                # Set session state flag to indicate signup completion
                st.session_state.signup_completed = True
                # Redirect to login page
                login()
            else:
                st.warning("Please fill in all fields before submitting.")

    with col2:
        if st.button("Reset", key="signup_reset_button"):
            # Reset the page
            st.session_state.clear()

    # Render the Login button below the Submit and Reset buttons
    st.markdown('<a href="Login.py"><button class="btn">Login</button></a>', unsafe_allow_html=True)

def login():
    set_page_bg()
    st.markdown("<h2 style='text-align: center;color: black;'>Login</h2>", unsafe_allow_html=True)
    
    # Retrieve or initialize values for the input fields
    username = st.session_state.get("login_username", "")
    password = st.session_state.get("login_password", "")

    # Render input fields
    username = st.text_input("UserName", value=username, key="login_username")
    password = st.text_input("PassWord", type="password", value=password, key="login_password")

    if st.button("Submit"):
        if username and password:  # Check if both fields are filled
            # Redirect to home page if authentication is successful
            st.session_state.login_completed = True
            home.home()
        else:
            st.warning("Please fill in both Username and Password fields.")

if __name__ == "__main__":
    signup()
