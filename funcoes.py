import sqlite3
from datetime import datetime


def conectar():
    return sqlite3.connect("registro.db", check_same_thread=False)


def criar_tabela():
    conn = conectar()
    conn.execute(
        """CREATE TABLE IF NOT EXISTS registros (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        descricao TEXT,
                        tipo TEXT,
                        valor REAL,
                        desconto REAL,
                        data TEXT
                    )"""
    )
    conn.commit()
    conn.close()


def inserir_registro(descricao, tipo, valor, desconto):
    conn = conectar()
    conn.execute(
        "INSERT INTO registros (descricao, tipo, valor, desconto, data) VALUES (?, ?, ?, ?, ?)",
        (
            descricao,
            tipo,
            valor,
            desconto,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        ),
    )
    conn.commit()
    conn.close()


def listar_registros():
    conn = conectar()
    df = conn.execute("SELECT * FROM registros").fetchall()
    conn.close()
    return df
