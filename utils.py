import os
import nltk
import spacy
import openai
import PyPDF2

# Download stopwords if not already present
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords

# Load spaCy Portuguese model
nlp = spacy.load("pt_core_news_sm")
portuguese_stopwords = set(stopwords.words('portuguese'))

# OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def preprocess_text(text):
    """Lowercase, remove stopwords, lemmatize, remove punctuation and spaces."""
    text = text.lower()
    doc = nlp(text)
    tokens = [
        token.lemma_ for token in doc
        if token.text not in portuguese_stopwords and not token.is_punct and not token.is_space
    ]
    return " ".join(tokens)

def analyze_email_openai(text):
    """Classify and suggest reply using OpenAI GPT."""
    prompt = (
        "Você é um assistente que classifica e-mails recebidos em duas categorias: Produtivo (requere ação/resposta) ou Improdutivo (não requer ação).\n"
        "Classifique o e-mail abaixo e sugira uma resposta automática adequada.\n\n"
        f"Email:\n\"\"\"{text}\"\"\"\n\n"
        "Responda no formato:\nCategoria: <Produtivo ou Improdutivo>\nResposta: <resposta automática>"
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()

def extract_text_from_pdf(file):
    """Extract text from a PDF file object."""
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text
