# Sistema de Gerenciamento de Produtos 

Este projeto é um **CRUD de produtos** para uma loja de informática, desenvolvido em **Streamlit** com dados armazenados em memória (lista Python). Não há persistência em banco de dados ou arquivo.

---

## 📂 Estrutura de Pastas

```plaintext
Gerenciamento/
├── .venv/
├── README.md
├── db.py
├── requirements.txt
└── pages/
    ├── Cadastrar_Produto.py
    └── Listar_Produtos.py
```

* **db.py**: contém a lista global `produtos = []`.
* **requirements.txt**: lista de dependências do projeto.
* **pages/**: scripts que o Streamlit reconhece como páginas:

  * **Cadastrar\_Produto.py**: formulário para cadastro de produtos.
  * **Listar\_Produtos.py**: exibição de tabela com os produtos cadastrados.

---

## 🚀 Pré-requisitos

* Python 3.7 ou superior
* Pip
* (Opcional) Ambiente virtual

---

## ⚙️ Instalação e Execução

1. **Clone ou baixe** este repositório e navegue até a pasta:

   ```bash
   cd Gerenciamento
   ```

2. **(Opcional) Crie e ative** um ambiente virtual:

   ```bash
   python -m venv .venv

   # Windows:
   .venv\Scripts\activate

   # Linux/Mac:
   source .venv/bin/activate
   ```

3. **Instale** as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute** a aplicação:

   * Para **cadastrar** um produto:

     ```bash
     streamlit run pages/Cadastrar_Produto.py
     ```

   * Para **listar** os produtos:

     ```bash
     streamlit run pages/Listar_Produtos.py
     ```

> **Observação:** como não há navegação central, cada página roda separadamente.

---

## 📝 Uso

* **Cadastrar Produto**: Informe nome, preço (use vírgula ou ponto como separador decimal) e quantidade. Ao submeter, o produto fica disponível na lista em memória.

* **Listar Produtos**: Exibe todos os produtos cadastrados em memória com formatação de preço em Real (R\$).

---

## 🔧 Customização

* Para **adicionar categorias** ou campos, edite o formulário em `pages/Cadastrar_Produto.py`.
* Para **manter dados** entre reinícios, implemente persistência em CSV, JSON ou banco de dados.

---

## 📞 Suporte

Qualquer dúvida ou sugestão, abra uma issue ou entre em contato.

---

**Desenvolvido por Nayara.**
