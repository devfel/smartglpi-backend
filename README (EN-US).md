<p align="center">
  <a href="https://devfel.com/" rel="noopener">
 <img src="https://devfel.com/imgs/devfel-logo-01.JPG" alt="DevFel"></a>
</p>

# 🎫 SmartGLPI 🛠️

## Table of Contents

- [Backend Part I - System for Searching, Processing, and Anonymizing GLPI Tickets](#backend-part-i---system-for-searching-processing-and-anonymizing-glpi-tickets)
  - [Features](#features)
  - [Initial Setup](#initial-setup)
  - [How to Use](#how-to-use)
  - [Requirements](#requirements)
  - [Directory Structure](#directory-structure)
  - [Contribution](#contribution)
  - [License](#license)
  - [More Detailed System Information](#more-detailed-system-information)
- [Backend Part II - Compare Searched Ticket with the Others, Recommending Similar OS and Response](#backend-part-ii---compare-searched-ticket-with-the-others-recommending-similar-os-and-response)
  - [Vectorize Ticket Questions, Compare Them with the Searched Ticket](#vectorize-ticket-questions-compare-them-with-the-searched-ticket)
  - [Under Construction](#under-construction)

# Backend Part I - System for Searching, Processing, and Anonymizing GLPI Tickets

Convert and process GLPI tickets, anonymizing sensitive information and storing the data in a JSON format.

## 🌟 Features

- Initialize and authenticate with the GLPI API.
- Fetch ticket details including general information, follow-up details, and solutions.
- Anonymize sensitive information such as CPFs.
- Process ticket content, removing HTML tags and images.
- Save processed details in a JSON file.

<a name="initial-setup"></a>

## ⚙️ Initial Setup

API GLPI configuration information is loaded from a `.env` file. You need to set up the following variables:

- `GLPI_API_URL`
- `GLPI_API_APP_TOKEN`
- `GLPI_API_USER_TOKEN`

🚨 **Attention**: Make sure to set up the API user privileges to fetch tickets. It may be necessary to associate the user with groups or the system may receive denied access to certain tickets.

- Configure API URL (Caminho: GLIP - Configurar - Geral - API, exemplo: http://192.168.0.155/apirest.php/)
- Configure API APP TOKEN (Caminho: GLIP - Configurar - Geral - API - Criar/Configurar Cliente de API - Token da aplicação [app_token])
- Configure IPv4 Address (Caminho: GLIP - Configurar - Geral - API - Criar/Configurar Cliente de API - configure o intervalo de endereço IPv4)

- Configure API USER TOKEN (Caminho: GLIP - Administração - Usuários - Busque/Crie o usuário - API token)

OPENAI API configuration information is also loaded from a `.env` file. You need to set up the following variable:

- `OPENAI_API_KEY`
- Go to the OpenAI API website, do the login and make sure to have an active plan for embeddings and text generation capabilities, $5 dollars annual plan should be enought for A LOT of ticket embeddings.

## 🚀 How to Use

1. Place the ticket IDs you wish to process in the script.
   1.1. You can provide a single ID or a range of IDs.
2. Run the main script.
3. The processed and anonymized tickets will be saved in a JSON file.

## 🔧 Requirements

- Python 3.x
- Libraries: `requests`, `bs4`, `re`, `os`, `html`, `json`, `dotenv`
- Configured and accessible GLPI API.

## 📂 Directory Structure

- `config.py`: Contains configurations and constants.
- `api_utils.py`: Contains functions related to the API.
- `content_utils.py`: Contains content processing and anonymizing functions.
- `main.py`: Contains the main logic for fetching and saving ticket data.

## 🙌 Contribution

Feel free to fork the project, open issues, and provide pull requests.

## 📜 License

This project is licensed under the MIT License.

## ➕ More Detailed System Information

- Execution:
  Inside the main function, session initialization is called, and ticket IDs are provided. The system has a way to fetch tickets individually or in a range, and ticket processing is started.

- Session Initialization:
  A session is started with the GLPI API using the credentials, and if the session is successfully initiated, a session token is returned for use in queries.

- CPF Anonymization:
  The system has a function (mask_cpf) that identifies and anonymizes CPFs in ticket data. CPFs in the format ###.###.###-## or ########### are replaced by "[#]".

- Ticket Details Collection:
  This function fetches the ticket details from the GLPI API including initial general information, follow-up details, and solutions. (currently, items registered as "Tasks" are not fetched.

- Tickets Processing:
  The system iterates over the provided ticket IDs.
  For each ticket, the detail fetching function is executed, content is anonymized to remove CPFs with the Anonymization function, and the HTML Cleaning function is also passed to remove HTML tags and images.
  Ticket information, including questions and answers, are structured in a specific format and added to a JSON list.
  Questions are formed by the initial details informed when opening the ticket, and also follow-ups that are made exclusively by the users who opened the ticket.
  Answers are formed by the follow-ups performed by users who did not open the OS and by solutions sent when closing the ticket.

- Saving in JSON:
  After processing all the tickets and passing the necessary filters and treatments, the system saves the details in a JSON file.
