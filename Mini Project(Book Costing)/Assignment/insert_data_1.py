import sqlite3

book=sqlite3.connect('m6book.db')

cursbook=book.cursor()

print(" This module for inserting new Book data")

    
cursbook.execute("CREATE TABLE IF NOT EXISTS book( ID INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT NOT NULL, author Text ,price FLOAT NOT NULL);")

    


while(True):
    print("Insert BOOk details")
    b_title=input("title : ")
    b_author=input("author : ")
    b_price=float(input("price : "))
    
    try:
        
        cursbook.execute("insert INTO book(title,author,price) VALUES(?,?,?);",(b_title,b_author,b_price))
        book.commit()
    
        print("Book added successfully")
    except:
        print("Error in inserting operation")
        book.rollback()

    rep=input("Add new book [Y= YES/Any Key= NO]")
    if(rep=='y'or rep == 'Y'):
        continue
    else:
        break

book.close()

                        
    
