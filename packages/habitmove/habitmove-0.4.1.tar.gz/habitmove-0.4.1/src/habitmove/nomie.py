#!/usr/bin/env python

import json
import re
from click import secho, echo
from habitmove.nomiedata import Tracker, Event, Activity, NomieImport


def load_file(filename):
    with open(filename) as f:
        nomie_data = json.load(f)
    return nomie_data


# generate a yes/no cli question with a default answer
def confirmation_question(question, default_no=True):
    choices = " [y/N]: " if default_no else " [Y/n]: "
    default_answer = "n" if default_no else "y"
    reply = str(input(question + choices)).lower().strip() or default_answer
    if reply[0] == "y":
        return True
    if reply[0] == "n":
        return False
    else:
        return False if default_no else True


# display stats and ask user to confirm if they seem okay
def verify_continue(data: NomieImport):
    trackers = ""
    for t in data.trackers:
        trackers += t.label + ", "
    trackers = trackers[:-2]

    activity_count = 0
    for e in data.events:
        activity_count += len(e.activities) if e.activities else 0

    secho(f"Exporting from nomie {data.version}:", fg="green")
    echo(f"Found trackers: {trackers}")
    echo(
        f"Found events: {len(data.events)} entries, containing {activity_count} individual activities."
    )
    if not confirmation_question("Do you want to continue?", default_no=False):
        echo("Aborted.")
        exit(0)


def get_trackers(raw_trackers):
    tracker_list = list[Tracker]()
    for tracker_tuple in raw_trackers.items():
        tracker_list.append(Tracker(**tracker_tuple[1]))
    return tracker_list


def get_events(raw_events, tracker_list):
    events = list[Event]()
    for event in raw_events:
        event["id"] = event["_id"]
        event.pop("_id")
        event["text"] = event["note"]
        event.pop("note")

        activities = get_activities_for_event(event["text"], tracker_list)

        events.append(Event(**event, activities=activities))

    return events


def extract_tags_from_text(text, tagmarker="#"):
    """Return lists of tuples of all event tags found in text.
    Parameters:
    text (str): The text to search through.
    tagmarker (str): Optional character marking beginning of tag, defaults to '#'.
    Returns:
    tags (list): List of tuples in the form [('tag', '3'), ('anothertag', '')].
    """
    string_tags = re.findall(rf"{tagmarker}(\w+)(?:\((\d+)\))?", text)
    tags_with_int_counters = []
    for tag in string_tags:
        tags_with_int_counters.append((tag[0], None if tag[1] == "" else int(tag[1])))
    return tags_with_int_counters


def get_activities_for_event(event_text, tracker_list):
    activities = []
    tag_list = extract_tags_from_text(event_text)
    for tracker in tracker_list:
        for tag in tag_list:
            if tracker.tag in tag[0]:
                activities.append(Activity(tracker=tracker, value=tag[1]))
    return activities


# return the data belonging to nomie
def get_data(file, interactive=True):
    raw_data = load_file(file)
    nomie_version = raw_data["nomie"]["number"]

    tracker_list = get_trackers(raw_data["trackers"])
    event_list = get_events(raw_data["events"], tracker_list)

    data = NomieImport(nomie_version, tracker_list, event_list)
    if interactive:
        verify_continue(data)

    return data
