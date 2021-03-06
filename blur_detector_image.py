# Python driver script that loads an input image from disk and then 
# applies FFT blur detection to it.
# USAGE:
# python blur_detector_image.py --image images

# import the necessary packages
from fourier_blur import detect_blur_fft
import numpy as np
import argparse
import imutils
import cv2
import os

# construct the argument parser and parse four command line arguments 
    # --image: the path to the input image for blur detection
    # --thresh: the threshold for blur detector calculation 
    # --vis: flag indicating whether to visualize the input image 
    # and the magnitude spectrum image 
    # --test: test results by progressively blurring input image and 
    # conduct FFT-based blur detection on each image 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path input image used to detect blur")
ap.add_argument("-t", "--thresh", type=int, default=20,
	help="threshold for blur detector to fire")
ap.add_argument("-v", "--vis", type=int, default=-1,
	help="whether or not intermediary steps will bev visualized")
ap.add_argument("-d", "--test", type=int, default=-1,
	help="whether or not image should be progressively blurred")
args = vars(ap.parse_args())

# loop over images 
for imagePath in os.listdir(args["image"]):
    image = args["image"] + "\\" + imagePath
    print(image)
# load the input image from disk, resize it, and convert it to
# grayscale
    orig = cv2.imread(image)
    orig = imutils.resize(orig, width=500)
    gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)


    # apply blur detector using the FFT function 
    (mean, blurry) = detect_blur_fft(gray, size=60,
        thresh=args["thresh"], vis=args["vis"] > 0)

    # draw on the image, indicating whether or not it is blurry
    # add two more channels to single-channel gray image, storing 
    # the result in image 
    image = np.dstack([gray] * 3)
    color = (0, 0, 255) if blurry else (0, 255, 0)
    # set color as red(if blurry) and green(if not blurry)
    text = "Blurry ({:.4f})" if blurry else "Not Blurry ({:.4f})"
    # draw blurry text indication and mean value in top-left corner 
    # of image, print out same info in terminal 
    text = text.format(mean)
    cv2.putText(image, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
        color, 2)
    print("[INFO] {}".format(text))

    # show the output image
    # cv2.imshow("Output", image)
    # cv2.waitKey(0)

    # check to see if are going FFT blurriness detector is tested 
    # using various sizes of a Gaussian kernel
    if args["test"] > 0:
        # loop over various blur radii
        for radius in range(1, 30, 2):
            # clone the original grayscale image
            image = gray.copy()

            #check to see if the kernel radius is greater than zero
            if radius > 0:
                # blur the input image by the supplied radius using a
                # Gaussian kernel
                image = cv2.GaussianBlur(image, (radius, radius), 0)

                # apply our blur detector using the FFT
                (mean, blurry) = detect_blur_fft(image, size=60,
                    thresh=args["thresh"], vis=args["vis"] > 0)

                # draw on the image, indicating whether or not it is
                # blurry
                image = np.dstack([image] * 3)
                color = (0, 0, 255) if blurry else (0, 255, 0)
                text = "Blurry ({:.4f})" if blurry else "Not Blurry ({:.4f})"
                text = text.format(mean)
                cv2.putText(image, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, color, 2)
                print("[INFO] Kernel: {}, Result: {}".format(radius, text))

            # show the image
            cv2.imshow("Test Image", image)
            cv2.waitKey(0)
