import streamlit as st    #library to create web app
import tensorflow as tf   #to load our model and getting the prediction
from PIL import Image    #to process the image
import numpy as np
import os

st.markdown("""
    <style>
        .stApp {
            background-color: #FFFDF7;
        }
    </style>
""", unsafe_allow_html=True)




# --- Set the title ---
st.title("Image Classification with Keras Model")
st.write("Upload an image, and I will predict the class using a trained model.")



model_path = os.path.join(os.getcwd(), "trained_fashion_mnist_model.keras")

#load the pretrained model
model = tf.keras.models.load_model(model_path)

#define class labels for Fashion MNIST dataset
class_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']


#function to preprocess the uploaded image
def preprocess_image(image):
    img = Image.open(image)
    img = img.resize((28,28))
    img = img.convert('L')      #convert to grayscale
    img_array = np.array(img)/255.0
    img_array = img_array.reshape((1,28,28,1))
    return img_array

#Streamlit App
uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])




if uploaded_image is not None:
    image = Image.open(uploaded_image)
    col1, col2 = st.columns(2)

    with col1:
        resized_img = image.resize((100,100))
        st.image(resized_img)

    with col2:
        if st.button('Classify'):
            #preprocess the uploaded image
            img_array = preprocess_image(uploaded_image)

        #make a prediction using pre-trained model
            result = model.predict(img_array)

        #st.write(str(result))
            predicted_class = np.argmax(result)
            prediction = class_names[predicted_class]

            st.success(f"prediction: {prediction}")

    
