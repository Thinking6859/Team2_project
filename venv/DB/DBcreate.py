# Database 연동

# 테이블 생성
import sqlite3


def create_table():
   conn = sqlite3.connect('team2.db')
   cur = conn.cursor()  # 커서 획득

   cur.execute('''create table log(
               username text,   
               email text,   
               id text,   
               password text   
            )'''
   )


   conn.commit()
   conn.close()

if __name__ == "__main__":
   create_table()