import psycopg2

from config import CREDENTIALS


class Publisher:
    
    
    def get_publisher():
        try:
            db = psycopg2.connect(host=CREDENTIALS['HOSTNAME'],
                                port=CREDENTIALS['PORT'],
                                database=CREDENTIALS['DATABASE'],
                                user=CREDENTIALS['USER'],
                                password=CREDENTIALS['PASSWORD']
                                )
            c = db.cursor()
            c.execute('SELECT * FROM publisher')
            data = c.fetchall()
            
            c.close()
            db.close()
            
            publishers = [row[0] for row in data]
            return publishers
        
        except (psycopg2.Error, psycopg2.DatabaseError) as err:
            c.close()
            db.close()
            return f'Error while connecting to PostgreSQL Database: {err}'



