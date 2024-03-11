# --------------------------------------------------------------------------------

# Creating or updating embeddings for a batch of tickets already in the JSON file
from src.openai_api_embed_controller import create_embedding_field
from src.database_utils import load_data


def main():
    # Load all the ticket IDs from the list of dictionaries
    #     (In this case from the JSON file)
    tickets = load_data()

    # First filter: Filter the ticket IDs to create embeddings for a specific RANGE of tickets
    #     Should be removed if want to create embeddings for all tickets
    range_filtered_tickets = [
        ticket for ticket in tickets if 12349 <= ticket["id"] <= 16600
    ]

    # Second filter: From the range filtered tickets, further select those without a valid questionEmbedding
    #     This will make sure we only create embeddings for tickets that don't have it yet.
    #     Should be removed if want to update embeddings for tickets,
    #     for example if the content of the question has changed or new information was added by the user
    embedding_needed_tickets = [
        ticket["id"]
        for ticket in range_filtered_tickets
        if "questionEmbedding" not in ticket
        or ticket["questionEmbedding"] is None
        or ticket["questionEmbedding"] == []
    ]

    # Create the embeddings for the filtered ticket IDs in batches
    #     This avoids API rate limits and minimize errors processing everything at once
    batch_size = 100
    for i in range(0, len(embedding_needed_tickets), batch_size):
        batch_ticket_ids = embedding_needed_tickets[i : i + batch_size]

        # Call the create_embedding_field function using the batch of ticket IDs
        create_embedding_field(tickets_id_list=batch_ticket_ids)
        print(f"Batch {i} to {i+batch_size} completed")


if __name__ == "__main__":
    main()


# --------------------------------------------------------------------------------
# Other use cases examples
# --------------------------------------------------------------------------------

# # [V] TESTING openai_api_embed_controller
# from src.openai_api_embed_controller import create_embedding_field
# from src.database_utils import load_data


# def main():
#     # # Extract the ticket IDs from the list of dictionaries
#     # tickets = load_data()
#     # ticket_ids = [ticket["id"] for ticket in tickets]
#     # filtered_ticket_ids = [
#     #     ticket_id for ticket_id in ticket_ids if 12349 <= ticket_id <= 12600
#     # ]

#     # batch_size = 60
#     # for i in range(0, len(filtered_ticket_ids), batch_size):
#     #     batch_ticket_ids = filtered_ticket_ids[i : i + batch_size]
#     #     # Call the create_embedding_field function using the batch of ticket IDs
#     #     create_embedding_field(tickets_id_list=batch_ticket_ids)
#     #     print(f"Batch {i} to {i+batch_size} completed")


# if __name__ == "__main__":
#     main()

# --------------------------------------------------------------------------------

# # Create or update embeddings for selected tickets already in the JSON file
# def main():
#     # Define the list of ticket IDs for which you want to create or update embeddings
#     # For this example, I'm using IDs 15440, and 15442, but you should replace them with
#     #     your actual ticket IDs you want to create or update the embeddings.
#     #     Obs.: this example will NOT create the embedding for ticket 15441.
#     ticket_ids = [15440, 15442]
#     create_embedding_field(tickets_id_list=ticket_ids)


# if __name__ == "__main__":
#     main()

# --------------------------------------------------------------------------------
