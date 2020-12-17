import sqlite3
from hashlib import sha256

DBNAME = 'memory.db'


class Database_Engine:
    def __init__(self):
        self.conn = sqlite3.connect(DBNAME)
        self.cur = self.conn.cursor()

    def exec(self, command: str) -> list:
        self.cur.execute(command)
        return self.cur.fetchall()

    def _hash_password(self, pwd: str):
        return sha256(pwd.encode('utf-8')).hexdigest()

    def add_new_user(self, id: int, name: str, password: str):
        try:
            self.exec(f'INSERT INTO users '
                      f'VALUES ({id}, {name}, {self._hash_password(password)})')
        except Exception as e:
            return False
        return True

    def update_user(self, id: int, name: str, password: str):
        try:
            self.exec(f'UPDATE users set name={name}, '
                      f'password={self._hash_password(password)} '
                      f'WHERE id={id}')
        except Exception as e:
            return False
        return True

    def delete_user(self, id: int):
        try:
            self.exec(f'DELETE FROM TABLE users '
                      f'WHERE id={id}')
        except Exception as e:
            return False
        return True


if __name__ == '__main__':
    dbe = Database_Engine()
    cmd = input("[DB]<- ")
    while cmd != 'exit':
        try:
            print(dbe.exec(cmd))
        except Exception as e:
            print(f'[ERROR]-> {e}')
        finally:
            cmd = input("[DB]<- ")
