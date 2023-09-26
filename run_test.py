# --------------------------------------------------------------------------------

# # [V] TESTING glpi_api_controller
# from src.glpi_api_controller import get_glpi_tickets

# if __name__ == "__main__":
#     # Example call with single individual tickets.
#     # get_glpi_tickets(individual_ticket_ids=[12084])

#     # Example call with multiple individual tickets.
#     get_glpi_tickets(
#         individual_ticket_ids=[13124],
#         use_interval=True,
#         start_id=12000,
#         end_id=12200,
#     )

#     # Example call with interval tickets.
#     # get_glpi_tickets(use_interval=True, start_id=12201, end_id=12600)

#     # # Example call with multiple individual tickets and interval tickets.
#     # get_glpi_tickets(individual_ticket_ids=[12492, 12084], use_interval=True, start_id=12000, end_id=12010)

#     # # Additional ticket IDs
#     # tickets2 = [12492, 12084, 12789, 11655, 12320, 12390, 12509, 12358, 12342, 12864,
#     #               12788, 12806, 12812, 12822, 12855, 12859, 12917, 12921, 12936, 12937,
#     #               12943, 12957, 12960, 12969, 13005, 13009, 13010, 13019, 13029, 13040,
#     #               13055, 13057, 13081, 13095, 13105, 13094, 13062, 13022, 12995, 12956,
#     #               12953, 12897]
#     # get_glpi_tickets(individual_ticket_ids=[12492, 12084, 12789, 11655, 12320, 12390, 12509, 12358, 12342, 12864])


# --------------------------------------------------------------------------------

# [V] TESTING openai_api_embed_controller
from src.openai_api_embed_controller import create_embedding_field
from src.database_utils import load_data


def main():
    # Define the list of ticket IDs for which you want to create or update embeddings
    # For this example, I'm using IDs 1, 2, and 3, but you should replace them with your actual ticket IDs
    ticket_ids = [
        12494,
        12497,
        12499,
        12500,
        12501,
        12502,
        12503,
        12504,
        12505,
        12510,
        12511,
        12514,
        12518,
        12519,
        12521,
        12522,
        12523,
        12524,
        12527,
        12528,
        12529,
        12530,
        12532,
        12533,
        12538,
        12539,
        12540,
        12544,
        12546,
        12548,
        12549,
        12550,
        12556,
        12557,
        12558,
        12559,
        12560,
        12561,
        12566,
        12568,
        12570,
        12571,
        12578,
        12579,
        12580,
        12590,
        12591,
        12593,
        12594,
        12596,
        12597,
    ]
    create_embedding_field(tickets_id_list=ticket_ids)

    # # Extract the ticket IDs from the list of dictionaries
    # tickets = load_data()
    # ticket_ids = [ticket["id"] for ticket in tickets]
    # filtered_ticket_ids = [
    #     ticket_id for ticket_id in ticket_ids if 12349 <= ticket_id <= 12600
    # ]

    # batch_size = 60
    # for i in range(0, len(filtered_ticket_ids), batch_size):
    #     batch_ticket_ids = filtered_ticket_ids[i : i + batch_size]
    #     # Call the create_embedding_field function using the batch of ticket IDs
    #     create_embedding_field(tickets_id_list=batch_ticket_ids)
    #     print(f"Batch {i} to {i+batch_size} completed")


if __name__ == "__main__":
    main()

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
