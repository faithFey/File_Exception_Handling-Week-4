def main():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\n--- File Content ---")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: The file '{filename}' could not be read.")

if __name__ == "__main__":
    main()
