import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Set your Hugging Face API key
HUGGING_FACE_API_KEY = "your_hugging_face_api_key"

# Streamlit interface
st.title("Text-to-Image Generator 🎨")
st.write("Enter a descriptive sentence or paragraph, and the AI will create an illustration for you!")

# Text input for descriptive prompt
user_input = st.text_area("Describe the scene you want to see in detail:")

# Function to generate image from text
def generate_image_from_text(prompt):
    # Hugging Face API endpoint for Stable Diffusion 3.5 Large
    api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
    headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}
    
    response = requests.post(api_url, headers=headers, json={"inputs": prompt})
    
    if response.status_code == 200:
        image_data = response.content
        return Image.open(BytesIO(image_data))
    else:
        st.error("Error generating image. Try a different prompt or check your API key.")
        return None

# Display generated image in Streamlit
if st.button("Generate Image"):
    if user_input:
        with st.spinner("Generating image..."):
            result_image = generate_image_from_text(user_input)
            if result_image:
                st.image(result_image, caption="Generated Illustration", use_column_width=True)
                
                # Save image to a downloadable file
                buf = BytesIO()
                result_image.save(buf, format="PNG")
                byte_im = buf.getvalue()
                
                # Add a download button to save the image
                st.download_button(
                    label="Download Image",
                    data=byte_im,
                    file_name="generated_image.png",
                    mime="image/png"
                )
    else:
        st.warning("Please enter a description to generate an image.")
