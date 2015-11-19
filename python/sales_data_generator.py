import testdata
import MySQLdb

# GENERATE TEST DATA FOR sales DATA


class Sales(testdata.DictFactory):
    ProductId= testdata.RandomInteger(100000, 1099999)
    PeriodId = testdata.RandomInteger(10101, 20151231)
    StoreId= testdata.RandomInteger(100000, 103999)
    CustomerId=testdata.RandomInteger(100000, 199999)
    Qunatity= testdata.RandomInteger(1,20)
    TransactionId=testdata.CountingFactory(1000)

u_list=[]
for user in Sales().generate(1000000):
    u_list.append(user)
#print u_list



# Open database connection
db = MySQLdb.connect("localhost","goutham","123456","Customer_Data" )
print db
# prepare a cursor object using cursor() method
cursor = db.cursor()
print cursor
try:
    table="Sales"
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