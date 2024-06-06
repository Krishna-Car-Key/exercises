import pandas


df = pandas.read_csv("articles.csv", dtype={'id': str})


class Book:
    def __init__(self, book_id):
        self.book_id = book_id
        self.stock = df.loc[df['id'] == book_id, 'in stock'].squeeze()

    def order(self):
        df.loc[df['id'] == book_id, 'in stock'] = self.stock - 1
        df.to_csv("articles.csv", index=False)

    def stock_available(self):
        if self.stock > 0:
            return True
        else:
            return False


class PurchaseReceipt:
    def generate(self):
        pass


print(df)
book_id = input("Enter the id of the book to purchase: ")
book = Book(book_id)
if book.stock_available():
    book.order()
    name = input("Enter your name : ")
    purchase_receipt = PurchaseReceipt()
    print(purchase_receipt.generate())
else:
    print("The book is out of stock")
