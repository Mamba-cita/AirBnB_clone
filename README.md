AIRBNB PROJECT - THE CONSOLE
INTRODUCTION
The project aims to replicate the functionality of airbnb.com through a fully working website. The Console serves as a command interpreter for data manipulation without a visual interface,facilitating development and debugging. Its functionalities include creating the data model, managing objects (creation, updating, deletion, etc.), and persisting objects to a JSON file.

The first component focuses on developing a robust storage system, which abstracts the storage and persistence of objects from the console code and the frontend and RestAPI to be developed later. This abstraction allows for easy swapping of storage types without extensive code updates.



# Overview

Welcome to the Airbnb Console Project! Our mission is to bring the power and convenience of Airbnb management right to your fingertips. This cutting-edge command-line interface (CLI) application empowers users with seamless control over property listings, reservations, and other essential tasks. Whether you're a property owner, manager, or simply an Airbnb enthusiast, our console project provides a sophisticated yet user-friendly interface to effortlessly interact with Airbnb data.

# step 1: 
# To get started
 Simply clone our repository using the following command:

   ```
git clone https://github.com/Mamba-cita/AirBnB_clone.git
   ```


# Step 2: 
# Install Dependencies

Navigate to the project directory and install the necessary dependencies:

cd Airbnb_clone
yarn install

# Step 3: 

# Run the Command

 Launch the Airbnb Console by running the following command:
   ```
   ./console.py
   ```

# Step 4:
Get more commands from the help

   ```
   ./console.py
   (hbnb) help
   ```
Expected output

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update


# To retrieve more all modals data 

(hbnb) User.all()
(hbnb) Place.all()
(hbnb) City.all()
(hbnb) Amenity.all()
(hbnb) Review.all()
(hbnb) State.all()

# Count instances

(hbnb) User.count()
(hbnb) Place.count()
(hbnb) City.count()
(hbnb) Amenity.count()
(hbnb) Review.count()
(hbnb) State.count()

# Show instances

(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) Place.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) City.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) Amenity.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) Review.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) State.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")

# Destroy the instance
(hbnb) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) Place.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) City.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) Amenity.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) Review.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) State.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
