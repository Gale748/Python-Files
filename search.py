def search_in_file(file_path, search_str):
    with open(file_path, 'r') as file:
        for line in file:
            if search_str in line:
                print(line)

def main():
    file_path = input("\TextFiles")
    search_str = input("Enter the string to search: ")
    search_in_file(file_path, search_str)

if __name__ == "__main__":
    main()