import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file


def resize_input_image(img, version):
    """
    Reshape image to average image size
    """
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]))
    my_image = np.expand_dims(img_resized, axis=0)/255

    return my_image


def load_model_and_predict(my_image, version):
    """
    Load and perform ML prediction over live images
    """

    model = load_model(f"outputs/{version}/powdery_mildew_detector_model.h5")

    pred = model.predict(my_image)[0, 0]

    target_map = {v: k for k, v in {'Healthy': 1, 'Infected with Powdery Mildew': 0}.items()}
    pred_class = target_map[pred > 0.5]

    st.write(
        f"The predictive analysis indicates the sample leaf is "
        f"**{pred_class.lower()}**!")

    return pred_class
