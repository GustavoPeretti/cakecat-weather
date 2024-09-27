// Referências aos elementos
const conceitoForm = document.getElementById('conceitoForm');
const tituloInput = document.getElementById('titulo');
const conceitoInput = document.getElementById('conceito');
const colorPicker = document.getElementById('colorPicker');
const conceitosCadastrados = document.getElementById('conceitosCadastrados');
const conceitoModal = document.getElementById('modalConceito'); // Renomeado para conceitoModal
const modalTitulo = document.getElementById('modalTitulo');
const modalDescricao = document.getElementById('modalDescricao');
const modalCor = document.getElementById('modalCor');
const spanClose = document.getElementsByClassName('close')[0];

// Função para fechar o modal
spanClose.onclick = function() {
    conceitoModal.style.display = "none"; // Fechar o modal
}

window.onclick = function(event) {
    if (event.target === conceitoModal) {
        conceitoModal.style.display = "none"; // Fechar modal se clicar fora
    }
}

// Função para adicionar novo conceito
conceitoForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Evita o envio padrão do formulário

    // Pegar valores dos inputs
    const titulo = tituloInput.value;
    const conceito = conceitoInput.value;
    const cor = colorPicker.value;

    // Criar novo item de conceito na lista
    const novoConceito = document.createElement('li');
    novoConceito.className = 'itens-lista-administracao';

    // Adicionar conteúdo ao novo item
    novoConceito.innerHTML = `
        ${titulo}
        <div>
            <button class="icones-administracao"><span class="material-symbols-outlined">person_remove</span></button>
            <button class="icones-administracao"><span class="material-symbols-outlined">edit</span></button>
            <button class="icones-administracao verDetalhes"><span class="material-symbols-outlined">visibility</span></button>
        </div>
    `;

    // Adicionar evento ao botão de visualizar (ícone "visibility")
    novoConceito.querySelector('.verDetalhes').addEventListener('click', function() {
        conceitoModal.style.display = "block";  // Exibe o modal
        modalTitulo.textContent = titulo;  // Define o título no modal
        modalDescricao.textContent = conceito;  // Define a descrição no modal
        modalCor.textContent = cor;  // Mostra a cor escolhida
        modalCor.style.backgroundColor = cor;  // Aplica a cor ao texto
    });

    // Adicionar o novo conceito à lista
    conceitosCadastrados.appendChild(novoConceito);

    // Limpar o formulário
    conceitoForm.reset();
});
