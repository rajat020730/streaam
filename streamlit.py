import streamlit as st
from PIL import Image

def main():
    st.title("Video and Photo Uploader")
    st.title(" For Pothole detection " )
    st.write("Upload your videos and photos here!")

    file = st.file_uploader("Upload file", type=["mp4", "jpg", "jpeg", "png"])
    location = st.text_input("Location", "")

    if file is not None:
        file_type = file.type.split('/')[0]

        if file_type == 'video':
            process_video(file, location)
        elif file_type == 'image':
            process_image(file, location)

def process_video(file, location):
    st.video(file)
    st.write("Location: " + location)

def process_image(file, location):
    image = Image.open(file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("Location: " + location)

if __name__ == '__main__':
    main()
