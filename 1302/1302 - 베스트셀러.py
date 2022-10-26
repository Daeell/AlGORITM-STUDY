import sys
input = sys.stdin.readline

n = int(input().strip())

books = {}
for _ in range(n):
    book = input().strip()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

max_selled_book = []
max_selled_count = 0
for book in books:
    book_name = book
    book_count = books[book]
    if book_count == max_selled_count:
        max_selled_book.append(book_name)
    elif book_count > max_selled_count:
        max_selled_book = [book_name]
        max_selled_count = book_count

max_selled_book.sort()

print(max_selled_book[0])