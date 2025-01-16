import sys

def nl_command(file_name):
    """
    Simulate the Unix 'nl' command by printing each line with its line number.
    
    :param file_name: The name of the file to read.
    """
    try:
        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file, 1):
                print(f"{line_number}\t{line}", end='')
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Command-line argument handling
if len(sys.argv) < 2:
    print("Usage: python nl_command.py <file_name>")
else:
    file_name = sys.argv[1]
    nl_command(file_name)
