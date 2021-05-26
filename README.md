# Cloak of Invisibility
A simple python script to experience the invisible cloak from the famous series of Harry Potter!

## How to use?

- Clone the repo and install the dependencies by using this command in the terminal: 

      pip install -r requirments.txt


- Just run the [Invisible_Cloak.py](./Invisible_Cloak.py) file to run the program

## Instructions to run the program:

- Just get a blue cloak(or towel) in a bright environment.
- If you do not have a blue one, take whatever color you have and follow the instructions to set the program for your own custom color of cloak and then continue for further instructions.
- Run the [Invisible_Cloak.py](./Invisible_Cloak.py) file while staying out of the camera view, so that a picture of background is saved properly.
- Once the window displaying camera video appears, you are good to go!
- Enjoy the Invisible Cloak you wished you had since your childhood!

## Set Program for your custom Cloak color:

- Run the [find_hsv.py](./find_hsv.py) file and make sure your cloak is visible for the camera.
- Two window will appear, one with the live video and another with the sliders with a blank space below them. We will use the one with the sliders.
- Move the sliders such that only you cloak is displayed completely white in the image below the sliders and rest everything around it is blacked out.
- Mark those values from the sliders and update them in the [Invisible_Cloak.py](./Invisible_Cloak.py) file where those values are stored in variables where "hsv ranges for cloak color" is commented.
- Thats it! Now, follow the further instructions and enjoy the program!
