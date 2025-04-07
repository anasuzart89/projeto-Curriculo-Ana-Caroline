document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('formContato');
  const mensagemContato = document.getElementById('mensagemContato');

  form.addEventListener('submit', function(e) {
    e.preventDefault();

    const nome = document.getElementById('nome').value.trim();
    const email = document.getElementById('email').value.trim();
    const mensagem = document.getElementById('mensagem').value.trim();

    if (!nome || !email || !mensagem) {
      mensagemContato.textContent = 'Por favor, preencha todos os campos.';
      mensagemContato.style.color = 'deeppink';
    } else {
      mensagemContato.textContent = `Obrigada, ${nome}! Sua mensagem foi enviada com sucesso.`;
      mensagemContato.style.color = 'hotpink';
      form.reset();
    }

    mensagemContato.style.opacity = '1';

    setTimeout(() => {
      mensagemContato.style.opacity = '0';
    }, 3000);
  });
});
