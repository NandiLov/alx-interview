#!/usr/bin/python3

import sys

# Initialize variables to store metrics
total_size = 0
status_code_counts = {}

try:
    line_count = 0
    for line in sys.stdin:
        # Split the input line into its components
        parts = line.split()
        if len(parts) == 9:
            ip, _, _, _, status_code, file_size = parts[0], parts[8], parts[10], parts[11], parts[13], parts[14]
            if status_code.isdigit():
                # Update the total file size
                total_size += int(file_size)

                # Update status code counts
                status_code = int(status_code)
                if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    if status_code in status_code_counts:
                        status_code_counts[status_code] += 1
                    else:
                        status_code_counts[status_code] = 1

                # Increment line count
                line_count += 1

                # Check if 10 lines have been processed
                if line_count == 10:
                    # Print the metrics
                    print(f"File size: {total_size}")
                    for code in sorted(status_code_counts.keys()):
                        print(f"{code}: {status_code_counts[code]}")
                    print()

                    # Reset the counters
                    total_size = 0
                    status_code_counts = {}
                    line_count = 0
except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    pass

# Print the final metrics
print(f"File size: {total_size}")
for code in sorted(status_code_counts.keys()):
    print(f"{code}: {status_code_counts[code]}")
