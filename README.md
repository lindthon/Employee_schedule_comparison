# Employee Schedule Comparison

Project created for IOET inc. Junior Software Developers applicant


## Overview of the solution

In general, it reads the file .txt of the input, iterate each line of the input, converting the data in a dictionary that have the name and the schedule of an employee, and save it on a list.

The list saves the previous employees meanwhile the file is reading, to compare the current read employee, and compare with the provious ones.

Then, i compare each schedule by day and comparing the time that have to be within the range of time of an employee from other. 

In the end it prints the name of each employee, and the times that they have been in the office in the range of time.


## Architecture

I use a main program that reads the file and iterate it and 3 functions to modularize the code and divide the work.

I used for cycle to iterate the file, as same as, the schedule of each employee, and comparing the times by converting the time to integer.

The input of the program is a .txt file, and the output is a print by screen of the solution of the problem.

The code cost is: T(n)=n1*((n1-1)*n2)
n1= the number of employees
n2= the number of days that the employee went to work


## Methology

To compare each schedule, i used a dictionary to access each day of an employee to compare with other, so i do not have to iterate each employee all schedule that A went to work with the employee B went too.

Also, to optimize the process, i was comparing the employees' schedule while it was reading the file, so i dont have to finsh reading the file and then compare the employees' schedule.

I guided by SOLID principles to do the code, and to refactoring too, to have an omptimized and cleaned code by modularizing with functions and have easy to read variables to reach an easy to maintain code.


How to run
Project created in Python version 3.9


## How to run

CMD
```bash
$>py main.py
```
or just executing the main.py file.
When the proyect runs, it'll wait to input the namefile with the extension


Examples:

```python
Employee schedule file: schedule.txt

RENE ASTRID 2
RENE ANDRES 2
ASTRID ANDRES 3
```

CMD
```bash
$> py main.py
$> Employee schedule file: schedule.txt
$> RENE ASTRID 2
$> RENE ANDRES 2
$> ASTRID ANDRES 3
```

No special libraries were used
The project comes with few example files to test.
