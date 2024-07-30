print("_____________________________task03________________________________________________________________")

import re
import sys
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    # use regular expression for split the log line into parts
    pattern = r'^(\S+) (\S+) (\S+) (.*)$'
    match = re.match(pattern, line)

    if match:
        return {
            'date': match.group(1),
            'time': match.group(2),
            'level': match.group(3),
            'message': match.group(4)
        }
    return {}

def load_logs(file_path: str) -> list:
    logs = []
    # try to read and parse each line in the file
    try:            
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                parsed_line = parse_log_line(line.strip())
                if parsed_line['level']:
                    logs.append(parsed_line)
    # handle exceptions        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: Hmmm... Something went wrong, unexpected error occurred - {e}")
        sys.exit(1)
    
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    # using lambda function to filter logs by level
    return list(filter(lambda log: log['level'].upper() == level.upper(), logs))

# counts all kind of logs 
def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)

    for log in logs:
        counts[log['level']] += 1
    
    return dict(counts)

# function which displays counts for all log levels in simple table 
def display_logs_count(counts: dict):
    levels = ['INFO', 'DEBUG', 'ERROR', 'WARNING']

    print(f"{'Level':<10} | {'Count':<5}")
    print("-" * 20)

    for level in levels:
        print(f"{level:<10} | {counts.get(level, 0):<5}")

def main():
    if len(sys.argv) < 2:
         print("For correct using script enter: python task0503.py <log_file_path> [log_level]")
         sys.exit(1)
    
    # get path to log file from second command argument
    path_2_log_file = sys.argv[1]
    # get a specific log level from a command argument
    log_level = sys.argv[2].upper() if len(sys.argv) == 3 else None 

    logs = load_logs(path_2_log_file)

    counts = count_logs_by_level(logs)
    display_logs_count(counts)

# filter all logs by log level and display relevant
    filtered_logs = filter_logs_by_level(logs, log_level) if log_level else print("\nNo logs level selected or wrong number of arguments")
    if filtered_logs:
        print(f"\nLogs at level {log_level}: ")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} {log['level']} {log['message']}")
    elif log_level:
        print(f"No logs found for level {log_level}")

if __name__ == "__main__":
    main()