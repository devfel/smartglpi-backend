import re
from html import unescape
from bs4 import BeautifulSoup


def mask_cpf(content):
    # Masking pattern for CPF in the format ###.###.###-##
    content = re.sub(r"\d{3}\.\d{3}\.\d{3}-\d{2}", "[#]", content)

    # Masking pattern for CPF in the format #############
    content = re.sub(r"\b\d{11}\b", "[#]", content)

    # Masking pattern for CPF in the format ###########-##
    content = re.sub(r"\d{9}-\d{2}", "[#]", content)

    return content


def clean_html_content(html_content):
    # Unescape the HTML entities
    unescaped_content = unescape(html_content)
    soup = BeautifulSoup(unescaped_content, "html.parser")

    # Remove all <img> tags
    for img_tag in soup.find_all("img"):
        img_tag.decompose()

    cleaned_content = soup.get_text(separator=" ", strip=True)

    return cleaned_content


def generate_ticket_ids(start, end):
    """Generate a list of ticket IDs based on the specified interval."""
    return list(range(start, end + 1))
