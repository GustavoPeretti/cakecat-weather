
const modal = document.getElementById("adminModal");
const openModalBtn = document.getElementById("openModalBtn");
const closeModalBtn = document.getElementsByClassName("close")[0];
const form = document.getElementById("adminForm");
const adminList = document.getElementById("adminList");

openModalBtn.onclick = function() {
  modal.style.display = "block"; 
}

closeModalBtn.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none"; 
  }
}

form.onsubmit = function(event) {
  event.preventDefault(); 

  const username = document.getElementById("username").value;

  if (username) {
    const li = document.createElement("li");
    li.className = "itens-lista-administracao";
    li.innerHTML = `
      ${username}
      <div>
          <button class="icones-administracao"><span class="material-symbols-outlined">person_remove</span></button>
          <button class="icones-administracao"><span class="material-symbols-outlined">edit</span></button>
      </div>
    `;

    adminList.appendChild(li);

    modal.style.display = "none";

    form.reset();
  }
}
