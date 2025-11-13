# 📘 Projeto Registro de Vendas

Este projeto tem como objetivo auxiliar pequenos empreendedores no controle de **vendas** e **gastos**, permitindo o registro de movimentações e a visualização de métricas em um **dashboard interativo** desenvolvido com **Streamlit**, **Python** e **SQLite**.

---

## ⚙️ Instalação do Ambiente (Windows)

### 
```bash
1️⃣ Clonar o repositório
git clone https://github.com/slkaique/projeto_registro_financeiro.git
cd projeto_controle

2️⃣ Criar o ambiente virtual
python -m venv myenv

3️⃣ Ativar o ambiente virtual
myenv\Scripts\activate
Ao ativar, o prompt exibirá (myenv) no início da linha de comando.

4️⃣ Instalar as dependências
pip install -r requirements.txt

🧩 Estrutura do Projeto
projeto_controle/
│
├── app.py                # Arquivo principal do Streamlit
├── database.py           # Criação e conexão com o banco SQLite
├── carregar_dados.py     # Script para popular o banco com dados iniciais
├── data/
│   └── registro.db       # Banco de dados SQLite
├── requirements.txt      # Dependências do projeto
└── README.md

🚀 Executando o Projeto
Após ativar o ambiente virtual e instalar as dependências, execute o comando abaixo para iniciar o dashboard:
streamlit run app.py
O Streamlit abrirá automaticamente o sistema no navegador, normalmente em:
http://localhost:8501

📊 Funcionalidades
Registro de vendas e gastos com campos: descrição, tipo de movimento, valor, desconto e data.
Dashboard com:
Produto mais vendido.
Total de vendas do último mês.
Gráfico de vendas acumuladas por mês.

💡 Observações
O projeto foi desenvolvido para rodar localmente, sem necessidade de Docker.
O banco de dados é criado automaticamente na pasta data/.
Recomendado para fins de aprendizado e testes acadêmicos.
```