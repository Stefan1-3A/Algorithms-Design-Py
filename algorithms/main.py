import os
from datagenerator import generate_data
from distribution import greedy_distribution, EMPLOYEES

def main():
    choice = int(input("Select which option you would like to perform:\n\n 1. Generate new experimental data\n 2. Run distribution with books\n\nEnter choice (1 or 2): "))

    if choice == 1:
        filename = input("Enter a filename for the new experimental data: ")
        number_of_books = int(input("Enter a number of books to generate (recommended amount 9, but your choice): "))
        generate_data(filename, number_of_books)
    elif choice == 2:
        try:
            with open("books.txt", "r") as file:
                books = []
                for line in file:
                    books.extend(map(int, line.split()))
        except IOError as e:
            print(f"ERROR: There has been a problem when trying to open this file! {e}")
            return
        except ValueError as e:
            print(f"ERROR: Invalid data format! {e}")
            return
        
        greedy_distribution(books, EMPLOYEES)

if __name__ == "__main__":
    main()
