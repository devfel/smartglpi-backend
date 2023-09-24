import openai
from src.openai_utils import get_ticket_details
from src.embedding_compare import find_most_similar_by_ticket_id
from src.apis_config import (
    OPENAI_API_KEY,
    SIMILARITY_THRESHOLD_FOR_RESPONSE,
    MAX_SIMILAR_TICKETS_FOR_ANSWER,
)

openai.api_key = OPENAI_API_KEY


def suggest_answer(searched_ticket_id):
    """
    Suggest an answer based on the given question and similar tickets.

    Args:
    - searched_ticket_id (int): The ID of the searched ticket.

    Returns:
    - str: The suggested answer from the OpenAI model.
    """

    # Searched Ticket Details
    searched_ticket = get_ticket_details(searched_ticket_id)
    prompt_parts = [f"Ordem de Serviço: '''{searched_ticket['question']}'''"]

    messages = [
        {
            "role": "system",
            "content": "Você é um técnico respondendo a usuários que não são especialistas em tecnologia da informação. Tente elaborar uma respsota final para o usuário e não deve informar que ainda estamos resolvendo. ",
        }
    ]
    messages.append({"role": "user", "content": prompt_parts[0]})

    ticket_count = 0
    similar_tickets = find_most_similar_by_ticket_id(searched_ticket_id)
    for ticket, similarity in similar_tickets:
        if similarity >= SIMILARITY_THRESHOLD_FOR_RESPONSE:
            print(f"Adding Answer Of Ticket: {ticket['id']}")
            message_content = f"Informação: '''{ticket['answer']}'''"
            messages.append({"role": "user", "content": message_content})

            ticket_count += 1
            if ticket_count >= MAX_SIMILAR_TICKETS_FOR_ANSWER:
                break  # Stop adding more tickets when the maximum limit is reached

    if ticket_count >= 1:
        # Request completion from OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=messages,
            temperature=0.2,  # You can adjust the temperature as needed
            max_tokens=450,  # You can adjust max tokens as needed
        )

        # The answer will be the content of the latest message from the "assistant" role
        return response.choices[0].message["content"].strip()
    else:
        return "Não foi possível encontrar respostas com similaridade relevante o suficiente na base de dados para gerarmos uma resposta."
