import pandas


df = pandas.read_csv("articles.csv")


class Book:
    def order(self):
        pass

    def stock_of(self):
        pass


class PurchaseReceipt:
    def generate(self):
        pass


book_id = input("Enter the id of the book to purchase: ")
book = Book(book_id)
if book.stock_of() > 0:
    book.order()
    name = input("Enter your name : ")
    purchase_receipt = PurchaseReceipt()
    print(purchase_receipt.generate())
else:
    print("The book is out of stock")
