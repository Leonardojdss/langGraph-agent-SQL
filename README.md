# LangGraph Agent SQL

Este projeto implementa um agente inteligente que permite interagir com um banco de dados SQLite usando linguagem natural. O agente é construído usando LangGraph e pode responder perguntas sobre dados do banco.

## 🚀 Funcionalidades

- **Chat com banco de dados**: Converse com seus dados usando linguagem natural
- **Consultas SQL automáticas**: O agente gera consultas SQL automaticamente baseadas nas suas perguntas
- **Validação de consultas**: Verificação automática de sintaxe antes da execução
- **Interface de linha de comando**: Interface simples e intuitiva
- **Dados de exemplo**: Banco de dados pré-configurado com dados de vendas

## 📁 Estrutura do Projeto

```
langGraph-agent-SQL/
├── app.py                          # Aplicação principal
├── requirements.txt                # Dependências do projeto
├── agents/
│   └── agent_sql.py               # Configuração do agente SQL
├── database/
│   ├── costumer-database.db       # Banco de dados SQLite
│   ├── create_table.sql           # Script de criação de tabelas
│   └── faturamento_vendas_insert.sql # Script com dados de exemplo
├── infra/
│   └── llm.py                     # Configuração do modelo de linguagem
└── tool/
    └── sql_tool.py                # Ferramentas para interação com SQL
```

## 🛠️ Pré-requisitos

### 1. Instalar SQLite

**macOS:**
```bash
brew install sqlite
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install sqlite3
```

**Windows:**
- Baixe o SQLite Tools do [site oficial](https://www.sqlite.org/download.html)
- Extraia os arquivos em uma pasta e adicione ao PATH

### 2. Extensões do VS Code (Recomendadas)

Instale as seguintes extensões no VS Code para melhor experiência:

- **SQLite Viewer** (`qwtel.sqlite-viewer`)
- **SQLite** (`alexcvzz.vscode-sqlite`)

### 3. Criar chave OpenAI API

1. Acesse [OpenAI Platform](https://platform.openai.com/)
2. Crie uma conta ou faça login
3. Vá para [API Keys](https://platform.openai.com/api-keys)
4. Clique em "Create new secret key"
5. Copie a chave gerada

## ⚙️ Configuração

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd langGraph-agent-SQL
```

### 2. Criar ambiente virtual

```bash
python -m venv env
source env/bin/activate  # macOS/Linux
# ou
env\Scripts\activate     # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```
### 4. Criar e popular o banco de dados

```bash
# Criar o banco de dados
sqlite3 database/costumer-database.db < database/create_table.sql

# Inserir dados de exemplo
sqlite3 database/costumer-database.db < database/faturamento_vendas_insert.sql
```

### 5. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
touch .env
```

Adicione as seguintes variáveis ao arquivo `.env`:

```env
# Chave da API OpenAI
OPENAI_API_KEY=sua_chave_da_openai_aqui

# Caminho para o banco de dados SQLite
DATABASE_SQLITE_PATH=path_do_banco_criado_executar_os_comandos_sql
```

## 🚀 Como usar

### 1. Executar a aplicação

```bash
python app.py
```

### 2. Interagir com o agente

Digite suas perguntas em linguagem natural.


### 3. Sair da aplicação

Digite `exit` ou `quit` para encerrar o chat.

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request