python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# instala as dependências
pip install -r requirements.txt

# sobe o servidor com reload automático
uvicorn app.main:app --reload --port 8000
