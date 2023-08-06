from __future__ import annotations

import sqlite3

from habitmove.nomiedata import Tracker
from habitmove.loopdata import Habit


def migrate(db: sqlite3.Connection, trackers: list[Tracker]):
    c = db.cursor()
    habits = trackers_to_habits(trackers)
    for habit in habits:
        existing_habit = check_habit_duplicate(c, habit)
        if not existing_habit:
            add_to_database(c, habit)
        else:
            print(f"Found duplicate Habit: {existing_habit} - skipping.")
    return habits


# By default set goal to half of max value
NOMIE_MAX_TO_TARGET_VALUE_RATIO = 2


def trackers_to_habits(trackers):
    habits = []
    for t in trackers:
        habits.append(
            Habit(
                archived=t.hidden,
                color=0 if t.score == -1 else 11,
                description=t.tag,
                name=f"{t.emoji} {t.label}",
                unit="" if t.uom == "num" else t.uom,
                uuid=t.id,
            )
        )
        if t.type == "range" and len(habits) > 0:
            habits[-1].type = 1
            # nomie only has concept of max value,
            # use a percentage of it for Loop range target
            habits[-1].target_value = (
                t.goal or int(t.max) // NOMIE_MAX_TO_TARGET_VALUE_RATIO
            )
    return habits


def check_habit_duplicate(cursor, habit):
    cursor.execute("select name from Habits where uuid = ?", [habit.uuid])
    name = cursor.fetchone()
    if name:
        return name[0]
    return False


def add_to_database(cursor, habit):
    """Takes a habit in the form of a dictionary and inserts it into the Habits table.
    Parameters:
    cursor (db.cursor): SQL executing cursor
    habit (Habit): A Loop habit to be added to the database.
    """
    habit_data = habit.__dict__
    placeholder = ", ".join("?" * len(habit_data))
    columns = ", ".join(habit_data.keys())
    sql = "insert into `{table}` ({columns}) values ({values});".format(
        table="Habits", columns=columns, values=placeholder
    )
    values = list(habit_data.values())
    cursor.execute(sql, values)
