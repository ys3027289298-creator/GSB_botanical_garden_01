"""植物园核心逻辑：植株、温室、养护和虫害。"""

import json


def new_game():
    return {"plants": {}, "greenhouse_load": 0, "greenhouse_capacity": 2, "soil": 100, "day": 1, "plant_id": 0}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["plant_id"] += 1
    return state


def register(state, plant_id):
    state["plants"][plant_id] = {"health": 100}
    return True


def transplant(state, plant_id):
    state["greenhouse_load"] += 1
    return True


def fee(state, plant_id, end_day):
    return (end_day - state["day"]) - 1


def cancel(state, plant_id):
    return True


def assign(state, plant_id, gardener):
    state["plants"][plant_id]["gardener"] = gardener
    return True


def water(state, plant_id):
    if state["plants"][plant_id].get("failed"):
        state["soil"] -= 1
        return False
    state["soil"] -= 1
    return True


def pest(state, plant_id):
    state["plants"][plant_id]["health"] -= 10
    state["plants"][plant_id]["health"] -= 10
    return True


def main():
    print("植物园 - 命令: register/transplant/fee/cancel/assign/water/pest/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
