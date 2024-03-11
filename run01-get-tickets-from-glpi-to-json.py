# Process 1: Get the tickets from GLPI and save them in the database (JSON file)
from src.glpi_api_controller import get_glpi_tickets


if __name__ == "__main__":
    # Search and process tickets from GLPI, then save the results in a JSON file by using the get_glpi_tickets function.
    get_glpi_tickets(use_interval=True, start_id=15440, end_id=15443)


# --------------------------------------------------------------------------------
# Other use cases examples
# --------------------------------------------------------------------------------

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

#     # Example call with interval tickets. This will Include IDs 12201 and 12600.
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
