import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery Mildew is a fungal disease that affects a "
        f"wide range of plants.\n"
        f"* This disease can significantly reduce a plants yield. \n"
        f"* The symptoms of a plant infected with Powdery Mildew are powdery"
        f"white spots that appear on the leaves and stems of the plant."
        f"These spots grow larger and denser as the disease progresses. \n"
        f"* There are treatments for infected plants, "
        f"but it is time consuming to identify infected plants. \n"
        f"* A leaf is obtained from a suspected plant, and photographed."
        f"Visual criteria are used to detect if powdery mildew is present. \n \n"
        f"**Project Dataset**\n"
        f"* The given dataset contains over 4000 images in total, half of "
        f"whichare of single healthy leaves and the rest are of "
        f"single leaves infected with powdery mildew.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Kristfur"
        f"/powdery_mildew_detection/blob/main/README.md).")

    st.success(
        f"**Business Requirements**\n"
        f"* 1 - The client is interested in conducting a study to visually "
        f"differentiate a cherry leaf that is healthy from one "
        f"that contains powdery mildew. \n"
        f"* 2 - The client is interested in predicting if a cherry "
        f" leaf is healthy or contains powdery mildew."
    )
