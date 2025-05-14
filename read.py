def main():
    input_file = "input.txt"        
    output_file = "output.txt"

    with open(input_file, 'r') as file:
        content = file.read()

    modified_content = content.upper()

    with open(output_file, 'w') as file:
        file.write(modified_content)

    print(f"Modified content has been written to '{output_file}'.")

if __name__ == "__main__":
    main()
