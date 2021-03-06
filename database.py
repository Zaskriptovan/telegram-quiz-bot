import sqlite3 as sql


class Database:
    def __init__(self, db_file):
        with sql.connect(db_file) as self.database:
            self.cursor = self.database.cursor()
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                index_question INTEGER NOT NULL DEFAULT 0,
                score INTEGER NOT NULL DEFAULT 0);"""
            )

    def add_user(self, user_id, user_name):
        with self.database:
            try:
                return self.cursor.execute("""INSERT INTO users (id, name) VALUES (?, ?)""", (user_id, user_name,))
            except sql.IntegrityError:
                pass

    def get_index_question(self, user_id):
        with self.database:
            self.cursor.execute("""SELECT index_question FROM users WHERE id == (?)""", (user_id,))
            results = self.cursor.fetchone()[0]
            return results

    def update_index_question(self, user_id):
        with self.database:
            self.cursor.execute("""UPDATE users SET index_question = (?) WHERE id == (?)""",
                                (self.get_index_question(user_id) + 1, user_id,))

    def reset_index_question(self, user_id):
        with self.database:
            self.cursor.execute("""UPDATE users SET index_question = (?) WHERE id == (?)""", (0, user_id,))

    def get_score(self, user_id):
        with self.database:
            self.cursor.execute("""SELECT score FROM users WHERE id == (?)""", (user_id,))
            results = self.cursor.fetchone()[0]
            return results

    def update_score(self, user_id):
        with self.database:
            self.cursor.execute("""UPDATE users SET score = (?) WHERE id == (?)""",
                                (self.get_score(user_id) + 1, user_id,))

    def reset_score(self, user_id):
        with self.database:
            self.cursor.execute("""UPDATE users SET score = (?) WHERE id == (?)""",
                                (0, user_id,))

    def get_table_records(self):
        with self.database:
            self.cursor.execute("""SELECT name, score FROM users ORDER BY score DESC""")  # ???????????????????? ???? ????????????????
            results = self.cursor.fetchall()
            table_records = ''
            num_user = 1
            for i in results:
                table_records += f'{num_user}. {i[0]} : {i[1]}\n'
                num_user += 1
            return table_records


db = Database('database.db')
