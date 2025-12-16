import streamlit as st
from PIL import Image
from io import BytesIO
import numpy as np
import cv2  


def convertto_watercolorsketch(inp_img):
    img_1 = cv2.edgePreservingFilter(inp_img, flags=2, sigma_s=50, sigma_r=0.8)
    img_water_color = cv2.stylization(img_1, sigma_s=100, sigma_r=0.5)
    return(img_water_color)

def pencilsketch(inp_img):
    img_pencil_sketch, pencil_color_sketch = cv2.pencilSketch(inp_img, sigma_s=50, sigma_r=0.07, shade_factor=0.0825)
    return(img_pencil_sketch)

def negative_filter(inp_img):
    negative_img = cv2.bitwise_not(inp_img)
    negative_img = cv2.cvtColor(negative_img, cv2.COLOR_BGR2RGB)
    return negative_img

def pixelation_filter(inp_img):
    pixel_size = 8  # <-- static pixel size
    h, w = inp_img.shape[:2]
    temp = cv2.resize(
        inp_img,
        (w // pixel_size, h // pixel_size),
        interpolation=cv2.INTER_LINEAR
    )
    pixelated = cv2.resize(
        temp,
        (w, h),
        interpolation=cv2.INTER_NEAREST
    )
    return pixelated

def load_an_image(image):
    img = Image.open(image)
    return img


def main():

    st.title('WEB APPLICATION TO CONVERT IMAGE TO SKETCH')
    st.write("This is an application developed for converting\
    your ***image*** to a ***Water Color Sketch*** OR ***Pencil Sketch***")
    st.subheader("Please Upload your image")

   
    image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])

    
    if image_file is not None:
      
        
        option = st.selectbox('How would you like to convert the image',
                              ( 'None',
                                'Convert to water color sketch',
                               'Convert to pencil sketch',
                               'Convert to negative filter',
                               'Convert to pixelation filter'))
        
        if option == 'Convert to water color sketch':
            image = Image.open(image_file)
            final_sketch = convertto_watercolorsketch(np.array(image))
            im_pil = Image.fromarray(final_sketch)

            
            col1, col2 = st.columns(2)
            with col1:
                st.header("Original Image")
                st.image(load_an_image(image_file), width=250)

            with col2:
                st.header("Water Color Sketch")
                st.image(im_pil, width=250)
                buf = BytesIO()
                img = im_pil
                img.save(buf, format="JPEG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="Download image",
                    data=byte_im,
                    file_name="watercolorsketch.png",
                    mime="image/png"
                )

        if option == 'Convert to pencil sketch':
            image = Image.open(image_file)
            final_sketch = pencilsketch(np.array(image))
            im_pil = Image.fromarray(final_sketch)
            
            
            col1, col2 = st.columns(2)
            with col1:
                st.header("Original Image")
                st.image(load_an_image(image_file), width=250)

            with col2:
                st.header("Pencil Sketch")
                st.image(im_pil, width=250)
                buf = BytesIO()
                img = im_pil
                img.save(buf, format="JPEG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="Download image",
                    data=byte_im,
                    file_name="watercolorsketch.png",
                    mime="image/png"
                )
    
        if option == 'Convert to negative filter':
            image = Image.open(image_file)
            final_image = negative_filter(np.array(image))
            im_pil = Image.fromarray(final_image)

            col1, col2 = st.columns(2)
            with col1:
                st.header("Original Image")
                st.image(load_an_image(image_file), width=250)

            with col2:
                st.header("Negative Image")
                st.image(im_pil, width=250)
                buf = BytesIO()
                img = im_pil
                img.save(buf, format="JPEG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="Download image",
                    data=byte_im,
                    file_name="negative_image.png",
                    mime="image/png"
                )
        if option == 'Convert to pixelation filter':
            image = Image.open(image_file)
            final_image = pixelation_filter(np.array(image))
            im_pil = Image.fromarray(final_image)

            col1, col2 = st.columns(2)
            with col1:
                st.header("Original Image")
                st.image(load_an_image(image_file), width=250)

            with col2:
                st.header("Pixelated Image")
                st.image(im_pil, width=250)
                buf = BytesIO()
                img = im_pil
                img.save(buf, format="JPEG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="Download image",
                    data=byte_im,
                    file_name="pixelated_image.png",
                    mime="image/png"
                )


main()