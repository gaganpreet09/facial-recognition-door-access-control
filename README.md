# Facial recognition door access control

Analysis of face recognition algorithm for door access control:
•	Encode a picture using the Histogram of oriented gradients (HOG) algorithm . 
•	Mark the main landmarks of the face.
•	Pass the image through a neural network to measure features of the face. Save those 128 measurements.
•	Compare the 128 saved measurements of the recently collected face to all images that have measured and stored in the database. See, which person has the closest measurements to our face’s measurements.
•	If the measurements are less than 0.5 then pass the data collected, to the serial monitor on which Arduino is connected.
•	If Arduino’s serial monitor will get some input it will open a door for the amount of time required for a person to pass through the door and then will lock it back again. 

![image](https://user-images.githubusercontent.com/70061105/112324708-11d69700-8cd9-11eb-839c-9e2ac6c0da9e.png)

![WhatsApp Image 2021-02-05 at 11 54 18 PM](https://user-images.githubusercontent.com/70061105/107073692-ad857400-680d-11eb-9fa7-89363cfe82f9.jpeg)
