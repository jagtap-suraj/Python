import os

def copy_file():
    input_file = input("Enter the name of the input file: ")
    output_file = input("Enter the name of the output file: ")

    with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
        content = input_file.read();
        output_file.write(content)

    print("File copied successfully")

def count_file():
    input_file = input("Enter the name of the input file: ")

    with open(input_file, 'r') as input_file:
        line_count = 0;
        word_count = 0;
        character_count = 0;

        for line in input_file:
            line_count += 1
            words = line.split()
            word_count += len(words)
            character_count = len(line)

        print("Line Count = ", line_count)
        print("Word Count = ",  word_count)
        print("Character Count = ", character_count)

def list_file():
    current_directory = os.getcwd()
    files = os.listdir(current_directory)

    print("Files in current directory: ")
    for file in files:
        print(file)

def main():
    while True:
        print("\nMenu:")
        print("1. Copy File Content\n2. Count File Content\n3. List Files\n4. Exit")
        choice = input("Enter the choice: ")
        if choice == "1":
            copy_file()
        elif choice == "2":
            count_file()
        elif choice == "3":
            list_file()
        elif choice == "4":
            print("Exit")
            break

if __name__ == "__main__":
    main()
            
    

    
