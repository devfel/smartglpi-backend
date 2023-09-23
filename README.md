<p align="center">
  <a href="https://devfel.com/" rel="noopener">
 <img src="https://devfel.com/imgs/devfel-logo-01.JPG" alt="DevFel"></a>
</p>

# 🎫 SmartGLPI 🛠️

# 🎫 Backend Part I - Sistema de Busca, Processamento e Anonimização de Tickets GLPI 🛠️

Converta e processe tickets do GLPI, anonimizando informações sensíveis e armazenando os dados em um formato JSON.

## 🌟 Características

- Inicialize e autentique com a API GLPI.
- Busque detalhes do ticket, incluindo informações gerais, detalhes de acompanhamento e soluções.
- Anonimize informações sensíveis, como CPFs.
- Processe o conteúdo do ticket, removendo tags HTML e imagens.
- Salve os detalhes processados em um arquivo JSON.

## ⚙️ Configuração Inicial

As informações de configuração da API GLPI são carregadas a partir de um arquivo `.env`. Você precisa configurar as seguintes variáveis:

- `GLPI_API_URL`
- `GLPI_API_APP_TOKEN`
- `GLPI_API_USER_TOKEN`

🚨 **Atenção**: Certifique-se de configurar os privilégios do usuário da API para carregar os tickets. Pode ser necessário associar o usuário aos grupos ou o sistema pode receber acesso negado a certos tickets.

## 🚀 Como Usar

1. Coloque os IDs dos tickets que você deseja processar no script.
   1.1. Você pode fornecer um único ID ou um intervalo de IDs.
2. Execute o script principal.
3. Os tickets processados e anonimizados serão salvos em um arquivo JSON.

## 🔧 Requisitos

- Python 3.x
- Bibliotecas: `requests`, `bs4`, `re`, `os`, `html`, `json`, `dotenv`
- API GLPI configurada e acessível.

## 📂 Estrutura de Diretórios

- `config.py`: Contém configurações e constantes.
- `api_utils.py`: Contém funções relacionadas à API.
- `content_utils.py`: Contém funções de processamento e anonimização de conteúdo.
- `main.py`: Contém a lógica principal para buscar e salvar dados do ticket.

## 🙌 Contribuição

Sinta-se à vontade para fazer fork do projeto, abrir issues e fornecer pull requests.

## 📜 Licença

Este projeto está licenciado sob a Licença MIT.

## ➕ Mais Informações Detalhadas do Sistema

- Execução:
  Dentro da função main, a inicialização da sessão é chamada e os IDs dos tickets são fornecidos O sistema possúi forma de buscar tickets de forma individal ou em um intervalo, e o processamento dos tickets é iniciado.

- Inicialização da Sessão:
  Uma sessão é iniciada com a API GLPI usando as credenciais e se a sessão for iniciada com sucesso, um token de sessão é retornado para ser usado nas consultas.

- Anonimização de CPFs:
  O sistema possui uma função (mask_cpf) que identifica e anonimiza CPFs nos dados dos tickets. Os CPFs no formato ###.###.###-## ou ########### são substituídos por "[#]".

- Coleta de Detalhes do Ticket:
  Essa função busca do sistema os detalhes do ticket da API GLPI, incluindo informações gerais inciais, detalhes de acompanhamento e soluções. (por enquanto os itens cadastrados como "Tarefas" não são coletados.

- Processamento dos Tickets:
  O sistema itera sobre os IDs dos tickets fornecidos.
  Para cada ticket, a função de coleta de detalhes é executada, o conteúdo é anonimizado para remover CPFs com a função Anonimização e a função de Limpar HTML também é passada para remover as tags HTML e as imagens.
  As informações do ticket, incluindo perguntas e respostas, são estruturadas em um formato específico e adicionadas a uma lista JSON.
  As perguntas (questions) são formadas pelos detalhes inicais informados na abertura do ticket, e também acompanhamentos que são feitos exclusivamente pelos usuários que abriram o ticket.
  As respostas (answers) são formadas pelos acompanhamentos realizados por usuários que não abriram a OS e por soluções enviadas no encerramento do ticket.

- Salvando em JSON:
  Após processar todos os tickets e passar os filtros e tratamentos necessários, o sistema salva os detalhes em um arquivo JSON.

# 🎫 Backend Part II - Comparar Ticket Buscado com os Demais, Recomendando OS Similares e Resposta 🛠️

## Vetorizar Perguntas dos Tickets, Compara-las com o Ticket buscado

## Em Construção
