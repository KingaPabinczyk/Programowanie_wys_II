from typing import Dict, Optional

class Library:
    def __init__(self, books: Dict[str, str]):
        self.books: Dict[str, str] = books

    def find_book(self, isbn: str) -> Optional[str]:
        return self.books.get(isbn)

lib = Library({
    "978-83-01-12345-6": "Pan Tadeusz",
    "978-83-02-98765-4": "Lalka",
})

print(lib.find_book("978-83-01-12345-6"))  # Pan Tadeusz
print(lib.find_book("000-00-00000-0"))     # None
