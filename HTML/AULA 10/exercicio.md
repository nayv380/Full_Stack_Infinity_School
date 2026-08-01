# Gerenciamento de Clientes.

a. Faça um formulário no HTML para armazenar dados de clientes, o formulário deve conter os campos: "nome", "email", "telefone", "dataNascimento"

b. Crie um "eventListener" no Javascript para o evento de submit desse formulário, você deve criar um objeto "cliente" com os dados que foram preenchidos no formulário e mostrar utilizando o "console.log"

c. Adicione validações no formulário para mostrar mensagens de error caso algum dos campos "nome", "email", "telefone", "dataNascimento" não sejam preenchido. Exemplo: "O campo nome é obrigatório"

```javascript
function mostrarMensagem(text, type) {
  const pMensagem = document.getElementById("mensagem");

  pMensagem.innerText = text;

  pMensagem.style.fontWeight = "bold";
  pMensagem.style.color = type == "success" ? "green" : "red";
}
```
