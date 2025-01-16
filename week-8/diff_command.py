import sys

def compare_files(file1, file2):
    """
    Compare two files and print whether they are the same or different.

    :param file1: First file name
    :param file2: Second file name
    """
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            file1_contents = f1.read()
            file2_contents = f2.read()

            if file1_contents == file2_contents:
                print("The files are the same.")
            else:
                print("The files are different.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Command-line argument handling
if len(sys.argv) < 3:
    print("Usage: python diff_command.py <file1> <file2>")
else:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    compare_files(file1, file2)
