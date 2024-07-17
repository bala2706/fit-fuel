###Fit Fuel Health Management APP

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import io

genai.configure(api_key="API-KEY-HERE")

## Function to load Google Gemini Pro Vision API And get response

def get_gemini_repsonse(input,image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##initialize our streamlit app

st.set_page_config(page_title="Fit Fuel App")


st.header("**Fit-Fuel App**")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #add8e6;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

input=st.text_input("Input Prompt: ",key="input")
def input_image_setup(uploaded_files):
    image_data = []
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        image_data.append(image)  # Assuming you process the image and append the result
    return image_data

uploaded_file0 = st.file_uploader("Choose an image for **Breakfast...**", type=["jpg", "jpeg", "png"])
image=""   
uploaded_file1 = st.file_uploader("Choose an image for **Lunch...**", type=["jpg", "jpeg", "png"])
image=""  
uploaded_file2 = st.file_uploader("Choose an image for **Dinner...**", type=["jpg", "jpeg", "png"])
image=""  
if uploaded_file0 is not None:
    image1 = Image.open(uploaded_file0)
    st.image(image1, use_column_width=True)
    st.markdown("<p style='text-align: center;'><strong>Breakfast.</strong></p>", unsafe_allow_html=True)

if uploaded_file1 is not None:
    image2 = Image.open(uploaded_file1)
    st.image(image2, use_column_width=True)
    st.markdown("<p style='text-align: center;'><strong>Lunch.</strong></p>", unsafe_allow_html=True)

if uploaded_file2 is not None:
    image3 = Image.open(uploaded_file2)
    st.image(image3, use_column_width=True)
    st.markdown("<p style='text-align: center;'><strong>Dinner.</strong></p>", unsafe_allow_html=True)
    
    



input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----
               ADD ALL THE 3 IMAGES GIVE SEPERATE KCAL FOR BREAKFAST , LUNCH, DINNER
               give me seperate like for breakfast,lunch,dinner is the required kcal give that in bold and sum up total
               there is  images first one for breakfast second one is for lunch and last is for dinner analyse that and add the kcal together
               give the total kcal in taken in bold .calculate  the total kcal and minus it with how much kacl should be taken to be healthy.
               give the total calories and minus with 1600 .then produce for burning the excess calories.
               average person to reduce weight is to intake 1600 kacl. to gain weight he should take more than 1800 calories
               to the remaining kacl give the solution to burn it. 
            And even add them how to reduce the amount of kcal intaken. how much workout to be done. if walking how much minutes and if in gym how much minutes workout. give in point wise...


"""

## If submit button is clicked

if st.button('Submit'):
    # Ensure all files are uploaded
    if uploaded_file0 and uploaded_file1 and uploaded_file2:
        # Process each file individually
        image_data0 = input_image_setup([uploaded_file0])[0]
        image_data1 = input_image_setup([uploaded_file1])[0]
        image_data2 = input_image_setup([uploaded_file2])[0]

        # Combine all processed image data
        image_data = [image_data0, image_data1, image_data2]

        # Your function to get a response from Gemini
        response = get_gemini_repsonse(input_prompt, image_data, input)
        
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please upload all three images.")

