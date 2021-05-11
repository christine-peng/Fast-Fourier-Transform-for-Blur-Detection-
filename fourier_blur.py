# implement Fast Fourier Transform blur detector with OpenCV 
# import the necessary packages
import matplotlib.pyplot as plt
import numpy as np

def detect_blur_fft(image, size=60, thresh=10, vis=False):
    # define the detect_blur_fft function with four parameters
        # image = input image 
        # size = size of radius around centerpoint of image, where 
        # Fast Fourier Transform(FFT) shift will be zeroed out 
        # thresh = a value which the mean value of the magnitudes 
        # will be compared to for determining whether an image is blurry 
        # vis = boolean indicating whether to visualize/ plot original 
        # input image and magnitude image using matplotlib 
	(h, w) = image.shape
	(cX, cY) = (int(w / 2.0), int(h / 2.0))
    # grab the dimensions of input image and use the dimensions to
	# compute the center (x, y)-coordinates

	# compute the FFT to find the frequency transform 
	fft = np.fft.fft2(image)
	# shift the zero frequency component to the center where it will be more
	# easy to analyze
	fftShift = np.fft.fftshift(fft)

	# check to see if we are visualizing our output
	if vis:
		# compute the magnitude spectrum of the transform
		magnitude = 20 * np.log(np.abs(fftShift))

		# display the original input image
		(fig, ax) = plt.subplots(1, 2, )
		ax[0].imshow(image, cmap="gray")
		ax[0].set_title("Input")
		ax[0].set_xticks([])
		ax[0].set_yticks([])

		# plot original input image next to magnitude 
        # spectrum image 
		ax[1].imshow(magnitude, cmap="gray")
		ax[1].set_title("Magnitude Spectrum")
		ax[1].set_xticks([])
		ax[1].set_yticks([])

		# display the result 
		plt.show()

	# zero-out the center of the FFT shift (i.e., remove low
	# frequencies)
	fftShift[cY - size:cY + size, cX - size:cX + size] = 0
    # apply the inverse shift to put the zero frequency component 
    # back in the top-left
	fftShift = np.fft.ifftshift(fftShift)
    # apply the inverse FFT
	recon = np.fft.ifft2(fftShift)

	# compute the magnitude spectrum of the reconstructed image
	magnitude = 20 * np.log(np.abs(recon))
    # calculate the mean of the magnitude values
	mean = np.mean(magnitude)

    # the image will be considered "blurry" if the mean value of the
	# magnitudes is less than the threshold value
	return (mean, mean <= thresh)