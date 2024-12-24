import streamlit as st

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

    .btn {
        background-color: #008CBA;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

def about():
    set_page_bg()
    st.markdown("""
    <html>
    <head>
        <title>About page</title>
        <link rel="stylesheet" href="style5.css">
        <style>
            .about {
                text-align: center;
            }
            .text-container {
                background-color: rgba(0, 0, 0, 0.5); /* Adjust the transparency here */
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
            }
            .heading {
                font-size: 60px;
                color: rgb(250, 8, 129);
                margin-bottom: 20px;
            }
            .paragraph {
                text-align: justify;
                color: white; /* Adjust the text color here */
            }
        </style>
    </head>
    <body>
        <section class="about">
            <div class="main">
                <div class="text-container">
                    <h1 class="heading">About Breast Cancer</h1>
                    <h3><b>What is Breast Cancer?</b></h3>
                    <p class="paragraph">Breast cancer is a type of cancer that forms in the cells of the breast. It commonly begins in the ducts or lobules of the breast tissue. Breast cancer can manifest as a lump or mass in the breast, changes in breast shape or size, skin dimpling, or nipple discharge. Early detection through screenings like mammograms and prompt treatment increase the chances of successful outcomes for those affected.</p>
                    <h3>Who invented the first medicine for Breast Cancer?</h3>
                    <p class="paragraph">The development of the first medicine specifically for breast cancer involved contributions from various researchers and pharmaceutical companies. One of the most significant breakthroughs came with the discovery of tamoxifen. Tamoxifen, a medication that blocks the effects of estrogen in breast tissue, was first synthesized by Dr. Arthur L. Walpole and his team at Imperial Chemical Industries (ICI) Pharmaceuticals in the United Kingdom in the 1960s. Tamoxifen has since become a cornerstone in the treatment of hormone receptor-positive breast cancer, significantly improving survival rates for many patients.</p>
                </div>
            </div>
        </section>
    </body>
    </html>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    about()