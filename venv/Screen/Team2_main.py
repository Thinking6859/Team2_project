from tkinter import *
import os
import sqlite3 as sql

# 메인화면
from tkinter import *
import os


def insert_inf():
    username_info = username.get()
    password_info = password.get()
    name_info = username.get()
    email_info = password.get()

    conn = sql.connect('Team2.db')  # 데이터베이스 커넥션 생성
    cur = conn.cursor()  # 커서 확보

    # 튜플을 이용한 데이터 입력
    cur.execute('INSERT INTO log VALUES (?, ?, ?, ?)',  (username_info, password_info, name_info, email_info))

    conn.commit()       # 데이터베이스 반영
    conn.close()        # 커넥션 닫기

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    name_entry.delete(0, END)
    email_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

def find_inf():
    con = sql.connect('Team2.db')
    cursor = con.cursor()
    cursor.execute("SELECT name FROM log WHERE type='"+ +"';")


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x350")

    global username
    global password
    global email
    global name

    global username_entry
    global password_entry
    global email_entry
    global name_entry

    username = StringVar()
    password = StringVar()
    email = StringVar()
    name = StringVar()


    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()

    name_lable = Label(register_screen, text="이름 ")
    name_lable.pack()
    name_entry = Entry(register_screen, textvariable=name)
    name_entry.pack()

    email_lable = Label(register_screen, text="이메일 ")
    email_lable.pack()
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()

    username_lable = Label(register_screen, text="아이디 ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    password_lable = Label(register_screen, text="비밀번호 ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()



    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command = insert_inf).pack()




def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()



def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()



def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()



def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()



def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()



def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()




def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("600x400")
    main_screen.title("Account Login")
    Label(text="학점관리시스템", width="300", height="2", relief="solid").pack()
    Label(text="").pack()
    Button(text="로그인", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="회원가입", height="2", width="30", command=register).pack()

    Label(text="").pack()
    Button(text="게시판", height="2", width="30").pack()
    Label(text="").pack()
    Button(text="종료", height="2", width="30", command=exit).pack()

    main_screen.mainloop()


main_account_screen()