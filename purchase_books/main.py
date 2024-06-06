import pandas
from pdf_generator import generate_receipt


df = pandas.read_csv("articles.csv", dtype={'id': str})


class Book:
    def __init__(self, book_id):
        self.book_id = book_id
        self.stock = df.loc[df['id'] == book_id, 'in stock'].squeeze()
        self.book_name = df.loc[df['id'] == book_id, 'name'].squeeze()

    def order(self):
        df.loc[df['id'] == book_id, 'in stock'] = self.stock - 1
        df.to_csv("articles.csv", index=False)

    def stock_available(self):
        if self.stock > 0:
            return True
        else:
            return False


class PurchaseReceipt:
    def __init__(self, customer_name, book_object):
        self.customer_name = customer_name.title()
        self.book_object = book_object
        self.price = df.loc[df['id'] == self.book_object.book_id, 'price'].squeeze()

    def generate_pdf(self):
        generate_receipt(self.customer_name, self.book_object.book_name, self.price, self.book_object.book_id)
        return print("Thanks for shopping with us!!")


print(df)
book_id = input("Enter the id of the book to purchase: ")
book = Book(book_id)
if book.stock_available():
    book.order()
    name = input("Enter your name : ")
    purchase_receipt = PurchaseReceipt(customer_name=name, book_object=book)
    purchase_receipt.generate_pdf()
else:
    print("The book is out of stock")
