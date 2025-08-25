
from utils import analisar_email_openai, preprocessar_texto, extrair_texto_pdf
from flask import Blueprint, render_template, request

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/processar", methods=["POST"])
def processar():
    # Pegar texto direto
    texto = request.form.get("email_texto")
    # Se não houver texto, tentar pegar arquivo
    if not texto and "email_arquivo" in request.files:
        arquivo = request.files["email_arquivo"]
        if arquivo.filename.endswith('.pdf'):
            texto = extrair_texto_pdf(arquivo)
        else:
            texto = arquivo.read().decode("utf-8")
    if not texto:
        return render_template("index.html", resultado="Nenhum texto fornecido.")
    # Chamar a IA da OpenAI para analisar
    try:
        texto_pre = preprocessar_texto(texto)
        resultado = analisar_email_openai(texto_pre)
    except Exception as e:
        resultado = f"Erro ao analisar email: {e}"
    return render_template("index.html", resultado=resultado)

