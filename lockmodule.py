import mysql.connector
def upborder():
    print("\t",end="")
    for a in range(25):
        print("*",end=" ")
    print()
    return
def downborder():
    print("\t",end="")
    for b in range(25):
        print("*",end=" ")
    print('\n')
    return
def lrborder(n=1):
    for c in range(n):
        print("\t*\t\t\t\t\t\t*")
    return 
def space(m=1):
    for d in range(m):
        s="\t*"
    return s
def fstpage():
    upborder()
    lrborder()
    print(space(),"\t\tWelcome To LOCKWORD\t",space())
    print(space(),"\t\t  Password Manager\t",space())
    lrborder()
    print(space(),"\tWe store your password with special",space())
    print(space(),"\tand unique encryption which ensures",space())
    print(space(),"\t\t Total Security\t\t",space())
    lrborder(2)
    print(space(),"\t\t>> New Registration\t",space())
    print(space(),"\t\t>> To Login\t\t",space())
    print(space(),"\t\t>> To Exit\t\t",space())
    lrborder(2)
    print(space(),"\t- Developed By Abhinav Rajpati\t",space())
    lrborder()
    downborder()
def sndpage():
    upborder()
    lrborder(1)
    print(space(),"\t\tSign Up for New User\t",space())
    lrborder(2)
    print(space(),"\t>> Name\t\t\t>> Mobile No.",space())
    lrborder()
    print(space(),"\t>> Email/Username\t>> Password",space())
    lrborder(1)
    downborder()
def trdpage():
    upborder()
    lrborder(1)
    print(space(),"\t    Login for Existing User\t",space())
    lrborder(2)
    print(space(),"\t\t>> Username\t\t",space())
    lrborder()
    print(space(),"\t\t>> Password\t\t",space())
    lrborder(1)
    downborder()
def fothpage():
    upborder()
    lrborder()
    print(space(),"\t\t     LOCKWORD\t\t",space())
    lrborder(2)
    print(space(),"\t>> Add/Update a Password\t",space())
    print(space(),"\t>> Lookup your stored Password\t",space())
    print(space(),"\t>> Delete the Password\t\t",space())
    print(space(),"\t>> Delete the Account\t\t",space())
    print(space(),"\t>> Exit Program\t\t\t",space())
    lrborder()
    downborder()
def fifthpage():
    upborder()
    lrborder()
    print(space(),"\t\t Add a Password\t\t",space())
    lrborder(2)
    print(space(),"\t>> Name of Application\t\t",space())
    print(space(),"\t>> Username in Application\t",space())
    print(space(),"\t>> Password in Application\t",space())
    lrborder()
    downborder()
def sixpage():
    upborder()
    lrborder()
    print(space(),"\t\t>> Home Page\t\t",space())
    print(space(),"\t\t>> Exit the Program\t",space())
    lrborder()
    downborder()
def secure():
    s=(('a','??????16'),("b","???100"),("c","??????17"),("d","??????211"),("e","??????19"),("f","??????333"),("g","??????366"),("h","??????636"),('i',"??????367"),("j","??????789"),("k","???123"),("l","???719"),
("m","???911"),("n","??????46"),("o","??55"),("p","???51"),("q","????????????101"),("r","??????742"),('s',"???943"),("t","???102"),("u","???317"),("v","??????109"),("w","???444"),("x","????????????577"),
("y","???210"),("z","?????????420"),('A','??????6'),("B","???8"),("C","??????2"),("D","??????1"),("E","??????7"),("F","??????0"),("G","??????21"),("H","??????63"),
('I',"??????33"),("J","??????122"),("K","???41"),("L","???32"),("M","???69"),("N","??????82"),("O","??99"),("P","???00"),("Q","????????????11"),("R","??????3"),('S',"???77"),("T","???20"),
("U","???352"),("V","??????87"),("W","???38"),("X","????????????29"),("Y","???90"),("Z","?????????60"),(" ","!00!"))
    return s
def adduser():
    name=input("Enter the Name: ")
    mobileno=input("Enter the Mobile No.: ")
    email_username=input("Enter the Email/Username: ")
    password=input("Enter the Password: ")
    b=(name,mobileno,email_username,password)
    connect=mysql.connector.connect(host="localhost",user="root",passwd="3344",database="lockword")
    cursor=connect.cursor()
    query1 = """create table %s(Name_of_Application varchar(100),Username_in_Application varchar(100),Password_in_Application varchar(100))"""%(email_username,)
    cursor.execute(query1)
    connect.close()
    connect=mysql.connector.connect(host="localhost",user="root",passwd="3344",database="lockword")
    cursor=connect.cursor()
    query3= """ INSERT INTO user (Name, Mobile, username, password) VALUES (%s, %s, %s, %s)"""
    cursor.execute(query3, b)
    connect.commit()
    connect.close()

def addpassword():
    name_of_application=input("Enter the Name of Application: ")
    username_in_application=input("Enter the Username in Application: ")
    password_in_application=input("Enter the Password in Application: ")
    l=secure()
    for m,n in l:
        name_of_application=name_of_application.replace(m,n)
        username_in_application=username_in_application.replace(m,n)
        password_in_application=password_in_application.replace(m,n)
    a=(name_of_application,username_in_application,password_in_application)
    connect=mysql.connector.connect(host="localhost",user="root",passwd="3344",database="lockword")
    cursor=connect.cursor()
    query0="insert into "+u+" values(%s,%s,%s)"
    cursor.execute(query0,a)
    connect.commit()
    connect.close()
    print("\nPassword added Sucessfully!..\n")

def login(username,password):
    global u
    u=username
    connect=mysql.connector.connect(host="localhost",user="root",passwd="3344",database="lockword")
    cursor=connect.cursor()
    query1='''Select * from user'''
    cursor.execute(query1)
    result = cursor.fetchall()
    connect.close()
    w=0
    v=0
    for i in result:
        w+=1
        if [i[2],i[3]] == [u,password]:
            g=True
        if [i[2],i[3]] != [u,password]:
            v=v+1
    if v==w:
        print("\nCredentials not found!..")
    while g:
        fothpage()
        opt=int(input("""Enter 1 to Add/Update a Password\nEnter 2 to Lookup a stored Password\nEnter 3 to Delete the Password
Enter 4 to Delete the Account\nEnter 5 to Exit Program\n: """))
        if opt == 1:
            fifthpage()
            addpassword()
            sixpage()
            choice=int(input("Enter 1 Home Page\nEnter 2 Exit the Program\n: "))
            if choice ==2 or choice>2:
                break
        elif opt == 2:
            connect=mysql.connector.connect(host="localhost",user="root",passwd="3344",database="lockword")
            cursor=connect.cursor()
            query7="""select * from %s"""%(u,)
            cursor.execute(query7)
            ls=secure()
            try:
                while True:
                    o=[]
                    l=cursor.fetchone()
                    if l==None:
                        break
                    #l=pickle.load(f)
                    for p in l:
                        k=str(p)
                        for a,b in ls:
                            k=k.replace(b,a)
                        o.append(k)
                    print("\t\t",o,"\n")
                else:
                    break
            except EOFError:
                g=True
            #f.close()
            sixpage()
            choice=int(input("Enter 1 Home Page\nEnter 2 Exit the Program\n: "))
            if choice ==2 or choice>2:
                break
        elif opt == 3:
            print("\n\t  COMING SOON...!\n")
        elif opt == 4:
            print("\n\t  COMING SOON...!\n")
        elif opt == 5:
            break
    else:
        go=False
