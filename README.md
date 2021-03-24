# Facial recognition door access control

### In this pandemic touching things is becoming dangerous, one doesn’t know where the virus is present. It can on anything plastic bags, furniture, railings, door handles, and many more uncountable things. We can’t solve this problem totally but we can to some extent and touching door handles is a problem we are going to solve here. Door handles are a small thing if we look at it but they can work as a medium to transfer the virus from one person to another. Currently, sanitizing the handles is a way to go but it is not 100% efficient, we need a way where we don’t even have to touch them, and with the existence of technology, it can be done. Further, door handlers are generally made of metals and the tendency for the virus to stay on the metal surfaces is longer over other materials.

### Applications of facial recognition are increasing day by day as it is secure and convenient. We are using our faces to unlock our phone devices from quite a time. Now, it’s a time to incorporate this technology to other aspects of our life. Facial recognition door access control is a big leap towards the autonomous and health conscious society

## Analysis of face recognition algorithm for door access control:
### •	Encode a picture using the Histogram of oriented gradients (HOG) algorithm . 
### •	Mark the main landmarks of the face.
### •	Pass the image through a neural network to measure features of the face. Save those 128 measurements.
### •	Compare the 128 saved measurements of the recently collected face to all images that have measured and stored in the database. See, which person has the closest measurements to our face’s measurements.
### •	If the measurements are less than 0.5 then pass the data collected, to the serial monitor on which Arduino is connected.
### •	If Arduino’s serial monitor will get some input it will open a door for the amount of time required for a person to pass through the door and then will lock it back again. 

## FLOW CHART

![image](https://user-images.githubusercontent.com/70061105/112324708-11d69700-8cd9-11eb-839c-9e2ac6c0da9e.png)

## HARDWARE

![WhatsApp Image 2021-02-05 at 11 54 18 PM](https://user-images.githubusercontent.com/70061105/107073692-ad857400-680d-11eb-9fa7-89363cfe82f9.jpeg)
