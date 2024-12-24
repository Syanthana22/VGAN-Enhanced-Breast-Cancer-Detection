# logout.py
import streamlit as st
import Login
import breastcanc

def logout():
    st.write("Logged out successfully! Redirecting to login page...")
    # Add code to redirect to login page
    # Assuming Login.login() contains the code for the login page
    breastcanc.main()

if __name__ == "__main__":
    breastcanc.main()
