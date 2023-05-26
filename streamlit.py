import streamlit as st
from PIL import Image

def main():
    st.title("Video and Photo Uploader")
    st.write("Upload your videos and photos here!")

    file = st.file_uploader("Upload file", type=["mp4", "jpg", "jpeg", "png"])

    if file is not None:
        file_type = file.type.split('/')[0]

        if file_type == 'video':
            process_video(file)
        elif file_type == 'image':
            process_image(file)

def process_video(file):
    st.video(file)

def process_image(file):
    image = Image.open(file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

if __name__ == '__main__':
    main()
