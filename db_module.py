import sqlite3

def createUserTable():
    con  = sqlite3.connect('data.db')
    cur = con.cursor()
    create_table = "CREATE TABLE user(id TEXT, password TEXT)"
    cur.execute(create_table)
    con.commit()
    con.close()


def insertUser(userId, userPwd):
    con  = sqlite3.connect('data.db')
    cur = con.cursor()
    insert_user = "INSERT INTO user(id, password) VALUES(?, ?)"
    cur.execute(insert_user, (userId, userPwd))
    con.commit()
    con.close()


# select all users
def getUsers():
    con  = sqlite3.connect('data.db')
    cur = con.cursor()
    select_users = "SELECT id, password from user"
    cur.execute(select_users)
    users = cur.fetchall()

    con.close()
    return users


# update pwd - takes id and updated pwd
def updateUser(userId, userPwd):
    con  = sqlite3.connect('data.db')
    cur = con.cursor()
    #get_user = "SELECT password from user WHERE id = ?"
    #cur.execute(get_user, (userId,))
    #rows = cur.fetchall()

    update_user = "UPDATE user SET password = ? where id = ?"
    cur.execute(update_user, (userPwd, userId))

    con.commit()
    con.close()


# delete user
def deleteUser(userId):
    con  = sqlite3.connect('data.db')
    cur = con.cursor()
    delete_user = "DELETE from user WHERE id = ?"
    cur.execute(delete_user, (userId,))
    con.commit()
    con.close()

# login, autheticate user
def login(userId, userPwd):
    con  = sqlite3.connect('data.db')
    cur = con.cursor()
    get_user = "SELECT id, password FROM user WHERE id = ? and password = ?"
    cur.execute(get_user, (userId, userPwd))
    user = cur.fetchall()
    con.close()
    return (len(user) > 0)


#create()
#
#insert('test1','testPwd')

#print(getUsers())

#update('ritesh', 'test3')

#delete('test1')

#print(getUsers())

#print(login('ritesh', 'test3'))
#print(login('ritesh', 'test2'))