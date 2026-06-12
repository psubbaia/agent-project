import json
import os

STATE_FILE = os.path.join("data", "state.json")


def load_state():
    if not os.path.exists(STATE_FILE):
        return {
            "current_goal": "",
            "current_plan": [],
            "completed_tasks": []
        }

    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)