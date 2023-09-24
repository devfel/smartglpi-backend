# --------------------------------------------------------------------------------

# # [V] TESTING glpi_api_controller
# from src.glpi_api_controller import get_glpi_tickets

# if __name__ == "__main__":
#     # Example call with single individual tickets.
#     # get_glpi_tickets(individual_ticket_ids=[12084])

#     # Example call with multiple individual tickets.
#     get_glpi_tickets(individual_ticket_ids=[12492, 12084, 12789, 11655, 12321])

#     # # Example call with interval tickets.
#     # get_glpi_tickets(use_interval=True, start_id=12000, end_id=12010)

#     # # Example call with multiple individual tickets and interval tickets.
#     # get_glpi_tickets(individual_ticket_ids=[12492, 12084], use_interval=True, start_id=12000, end_id=12010)

#     # First Testing Database Tickets:
#     # get_glpi_tickets(individual_ticket_ids=[12492, 12084, 12789, 11655, 12320, 12390, 12509, 12358, 12342, 12864])


# --------------------------------------------------------------------------------

# # [V] TESTING openai_api_embed_controller
# from src.openai_api_embed_controller import create_embedding_field


# def main():
#     # Define the list of ticket IDs for which you want to create or update embeddings
#     # For this example, I'm using IDs 1, 2, and 3, but you should replace them with your actual ticket IDs
#     ticket_ids = [12084, 12789]
#     # Call the create_embedding_field function
#     create_embedding_field(tickets_id_list=ticket_ids)


# if __name__ == "__main__":
#     main()

# --------------------------------------------------------------------------------

# # [V] TESTING openai_api_chat_controller
# from src.openai_api_chat_controller import suggest_answer


# def main():
#     ticket_id = 12342  # Replace (Ex. 12342 ou 12789)
#     suggested_response = suggest_answer(ticket_id)
#     print(suggested_response)


# if __name__ == "__main__":
#     main()

# --------------------------------------------------------------------------------
