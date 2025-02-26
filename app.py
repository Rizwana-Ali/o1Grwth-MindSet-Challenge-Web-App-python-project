
import streamlit as st

# Custom CSS for styling and responsiveness
st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .header {
        background-color: #002F6C;
        padding: 15px;
        color: white;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
    }
    .container {
        max-width: 800px;
        margin: auto;
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .form-container {
        padding: 20px;
    }
    .title {
        color: #002F6C;
        font-size: 28px;
        font-weight: bold;
        text-align: center;
    }
    .subtitle {
        font-size: 18px;
        font-weight: bold;
        color: #007bff;
        text-align: center;
    }
    .footer {
        text-align: center;
        margin-top: 20px;
        font-size: 14px;
        color: #555;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Growth Mind-Set Challenge App")

# Header
st.markdown('<div class="header">Tuition Free Education Program on Latest Technologies</div>', unsafe_allow_html=True)

# Logo Image
logo_url = "logo.png"
st.image(logo_url, width=100)


# Second Image (Governor Image)
governor_image_url = "governor sindh.png"
st.image(governor_image_url, width=300)

# Content
st.markdown("<div class='container'>", unsafe_allow_html=True)

st.markdown("<div class='title'>Governor Sindh</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; font-size:20px;'>Kamran Khan Tessori</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Certified Cloud Applied Generative AI Engineer (GenEng)</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; font-size:16px; font-weight:bold;'>Earn up to $5,000/month</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; font-size:16px;'>Now admissions are open in Hyderabad</div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Admission Form
st.markdown("<div class='form-container'>", unsafe_allow_html=True)

st.header("Admission Form")


display_image = st.file_uploader("Upload Your Image Here", type=["png", "jpg", "jpeg"])



if display_image is not None:
    st.image(display_image, width=200)  # Adjust width as needed
else:
    st.warning("Please upload an image to display.")


name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
city = st.text_input("City")
education = st.selectbox("Highest Education Level", ["High School", "Diploma", "Undergraduate", "Postgraduate", "Other"])
experience = st.text_area("Relevant Experience (if any)")

if st.button("Submit Application"):
    if name and email and phone and city and education:
        st.success("Thank you for applying! We will get back to you soon.")
    else:
        st.error("Please fill in all required fields.")

st.markdown("<div class='footer'>© 2025 Governor Sindh - All Rights Reserved</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)















