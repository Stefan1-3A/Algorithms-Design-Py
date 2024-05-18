EMPLOYEES = 3

def greedy_distribution(books, employees=EMPLOYEES):
    books.sort(reverse=True)

    pages = [0] * employees

    for book in books:
        min_index = 0
        for j in range(1, employees):
            if pages[j] < pages[min_index]:
                min_index = j
        pages[min_index] += book

    max_pages = max(pages)
    min_pages = min(pages)

    print("Greedy Distribution: ", end="")
    for page in pages:
        print(page, end=" ")
    print(f"\nMin Difference: {max_pages - min_pages}")

    return pages

