# APRAFAP — Associação dos Produtores Rurais e Agricultores Familiares de Picuí

Portal institucional e **Portal da Transparência** desenvolvido para a **APRAFAP** (Picuí - PB), com o objetivo de divulgar informações sobre a associação, suas atividades, projetos e prestar contas sobre recursos financeiros, maquinários e equipamentos recebidos.

## Funcionalidades

- **Página Institucional (`/`):** Apresentação da associação, missão, áreas de atuação (agricultura familiar, capacitação e desenvolvimento rural) e projetos.
- **Portal da Transparência (`/transparencia/`):**
  - Listagem de publicações oficiais e prestações de contas.
  - Filtro dinâmico por categoria.
  - Barra de busca por título ou palavra-chave.
  - Exibição de órgão responsável, data de recebimento, valor e download de documentos comprobatórios (PDF).
- **Painel Administrativo (`/admin/`):** Gerenciamento completo das publicações de transparência, controle de status de publicação e upload de arquivos.

## Tecnologias Utilizadas

- **Back-end:** Python 3.12+, Django
- **Front-end:** HTML5, Tailwind CSS, JavaScript
- **Banco de Dados:** SQLite (ambiente de desenvolvimento)
- **Gerenciador de Pacotes:** `uv`

## Como executar o projeto localmente

### 1. Clonar o repositório
```bash
git clone https://github.com
cd aprafap
```

### 2. Instalar as dependências e ativar o ambiente virtual
Usando o **uv** (recomendado, pois o projeto utiliza `pyproject.toml` e `uv.lock`):
```bash
uv sync
```

Ou utilizando o `venv` padrão do Python:
```bash
python -m venv .venv
# No Windows:
.venv\Scripts\activate
# No Linux/macOS:
source .venv/bin/activate
```

### 3. Aplicar as migrações do banco de dados
```bash
python manage.py migrate
```

### 4. Criar um superusuário (para acessar o `/admin/`)
```bash
python manage.py createsuperuser
```

### 5. Iniciar o servidor de desenvolvimento
```bash
python manage.py runserver
```

Acesse no navegador:
- **Site:** `http://127.0.0`
- **Portal da Transparência:** `http://127.0.0transparencia/`
- **Painel Administrativo:** `http://127.0.0admin/`

## Estrutura do Projeto

```text
aprafap/
├── config/           # Configurações principais do Django (settings, urls)
├── institucional/    # App principal (models, views, templates, admin, static)
├── manage.py         # Utilitário de linha de comando do Django
├── pyproject.toml    # Dependências e metadados do projeto
└── uv.lock           # Trava de versões dos pacotes
```

## Licença

Este projeto foi desenvolvido para fins institucionais da **APRAFAP — Picuí - PB**.
