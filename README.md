
# Text-to-Image Generator 🎨

This project provides a **Streamlit-based web application** for generating illustrations based on detailed text descriptions, using the **Stable Diffusion 3.5 Large** model by Stability AI. Users can enter a descriptive sentence or paragraph, and the model will create an illustration based on the text prompt.

## Project Overview

The project integrates the `stabilityai/stable-diffusion-3.5-large` model from Hugging Face’s model hub to generate high-quality, prompt-adhering images up to 1-megapixel resolution. This setup is ideal for personal research, creative exploration, and high-quality non-commercial image generation.

## Features

- **Easy-to-use Web Interface**: Built with Streamlit, making it interactive and user-friendly.
- **Detailed Prompt Support**: Accepts multi-line, descriptive prompts, producing images based on complex descriptions.
- **Hugging Face Model Integration**: Uses the Stable Diffusion 3.5 Large model via Hugging Face’s API.

## Requirements

1. **Python 3.7+**
2. **API Key from Hugging Face**
   - You’ll need an API key from [Hugging Face](https://huggingface.co/) to access the model.

3. **Dependencies**:
   Install the dependencies by running:
   ```bash
   pip install streamlit requests pillow
   ```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/gamzeakkurt/text-to-image-generator.git
cd text-to-image-generator
```

### 2. Configure API Key

Open the `app.py` file and add your Hugging Face API key:
```python
HUGGING_FACE_API_KEY = "your_hugging_face_api_key"
```

### 3. Run the Application

To start the Streamlit app, run:
```bash
streamlit run app.py
```

### 4. Using the Application

- Once the app is running, open your browser to `http://localhost:8501`.
- Enter a detailed prompt in the text area, then click on **Generate Image** to create an illustration.
- The generated image will display below the prompt area.

## Code Explanation

The application consists of a few main components:
- **Text Input**: Uses `st.text_area` to capture the user’s prompt.
- **Image Generation**: Sends the prompt to Hugging Face’s Stable Diffusion 3.5 Large API and receives the generated image.
- **Display**: If successful, the image is displayed using `st.image`.

## Example

**Prompt**: _"A futuristic city skyline at sunset, with flying cars and neon lights reflecting off skyscrapers."_

**Sample Output**:

<img width="724" alt="Screenshot 2024-10-25 at 22 01 25" src="https://github.com/user-attachments/assets/d3424d3b-b3b0-434e-8cfd-fbc09209d014"> 


## License

This project is for non-commercial research and educational use. Refer to Stability AI’s license for more information on usage limitations.

---

## Acknowledgments

- **Stable Diffusion 3.5 Large** by Stability AI.
- **Streamlit** for creating a seamless web interface.
- **Hugging Face** for providing the model hosting and API infrastructure.

---
