#!/usr/bin/python3
"""log parsing"""
import sys
import signal

# Initialize global variables for total file size and status code count
total_file_size = 0
status_code_count = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
line_counter = 0


# Function to print metrics
def print_stats():
    """ print status """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")


# Function to handle keyboard interruption (CTRL + C)
def handle_interrupt(signal, frame):
    """ handle interupt """
    print_stats()
    sys.exit(0)


# Capture keyboard interruption (CTRL + C)
signal.signal(signal.SIGINT, handle_interrupt)

try:
    # Read lines from stdin
    for line in sys.stdin:
        # Check if line matches the expected format
        parts = line.split()

        if len(parts) < 7:
            continue

        # Extract the <file size> and <status code>
        ip = parts[0]
        date = parts[3][1:]
        request = parts[5][1:]
        status_code = parts[-2]
        file_size = parts[-1]

        # Skip if the request is not "GET /projects/260 HTTP/1.1"
        if (parts[5] != '"GET' or parts[6] != '/projects/260'
           or parts[7] != 'HTTP/1.1"'):
            continue

        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue  # Skip lines with non-integer status codes or file sizes

        # Increment total file size
        total_file_size += file_size

        # Count the status code if it's one of the expected codes
        if status_code in status_code_count:
            status_code_count[status_code] += 1

        line_counter += 1

        # Print stats every 10 lines
        if line_counter % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print stats upon keyboard interruption
    print_stats()
    sys.exit(0)
