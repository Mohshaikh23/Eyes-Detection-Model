# Eyes-Detection-Model
Eye Detection using Haar Cascades

This code performs eye detection in an image using a Haar cascade classifier. It detects the presence and location of eyes in a given image and draws rectangles around them.

The main steps of the code include:
1. Loading a pre-trained Haar cascade classifier specifically trained for eye detection.
2. Providing the path to the image file to be processed.
3. Reading the color image and converting it to grayscale.
4. Applying the cascade classifier to detect eyes in the grayscale image.
5. Drawing rectangles around the detected eye regions on the color image.
6. Displaying the image with the detected eyes.

This eye detection code can be used as a part of computer vision applications or as a starting point for more advanced projects involving face recognition, gaze tracking, or driver drowsiness detection.

Please make sure to have the Haar cascade XML file for eye detection (e.g., haarcascade_eye.xml) in the same directory as the code.

Feel free to modify and adapt the code according to your specific requirements.

Dependencies:
- Python 3.x
- OpenCV (cv2)

Usage:
1. Ensure that Python and OpenCV are installed on your system.
2. Provide the path to the image file you want to process.
3. Run the script and observe the output with detected eyes.

Enjoy experimenting with eye detection in your projects!

