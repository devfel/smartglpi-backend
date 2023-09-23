from src.utils import *
from src.api_glpi_routes import *
from src.api_glpi_controller import *


def main():
    session_token = init_session()
    if session_token:
        # Individual ticket IDs
        individual_ticket_ids = [
            # 12492,
            # 12084,
            # 12789,
            # 11655,
            # 12320,
            # 12390,
            # 12509,
            # 12358,
            # 12342,
            # 12864,
            # 13026, #Example with image
        ]  # Adjust as necessary, leave empty if not using

        # Interval of ticket IDs
        use_interval = True  # Set to False if you don't want to use interval
        start_id = 12000
        end_id = 12010
        interval_ticket_ids = (
            generate_ticket_ids(start_id, end_id) if use_interval else []
        )

        # Combine individual ticket IDs and interval ticket IDs
        ticket_ids = individual_ticket_ids + interval_ticket_ids

        # If ticket_ids is empty, print a message and exit
        if not ticket_ids:
            print("No ticket IDs provided. Exiting.")
            return

        # Process the tickets and get the list of ticket objects
        ticket_objects_list = process_tickets(session_token, ticket_ids)

        # Save the list of ticket objects to a JSON file
        save_to_json(ticket_objects_list)
    else:
        print("Failed to initialize session.")


if __name__ == "__main__":
    main()
