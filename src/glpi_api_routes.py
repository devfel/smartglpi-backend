import requests
from src.apis_config import *


def init_session():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"user_token {GLPI_API_USER_TOKEN}",
        "App-Token": GLPI_API_APP_TOKEN,
    }
    url = f"{GLPI_API_URL}/initSession"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()["session_token"]
    else:
        return None


def get_ticket_details(session_token, ticket_id):
    headers = {
        "Content-Type": "application/json",
        "Session-Token": session_token,
        "App-Token": GLPI_API_APP_TOKEN,
    }
    url = f"{GLPI_API_URL}/Ticket/{ticket_id}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Failed to retrieve details for ticket ID {ticket_id}. HTTP Status code: {response.status_code}"


def get_followup_details(session_token, ticket_id):
    headers = {
        "Content-Type": "application/json",
        "Session-Token": session_token,
        "App-Token": GLPI_API_APP_TOKEN,
    }
    url = f"{GLPI_API_URL}/Ticket/{ticket_id}/ITILFollowup"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Failed to retrieve follow-up details for ticket ID {ticket_id}. HTTP Status code: {response.status_code}"


def get_itil_solution_details(session_token, ticket_id):
    headers = {
        "Content-Type": "application/json",
        "Session-Token": session_token,
        "App-Token": GLPI_API_APP_TOKEN,
    }
    url = f"{GLPI_API_URL}/Ticket/{ticket_id}/ITILSolution"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Failed to retrieve ITILSolution details for ticket ID {ticket_id}. HTTP Status code: {response.status_code}"
