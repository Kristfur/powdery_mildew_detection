import streamlit as st
import matplotlib.pyplot as plt


def page_hypothesis_body():
    st.write(
        f"1. The leaves infected with powdery mildew have patches of white "
        f"discoloration on the leaf. \n"
        f"* An average image study will be useful to investigate this. We are "
        f"expecting the average powdery mildew image to show white patches "
        f"where the powdery mildew is present. We will compare the healthy "
        f"to the powdery mildew average image and we expect to not see white "
        f"patches on the average healthy image. \n \n"
        f"Result: As expected. The powdery mildew appears as white "
        f"powdery patched on an infected leaf.")

    st.write(
        f"2. Healthy leaves have a more uniform, greener color. \n"
        f"* An average variability image study will be useful to investigate "
        f"this. We expect to see a dark area on the healthy variability "
        f"image, meaning that the leaves have a more consistant color. And "
        f"for the powdery mildew, we expect to see more lighter areas all "
        f"over the leaf in the variavility image indicating that the powdery "
        f"mildew leaves are not a consistant green color. \n \n"
        f"Result: As expected, but the discolouration could also be caused by "
        f"the white powdery mildew patches, instead of just the pigment of "
        f"the leaf. The powdery mildew seems to cause the leaf to loose some "
        f"of it's vibrant green pigment.\n")

    st.write(
        f"3. Infected leaves have overall smoother edges, and a less "
        f"defined 'leaf' shape. \n"
        f"An average image study will be useful to investigate this. We will "
        f"use the difference of average healthy and average powdery mildew "
        f"images. We expect to see a lighter area around the outline of the "
        f"leaves, which indicate that the edges of the leaves are different "
        f"when it is healthy to when it has powdery mildew. \n \n"
        f"Result: As expected. The powdery mildew causes the leaves' edges to "
        f"become less defined and smoother.")
