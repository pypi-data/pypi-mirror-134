import sqlite3
import sys


def create_database(db_file: str = ":memory:") -> sqlite3.Connection:
    """create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
        sys.exit(1)


def create_tables(c: sqlite3.Cursor):
    c.execute(
        """ CREATE TABLE IF NOT EXISTS Habits (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        archived integer,
                                        color integer,
                                        description text,
                                        freq_den integer,
                                        freq_num integer,
                                        highlight integer,
                                        name text,
                                        position integer,
                                        reminder_hour integer,
                                        reminder_min integer,
                                        reminder_days integer NOT NULL DEFAULT 127,
                                        type integer NOT NULL DEFAULT 0,
                                        target_type integer NOT NULL DEFAULT 0,
                                        target_value real NOT NULL DEFAULT 0,
                                        unit text NOT NULL DEFAULT "",
                                        question text,
                                        uuid text 
                                    ); """
    )
    c.execute(
        """ CREATE TABLE IF NOT EXISTS Repetitions (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        habit integer NOT NULL REFERENCES Habits(id),
                                        timestamp integer NOT NULL,
                                        value integer NOT NULL
                                    ); """
    )


def create_constraints(c: sqlite3.Cursor):
    c.execute(
        """ CREATE UNIQUE INDEX IF NOT EXISTS idx_repetitions_habit_timestamp 
            on Repetitions( habit, timestamp);
        """
    )


def create_pragma(c: sqlite3.Cursor):
    c.execute(""" PRAGMA user_version = 24; """)
    c.execute(""" PRAGMA schema_version = 30; """)


def migrate(fname):
    db = create_database(fname)
    c = db.cursor()
    create_tables(c)
    create_constraints(c)
    create_pragma(c)
    return db
