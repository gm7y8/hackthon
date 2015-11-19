import testdata
import string
import MySQLdb

# GENERATE TEST DATA FOR USERS DATA

rand=list(string.ascii_lowercase);
class Product(testdata.DictFactory):
    StoreId= testdata.CountingFactory(100000)
    StoreName= testdata.RandomLengthStringFactory()
    Zipcode = testdata.RandomInteger(700, 99950)

u_list=[]
for user in Product().generate(4000):
    u_list.append(user)
print u_list



# Open database connection
db = MySQLdb.connect("localhost","goutham","123456","Customer_Data" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
try:
    table="Store"
    for u in u_list:
        placeholders = ', '.join(['%s'] * len(u))
        columns = ', '.join(u.keys())
        qry = "Insert Into %s (%s) Values (%s)" %(table,columns, placeholders)
        #print qry
        #print u.values()
        # Execute the SQL command
        cursor.execute(qry, u.values())
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()
# disconnect from server
db.close()