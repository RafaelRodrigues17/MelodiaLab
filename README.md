# MelodiaLab 🎶

Plataforma de organização e criação musical, voltada para artistas e músicos que desejam criar, gerenciar e personalizar seus projetos musicais.  
![Logo](Logo.png)

## Tecnologias Utilizadas

- *Backend*: Python com Flask
- *Frontend*: HTML, CSS e JavaScript
- *Banco de Dados*: SQLite3 com Python

---

## ✅ Casos de Uso

1. **Criar Conta**(concluido)  
   - Formulário: Nome, E-mail, Senha.  
   - Cadastro na tabela de usuários.

2. **Fazer Login**(concluido)
   - Verificação de e-mail e senha.
   - Se válido, manter login com sessão (`session` do Flask).

3. **Excluir Conta**(concluido)  
   - Remover usuário da tabela.
   - Remover todos os projetos musicais ligados a esse usuário.

4. **Criar Projetos Musicais**(concluido) 
   - Formulário: Nome da música, artista, status (ex: composição, gravação, finalizada), letra.
   - Opcional: Upload de uma capa de imagem.

5. **Ver Projetos Musicais**(concluido)
   - Exibir em cards com capa, nome da música, artista, status e trecho da letra.

6. **Excluir Projeto Musical**(concluido)
   - Botão de deletar projeto associado ao usuário.

7. **Adicionar Capa ao Projeto Musical**(concluido)
   - Upload de imagem (.jpg, .png) e associação ao projeto.

8. **Editar Projeto Musical**(concluido)
   - Alterar informações: nome da música, artista, status, letra, capa.

---

## 🗃 Diagrama Banco de Dados

**Tabelas:**  

- `usuarios`
  - email (primary key)
  - nome
  - senha

- `projetos_musicais`
  - id (primary key)
  - nome_musica
  - artista
  - status
  - letra
  - caminho_capa (para o arquivo de imagem)
  - email_usuario (foreign key ligando ao usuário)

---

## Diagrama de classes
![Diagrama de Classes](/Diagrama%20de%20Classes.jpg)

## Como instalar o sistema
### Requisitos 
- Computador
- Internet
- Visual Studio Code
- Python
- Biblioteca flask para Python
- Extensão Python do VS Code
- Git 

### Clonar repositório do Github
1. Abra o Visual Studio Code e clique no botão "Controle de código de fonte"

2. Clique em "Clonar repositório", "Clonar de Github" e Clique em "Permitir" na janela que vai aparecer.

3. Faça o login, autorize o Visual Code e depois "Abrir Link" para abrir novamente o programa.

4. Escolha o repositório do projeto para clonar

5. Deseja abrir o repositório clonado? Abrir

### Instalar a extensão do Python 
1. Clique em "Extensões" no menu a esquerda ou CTRL+SHIFT+X
2. Procure por "Python"
3. Clique em "Instalar"

### Instalar a biblioteca Flask
1. Abrir um novo terminal: Barra de ferramentas > Três pontinhos > Terminal > Novo Terminal

2. No terminal, digite o comando `pip install flask` e pressione enter

### Configurando GIT
1. No terminal digite os comandos: 

`git config user.name seu_usuario`

`git config user.email seu_nome@email.com`

## Como executar o servidor 
1. Clique com o botão direito no arquivo "app.py" e selecione "Executar o arquivo Python no terminal"
