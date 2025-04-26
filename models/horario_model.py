from database.db import get_db_connection

class HorarioModel:
    @staticmethod
    def find_by_filehorario(filehorario):
        conn = get_db_connection()
        file = conn.execute('SELECT * FROM uploads WHERE filehorario = ?', (filehorario,)).fetchone()
        conn.close()
        return file