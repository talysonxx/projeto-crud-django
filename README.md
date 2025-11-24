# 🗂️ CRUD de Tópicos com Autenticação – Projeto Django

Um aplicativo web desenvolvido com **Django**, funcionando como um **bloco de notas organizado por tópicos**. Usuários autenticados podem criar, visualizar, editar e excluir tópicos e descrições, mantendo suas anotações de forma simples, segura e organizada.

---

## ✨ Funcionalidades

- 🔐 **Autenticação completa**
  - Registro, login e logout
  - Gerenciamento de sessão segura

- 📝 **CRUD de Tópicos**
  - Criar novos tópicos
  - Adicionar descrições/notas dentro de cada tópico
  - Editar e excluir tópicos
  - Visualizar detalhes individualmente

- 🛡️ **Controle de acesso (permissões)**
  - Cada usuário só acessa seus próprios tópicos
  - Tentativas de acessar tópicos de outros usuários retornam 404

- 📄 **Interface simples e intuitiva**
  - Navegação fácil
  - Layout limpo para leitura e escrita de notas

---

## 🧰 Tecnologias Utilizadas

- **Python**
- **Django**
- **SQLite** (padrão)
- **HTML / CSS**
- **Bootstrap**

---

## 🚀 Como executar o projeto

```bash
# 1. Clonar o repositório
git clone https://github.com/SEU-USUARIO/SEU-REPO.git
cd SEU-REPO

# 2. Criar e ativar o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\\Scripts\\activate     # Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Executar migrações
python manage.py migrate

# 5. Iniciar o servidor
python manage.py runserver

```
obs: super usuário já criado
acesso: admin
senha: admin