# Prog-Scrip-Problems
# Weekly Problems for Programming and Scripting
This repository is the overarching file that is made up of the weekly problems
set for the Programming and scripting module

## Table of Contents
* [1. Topic 2 BMI Calculation](#1-topic-2-bmi-calculation)
** [1.1 General Info](#11-general-info)
** [1.2 Technology / Running code](#12-technology--running-code)
** [1.3 Sources](#13-sources)
** [1.4 License](#14-license)
* [2. Topic 3 Variables](#2-topic-3-variables)
** [2.1 General Info](#21-general-info)
** [2.2 Technology / Running code](#22-technology--running-code)
** [2.3 Sources](#23-sources)
** [2.4 License](#24-license)
* [3. Topic 4 Control the flow](#3-topic-4-control-the-flow)
** [3.1 General Info](#31-general-info)
** [3.2 Technology / Running code](#32-technology--running-code)
** [3.3 Sources](#33-sources)
** [3.4 License](#34-license)
* [4. Topic 5 Data Structures](#4-topic-5-data-structures)
** [4.1 General Info](#41-general-info)
** [4.2 Technology / Running code](#42-technology--running-code)
** [4.3 Sources](#43-sources)
** [4.4 License](#44-license)
* [5. Topic 6 Newton Raphson Sqrt method](#5-topic-6-newton-raphson-sqrt-method)
** [5.1 General Info](#51-general-info)
** [5.2 Technology / Running code](#52-technology--running-code)
** [5.3 Sources](#53-sources)
** [5.4 License](#54-license)
* [6. Topic 7 Reading & Writing Files](#6-topic-7-reading--writing-files)
** [6.1 General Info](#61-general-info)
** [6.2 Technology / Running code](#62-technology--running-code)
** [6.3 Sources](#63-sources)
** [6.4 License](#64-license)
* [7. Topic 8 Plotting](#7-topic-8-plotting)
** [7.1 General Info](#71-general-info)
** [7.2 Technology / Running code](#72-technology--running-code)
** [7.3 Sources](#73-sources)
** [7.4 License](#74-license)

## 1. Topic 2 BMI Calculation
### 1.1 General Info
This program calculates the BMI of the user using the formula "BMI = Weight (Kg) ÷ Height (Metres²)".
The user inputs Weight in (Kg) and Height in (cm)
### 1.2 Technology / Running code
This program was written in Python 3.7.4
The inputs are taken in as floats to allow a decimal precision in calculation of BMI.
BMI is calculated using the formula and the print function outputs the aamswer.
Additional formatting was added in to ensure precision was to two decimal places.
### 1.3 Sources
The main sources used in completion of this task were:
A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly). Copyright 2016 O’Reilly Media, Inc
https://stackoverflow.com/questions/2075128/python-print-all-floats-to-2-decimal-places-in-output

### 1.4 License
This project is licensed under the MIT License

## 2. Topic 3 Variables
### 2.1 General Info
This program is designed to take a sentence (otherwise known as a string) inputted by the user and output 
the same sentence in reverse order while removing every second character.
### 2.2 Technology / Running code
This program was written in Python 3.7.4
This code is relatively simple. The input function takes whatever string the user types.
The print function displays the string. The [::-2] takes all of the characters from start
to finish, the "2" displays every second character and the "-" reverses the order of the 
characters.
### 2.3 Sources
The main sources used in completion of this task were:
A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly). Copyright 2016 O’Reilly Media, Inc
https://stackoverflow.com/questions/3940128/how-can-i-reverse-a-list-in-python
https://docs.python.org/3/library/string.html#index-2
### 2.4 License
This project is licensed under the MIT License

## 3. Topic 4 Control the flow
### 3.1 General Info
This program takes a positive integer as an input from the user and performs calculations on 
the integer depending on whether it is even or odd. It takes the output of the calculation as the next input.
It then runs in a loop until the final value for "b" is 1.
### 3.2 Technology / Running code
This program was written in Python 3.7.4
Input function takes in an integer. Varialbles are assigned for calculations. The while loop sets the conditions for the loop to run. In this case the while loop will run while b > 1. The if statement runs the calculation if the remainder of dividing the input by 2 gives an output of 0. (This means the integer would be even) The elif statement will run if the conditions for the if statement are not met (if the remainder of dividing the input by 2 is not equal to 0, which makes it odd.)
The values for the calculations are then printed.
### 3.3 Sources
The main sources used in completion of this task were:
A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly). Copyright 2016 O’Reilly Media, Inc
https://docs.python.org/3/tutorial/controlflow.html?highlight=control 
### 3.4 License
This project is licensed under the MIT License

## 4. Topic 5 Data Structures
### 4.1 General Info
This program will output whether the day it is run on is a weekday or a weekend. Utilising the datetime module and using if statements.
### 4.2 Technology / Running code
This program was written in Python 3.7.4
The datetime module is imported into python. The weekday is then assigned to the variable "tday". Each day from Monday - Sunday in the week is assigned an integer from 0 - 6. The if statnent checks whether the current integer assigned to todays date is greater than or equal to 5. If it's true then the program will print "Thank God it's the Weekend". If the statement is false or the integer value is between 0-4, the program will print that it is a weekday. Extra formatting was added to underline "weekday"
### 4.3 Sources
The main sources used in completion of this task were:
A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly). Copyright 2016 O’Reilly Media, Inc
https://stackoverflow.com/questions/35401019/how-do-i-print-something-underlined-in-python
https://www.tutorialspoint.com/python3/python_tutorial.pdf
### 4.4 License
This project is licensed under the MIT License

## 5. Topic 6 Newton Raphson Sqrt method
### 5.1 General Info
This program approximates the squareroot of the value entered by the user using Newton Raphsons Method for approximation of squareroots (NR).
### 5.2 Technology / Running code
This program was written in Python 3.7.4
Firstly the function new_raph was defined. This will allow the calculations to be used in future pieces of code/programs by calling the function. The arguement "N" is added into the parenthesis after the function. When calling the function a value will be given to "N". "N" will be the value of the number that the user wants to get the squareroot of. "x0" will be the inital guess and "fxn" the function used in NR method. The "while" loop has the parameters that means it will run if "fxn" is greater than 0.1(If fxn goes below this the loop will be stopped, 0.1 was chosen as if "fxn" was equal to 0 this would be the exact squareroot of the input). NR method is calculated by using the intial guess to calculate a more accurate guess. The formula is the following: x1 = x0 - (fxn) / (fpxn) where:
x1 = The next approximated guess
x0 = The initial, last approximation
fxn = Function used in NR method
fpxn = The derivative of fxn
If the value of "fxn" for the calculated value of "x0" & "x1" is less than 0.1 then the approximation will be complete otherwise the value of "x1" will be assigned to "x0" and the calculations will be completed again until "fxn" is less than 0.1. These calculations are run when the function is called, in this instance the user is required to input any positive value with decimals allowed and the output will return the approximation to two decimal places.
### 5.3 Sources
The main sources used in completion of this task were:
A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly). Copyright 2016 O’Reilly Media, Inc
http://anh.cs.luc.edu/python/hands-on/3.1/Hands-onPythonTutorial.pdf
https://www.tutorialspoint.com/python3/python_tutorial.pdf
### 5.4 License
This project is licensed under the MIT License

## 6. Topic 7 Reading & Writing Files
### 6.1 General Info
This program reads in a text file from the user and counts the number of times a selected character is used in the text file. It then closes the text file when the output is displayed.
### 6.2 Technology / Running code
This program was written in Python 3.7.4
The function is defined the arguements added that need to be passed into the function. The file is opened, read and the number of times that the character is used is displayed as an output. Using "with open...as f" allows for less lines of code as the program will close the file automatically once the output is displayed. First input requires the user to enter the directory or file path of the text file that will be used. The user must then choose a character.
### 6.3 Sources
The main sources used in completion of this task were:
A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly). Copyright 2016 O’Reilly Media, Inc
https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
https://docs.python.org/3/tutorial/datastructures.html?highlight=count 
### 6.4 License
This project is licensed under the MIT License

## 7. Topic 8 Plotting
### 7.1 General Info
This program takes in three values for a = starting point of the range, b = finishing point of the range and c = the step size or increments the user wants to increase in. Eg. (0:15:1). By using the arange function values are returned evenly spaced in an array with step size taken into account.
### 7.2 Technology / Running code
This program was written in Python 3.7.4
Numpy and matplotlib.pyplot are imported to allow the arange function and plotting functions of python to be utilised. The function is created and the variables Fp, Ep & Incr are set as the arguements. The values used in the arange function are specified by the user as floats. np.arange returns the values in an evenly spaced array depending on the inputs. The functions for f(x), g(x), h(x) are calculated and values assigned. These functions are plotted to the same graph with formatting to allow distinction. Labels, legend and the title are also included in the code to make graph more presentable. plt.show() prints the graph to the screen.
### 7.3 Sources
The main sources used in completion of this task were:
A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly). Copyright 2016 O’Reilly Media, Inc
https://www.python-course.eu/matplotlib_subplots.php
https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
### 7.4 License
This project is licensed under the MIT License