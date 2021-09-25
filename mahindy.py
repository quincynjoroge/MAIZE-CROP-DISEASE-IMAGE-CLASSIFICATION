# Import libraries

import tensorflow as tf
import torch
import numpy as np
import pandas as pd
import cv2
import streamlit as st

# page selector
my_page = st.sidebar.radio('Page Navigation', ['Home', 'Model'])

if my_page == 'Home':
    #st.title('')
    #button = st.button('a button')
    #if button:
        #st.write('clicked')
#else:
    #st.title('this is a different page')
    #slide = st.slider('this is a slider')
    #slide


# Horizontal partitions
    icon = st.container()
    header = st.container()
    overview1 = st.container()
    #spacing = st.container()
    overview2 = st.container()
    predictor = st.container()
    view = st.container()
    recommend = st.container()


# add elements to containers
# icon
    #with icon:
        #st.set_page_config(page_title='Mahindy', page_icon='🖖')
# header
    with header:
        #st.title('MAHINDY')
        st.markdown("<h1 style='text-align: center; color: lightgreen;'>MAHINDY</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center;'><i>Maize Crop Disease Identification</i></h4>", unsafe_allow_html=True)
        #st.write('__*Maize Crop Disease Identification.*__')
        st.write('')
        st.write('')
    # overview 1
    with overview1:
        col1,col2 = st.columns(2)
        with col1:
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            maize ='https://th.bing.com/th/id/OIP.n-fH7-heN1AqnBHt4lrwkgHaE8?w=249&h=180&c=7&r=0&o=5&pid=1.7'
            st.image(maize, width=300)
        with col2:
            st.write('')
            st.write('## Overview')
            st.write("Maize is a cereal crop that was first introduced to Kenya in the 16th century by Arab traders. Millions of Kenyans eat maize as part of their daily diet. The average Kenyan consumes 98kg of maize per year, and maize and maize products account for 28% of the country's income. This crop thrives in warm climates with high rainfall and loamy, well-drained soil.Throughout Kenya, maize growing is practiced in the Rift Valley, Central Kenya, and other locations.")

    # overview 2
    with overview2:
        col1,col2 = st.columns(2)
        with col1:
            st.write('## Maize Disease')
            st.write("The growth of the population has outpaced maize output. Drought, low soil fertility, pests, and diseases are all obstacles to maize production. Maize diseases diminish yields by up to 90% in maize-growing regions such as Kenya and other African countries. Maize is susceptible to a number of leaf diseases, including Maize Gray Leaf Spot, Maize Streak Virus, Common Rust, Head Smut, and Northern Blight. Both the quality and quantity of maize crops are affected by the diseases.")
        with col2:
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            maize2 = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.bVeDRo86SZKlTjIHV_x8ZQHaE8%26pid%3DApi&f=1'
            st.image(maize2,width=300)
    # predictor
    with predictor:
        st.write(' ')
        st.write('## Identify Disease')
        st.write(' ')
        uploaded_file = st.file_uploader("Upload your image")
    #view
    if uploaded_file is not None:
        with view:
            col1,col2 =st.columns(2)

            with col1:

                # Convert the file to an opencv image.
                file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
                opencv_image = cv2.imdecode(file_bytes, 1)

                # Now do something with the image! For example, let's display it:
                st.image(opencv_image, channels="BGR")
         # predictor
            with col2:
                st.write('##### Class')
                st.write('##### Confidence interval')

    # recommend
            with recommend:
                col1,col2 = st.columns(2)
                with col1:
                    st.write('#### Causes')
                with col2:
                    st.write('#### Management')
else:
    st.title('Models')