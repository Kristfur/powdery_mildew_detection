import streamlit as st
import os
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random


def page_leaf_visualizer_body():
    st.write("### Leaf Visualizer")
    st.info(
        f"* The client is interested in conducting a study to visually "
        f"differentiate a cherry leaf that is healthy from one "
        f"that contains powdery mildew. \n")

    version = 'v1'
    if st.checkbox("Difference between average and variability image"):
        st.info(
            f"As we can see, the average healthy leaf image has an distinct, "
            f"uniform green colour in the centre where all the "
            f"leaves overlap.\n"
            f"The average variability between the healthy leaf images "
            f"has a dark centre, indicating that the colour of the leaves "
            f"don't vary a lot.\n"
            )

        avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")

        st.info(
            f"Compared to the average healthy leaves, the average powdery "
            f"mildew leaves have a less green colour, and appears to "
            f"have white discolourations throughout the leaves. \n"
            f"The centre of the average variability image is "
            f"significantly lighter and noisier than the average "
            f"variability for the healthy leaves, indicating a substantial "
            f"difference between healthy and powdery mildew leaves.")
        avg_powdery_mildew = plt.imread(
            f"outputs/{version}/avg_var_powdery_mildew.png")

        st.image(avg_healthy, caption='Healthy Leaf - Average and Variability')
        st.image(avg_powdery_mildew,
                 caption='Powdery Mildew Leaf - Average and Variability')

        st.write("---")

    if st.checkbox("Differences between average powdery mildew and "
                   "average healthy leaves"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        st.info(
            f"The average image difference between healthy and powdery "
            f"mildew leaves does not show much helpful data. Although the "
            f"outline of the leaves in the image is lighter, indicating that "
            f"the average leaves have different edges depending  on wether "
            f"they are healthy or not.")

        st.image(diff_between_avgs,
                 caption='Difference between average images')

    if st.checkbox("Image Montage"): 
      st.write("* To refresh the montage, click on the 'Create Montage' button")
      my_data_dir = 'inputs/mildew_detection/cherry_leaves'
      labels = os.listdir(my_data_dir+ '/validation')
      label_to_display = st.selectbox(label="Select label", options=labels, index=0)
      if st.button("Create Montage"):      
        image_montage(dir_path= my_data_dir + '/validation',
                      label_to_display=label_to_display,
                      nrows=8, ncols=3, figsize=(10,25))
      st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
  sns.set_style("white")
  labels = os.listdir(dir_path)

  # subset the class you are interested to display
  if label_to_display in labels:

    # checks if your montage space is greater than subset size
    # how many images in that folder
    images_list = os.listdir(dir_path+'/'+ label_to_display)
    if nrows * ncols < len(images_list):
      img_idx = random.sample(images_list, nrows * ncols)
    else:
      print(
          f"Decrease nrows or ncols to create your montage. \n"
          f"There are {len(images_list)} in your subset. "
          f"You requested a montage with {nrows * ncols} spaces")
      return
    

    # create list of axes indices based on nrows and ncols
    list_rows= range(0,nrows)
    list_cols= range(0,ncols)
    plot_idx = list(itertools.product(list_rows,list_cols))


    # create a Figure and display images
    fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=figsize)
    for x in range(0,nrows*ncols):
      img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
      img_shape = img.shape
      axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
      axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
      axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
      axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
    plt.tight_layout()
    
    st.pyplot(fig=fig)

  else:
    print("The label you selected doesn't exist.")
    print(f"The existing options are: {labels}")