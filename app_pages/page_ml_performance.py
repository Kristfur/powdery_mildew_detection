import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics():

    if st.checkbox("Version 1"):
        version = 'v1'

        st.write("### Train, Validation and Test Set: Labels Frequencies")

        labels_distribution = plt.imread(
            f"outputs/{version}/label_distribution.png")
        st.image(labels_distribution,
                 caption="Labels Distribution on Train, Validation and Test Sets")
        st.write("---")

        st.write("### Model History")
        col1, col2 = st.beta_columns(2)
        with col1:
            model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
            st.image(model_acc, caption='Model Training Accuracy')
        with col2:
            model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
            st.image(model_loss, caption='Model Training Losses')
        st.write("---")

    if st.checkbox("Version 2"):
        version = 'v2'

        st.write("### Train, Validation and Test Set: Labels Frequencies")

        labels_distribution = plt.imread(
            f"outputs/{version}/label_distribution.png")
        st.image(labels_distribution,
                 caption="Labels Distribution on Train, Validation and Test Sets")
        st.write("---")

        st.write("### Model History")
        col1, col2 = st.beta_columns(2)
        with col1:
            model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
            st.image(model_acc, caption='Model Training Accuracy')
        with col2:
            model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
            st.image(model_loss, caption='Model Training Losses')
        st.write("---")

        st.write("### Generalised Performance on Test Set")
        st.dataframe(pd.DataFrame(load_test_evaluation(
            version), index=['Loss', 'Accuracy']))

    if st.checkbox("Version 3"):
        version = 'v3'

        st.write("### Train, Validation and Test Set: Labels Frequencies")

        labels_distribution = plt.imread(
            f"outputs/{version}/label_distribution.png")
        st.image(labels_distribution,
                 caption="Labels Distribution on Train, Validation and Test Sets")
        st.write("---")

        st.write("### Model History")
        col1, col2 = st.beta_columns(2)
        with col1:
            model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
            st.image(model_acc, caption='Model Training Accuracy')
        with col2:
            model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
            st.image(model_loss, caption='Model Training Losses')
        st.write("---")

        st.write("### Generalised Performance on Test Set")
        st.dataframe(pd.DataFrame(load_test_evaluation(
            version), index=['Loss', 'Accuracy']))
