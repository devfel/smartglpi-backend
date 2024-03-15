import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# GLPI API CONFIG
GLPI_API_URL = os.getenv("GLPI_API_URL")
GLPI_API_APP_TOKEN = os.getenv("GLPI_API_APP_TOKEN")
GLPI_API_USER_TOKEN = os.getenv("GLPI_API_USER_TOKEN")


# OPENAI API CONFIG
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MAX_SIMILAR_TICKETS_FOR_RELATED = 6  # Maximum # to show in the similar tickets table
MAX_SIMILAR_TICKETS_FOR_ANSWER = 2  # Maximum # of tickets to consider for a response
SIMILARITY_THRESHOLD_FOR_RESPONSE = 0.94511  # 60%|Prob/1330 + 0.9|(x - 0.9) * 10 * 1.33
SIMILARITY_THRESHOLD_FOR_SEARCHBYID = SIMILARITY_THRESHOLD_FOR_RESPONSE - 0.9075  # 10%
EMBEDDING_MODEL = "text-embedding-ada-002"  # version of text embedding openAI model
OPENAI_EMBEDDING_ENDPOINT = "https://api.openai.com/v1/embeddings"
TIME_TO_WAIT_BETWEEN_EMBEDDING_REQUESTS = 22  # FREE limit is 3/min. Tier1-5$ 500/minute
CHAT_RESPONSE_TEMPERATURE = 0.2  # (0 to 1) Higher the temperatures => creative response
CHAT_RESPONSE_MAX_TOKENS = 660  # Maximum in a response. 220 tokens ~= 1 paragraph
CHAT_RESPONSE_MODEL = "gpt-3.5-turbo-16k"  # OpenAI Chat Model to use
