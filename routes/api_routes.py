from utils import analyze_email_openai
from flask import Blueprint, jsonify, request

api_bp = Blueprint('api', __name__)

# --- MOCK DATA (examples for testing) ---
MOCK_EMAILS = [
    {
        "id": 1,
        "from": "cliente@exemplo.com",
        "subject": "Atualização do chamado #345",
        "body": "Olá, preciso de uma atualização sobre o chamado #345. Cliente aguardando."
    },
    {
        "id": 2,
        "from": "amigo@ex.com",
        "subject": "Feliz Natal!",
        "body": "Feliz Natal! Abraços a todos."
    }
]

# --- HEALTH ENDPOINT ---
@api_bp.route("/health")
def health():
    return jsonify({"status": "ok"})

# --- LIST ALL EMAILS ---
@api_bp.route("/emails", methods=["GET"])
def list_emails():
    return jsonify(MOCK_EMAILS)

# --- GET EMAIL BY ID ---
@api_bp.route("/emails/<int:email_id>", methods=["GET"])
def get_email(email_id):
    email = next((e for e in MOCK_EMAILS if e["id"] == email_id), None)
    if email is None:
        return jsonify({"error": "Email não encontrado"}), 404
    return jsonify(email)


# Endpoint for classification via API using OpenAI
@api_bp.route("/classify", methods=["POST"])
def classify_email():
    data = request.get_json()
    email_text = data.get("email", "")
    if not email_text:
        return jsonify({"error": "Campo 'email' é obrigatório"}), 400
    try:
        result = analyze_email_openai(email_text)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500