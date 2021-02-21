#  The Parking Lot Project 

In this Parking Lot Project you will get an automated ticketing system that allows customers to use the parking lot without **human intervention**.

## Brief Explanation of Project

When a car enters in parking lot, the ticket issued to the driver automatically. The
ticket issuing process includes us documenting the registration number (number
plate) and the colour of the car and allocating an available parking slot to the car
before actually handing over a ticket to the driver (we assume that our customers are
nice enough to always park in the slots allocated to them). The customer should be
allocated a parking slot which is nearest to the entry. At the exit the customer returns
the ticket which then marks the slot they were using as being available.
Due to government regulation, the system should provide me with the ability to find out:

* Registration numbers of all cars of a particular colour.
* Slot number in which a car with a given registration number is parked.
* Slot numbers of all slots where a car of a particular colour is parked.

We interact with the system via a simple set of commands which produce a specific
output. The system allow input in two ways. Just to clarify, the same  codebase should
 support both modes of input - we two distinct submissions.

1. It will provide you with an interactive command prompt based shell where
commands can be typed in.

1. It will accept a filename as a parameter at the command prompt and read the
commands from that file.

## Files and Folders

This project is covered in five files. In which four files are python files and one is text file.
In those files there is one main file and  two class files and one process file and lastly one command file.
The names of files are -

1. main.py
2. car.py
3. parking_details.py
4. process_input.py
5. commands.txt

## Reqirements

1. Python installation
2. Any IDE (Pycharm, Visual Studio Code etc.)

## How to Run

For using  Python build Parking Lot System, you just have to run the main.py file in terminal or IDE for manual Output. And if you want to use Command Line Method for running the project you will have to use ""python process_input.py commands.txt "" in the Terminal. It will run the two file together(the process_input.py file and commands.txt file). 
And yes if you want to use your commands to use this Parking Lot System, you have to just change the commands written in commands.txt file.