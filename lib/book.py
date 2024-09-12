import psycopg2
from config import CREDENTIALS


class Book:
    
    
    def get_books():
        try:
            db = psycopg2.connect(host=CREDENTIALS['HOSTNAME'],
                                port=CREDENTIALS['PORT'],
                                database=CREDENTIALS['DATABASE'],
                                user=CREDENTIALS['USER'],
                                password=CREDENTIALS['PASSWORD']
                                )
            c = db.cursor()
            c.execute('SELECT * FROM book')
            data = c.fetchall()
            
            res = []
            for index in data:
                book = {
                    "book_number": index[0],
                    "book_name": index[2],
                    "publicationyear": index[3],
                    "pages": index[1],
                    "pname": index[4]
                }
                res.append(book)
            
            c.close()
            db.close()
            
            return res
        
        except (psycopg2.Error, psycopg2.DatabaseError) as err:
            c.close()
            db.close()
            return f'Error while connecting to PostgreSQL Database: {err}'
        
        
    def get_book(id):
        try:
            db = psycopg2.connect(host=CREDENTIALS['HOSTNAME'],
                                    port=CREDENTIALS['PORT'],
                                    database=CREDENTIALS['DATABASE'],
                                    user=CREDENTIALS['USER'],
                                    password=CREDENTIALS['PASSWORD']
                                    )
            c = db.cursor()
            c.execute(f"""SELECT * FROM book
                      WHERE book_number={id}""")
            data = c.fetchone()
            
            c.close()
            db.close()
            
            return str(data)
        
        except (psycopg2.Error, psycopg2.DatabaseError) as err:
            c.close()
            db.close()
            return f'Error while connecting to PostgreSQL Database: {err}'

        
    def add_book(req):
        book_number = int(req['book_number'])
        book_name = req['book_name']
        publication_year = req['publication_year']
        pages = int(req['pages'])
        pname = req['pname']
        
        try:
            db = psycopg2.connect(host=CREDENTIALS['HOSTNAME'],
                                    port=CREDENTIALS['PORT'],
                                    database=CREDENTIALS['DATABASE'],
                                    user=CREDENTIALS['USER'],
                                    password=CREDENTIALS['PASSWORD']
                                    )
            c = db.cursor()
            c.execute("""INSERT INTO book (booknumber, bookname, publicationyear, page, publishername)
                        VALUES (%s, %s, %s, %s, %s)""",
                    (book_number, book_name, publication_year, pages, pname))
            
            c.close()
            db.commit()
            db.close()
            
            return 'success'
        
        except (psycopg2.Error, psycopg2.DatabaseError) as err:
            c.close()
            db.close()
            return f'Error while connecting to PostgreSQL Database: {err}'
        
    def update_book(id, req):
        book_name = req['book_name']
        publication_year = req['publication_year']
        pages = int(req['pages'])
        pname = req['pname']

        print(pages)
        
        try:
            db = psycopg2.connect(
                host=CREDENTIALS['HOSTNAME'],
                port=CREDENTIALS['PORT'],
                database=CREDENTIALS['DATABASE'],
                user=CREDENTIALS['USER'],
                password=CREDENTIALS['PASSWORD']
            )
            c = db.cursor()
            # Use parameterized queries to prevent SQL injection
            c.execute(
                """UPDATE book
                SET bookname = %s, publicationyear = %s, page = %s, publishername = %s
                WHERE booknumber = %s""",
                (book_name, publication_year, pages, pname, id)
            )
            
            c.close()
            db.commit()
            db.close()
            
            return 'success'
        
        except (psycopg2.Error, psycopg2.DatabaseError) as err:
            print(f'Error while connecting to PostgreSQL Database: {err}')
            c.close()
            db.close()
            return f'Error while connecting to PostgreSQL Database: {err}'
        
    def delete_book(id):
        try:
            db = psycopg2.connect(host=CREDENTIALS['HOSTNAME'],
                                    port=CREDENTIALS['PORT'],
                                    database=CREDENTIALS['DATABASE'],
                                    user=CREDENTIALS['USER'],
                                    password=CREDENTIALS['PASSWORD']
                                    )
            c = db.cursor()
            # Use parameterized queries to prevent SQL injection
            c.execute("""DELETE FROM book
                        WHERE booknumber = %s""",
                    (id,))
            
            c.close()
            db.commit()
            db.close()
            
            return 'success'
        
        except (psycopg2.Error, psycopg2.DatabaseError) as err:
            print(f'Error while connecting to PostgreSQL Database: {err}')
            c.close()
            db.close()
            return f'Error while connecting to PostgreSQL Database: {err}'
    