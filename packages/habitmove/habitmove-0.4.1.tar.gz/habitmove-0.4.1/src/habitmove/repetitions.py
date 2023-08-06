from __future__ import annotations

import sqlite3
from typing import Optional
from datetime import datetime
from habitmove.loopdata import Habit, Repetition
from habitmove.nomiedata import Event


def migrate(db: sqlite3.Connection, habits: list[Habit], events: list[Event]) -> None:
    """Move Loop Activities contained in all Events matching Habits passed in into database.
    :param db: Database to populate.
    :param habits: List of Habits to find matching repetitions for.
    :param events: List of events to find repetitions in.
    """
    c = db.cursor()
    habits_with_sql_id = habit_list_add_ids(c, habits)
    repetitions = get_all_repetitions(habits_with_sql_id, events)
    for rep in repetitions:
        add_to_database(c, habits_with_sql_id, rep)


LOOP_RANGE_VALUE_MULTIPLIER = 1000


def get_all_repetitions(
    habits: dict[int, Habit], events: list[Event]
) -> list[Repetition]:
    """Return list of all repetitions found in events passed in.
    :param habits: Dict of habits with sql_ids that repetitions can be for.
    :param events: List of events to search through for repetitions.
    :return repetitions: List of Loop repetitions.
    """
    repetitions = []
    for event in events:
        for activity in event.activities:
            for habit in habits.values():
                # TODO Fix reaching a layer too far into activity -> tracker
                if habit.uuid == activity.tracker.id:
                    rep = Repetition(
                        habit_uuid=habit.uuid, timestamp=event.end, value=2
                    )
                    if habit.type == 1 and activity.value:
                        rep.value = activity.value * LOOP_RANGE_VALUE_MULTIPLIER
                    repetitions.append(rep)

    return repetitions


# TODO possibly just get rid of this entirely
def habit_list_add_ids(c: sqlite3.Cursor, habitlist: list[Habit]) -> dict[int, Habit]:
    """Return the collection of habits with their sqlite id added.
    :param c: SQL cursor of database to query.
    :param habitlist: Habits to get sql IDs for.
    :return habit_id_dict: The habit collection as a dict with the keys
                                 consisting of the habit's sqlite database ID.
    """
    with_id = {}
    for h in habitlist:
        sql_id = fetch_habit_id(c, h.uuid or "")
        with_id[sql_id] = h

    return with_id


def fetch_habit_id(cursor: sqlite3.Cursor, uuid: str) -> Optional[int]:
    """Return sqlite internal id for habit with uuid.
    :param c: SQL cursor of database to query.
    :param uuid: Unique id of habit to query for.
    :return id: SQLite internal id for habit queried for.
    """
    cursor.execute("select id from Habits where uuid = ?", ([uuid]))
    id = cursor.fetchone()
    if id is not None:
        return id[0]


def add_to_database(
    cursor: sqlite3.Cursor, habits: dict[int, Habit], repetition: Repetition
) -> None:
    """Insert the repetition into a sqlite3 table suitable for Loop.
    :param c: SQL cursor of database to query.
    :sql_id: Internal sqlite database id of the habit the repetition belongs to.
    """
    for sql_id, habit in habits.items():
        if repetition.habit_uuid == habit.uuid:
            try:
                cursor.execute(
                    """
                    INSERT INTO
                    Repetitions(id, habit, timestamp, value)
                    VALUES (NULL, ?, ?, ?)
                    """,
                    (sql_id, repetition.timestamp, repetition.value),
                )
            except sqlite3.IntegrityError:
                # FIXME better error handling
                # TODO think about adapting this to allow importing into existing databases
                print(
                    f"{sql_id}, {habit.name}: timestamp {datetime.fromtimestamp(repetition.timestamp/1000)} not unique, moving timestamp slightly."
                )
                add_to_database(
                    cursor,
                    habits,
                    Repetition(
                        repetition.habit_uuid,
                        repetition.timestamp + 1,
                        repetition.value,
                    ),
                )
