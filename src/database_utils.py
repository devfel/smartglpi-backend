import json
import os


# Load Dataset
def load_data(filename=None):
    if filename is None:
        filename = os.path.join(
            os.path.dirname(__file__), "..", "tmp", "ticket_details.json"
        )

    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(f"Opening File: {filename}")
            return json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found. Using an empty dataset.")
        return []


# Save Dataset
def save_to_json(
    data_list,
    filename=None,
):
    if filename is None:
        filename = os.path.join(
            os.path.dirname(__file__), "..", "tmp", "ticket_details.json"
        )

    # Saving the list of ticket objects to a JSON file
    with open(filename, "w", encoding="utf-8") as file:
        print(f"Saving to File: {filename}")
        json.dump(data_list, file, ensure_ascii=False, indent=4)
    print(f"File Saved.")
