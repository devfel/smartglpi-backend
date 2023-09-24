import json
import requests
import time
from src.apis_config import (
    OPENAI_API_KEY,
    EMBEDDING_MODEL,
    TIME_TO_WAIT_BETWEEN_EMBEDDING_REQUESTS,
    OPENAI_EMBEDDING_ENDPOINT,
)
from src.database_utils import save_to_json, load_data


def create_embedding_field(
    field="questionEmbedding", search_field="question", tickets_id_list=None
):
    """
    Create embedding vectors for all tickets in the tickets_id_list.
    Create or update the embedding for a specified field in the ticket objects.

    This function goes through each ticket ID provided in the `tickets_id_list`,
    retrieves the content from the `search_field` of that ticket, and generates
    an embedding for that content. The generated embedding is then stored in the
    specified `field` of the ticket object.

    If the `field` already exists in the ticket object, its value will be updated
    with the new embedding. If it doesn't exist, it will be created.

    Args:
    - field (str, optional):            The field in the ticket object where the embedding
                                          should be stored or updated. Defaults to "questionEmbedding".
    - search_field (str, optional):     The field in the ticket object from which the
                                          content should be retrieved to generate the embedding.
                                          Defaults to "question".
    - tickets_id_list (list, optional): List of ticket IDs for which embeddings should
                                          be created or updated. If not provided, the function
                                          will exit without processing.

    Note:
    - If the `search_field` doesn't exist or is empty for a ticket, a message will be
      printed indicating this.
    - If a ticket ID from the `tickets_id_list` is not found in the dataset, a message
      will be printed indicating this.
    - After processing all tickets, the modified data is saved back to the JSON file
      using the `save_to_json` function.

    Example:
    ```python
    create_embedding_field(tickets_id_list=[1,2,3])
    ```
    This will create or update the "questionEmbedding" field for tickets with IDs 1, 2, and 3
    using the content from the "question" field of each ticket.
    """

    # Load the JSON content from the file
    data = load_data()

    if not tickets_id_list:  # If tickets_id_list is None or empty
        print("No ticket IDs provided. Exiting.")
        return

    # For each ticket_id in tickets_id_list, find the corresponding ticket in data
    total_tickets = len(tickets_id_list)
    for idx, ticket_id in enumerate(tickets_id_list):
        ticket = next((item for item in data if item["id"] == ticket_id), None)

        if ticket:
            content_to_embed = ticket.get(search_field)
            if content_to_embed:
                # Generate the embedding for the content of search_field
                embedding = create_embedding(content_to_embed)
                print(
                    f"Embedding created for ticket {ticket_id} ({idx + 1}/{total_tickets})"
                )
                # Sleep if it's not the last ticket, free OpenAI API rate limit is 3 requests per minute
                if idx < total_tickets - 1:
                    time.sleep(TIME_TO_WAIT_BETWEEN_EMBEDDING_REQUESTS)

                # Update (or create) the field in the ticket with the generated embedding
                ticket[field] = embedding
            else:
                print(
                    f"'{search_field}' not found or empty for ticket with ID {ticket_id}."
                )
        else:
            print(f"Ticket with ID {ticket_id} not found.")

    # Save the modified JSON content back to the file
    save_to_json(data)


def create_embedding(text, model=EMBEDDING_MODEL):
    """
    create embeddings for the given text using the specified OpenAI model.

    Args:
    - text (str): The input text for which the embedding is to be generated.
    - model (str): The OpenAI model ID to be used. Default is "text-embedding-ada-002".

    Returns:
    - list: The embedding for the input text.
    """

    endpoint = OPENAI_EMBEDDING_ENDPOINT
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }
    data = {"input": text, "model": model}

    response = requests.post(endpoint, headers=headers, data=json.dumps(data))
    response_json = response.json()

    if "data" in response_json and len(response_json["data"]) > 0:
        return response_json["data"][0]["embedding"]
    else:
        print(f"Error: {response.text}")
        return None
