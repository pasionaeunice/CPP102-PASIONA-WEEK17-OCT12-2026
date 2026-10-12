Simulated Device Monitoring and Alert System

Student Name: Pasiona, Eunice R.

Student Number: 2600396

Section: 1CPE-A

1. Project Title

Simulated Device Monitoring and Alert System

2. Student Name
 Pasiona, Eunice R.

3. Student Number

2600396
4. Section

1CPE-A

5. Project Description

This project is a Python program that monitors simulated device temperature readings. It allows users to view and add readings, classify temperatures, and generate a numerical summary. It also determines the overall monitoring status based on the temperature classifications.

6. Features
View all current temperature readings.
Add valid temperature readings from 0 to 100.
Classify readings as NORMAL, WARNING, or CRITICAL.
Calculate the total, average, minimum, and maximum temperatures.
Display category counts and percentages.
Determine the overall monitoring status.
Reject invalid readings and menu choices.
7. Requirements
Python 3
Visual Studio Code or another Python editor
Terminal or command prompt

No external packages are required.

8. How to Run
Open the project folder in Visual Studio Code.
Open the terminal.
Run the following command:
python device_moonitor.py

9. Sample Output

The following output was observed when testing the program with the initial readings.

MONITORING SUMMARY
------------------
Number of readings  : 5
Total of readings   : 160
Average temperature : 32.00 °C
Minimum temperature : 28 °C
Maximum temperature : 37 °C

NORMAL   : 2 (40.00%)
WARNING  : 2 (40.00%)
CRITICAL : 1 (20.00%)

Overall Status: ATTENTION REQUIRED

10. Test Cases

Ten test cases cover viewing readings, adding valid and invalid values, checking classification boundaries, generating the numerical summary, handling invalid menu choices, and exiting the program.

The detailed test results are available in test_cases.md.

11. Known Limitations
The program uses simulated temperature readings only.
Readings are not saved after the program closes.
The program does not connect to real devices or sensors.
The temperature limits are for classroom simulation only.
12. Reflection

This project helped me practice Python functions, lists, loops, and conditional statements. I learned how to validate user input and calculate a numerical summary using loops. One challenging part was fixing the error that occurred when the readings list was not returned correctly. I also learned the importance of testing boundary values such as 30 °C and 35 °C.
