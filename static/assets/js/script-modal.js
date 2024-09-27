// Pega os elementos do DOM
const modal = document.getElementById("adminModal");
const openModalBtn = document.getElementById("openModalBtn");
const closeModalBtn = document.getElementsByClassName("close")[0];
const form = document.getElementById("adminForm");
const adminList = document.getElementById("adminList");

// Função para abrir o modal
openModalBtn.onclick = function() {
  modal.style.display = "block"; // Abre o modal
}

// Função para fechar o modal ao clicar no "x"
closeModalBtn.onclick = function() {
  modal.style.display = "none"; // Fecha o modal
}

// Função para fechar o modal ao clicar fora do conteúdo do modal
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none"; // Fecha o modal
  }
}

// Função para adicionar o novo administrador
form.onsubmit = function(event) {
  event.preventDefault(); // Evita o envio do formulário

  const username = document.getElementById("username").value; // Pega o valor do campo de nome de usuário

  if (username) {
    // Cria o novo item da lista
    const li = document.createElement("li");
    li.className = "itens-lista-administracao";
    li.innerHTML = `
      ${username}
      <div>
          <button class="icones-administracao"><span class="material-symbols-outlined">person_remove</span></button>
          <button class="icones-administracao"><span class="material-symbols-outlined">edit</span></button>
          <button class="icones-administracao"><span class="material-symbols-outlined">visibility</span></button>
      </div>
    `;

    // Adiciona o novo item à lista de administradores
    adminList.appendChild(li);

    // Fecha o modal
    modal.style.display = "none";

    // Limpa os campos do formulário
    form.reset();
  }
}
