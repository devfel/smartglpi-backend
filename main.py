from src.glpi_api_controller import *

if __name__ == "__main__":
    # Example call with single individual tickets.
    # search_tickets(individual_ticket_ids=[12084])

    # Example call with multiple individual tickets.
    search_tickets(
        individual_ticket_ids=[
            12492,
            12084,
            12789,
            11655,
            12320,
            12390,
            12509,
            12358,
            12342,
            12864,
        ]
    )

    # # Example call with interval tickets.
    # search_tickets(use_interval=True, start_id=12000, end_id=12010)

    # # Example call with multiple individual tickets and interval tickets.
    # search_tickets(individual_ticket_ids=[12492, 12084], use_interval=True, start_id=12000, end_id=12010)
