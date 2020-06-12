# Animal Classification
## About the Dataset
DATASET: https://docs.google.com/forms/d/e/1FAIpQLSeerwGmVkxbZsI0jxGLWfND8nmRCDDSoW1OAVpa8ZzCCR2e-A/viewform

1. Meta information
    - 50,000 Images
    - resolution: 64x64 (RGB)

2. Noise Rate
    - The noise rate was estimated at 8%.
 
3. File name & Label Information
    - file name is "label" + _ + "indexed name"
    - label mappings
      - 0: cat
      - 1: lynx
      - 2: wolf
      - 3: coyote
      - 4: cheetah
      - 5: jaguar
      - 6: chimpanzee
      - 7: orangutan
      - 8: hamster
      - 9: guinea pig
# About the Model

  -  A VGG19 Computer-vision model that can classify images of animals into the 10 categories mentioned above

Uses a large size dataset of  50,000 images with around 5000 images of each class to train the model. The images were then split into training and validation data: 80% of the data was used for training and the remaining 20% was used for testing.



### Data Modeling

My input data consisted of 40000 RGB 64x64 images. Given a directory containing all the images, I utilize Keras' 'ImageDataGenerator' to create a training The list containing data variables is then normalized and both label and data lists are re-assigned as numpy arrays. After the data is split up by category and divided into training and testing, I used Keras' ImageDataGenerator to create a testing and training, and used to perform some transformations on the data, such as zooming or rotating the image, to make it more impactful when training.


### Architecture:



### Limitations



### Possible Improvements

 -  Another CNN for Facial recognition or an extremely effective algorithm for preprocessing the data and forming a 'region of interest' around a person's face(perhaps a modified Haar Cascade Classifier). This would work well with the LeNet, which resizes the image to a measly 28 by 28.
 
 -  Add another neutral net to create a region of interest around the target in the image




 
