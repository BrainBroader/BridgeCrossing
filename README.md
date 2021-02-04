# Bridge Crossing Problem
A solution to the Bridge Crossing problem using A* search algorithm.

**University:** Athens University of Economics and Business  
**Department:** Informatics  
**Subject:** Artificial Intelligence

**Team:** Lampros Lountzis (@lamproslntz), Andreas Gouletas (@BrainBroader)

## Table of Contents
* [Problem Description](#problem-description)
* [Dataset](#dataset)
* [Execution Instructions](#execution-instructions)

### Problem Description 
In this problem a family needs to cross a river using a bridge that connects the two banks. The bridge can withstand a maximum of two people at a time. 
Also, the family has one lamp which must be used by one of the people who cross the river every time. Each member of the family needs a different time to cross
the river. This time is fixed (in any direction) for each member of the family. When two members of the family cross the river together, 
the time of crossing is of the slowest. The time it takes each family member to cross the river is known beforehand. 

Your program should find the optimal solution, that is in what order (and in what pairs or individually at each crossing) the family members should pass across, 
so that the whole family spends the minimum time crossing the river. 

The number of family members, let N, the time (eg minutes) each family member needs to cross the river and a limit for the maximum time given to the family 
to cross the river are given as inputs to your program.

### Dataset 
To represent the data, the **CSV (Comma Separated Values)** format is used. The first line of the file is used as a header and informs that the first column of
the file houses the names of the family members (alphanumerics) and the second conlumn the time of each family member (integers greater than zero).
An example of such a csv file is given in the dataset folder.

### Execution instrusctions
To execute the program the following command is used:
```
python main.py arg1 arg2
```
where 
* arg1 is the path for the dataset that is going to be used,
* arg2 is zero or a postive integer and represents the maximum time limit given to the family to cross the river (if zero then it isn't taken into consideration.

For example, 
```
python main.py .\dataset\dataset1.csv 30
```
where dataset1.csv is in the dataset folder above.
