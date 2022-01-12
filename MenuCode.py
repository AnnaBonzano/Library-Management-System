Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import mysql.connector
import datetime

def displayMenu():
    print("Library Tracking System")
    print("**************************")
    print("1-Show the number of copies for a particular library item")
    print("2-Show the details of the patrons who have at least an overdue library item today")
    print("3-Identify the total fines owed by a patron currently in the system")
    print("4-Show the details of the payment made by a patron")
    print("5-List the copies of library items that are grossly overdue")
    print("6-Show the details ofthe current pending requests in the system")
    print("7-Identify the total fines revenue to the library between April 1, 2014 to October 1st, 2014")
    print("8-List the details of the checkout periods and number of renewals for categories of library items")
    print("9-Show total number and details of library items that are checked out and renewed by a patron")
    print("10-Quit")
    print()
    #print(">> ",end="")

def getChoice():
    choice = eval(input(">>"))
    return choice
def main():
    cnx = mysql.connector.connect(host= HOSTNAME,user=USERNAME, password=PASSWORD, database='{0}_FINAL_PROJECT'.format(USERNAME))
    cursor = cnx.cursor()
    displayMenu()
    choice = getChoice()
    while(choice!=10):
        if (choice ==1):
            result=cursor.execute("SELECT COUNT(*) AS 'Number of Copies' FROM ItemCopy WHERE itemID = '6565'")
            print("Number of Copies = ", cursor.fetchone()[0])
            print()
            displayMenu()
            choice=getChoice()
        elif (choice==2):
            cursor.execute("SELECT p.patronID, p.cardID, p.fName, p.lName, f.fineAmount FROM Patron p, Fine f WHERE p.patronID = f.patronID AND f.fineAmount > 0")
            
            print()
            
            print("{0:<10}  {1:<10}  {2:<10}  {3:<10}  {4:<10}".format(
                "Patron ID", "Card ID", "First Name", "Last Name", "Fine Amount"))
            
            print("{0:=<10s}  {1:=<10s}  {2:=<10s}  {3:=<10s}  {4:=<10s}".format(
                '=', '=', '=', '=', '='))
            for (patronID, cardID, fName, lName, fineAmount) in cursor:
                print("{0:<10}  {1:<10}  {2:<10}  {3:<10}  {4:<10}".format(
                patronID, cardID, fName, lName, fineAmount))
                
            print()
            displayMenu()
            choice=getChoice()
        elif (choice==3):
            cursor.execute("SELECT p.cardID, SUM(f.fineAmount) AS 'Total Fines' FROM Patron p, Fine f WHERE p.patronID = f.patronID GROUP BY p.cardID")
            print()
            
            print("{0:<8}  {1:<8}".format(
                "Card ID", "Total Fines"))
            
            print("{0:=<7s}  {1:=<11s}".format(
                '=', '='))
            for (cardID, fineAmount) in cursor:
                print("{0:<8}  {1:<8}".format(
                cardID, fineAmount))
                
            print()
            displayMenu()
            choice=getChoice()
        elif (choice==4):
            cursor.execute("SELECT f.patronID, f.fineID, f.damage, f.dateIssued, SUM(f.fineAmount) AS 'Amount Owed' FROM Fine f GROUP BY f.patronID, f.fineID, f.damage, f.dateIssued ORDER BY f.patronID, f.fineID, f.damage, f.dateIssued")
            print()
            
            print("{0:<20}  {1:<20} {2:<20}  {3:<20}  {4:<20}".format(
                "Patron ID", "Fine ID", "Damage", "Date Issued", "Amount Owed"))
            
            print("{0:=<20s}  {1:=<20s}  {2:=<20s}  {3:=<20s}  {4:=<20s}".format(
                '=', '=', '=', '=', '='))
            for (patronID, fineID, damage, dateIssued, fineAmount) in cursor:
                print("{0:<20}  {1:<20}  {2:<20}  {3:<20}  {4:<20}".format(
                patronID, fineID, damage, dateIssued, fineAmount))
                
            print()
            displayMenu()
            choice=getChoice()
        elif (choice==5):
            cursor.execute("SELECT ic.copyID, ic.itemID, ic.categoryID, (DATEDIFF (r.expectedReturn, r.dateLoaned) - icat.checkoutPeriod) AS 'Overdue' FROM ItemCopy ic, Request r, ItemCategory icat WHERE ic.categoryID = icat.categoryID AND ic.itemID = r.itemID AND icat.checkoutPeriod < DATEDIFF(r.expectedReturn, r.dateLoaned)")
            print()
            
            print("{0:<10}  {1:<10}  {2:<10}  {3:<10}".format(
                "Copy ID", "Item ID", "Category ID", "Overdue"))
            
            print("{0:=<10s}  {1:=<10s}  {2:=<10s}  {3:=<10s}".format(
                '=', '=', '=', '='))
            for (copyID, itemID, categoryID, DATEDIFF) in cursor:
                print("{0:<10}  {1:<10}  {2:<10}  {3:<10}".format(
                copyID, itemID, categoryID, DATEDIFF))
                
            print()
            displayMenu()
            choice=getChoice()
        elif (choice==6):
            cursor.execute("SELECT requestID, patronID, itemID, dateRequested, dateLoaned FROM Request WHERE dateLoaned > '2020-05-15'")
            print()
            
            print("{0:<15}  {1:<15}  {2:<15}  {3:<15}  {4:<15}".format(
                "Request ID", "Patron ID", "Item ID", "Date Requested", "Date Loaned"))
            
            print("{0:=<15s}  {1:=<15s}  {2:=<15s}  {3:=<15s}  {4:=<15s}".format(
                '=', '=', '=', '=', '='))
            for (requestID, patronID, itemID, dateRequested, dateLoaned) in cursor:
                print("{0:<15}  {1:<15}  {2:<15}  {3:<15}  {4:<15}".format(
                requestID, patronID, itemID, dateRequested, dateLoaned))
                
            print()
            displayMenu()
            choice=getChoice()
        elif (choice==7):
            result=cursor.execute("SELECT SUM(fineAmount) AS 'Total Revenue' FROM Fine")
            print("Total Revenue = $", cursor.fetchone()[0])
            print()
            displayMenu()
            choice=getChoice()
        elif (choice==8):
            cursor.execute("SELECT categoryID, categoryName, maxRenewals, checkoutPeriod AS 'Max. of Checkout Days' FROM ItemCategory")
            print()
            
            print("{0:<20}  {1:<20}  {2:<20}  {3:<20}".format(
                "Category ID", "Category Name", "Max. Renewals", "Max. Checkout Days"))
            
            print("{0:=<20s}  {1:=<20s}  {2:=<20s}  {3:=<20s}".format(
                '=', '=', '=', '='))
            for (categoryID, categoryName, maxRenewals, checkoutPeriod) in cursor:
                print("{0:<20}  {1:<20}  {2:<20}  {3:<20}".format(
                categoryID, categoryName, maxRenewals, checkoutPeriod))
                
            print()
            displayMenu()
            choice=getChoice() 
        elif (choice==9):
            cursor.execute("SELECT r.patronID, r.requestID, r.dateLoaned, i.itemName, i.type, COUNT(r.itemID) AS 'No. of Items' FROM Request r, Item i WHERE r.itemID = i.itemID GROUP BY r.patronID, r.requestID, r.dateLoaned, i.itemName, i.type")
            print()
            
            print("{0:<20}  {1:<20}  {2:<20}  {3:<20}  {4:<20}  {5:<20}".format(
                "Patron ID", "Request ID", "Date Loaned", "Item Name", "Type", "Number of Items"))
            
            print("{0:=<20s}  {1:=<20s}  {2:=<20s}  {3:=<20s}  {4:=<20s}  {5:=<20s}".format(
                '=', '=', '=', '=', '=', '='))
            for (patronID, requestID, dateLoaned, itemName, type, itemID) in cursor:
                print("{0:<20}  {1:<20}  {2:<20}  {3:<20}  {4:<20}  {5:<20}".format(
                patronID, requestID, dateLoaned, itemName, type, itemID))
                
            print()
            displayMenu()
            choice=getChoice() 
        elif (choice==10):
            cursor.close()
            cnx.close()
            
if __name__ == "__main__":
    main()
