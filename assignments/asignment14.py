                                # Assignment #14
'''Create Program which makes Name Error and TypeError Handling both using Exceptions'''


def main():
    try:
        # Intentionally causing a NameError by using an undefined variable
        print(a)
    except NameError as ne:
        print(f"NameError: {ne} - The variable is not defined.")

    try:
        # Intentionally causing a TypeError by adding an integer and a string
        result = 10 + "5"
    except TypeError as te:
        print(f"TypeError: {te} - Cannot add an integer and a string.")

if __name__ == "__main__":
    main()
