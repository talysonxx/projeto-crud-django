# 🗂️ CRUD de Tópicos com Autenticação – Projeto Django

Um aplicativo web desenvolvido com **Django**, funcionando como um **bloco de notas organizado por tópicos**. Usuários autenticados podem criar, visualizar, editar e excluir tópicos e descrições, mantendo suas anotações de forma simples, segura e organizada.

## Fotos 🖼
<img width="1366" height="609" alt="image" src="https://github.com/user-attachments/assets/2be60e00-77e6-4661-b485-7ddab8623801" />
<img width="1366" height="607" alt="image" src="https://github.com/user-attachments/assets/7cbc4ec4-a217-4908-b2b7-19da4241b7a5" />
<img width="1366" height="605" alt="image" src="https://github.com/user-attachments/assets/d8385aab-fd92-4b70-8c10-9a845735c914" />
<img width="1366" height="604" alt="image" src="https://github.com/user-attachments/assets/ba3ae77e-e68d-4c26-abb6-5764204e1b5e" />
<img width="1366" height="608" alt="image" src="https://github.com/user-attachments/assets/4a394e7d-d0f4-4569-9a28-303826d7107f" />
<img width="1366" height="597" alt="image" src="https://github.com/user-attachments/assets/fdf62e57-cfa9-4836-85ad-3ada54433a88" />







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
