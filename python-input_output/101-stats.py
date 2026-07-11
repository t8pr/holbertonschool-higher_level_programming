#!/usr/bin/python3
"""Script that reads stdin line by line and computes log metrics."""
import sys


def print_stats(total_size, status_codes):
    """Prints the computed statistics.

    Args:
        total_size (int): The total file size accumulated.
        status_codes (dict): Dictionary of status codes and their counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


def main():
    """Reads stdin and computes metrics every 10 lines or on interruption."""
    total_size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            try:
                total_size += int(parts[-1])
                code = parts[-2]
                if code in valid_codes:
                    status_codes[code] = status_codes.get(code, 0) + 1
            except (IndexError, ValueError):
                pass
            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    if line_count % 10 != 0 or line_count == 0:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
