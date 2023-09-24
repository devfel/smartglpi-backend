from scipy.spatial import distance
from src.database_utils import load_data
from src.apis_config import (
    SIMILARITY_THRESHOLD_FOR_SEARCHBYID,
    MAX_SIMILAR_TICKETS_FOR_RELATED,
)


def find_most_similar_by_ticket_id(ticket_id_to_compare, field="questionEmbedding"):
    """
    Finds tickets that are most similar to the given ticket ID based on their embeddings.

    This function takes a ticket ID and compares its embedding (a numerical representation
    of the ticket's content) with the embeddings of all other tickets in the dataset using
    the specified field (default is "questionEmbedding"). The comparison is made using the
    cosine similarity metric. The tickets are then sorted by similarity, and the top N most
    similar tickets are returned.

    Args:
    - ticket_id_to_compare (int): The ID of the ticket to compare against others in the dataset.
    - field (str, optional): The field in the data to use for embedding comparison.
                             Defaults to "questionEmbedding".

    Returns:
    - list: A list of tuples, where each tuple contains a ticket and its similarity score
            to the provided ticket_id_to_compare. The list is sorted in descending order of
            similarity and is limited to the top N most similar tickets.

    Note:
    - If the embedding for the given ticket ID or the specified field is not found, an empty list is returned.
    - Tickets with no embeddings or whose embeddings are set to None are skipped.
    - Tickets with similarity below the threshold (SIMILARITY_THRESHOLD_FOR_SEARCHBYID)
      are excluded from the final result.

    Example:
    If the function returns [(ticket_1, 0.95), (ticket_2, 0.93)], it means ticket_1 and
    ticket_2 are the most similar to the provided ticket_id_to_compare with similarity
    scores of 0.95 and 0.93 respectively.
    """

    # Load the data from the json file
    data = load_data()

    # Find the embedding for the given ticket ID to compare
    field_embbeding = None
    for item in data:
        if item["id"] == ticket_id_to_compare:
            field_embbeding = item.get(
                field
            )  # Use the provided field to fetch embedding
            if field_embbeding is None:
                print(f"{field} not found for ticket ID {ticket_id_to_compare}")
                return []
            break  # Found the ticket, exit the loop

    if ticket_id_to_compare is None:
        print(f"Ticket ID {ticket_id_to_compare} not found in the dataset.")
        return []

    # Calculate cosine similarity with each embedding in the dataset
    similarities = []
    for item in data:
        item_field_embedding = item.get(
            field
        )  # Use the provided field to fetch embedding

        if item_field_embedding is not None:
            # Using 1 - cosine distance to get similarity
            similarity = 1 - distance.cosine(field_embbeding, item_field_embedding)
            if item["id"] != ticket_id_to_compare:
                similarities.append((item, similarity))

        else:
            # Handle the case where item_field_embedding is None (optional)
            print(f"Skipping item with None {field}: {item['id']}")

    # Sort by similarity
    sorted_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)

    # Filter tickets with less than 25% similarity and return the top 6
    return [
        item
        for item in sorted_similarities
        if item[1] >= SIMILARITY_THRESHOLD_FOR_SEARCHBYID
    ][:MAX_SIMILAR_TICKETS_FOR_RELATED]
