from tkinter import *
import tkFont
import mysql.connector
from datetime import datetime
from bank import *


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
        SubmitBtn = Button(Withdrawal, text="Submit", command = lambda : self.subtractfunds(v.get(), Withdrawal)).grid(row=1,column=0)


    def Deposit(self):
        DepositWindow = Tk()
        DepositWindow.title("DepositAmt")
        DepositWindow.geometry("250x250")
        v = StringVar(master=DepositWindow)

        #Getting the account number
        DepositLabel = Label(DepositWindow, text="Enter an account number").grid(row=0,column=0)
        DepositAcct = Entry(DepositWindow,textvariable=v).grid(row=1,column=0)
        SubmitBtn = Button(DepositWindow, command = lambda : self.addfunds(v.get(), DepositWindow), text="Submit").grid(row=2, column=0)

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
        SubmitBtn = Button(TransferW, text="Transfer", command= lambda: BankFunctions().transfer(v.get(), TransferW)).grid(row=2,column=0)
        print("Clicked!", 1)
