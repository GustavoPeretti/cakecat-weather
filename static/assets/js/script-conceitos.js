
// const conceitoForm = document.getElementById('conceitoForm');
// const tituloInput = document.getElementById('titulo');
// const conceitoInput = document.getElementById('conceito');
// const colorPicker = document.getElementById('colorPicker');
// const conceitosCadastrados = document.getElementById('conceitosCadastrados');
// const conceitoModal = document.getElementById('modalConceito');
// const modalTitulo = document.getElementById('modalTitulo');
// const modalDescricao = document.getElementById('modalDescricao');
// const modalCor = document.getElementById('modalCor');
// const spanClose = document.getElementsByClassName('close')[0];

// spanClose.onclick = function() {
//     conceitoModal.style.display = "none";
// }

// window.onclick = function(event) {
//     if (event.target === conceitoModal) {
//         conceitoModal.style.display = "none";
//     }
// }

// conceitoForm.addEventListener('submit', function(event) {
//     event.preventDefault(); 

//     const titulo = tituloInput.value;
//     const conceito = conceitoInput.value;
//     const cor = colorPicker.value;

//     const novoConceito = document.createElement('li');
//     novoConceito.className = 'itens-lista-administracao';

//     novoConceito.innerHTML = `
//         ${titulo}
//         <div>
//             <button class="icones-administracao"><span class="material-symbols-outlined">person_remove</span></button>
//             <button class="icones-administracao"><span class="material-symbols-outlined">edit</span></button>
//             <button class="icones-administracao verDetalhes"><span class="material-symbols-outlined">visibility</span></button>
//         </div>
//     `;

//     novoConceito.querySelector('.verDetalhes').addEventListener('click', function() {
//         conceitoModal.style.display = "block";  
//         modalTitulo.textContent = titulo; 
//         modalDescricao.textContent = conceito;  
//         modalCor.textContent = cor;  
//         modalCor.style.backgroundColor = cor;  
//     });


//     conceitosCadastrados.appendChild(novoConceito);

//     conceitoForm.reset();
// });
