from src.utils import *
from src.api_glpi_routes import *


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
