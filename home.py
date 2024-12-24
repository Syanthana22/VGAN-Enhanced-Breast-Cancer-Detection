# home.py
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

def set_page_bg():
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: url("https://www.nikkisplate.com/wp-content/uploads/2023/01/Blush-Pink-Wallpaper-for-Desktop-13.png");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
        background-attachment: local;s
    }

    .title {
        font-size: 32px; /* Change this value to adjust the title size */
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Load the VAE model
def load_vae_model():
    return tf.keras.models.load_model("vae_main")

# Function to preprocess the uploaded image
def preprocess_image(image):
    # Convert the image to grayscale if it's not already
    if image.mode != "L":
        image = image.convert("L")
    
    # Resize to match model input shape
    image = image.resize((64, 64))
    image = np.array(image)
    image = image / 255.0  # Normalize pixel values
    image = np.expand_dims(image, axis=-1)  # Add channel dimension
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Function to generate image predictions
def generate_predictions(image, vae_model):
    reconstructed_image = vae_model.predict(image)
    return reconstructed_image

# Function to classify the reconstructed image
def classify_image(image, vae_model):
    def detect_tumors(image, vae_model):
        try:
            # Reconstruct the image and compute reconstruction error
            reconstructed_image = generate_predictions(image, vae_model)

            # Compute features indicative of tumors
            average_intensity = np.mean(reconstructed_image)
            variance = np.var(reconstructed_image)

            # Adjusted thresholds for tumor classification
            intensity_threshold_tumor = 0.25
            variance_threshold_tumor = 0.05

            # Adjusted thresholds for non-tumor classification
            intensity_threshold_non_tumor = 0.2
            variance_threshold_non_tumor = 0.03

            if average_intensity > intensity_threshold_tumor and variance > variance_threshold_tumor:
                return "Tumorous image detected."
            elif average_intensity < intensity_threshold_non_tumor and variance < variance_threshold_non_tumor:
                return "Non-tumorous image detected."
            else:
                # Return "Non-tumorous image detected." for cases that don't meet tumor criteria
                return "Non-tumorous image detected."
        except Exception as e:
            return f"Error detecting tumors: {e}"

    # Classify the reconstructed image
    classification_result = detect_tumors(image, vae_model)
    return classification_result

# Home page
def home():
    set_page_bg()
    st.markdown("<h2 style='text-align: center;color: black;'>Breast Cancer Detection</h2>", unsafe_allow_html=True)
    
    # Initialize session state
    session_state = st.session_state
    
    # Set default page to home
    if 'page' not in session_state:
        session_state.page = 'home'
    
    # Render different pages based on session_state
    if session_state.page == 'home':
        # File upload
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            # Preprocess uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            # Preprocess the image for the VAE model
            processed_image = preprocess_image(image)
            
            # Load the VAE model
            vae_model = load_vae_model()
            
            # Generate predictions
            reconstructed_image = generate_predictions(processed_image, vae_model)
            
            # Classify the reconstructed image
            classification_result = classify_image(processed_image, vae_model)
            st.write("<h3 style='color: black;'>Classification Result: " + classification_result + "</h3>", unsafe_allow_html=True)

if __name__ == "__main__":
    home()
