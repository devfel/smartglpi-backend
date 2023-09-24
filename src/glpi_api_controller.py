from src.glpi_utils import generate_ticket_ids, mask_cpf, clean_html_content
from src.database_utils import save_to_json
from src.glpi_api_routes import (
    init_session,
    get_ticket_details,
    get_followup_details,
    get_itil_solution_details,
)


def search_tickets(
    individual_ticket_ids=None,
    use_interval=False,
    start_id=None,
    end_id=None,
):
    """
    Search and process tickets from GLPI, then save the results in a JSON file.

    This function initializes a session to GLPI, fetches tickets based on the provided
    parameters, processes them to generate clean "questions" and "answers", and finally
    saves the results in a JSON file.

    Parameters:
    - individual_ticket_ids (list, optional): A list of individual ticket IDs to process.
    - use_interval (bool, optional): Flag to indicate if a range of ticket IDs should be processed. Defaults to False.
    - start_id (int, optional): The start of the ticket ID interval to be processed. Required if use_interval is True.
    - end_id (int, optional): The end of the ticket ID interval to be processed. Required if use_interval is True.

    Returns:
    None. If successful, results are saved to a JSON file. If no tickets are found or if there's
    an error in initializing a session, appropriate messages are printed.

    Example:
    # Example call with single individual tickets.
    search_tickets(individual_ticket_ids=[12084])

    # Example call with multiple individual tickets.
    search_tickets(individual_ticket_ids=[12492, 12084])

    # Example call with interval tickets.
    search_tickets(use_interval=True, start_id=12000, end_id=12010)

    # Example call with multiple individual tickets and interval tickets.
    search_tickets(individual_ticket_ids=[12492, 12084], use_interval=True, start_id=12000, end_id=12010)
    """

    session_token = init_session()
    if session_token:
        # If individual_ticket_ids is None, initialize as an empty list
        if individual_ticket_ids is None:
            individual_ticket_ids = []

        # if interval ticket is True, generate the ticket ids
        interval_ticket_ids = []
        if use_interval and (start_id is None or end_id is None):
            print(
                "Since use_interval is set to True, start_id and end_id must be provided."
            )
            return
        if use_interval and start_id is not None and end_id is not None:
            interval_ticket_ids = generate_ticket_ids(start_id, end_id)

        # Combine individual ticket IDs and interval ticket IDs
        ticket_ids = individual_ticket_ids + interval_ticket_ids

        # If ticket_ids is empty, print a message and exit
        if not ticket_ids:
            print("No ticket IDs provided. Exiting.")
            return

        # Process the tickets and get the list of ticket objects
        ticket_objects_list = process_tickets(session_token, ticket_ids)

        # Save the list of ticket objects to the specified JSON file
        save_to_json(ticket_objects_list)
    else:
        print("Failed to initialize session.")


def process_tickets(session_token, ticket_ids):
    ticket_objects_list = []

    # Loop through each ticket ID and fetch its details
    for ticket_id in ticket_ids:
        print("Genereting Content: ", ticket_id)  # Counter print

        ticket_details = get_ticket_details(session_token, ticket_id)

        if isinstance(ticket_details, str):
            print(f"Error fetching details for ticket ID {ticket_id}: {ticket_details}")
            continue  # Skip this ticket and move to the next one
        followup_details = get_followup_details(session_token, ticket_id)
        itil_solution_details = get_itil_solution_details(session_token, ticket_id)

        # Format the details and append to the list
        ticket_id = ticket_details["id"]
        ticket_title = mask_cpf(ticket_details["name"])
        creation_date = ticket_details["date"]
        user_id = ticket_details["users_id_recipient"]
        question_parts = [clean_html_content(ticket_details["content"])]
        answer_parts = []

        for followup in followup_details:
            content_text = clean_html_content(followup["content"])
            if followup["users_id"] == user_id:
                question_parts.append(content_text)
            else:
                answer_parts.append(content_text)

        for solution in itil_solution_details:
            content_text = clean_html_content(solution["content"])
            answer_parts.append(content_text)

        question = mask_cpf(" ".join(question_parts))
        answer = mask_cpf(" ".join(answer_parts))
        ticket_object = {
            "id": ticket_id,
            "title": ticket_title,
            "date": creation_date,
            "user": user_id,
            "question": question,
            "answer": answer,
        }

        ticket_objects_list.append(ticket_object)

    return ticket_objects_list
