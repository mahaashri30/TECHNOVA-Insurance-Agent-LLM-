import sqlite3
import os
from typing import List, Dict

# ✅ Database path (ensure it's inside the backend directory)
DB_PATH = os.path.join(os.getcwd(), "insurance_ai.db")

def get_connection() -> sqlite3.Connection:
    """Create and return a database connection."""
    return sqlite3.connect(DB_PATH)

def init_db() -> None:
    """Initialize database tables if they do not exist."""
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # ✅ Table for storing documents and text chunks
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            text_chunk TEXT NOT NULL
        )
        """)
        
        # ✅ Table for storing policy plans
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            details TEXT
        )
        """)
        
        conn.commit()

def insert_document(filename: str, text_chunk: str) -> None:
    """Insert a document chunk into the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO documents (filename, text_chunk) VALUES (?, ?)",
            (filename, text_chunk)
        )
        conn.commit()

def get_all_documents() -> List[Dict]:
    """Fetch all documents and text chunks."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, filename, text_chunk FROM documents")
        rows = cursor.fetchall()
    
    return [{"id": r[0], "filename": r[1], "text_chunk": r[2]} for r in rows]

def get_all_plans() -> List[Dict]:
    """Fetch all insurance plans."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, details FROM plans")
        rows = cursor.fetchall()
    
    return [{"id": r[0], "name": r[1], "details": r[2]} for r in rows]

def insert_plan(name: str, details: str) -> None:
    """Insert a new insurance plan."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO plans (name, details) VALUES (?, ?)",
            (name, details)
        )
        conn.commit()
