Python Code:

```python
# Import necessary libraries
import os

# Define the file paths
input_file_path = "input.dat"
vip_file_path = "vip.dat"
normal_file_path = "normal.dat"

# Initialize the counters
count_vip = 0
count_normal = 0

# Open the input file
with open(input_file_path, 'r') as input_file:
    # Open the VIP and Normal files
    with open(vip_file_path, 'w') as vip_file, open(normal_file_path, 'w') as normal_file:
        # Loop through each line in the input file
        for line in input_file:
            # Parse the line
            cust_id = int(line[0:5])
            name = line[5:25].strip()
            balance = float(line[25:33] + '.' + line[33:35])

            # Check if the balance is greater than 10000
            if balance > 10000:
                # Write the line to the VIP file
                vip_file.write(line)
                # Increment the VIP counter
                count_vip += 1
            else:
                # Write the line to the Normal file
                normal_file.write(line)
                # Increment the Normal counter
                count_normal += 1

# Print the counts
print("VIP COUNT: ", count_vip)
print("NORMAL COUNT: ", count_normal)
```

Explanation:

1. The `IDENTIFICATION DIVISION` and `PROGRAM-ID` in COBOL are not needed in Python.
2. The `ENVIRONMENT DIVISION` and `INPUT-OUTPUT SECTION` in COBOL are replaced by importing necessary libraries and defining file paths in Python.
3. The `FILE-CONTROL` and `DATA DIVISION` in COBOL are replaced by opening files using `with open` in Python.
4. The `WORKING-STORAGE SECTION` in COBOL is replaced by initializing variables in Python.
5. The `PROCEDURE DIVISION` in COBOL is replaced by the main body of the Python script.
6. The `MAIN-PARA` and `PROCESS-REC` in COBOL are replaced by a for loop that iterates over each line in the input file in Python.
7. The `READ INPUT-FILE` and `AT END` in COBOL are replaced by the end of the for loop in Python.
8. The `MOVE` and `WRITE` in COBOL are replaced by writing to files in Python.
9. The `ADD 1 TO COUNT-VIP` and `ADD 1 TO COUNT-NORMAL` in COBOL are replaced by incrementing counters in Python.
10. The `DISPLAY` in COBOL is replaced by the `print` function in Python.
11. The `CLOSE INPUT-FILE`, `CLOSE VIP-FILE`, and `CLOSE NORMAL-FILE` in COBOL are automatically handled by the `with open` statement in Python.
12. The `STOP RUN` in COBOL is not needed in Python.