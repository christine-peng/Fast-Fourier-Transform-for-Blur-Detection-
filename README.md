# Fast-Fourier-Transform-for-Blur-Detection-

### Introduction 
The Fourier Transform is an image processing tool which is used to decompose an image into its sine and cosine components. The output of the transformation convert an incoming signal from time domain to a Fourier, or frequency domain. In the simplest terms, a fourier transform breaks down an incoming signal into its building blocks. It is useful in a wide range of applications, such as image analysis, image filtering, image reconstruction and image compression. For digital images, the 2D Discrete Fourier Transform (DTF) is used to find the frequency domain. A fast algorithm called Fast Fourier Transform (FFT) is used for the calculation of DTF. 

In terms of computer vision, FFT is an image processing tool that represents an image in two domains: 
1.	Fourier (frequency) domain 
2.	Spatial domain 

Therefore, the FFT represents the image in both real and imaginary components. When a FFT is applied to an image, it converts an input image from a spatial domain to frequency domain, which separates an image’s high and low frequencies. 
![image](https://user-images.githubusercontent.com/83466109/118300661-0ca2f680-b497-11eb-8c73-4c5d49a6ee02.png)
In the FFT transform of an image, low frequencies are situated towards the center of the image and high frequencies are scattered around, as shown above. A Boolean mask can then be created to represent the center as zeros and the rest of the area as ones. When the mask is applied to the original image, the resultant image would only have high frequencies. Low frequencies correspond to edges in a spatial domain. Essentially, an image is a considered a signal sampled in two directions, so taking the Fourier transform in both X and Y directions results in the frequency representation of the image. 

Once the FFT is visualized, an FFT shift can be made to remove low frequencies. This can be done by applying the inverse shift to put the zero frequency component in the top-left of the image, and apply the inverse FFT to enable edge detection functionality.  

In order to determine if an image is blurry, the magnitude spectrum of an image is derived again from the reconstructed image after the zero frequency component have been zeroed out. The mean of the magnitude representation is then calcualated, returning a boolean indicating whether the input image is blurry or not. 

### How to use
There are two Python files: 
fourier_blur.py
  Implements fast fourier transform (FFT) blur detector algorithm  
blur_detector_image.py: 
  Python driver script that loads an input image from disk and then applies FFT blur detection to it. 
  
  Place images in one project folder, and run command prompt to access project folder:  
   
	imagepath python blur_detector_image.py --i images  
 
 To change threshold of image output: 
 
  ```imagepath python blur_detector_image.py --i images --thresh 15```
  
### Results Analysis 
Screenshot of images used (left) and blur results (right). 
![image](https://user-images.githubusercontent.com/83466109/118338178-4c370600-b4ca-11eb-9a46-ba5a86aa2d65.png)
Similar to the Laplacian method, blur detection using the Fast Fourier Transform is dependant on the pre-defined threshold, which will range depending on type of images taken. For example, the image below is has a threshold of "30.2", which is too blurry for analysis, so a threshold of "32" was set to manually set it to blurry. 
![image](https://user-images.githubusercontent.com/83466109/118324378-d1182480-b4b6-11eb-8774-2d52aaaa76ae.png)
A threshold of "32" accurately represents blur in the photo above, yet the same blur threshold doesn't work for all the images, as demonstrated in the four pictures below. 
![image](https://user-images.githubusercontent.com/83466109/118325078-c6aa5a80-b4b7-11eb-8b32-75d38a421a54.png)
![image](https://user-images.githubusercontent.com/83466109/118312007-8f32b280-b4a5-11eb-9cb9-73dc492464fb.png)
![image](https://user-images.githubusercontent.com/83466109/118325846-ec842f00-b4b8-11eb-8b36-d0f42d2e221f.png)
![image](https://user-images.githubusercontent.com/83466109/118313012-15032d80-b4a7-11eb-8188-b1c43b145e44.png)

### Limitations 
Similar to the Laplacian method, the FFT also requires manual tuning to define the blur threshold. The advantage of a pre-defined threshold is that this method can be custom tailored to different types of images, but it's disadvantage lays in the fact that each set of images must be of similar location, and with similar attributes. Variations in characteristics of images, such as snow (as shown below), is mistaken as blurry due to low levels of edge variation, would not work with the FFT method unless they were isolated from other images, with a new threshold manually set.
![image](https://user-images.githubusercontent.com/83466109/118326829-5c46e980-b4ba-11eb-9528-17c6eb9292a7.png)
 Results also seemed inconsistent for images with a clear object of interest and blurred background, as shown in examples below. 
![image](https://user-images.githubusercontent.com/83466109/118312007-8f32b280-b4a5-11eb-9cb9-73dc492464fb.png)
 Results were also inconsistent for images with reflections, as shown in examples below. 
 ![image](https://user-images.githubusercontent.com/83466109/118329243-95cc2480-b4bb-11eb-9cc6-9f17997aa7b3.png)
![image](https://user-images.githubusercontent.com/83466109/118329391-cd3ad100-b4bb-11eb-903e-c7151031ead5.png)

### Conclusion 
While the Fast Fourier Transform method can be potentially used to detect blur in UAV images, it would have to be manually tuned to a threshold appropriate for each set of images. Environmental factors such as snow and rain may likely result in mixed results. Reflections and background blur may also result in mixed results. The FFT method is best used for images taken within a similar setting, set in a controlled environment. Large variations in imagery changes will likely produce mixed results.  
