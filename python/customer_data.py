import testdata

import MySQLdb

# GENERATE TEST DATA FOR USERS DATA
class Users(testdata.DictFactory):
    CustomerId= testdata.CountingFactory(100000)
    FirstName = testdata.FakeDataFactory('firstName')
    LastName = testdata.FakeDataFactory('lastName')
    Zipcode = testdata.RandomInteger(700, 99950)
    Age = testdata.RandomInteger(10, 30)
    Gender = testdata.RandomSelection(['female', 'male'])


u_list=[]
for user in Users().generate(100000):
    u_list.append(user)
#print u_list

#header_list=[ "id", "firstname", "lastname","zipcode", "age", "gender" ]

#wb=Workbook("New File.xlsx")
#ws=wb.add_worksheet("New Sheet")
#first_row=0
#for header in header_list:
    #col=header_list.index(header)
    #ws.write(first_row,col,header)
#row=1
#for u in u_list:
    #for _key,_value in u.items():
        #col=header_list.index(_key)
        #ws.write(row,col,_value)
    #row+=1
#wb.close()

# Open database connection
db = MySQLdb.connect("localhost","goutham","123456","Customer_Data" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
try:
    table="Customer"
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