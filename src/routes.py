from flask import jsonify, request
import time

from src.embedding_compare import find_most_similar_by_ticket_id
from src.openai_utils import get_ticket_details
from src.openai_api_chat_controller import suggest_answer
from src.glpi_api_controller import get_glpi_tickets
from src.openai_api_embed_controller import create_embedding_field


def init_app(app):
    @app.route("/get-ticket-details", methods=["POST"])
    def get_ticket_details_route():
        ticket_id = int(request.json["ticket_id"])
        ticket = get_ticket_details(ticket_id)
        if ticket:
            return jsonify(ticket)
        else:
            return jsonify({"error": "Ticket not found"}), 404

    @app.route("/create-and-embed-ticket", methods=["POST"])
    def create_and_embed_ticket():
        ticket_id = int(request.json["ticket_id"])
        # Fetch it from GLPI
        get_glpi_tickets(individual_ticket_ids=[ticket_id])
        # Generate its embedding
        create_embedding_field(tickets_id_list=[ticket_id])
        ticket = get_ticket_details(ticket_id)
        if ticket:
            return jsonify(ticket)
        else:
            return jsonify({"error": "Failed to fetch or embed ticket"}), 500

    @app.route("/find-similar-tickets", methods=["POST"])
    def find_similar_tickets():
        ticket_id = int(request.json["ticket_id"])
        results = find_most_similar_by_ticket_id(ticket_id)
        return jsonify(results)

    @app.route("/get-suggested-answer", methods=["POST"])
    def get_suggested_answer():
        ticket_id = int(request.json["ticket_id"])
        answer = suggest_answer(ticket_id)
        return jsonify({"suggested_answer": answer})
