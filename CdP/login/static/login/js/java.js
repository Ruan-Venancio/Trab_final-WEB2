function cadastrarPix() {
    // Obtém os valores dos campos
    var email = document.getElementById('email').value;
    var celular = document.getElementById('celular').value;
    var cpf = document.getElementById('cpf').value;

    // Verifica se pelo menos dois dos três campos foram preenchidos
    if ((email && celular) || (email && cpf) || (celular && cpf)) {
        alert("Chave PIX cadastrada com sucesso!");

        window.location.href = 'concluido.html';

    } else {
        alert("Preencha pelo menos dois dos três campos: E-mail, Celular ou CPF.");
    }
}