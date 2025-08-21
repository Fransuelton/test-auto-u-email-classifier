from flask import Flask, jsonify, request

app = Flask(__name__)

# --- DADOS MOCK (exemplos para testar) ---
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

# --- ENDPOINT DE SAÚDE ---
@app.route("/health")
def health():
    return jsonify({"status": "ok"})

# --- LISTAR TODOS OS EMAILS ---
@app.route("/emails", methods=["GET"])
def list_emails():
    return jsonify(MOCK_EMAILS)

# --- PEGAR UM EMAIL PELO ID ---
@app.route("/emails/<int:email_id>", methods=["GET"])
def get_email(email_id):
    email = next((e for e in MOCK_EMAILS if e["id"] == email_id), None)
    if email is None:
        return jsonify({"error": "Email não encontrado"}), 404
    return jsonify(email)

if __name__ == "__main__":
    # debug=True reinicia o servidor quando o código muda
    app.run(debug=True)
