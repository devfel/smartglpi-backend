from flask import jsonify, request

from src.embedding_compare import find_most_similar_by_ticket_id
from src.openai_utils import get_ticket_details
from src.openai_api_chat_controller import suggest_answer


# TODO MUDAR NOEM DAS ROTAS...
def init_app(app):
    @app.route("/find-similar-tickets", methods=["POST"])
    def find_similar_tickets():
        ticket_id = int(request.json["ticket_id"])
        results = find_most_similar_by_ticket_id(ticket_id)
        return jsonify(results)

    @app.route("/get-ticket-details", methods=["POST"])
    def get_ticket_details_route():
        ticket_id = int(request.json["ticket_id"])
        ticket = get_ticket_details(ticket_id)
        if ticket:
            return jsonify(ticket)
        else:
            return jsonify({"error": "Ticket not found"}), 404

    @app.route("/get-suggested-answer", methods=["POST"])
    def get_suggested_answer():
        ticket_id = int(request.json["ticket_id"])
        answer = suggest_answer(ticket_id)
        return jsonify({"suggested_answer": answer})
