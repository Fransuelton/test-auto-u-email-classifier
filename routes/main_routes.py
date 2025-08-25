
from utils import analyze_email_openai, preprocess_text, extract_text_from_pdf
from flask import Blueprint, render_template, request

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/process", methods=["POST"])
def process_email():
    # Get text directly
    text = request.form.get("email_text")
    # If no text, try to get file
    if not text and "email_file" in request.files:
        file = request.files["email_file"]
        if file.filename.endswith('.pdf'):
            text = extract_text_from_pdf(file)
        else:
            text = file.read().decode("utf-8")
    if not text:
        return render_template("index.html", result="Nenhum texto fornecido.")
    # Call OpenAI to analyze
    try:
        preprocessed_text = preprocess_text(text)
        result = analyze_email_openai(preprocessed_text)
        # Separate category and response
        category = None
        response = None
        if result:
            for line in result.splitlines():
                if line.lower().startswith('categoria:'):
                    category = line.split(':',1)[1].strip()
                elif line.lower().startswith('resposta:'):
                    response = line.split(':',1)[1].strip()
        if not category:
            category = 'Não identificado'
        if not response:
            response = result
    except Exception as e:
        category = 'Erro'
        response = f"Erro ao analisar email: {e}"
    return render_template("index.html", category=category, response=response)

