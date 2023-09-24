from src.database_utils import load_data


def get_ticket_details(ticket_id):
    # Load the data from the json file
    data = load_data()

    for ticket in data:
        if ticket["id"] == ticket_id:
            return ticket
    return None  # Return None if ticket not found
