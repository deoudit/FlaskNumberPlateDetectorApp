# FlaskNumberPlateDetectorApp
This App Detects returns the Number of Automobile which is given as Image to it


Modules used :
1. Numpy : NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays
and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. Used here
for : Converting image to matrix.
2. OpenCV : OpenCV stands for Open Source Computer Vision. It is an open source computer vision and machine learning
software library. The library has more than 2500 optimized algorithms, which includes a comprehensive set of both
classic and state-of-the-art computer vision and machine learning algorithms. These algorithms can be used to detect
and recognize faces, identify objects, classify human actions in videos, track camera movements, track moving
objects, extract 3D models of objects, produce 3D point clouds from stereo cameras, stitch images together to produce
a high resolution image of an entire scene, find similar images from an image database, remove red eyes from images
taken using flash, follow eye movements, recognize scenery and establish markers to overlay it with augmented reality,
etc. Used here for : Identifying and extracting objects.
3. Imutils : Imutils include a series of convenience functions to make basic image processing functions such as translation,
rotation, resizing, skeletonization, and displaying Matplotlib images easier with OpenCV and both Python 2.7 and
Python 3. Used here for : Resizing the image.
4. Pytesseract : Library to use the Tesseract-OCR. Tesseract is an optical character recognition engine for various
operating systems. Tesseract is considered to be one of the most accurate open-source OCR engines available. What is
OCR ? Optical character recognition or optical character reader is the electronic or mechanical conversion of images of
typed, handwritten or printed text into machine-encoded text, whether from a scanned document, a photo of a
document, a scene-photo or from subtitle text superimposed on an image. Used here for : Converting cropped number
plate image obtained into text.
5. Pandas : In computer programming, pandas is a software library written for the Python programming language for data
manipulation and analysis. Used here for : Converting data extracted to a DataFrame.
6. Time : The time() function returns the number of seconds passed since epoch.
7. Flask: It is Web-Developement Framework of Python.
8. Heroku: It is used for deploying the Application so that it can be accessed in just a click through link from anywhere.

# FlowChart of the Procedure followed
1. Read the original image
2. Resize the image
3. Convert it to grayscale.
4. Apply Bilateral Filter. What is bilateral filter ? A bilateral filter is a non-linear, edge-preserving, and noise-reducing
smoothing filter for images. It replaces the intensity of each pixel with a weighted average of intensity values from nearby
pixels.
5. Identify and store the Canny edges. What are Canny edges ? The Canny edge detector is an edge detection operator that
uses a multi-stage algorithm to detect a wide range of edges in images.
6. Find the contours in from the edges detected and sort the top 30 contours.
7. Get the perimeter of each contour and select those with 4 corners.
8. Mask all other parts of the image and show the final image.
9. Read the text using Tesseract OCR.
10. Append to csv file (if needed)
11. Create a Web Application using Flask.
12. Deploy it using Heroku.


# The Code is displayed in the Files section.
