from tkinter import *
import tkFont
import mysql.connector
from datetime import datetime
import time
"""" ------------------------------------------------------------------------------------------------"""

class MySQLdB:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.host  = ""
        self.conn = mysql.connector.connect( database='cse4701f19_project2', user="root", password="?Drogba96")

    def InsertInTbl(self, name, balance):
        curA = self.conn.cursor(buffered=True)
        print(name)
        id = curA.lastrowid

        insert = 'INSERT INTO account (account_no, name_on_account, balance, account_open_date) VALUES (%s, %s, %s, NOW());'
        curA.execute(insert, (id, name, float(balance)))
        self.conn.commit()
        curA.close()
        print("Successful insertation")

    def GettingData(self, acct):
        #print(acct)
        curA  = self.conn.cursor(buffered=True)
        rows = 'SELECT * FROM account WHERE account_no = %s'
        curA.execute(rows, (acct,))
        recordsA = curA.fetchall()
        #print(recordsA)

        self.conn.commit()
        curA.close()
        return recordsA


"""" ------------------------------------------------------------------------------------------------"""

class window:
    def __init__(self):
        pass
    """Front-end Design """
    def startup(self):

        window = Tk()
        window.title("Reuben Finanical Co. Banking Application")
        frame = Frame(window, height='300', width='300')
        frame.pack()

        def end_menu():
            window.destroy()


        """ Button Design """
        BtnArry = ["Red", "blue", "Green", "Purple", "Orange", "Yellow"]
        FontColor = "White"
        BtnHeignt = 25
        BtnWidth = 25
        BtnFont = tkFont.Font(family='Helvetica', size=12, weight='bold')

        create_new_account = Button(frame,highlightbackground=BtnArry[0], fg=FontColor, font=BtnFont, height=BtnHeignt, width=BtnWidth, command = Bank().create_account,text="Create New Account!").grid(row=0, column=0)
        checkBalance = Button(frame, highlightbackground=BtnArry[1], fg=FontColor,font=BtnFont,height=BtnHeignt, width=BtnWidth, command = Bank().checkBalance, text="Check Your Balance").grid(row=1, column=0)
        withdraw = Button(frame,highlightbackground=BtnArry[2],fg=FontColor,font=BtnFont,height=BtnHeignt,width=BtnWidth,command= Bank().withdraw, text="Withdrawal").grid(row=0,column=1)
        transfer = Button(frame, highlightbackground=BtnArry[3], fg=FontColor, font=BtnFont,height=BtnHeignt,width=BtnWidth, command=Bank().transferW, text="Transfer").grid(row=0, column=2)
        Deposit = Button(frame, highlightbackground=BtnArry[4], fg=FontColor, font=BtnFont,height=BtnHeignt,width=BtnWidth, command=Bank().Deposit, text="Deposit").grid(row=1, column=1)
        Quit = Button(frame, highlightbackground=BtnArry[5], fg=FontColor, font=BtnFont, height=BtnHeignt, width=BtnWidth, command=end_menu, text= "Exit Application").grid(row=1, column=2)
        """end """
        window.mainloop()


"""" ------------------------------------------------------------------------------------------------"""
frombalance = None
tobalance = None
class Bank:

    def __init__(self):
        pass


    def start_menu(self):
        return self.new_client.startup()


    def create_account(self):
        create_account_window = Tk()
        create_account_window.title("New Client")

        var = StringVar(master=create_account_window)
        var2 = StringVar(master=create_account_window)


        def info(self=None):
            content = var.get()
            content2 = var2.get()
            print(content)
            Transaction = MySQLdB()
            Transaction.InsertInTbl(content, content2)


            confirmation  = "---Account Successfully Created!--- "
            AccountConfirmation = "Name on account :" + content + "\n" +"Account Number: " + str(20102) + "\n" + "New Availiable Balance: " + "$"+ str(float(content2)) + "\n" +"Account opened on: " + str(datetime.now())
            ConfirmLabel = Label(create_account_window, text = confirmation + "\n" + AccountConfirmation).grid(row=3,column=0)




        EnterLabel = Label(create_account_window, text="Enter your Name" ).grid(row=0,column=0)
        SignupClient = Entry(create_account_window, textvariable=var).grid(row=0,column=1)

        EnterBalance = Label(create_account_window, text="Enter initial Balance").grid(row=1,column=0)
        Amt = Entry(create_account_window, textvariable=var2).grid(row=1,column=1)
        SubmitBtn = Button(create_account_window, text="Submit", command=info).grid(row=2,column=1)


        #confirmation  = "---Account Successful!--- "
        #AccountConfirmation = "Name: " + Name + "Account Number: " + Row



    def checkBalance(self):
        checkBalance = Tk()
        checkBalance.title("Balance")
        acctnum = StringVar(master= checkBalance)
        Amt = 0.0
        def checking(self=None):
            content = acctnum.get()

            Transaction = MySQLdB()
            out = Transaction.GettingData(content)
            #print(out[0][3])
            confirmation  = "--- Checking Account --- "

            AccountConfirmation = "Name on account :" + out[0][1]+ "\n" +"Account Number: " + str(out[0][0]) + "\n" + "New Availiable Balance: " + "$"+ str(out[0][2]) + "\n" + "Account opened on: " + str(out[0][3])
            ConfirmLabel = Label(checkBalance, text = confirmation + "\n" + AccountConfirmation).grid(row=2,column=0)




        AskingAccountLabel = Label(checkBalance, text="What is the account number").grid(row=0,column=0)
        checkBalanceEntry = Entry(checkBalance, textvariable=acctnum).grid(row=0,column=1)
        SubmitBtn = Button(checkBalance, command=checking, text="Submit").grid(row=1,column=0)


    def withdraw(self):
        Withdrawal = Tk()
        Withdrawal.title("withdraw")
        Balance = 0.0
        v = StringVar(master = Withdrawal)
        Withdrawal_Label = Label(Withdrawal, text="Enter your account number").grid(row=0, column=0)
        WithdrawalAmt = Entry(Withdrawal, textvariable= v).grid(row=0,column=1)
        SubmitBtn = Button(Withdrawal, text="Submit", command = lambda : self.subtractfunds(client=v.get(), window=Withdrawal)).grid(row=1,column=0)


    def Deposit(self):
        DepositWindow = Tk()
        DepositWindow.title("DepositAmt")
        DepositWindow.geometry("250x250")
        v = StringVar(master=DepositWindow)

        #Getting the account number
        DepositLabel = Label(DepositWindow, text="Enter an account number").grid(row=0,column=0)
        DepositAcct = Entry(DepositWindow,textvariable=v).grid(row=1,column=0)
        SubmitBtn = Button(DepositWindow, command = lambda : self.addfunds(accts_no = v.get(), window=DepositWindow), text="Submit").grid(row=2, column=0)

        #Showing the account information
        #SubmitBtn = Button(DepositWindow, text="Submit").grid(row=1,column=0)
        #checkBalance = Label(DepositWindow, text=get).grid(row=2,column=0)

    def transferW(self):
        TransferW = Tk()
        TransferW.title("Transfer")
        TransferW.geometry("500x250")
        v = StringVar(master=TransferW)

        Transferlabel = Label(TransferW, text="Enter the client account_no you want to transfer ").grid(row=0,column=0)
        TransferE = Entry(TransferW, textvariable= v).grid(row=0,column=1)
        SubmitBtn = Button(TransferW, text="Transfer", command= lambda: self.transfer(v.get(), TransferW)).grid(row=2,column=0)
        #print("Clicked!", 1)

    def transfer(self, fromWho, window):
        db = MySQLdB()
        newFromWhoBalance = None
        newTowhoBalance = None
        ResultantBalance  = None

        out = db.GettingData(fromWho)
        v = StringVar(master=window)

        def depositamt2(towho, fromWho, amt ,window2):
            db = MySQLdB()
            curA = db.conn.cursor(buffered=True)
            curB = db.conn.cursor(buffered=True)
            fromnewbalance = 0.0
            tonewbalance2 = 0.0

            v = StringVar(master=window)
            out = db.GettingData(fromWho)


            Getting_row= 'SELECT balance FROM account WHERE account_no = %s  '
            curA.execute(Getting_row,(fromWho,))
            recordsA = curA.fetchall()
            print(recordsA[0][0])
            r = self.withdrawfunds(fromWho, window2, recordsA[0][0], float(amt))
            if  r != 1:
                return None
            else:
                print("Going to sleep")
                time.sleep(10)
                print("Awake up!")
                Getting_row= 'SELECT balance FROM account WHERE account_no = %s '
                curB.execute(Getting_row,(towho,))
                recordsB = curB.fetchall()
                print(recordsB[0][0])
                self.Depositfunds(towho, window2, recordsB[0][0], float(amt))








        def transferdepositTo(towho, fromWho, window):
            g = StringVar(master= window)
            Enter_amt_to_deposit_label = Label(window, text="Enter the amount you want to Deposit to their account").grid(row=5,column=0)
            Enter_amt_to_deposit = Entry(window, textvariable = g).grid(row=5,column=1)
            submit_amt_ = Button(window, text="Submit", command= lambda : depositamt2(towho, fromWho, g.get(), window)).grid(row=6, column=0)


        printStatement = "--- Checking Account --- "
        AccountConfirmation = "Name on account :" + out[0][1]+ "\n" +"Account Number: " + str(out[0][0]) + "\n" + "New Availiable Balance: " + "$"+ str(out[0][2]) + "\n" + "Account opened on: " + str(out[0][3])
        account_information = Label(window, text = printStatement + "\n" + AccountConfirmation ).grid(row=2, column=0)
        Enter_amt_to_withdrawl_label = Label(window, text="Enter the account you want to transfer to").grid(row=3,column=0)
        Enter_amt_to_withdrawl = Entry(window, textvariable = v).grid(row=3,column=1)
        submit_amt_ = Button(window, text="Submit", command= lambda: transferdepositTo(fromWho, v.get(),window)).grid(row=4, column=0)
        #print("Clicked", 2)
# A is the client balance B is who we transferring to
    def withdrawfunds(self, client, window, A=None, amt=None):
        db = MySQLdB()
        print("Subtracted funds client number", client)
        print("Subtracted funds A:", A)
        print("Subtracted funds B:", amt)
        rows = 'SELECT balance FROM account WHERE account_no = %s FOR UPDATE'
        curA = db.conn.cursor(buffered=True)
        curA.execute(rows,(client,))
        recordsA = curA.fetchall()
        print("Values A and B in getAmt", A, amt)
        if A != None and amt != None:
            if amt > A:
                confirmation = Tk()
                errorLabel= Label(confirmation, text= "Insufficient Funds!").grid(row=5,column=0)
                return None
            else:
                newbalance =  A - amt
                frombalance = newbalance
                print(newbalance)

                updatedRow = ('UPDATE account SET balance = %s WHERE account_no = %s')
                curA.execute(updatedRow, (newbalance,client,))
                confirmation = Tk()
                ConfirmLabel= Label(confirmation, text= "Withdrawal Successful!").grid(row=5,column=0)
                db.conn.commit()
                db.conn.close()
                print("Subtracted Funds!")
                return 1




    #Subtracted funds from balance
    def subtractfunds(self, client, window, A=None, B=None):
        def getamt(amt):
            db = MySQLdB()
            print("Subtracted funds client number", client)
            print("Subtracted funds A:", A)
            print("Subtracted funds B:", B)
            rows = 'SELECT balance FROM account WHERE account_no = %s FOR UPDATE'
            curA = db.conn.cursor(buffered=True)
            curA.execute(rows,(client,))
            recordsA = curA.fetchall()
            amount = amt
            for balance in recordsA:
                if float(v.get()) > balance[0]:
                    errorLabel= Label(confirmation, text= "Insufficient Funds!").grid(row=5,column=0)
                else:
                    newbalance = balance[0] - float(amt)
                    updatedRow = ('UPDATE account SET balance = %s WHERE account_no = %s')
                    curA.execute(updatedRow, (newbalance,client,))
                    confirmation = Tk()
                    ConfirmLabel= Label(confirmation, text= "Withdrawal Successful!").grid(row=5,column=0)

                    db.conn.commit()
                    db.conn.close()

                    print("Subtracted Funds!")

        v = StringVar(master=window)
        #printStatement = "--- Checking Account --- "
        #out = MySQLdB().GettingData(client)
        #AccountConfirmation = "Name on account :" + out[0][1]+ "\n" +"Account Number: " + str(out[0][0]) + "\n" + "New Availiable Balance: " + "$"+ str(out[0][2]) + "\n" + "Account opened on: " + str(out[0][3])
        #account_information = Label(window, text = printStatement + "\n" + AccountConfirmation ).grid(row=2, column=0)
        Enter_amt_to_withdrawl_label = Label(window, text="Enter the amount you want to withdraw").grid(row=3,column=0)
        Enter_amt_to_withdrawl = Entry(window, textvariable = v).grid(row=3,column=1)
        submit_amt_ = Button(window, text="Submit", command = lambda: getamt(v.get())).grid(row=4, column=0)

    def Depositfunds(self, client, window, A=None, amt=None):
        db = MySQLdB()
        rows = 'SELECT balance FROM account WHERE account_no = %s FOR UPDATE'

        curA = db.conn.cursor(buffered=True)
        curA.execute(rows,(client,))
        recordsA = curA.fetchall()
        v = StringVar(master=window)
        newbalance = amt+ A
        tobalance = newbalance
        updatedRow = 'UPDATE account SET balance = %s WHERE account_no = %s'
        curA.execute(updatedRow, (newbalance,client,))
        confirmation = Tk()
        ConfirmLabel= Label(confirmation, text= "Transfer Successful!").grid(row=5,column=0)

        db.conn.commit()
        db.conn.close()
        print("Added Funds Final")




    #Added funds from balance to user
    def addfunds(self,accts_no, window, A=None, B=None):
        db = MySQLdB()
        rows = ('SELECT balance FROM account WHERE account_no = %s FOR UPDATE' )

        curA = db.conn.cursor(buffered=True)
        curA.execute(rows,(accts_no,))
        recordsA = curA.fetchall()
        v = StringVar(master=window)
        def depositamt(amt):
            if A  != None and B != None:
                newbalance = B + A
                tobalance = newbalance
                ConfirmLabel= Label(confirmation, text= "Withdrawal Successful!").grid(row=5,column=0)
                return newbalance
            else:

                newbalance = 0.00
                for balance in recordsA:
                    newbalance = balance[0] + float(amt)
                updatedRow = ('UPDATE account SET balance = %s WHERE account_no = %s')
                curA.execute(updatedRow, (newbalance,accts_no,))
                db.conn.commit()
                db.conn.close()
                print("Added Funds")

        #Showing the account information
        printStatement = "--- Checking Account --- "
        out = MySQLdB().GettingData(accts_no)
        AccountConfirmation = "Name on account :" + out[0][1]+ "\n" +"Account Number: " + str(out[0][0]) + "\n" + "New Availiable Balance: " + "$"+ str(out[0][2]) + "\n" + "Account opened on: " + str(out[0][3])
        account_information = Label(window, text = printStatement + "\n" + AccountConfirmation ).grid(row=4, column=0)
        Enter_amt_to_deposit_label = Label(window, text="Enter the amount you want to Deposit").grid(row=5,column=0)
        Enter_amt_to_deposit = Entry(window, textvariable = v).grid(row=5,column=1)
        submit_amt_ = Button(window, text="Submit", command= lambda : depositamt(v.get())).grid(row=6, column=0)







new_client = window()
new_client.startup()
