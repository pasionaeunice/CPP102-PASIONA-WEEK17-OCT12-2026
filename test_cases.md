# Test Cases – Simulated Device Monitoring and Alert System

## Test Case Table

| Test Case ID | Test Description | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC01 | View initial readings | Select 1 | Displays 28, 31, 35, 37, 29 | Displayed all five initial readings correctly. | PASS |
| TC02 | Add a valid reading | Select 2, enter 33 | Reading 33 is added successfully | Displayed "Reading added successfully." | PASS |
| TC03 | Add a non-numeric reading | Select 2, enter abc | Displays an invalid input message | Displayed "Invalid input. Enter a whole number only." | PASS |
| TC04 | Add a reading above the valid range | Select 2, enter 120 | Rejects the reading | Displayed "Invalid reading. Enter a value from 0 to 100." | PASS |
| TC05 | Add a negative reading | Select 2, enter -5 | Rejects the reading | Displayed "Invalid reading. Enter a value from 0 to 100." | PASS |
| TC06 | Classify readings | Select 3 | Displays NORMAL, WARNING, or CRITICAL for each reading | Displayed the correct classifications, including 30 °C and 35 °C as WARNING. | PASS |
| TC07 | Generate summary | Select 4 | Displays total, average, minimum, maximum, category counts, and overall status | Displayed the summary with numerical values, category counts, and overall status. | PASS |
| TC08 | Verify initial summary | Restart program and select 4 | Total: 160; Average: 32.00; Minimum: 28; Maximum: 37 | Total: 160; Average: 32.00 °C; Minimum: 28 °C; Maximum: 37 °C; Overall Status: ATTENTION REQUIRED. | PASS |
| TC09 | Enter an invalid menu option | Enter 9 | Displays an invalid menu option message | Displayed "Invalid choice. Please enter a number from 1 to 5." and showed the menu again. | PASS |
| TC10 | Exit the program | Select 5 | Displays an exit message and ends the program | Thank you for using the Device Monitoring System. Program ended and returned to the PowerShell prompt. | PASS |

## Notes

- Run each test case using the actual program.
- Record the observed output in the Actual Result column.
- Mark the Status as PASS if the actual result matches the expected result; otherwise, mark it FAIL.

## Bugs Found and Fixed

- Fixed a TypeError caused by the readings variable being None instead of a list.
- Tested invalid inputs such as abc, 120, and -5 to confirm that they are rejected.
- Verified that 30 °C and 35 °C are classified as WARNING.
- Tested the exit option to confirm that the program terminates correctly.