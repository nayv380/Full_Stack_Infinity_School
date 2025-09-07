# 🚀 Terminal Product Manager 🛒

Um **CRUD de Produtos no Terminal** com persistência em **CSV** usando **Python + Pandas**.

Se você sempre quis gerenciar uma lojinha imaginária direto do terminal, com direito a salvar tudo num CSV e brincar de "mini ERP", este projeto é pra você! 😄

---

## 📚 Sobre o Projeto

Este é um sistema simples de **Gestão de Produtos**, onde você pode:

✅ Cadastrar produtos  
✅ Listar todos os produtos cadastrados  
✅ Editar qualquer produto da lista  
✅ Excluir produtos que já não fazem mais sentido  
✅ E o melhor: tudo fica salvo num arquivo CSV, pronto pra ser reaberto na próxima execução!

📌 Ah, e o **pandas** cuida de ler e escrever os dados pra gente!

---

## 📂 Estrutura de Pastas

projeto2/
├── database.csv # Onde os produtos vivem (armazenamento em CSV)
├── db.py # Módulo de importação/exportação dos dados
├── produtos.py # Toda a mágica do CRUD acontece aqui
├── main.py # O "coração" do projeto, com o menu principal
├── requirements.txt # Lista de dependências
└── README.md # Essa documentação que você está lendo

---

## 🏗️ Como Rodar o Projeto (Passo a Passo)

### 1. Clone ou baixe o projeto:

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd projeto2
```
Ou baixe o ZIP, extraia e abra a pasta no VS Code (ou seu editor favorito).

### 2. Crie um ambiente virtual (Opcional, mas Super Recomendado 🚀)

```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual:

Windows:

```bash
.venv\Scripts\activate
```

Linux / MacOS:

```bash
source .venv/bin/activate
```

### 4. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

### 5. Execute o programa:

```bash
python main.py
```

---

🎮 Navegação no Sistema

Ao rodar, o terminal vai te mostrar um menu assim:

```
==============================
   Gerenciamento de Produtos   
==============================
[1] - Listar Produtos
[2] - Cadastrar Produto
[3] - Editar Produto
[4] - Excluir Produto
[5] - Sair
==============================
--> Selecione uma Opção: 
```

📌 As alterações são salvas automaticamente no CSV quando você escolhe sair.

---

✅ Requisitos para rodar

- Python 3.11 ou superior  
- Pip  
- Biblioteca pandas

---

💡 Exemplos de Uso:

✔️ Cadastrar um Produto:  
Informe o nome, o preço (usando vírgula como separador decimal) e a quantidade.

✔️ Listar Produtos:  
Visualize todos os produtos com preços formatados em reais.

✔️ Editar Produto:  
Atualize nome, preço e quantidade de qualquer item.

✔️ Excluir Produto:  
Remova produtos indesejados.

---

🌱 Próximos Passos (Ideias de Melhorias)

- Exportação para outros formatos: JSON, Excel  
- Filtros de busca por nome, preço ou quantidade  
- Interface gráfica (Tkinter ou PyQt)  
- Validação de entrada mais robusta  
- Controle de estoque avançado

---

💬 Contribuições

Esse projeto foi feito como exercício de prática de Python, pandas e manipulação de CSV.  
Se quiser contribuir, fique à vontade para abrir um pull request ou me mandar um feedback! 😄

🚀 Divirta-se codando!
