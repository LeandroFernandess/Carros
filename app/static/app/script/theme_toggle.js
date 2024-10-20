// Adiciona um evento que será acionado quando o conteúdo do DOM for totalmente carregado
document.addEventListener('DOMContentLoaded', function () {

    // Recupera o tema atual do localStorage do navegador
    const theme = localStorage.getItem('theme');
    // Obtém a referência para o elemento body do documento
    const body = document.body;
    // Obtém o ícone que representa o tema, usando seu ID
    const themeIcon = document.getElementById('theme-icon');

    // Função que alterna o tema e o ícone 
    function toggleTheme() {
        // Adiciona ou remove a classe 'dark-mode' ao corpo
        body.classList.toggle('dark-mode');

        // Verifica se o modo escuro está ativo
        if (body.classList.contains('dark-mode')) {
            // Altera o ícone para o sol, indicando modo claro
            themeIcon.classList.replace('bi-moon-fill', 'bi-sun-fill');
            // Armazena 'dark' no localStorage para persistir o tema
            localStorage.setItem('theme', 'dark');
        } else {
            // Altera o ícone para a lua, indicando modo escuro
            themeIcon.classList.replace('bi-sun-fill', 'bi-moon-fill');
            // Armazena 'light' no localStorage para persistir o tema
            localStorage.setItem('theme', 'light');
        }
    }

    // Aplica o tema salvo anteriormente 
    if (theme === 'dark') {
        // Adiciona a classe 'dark-mode' para aplicar o tema escuro
        body.classList.add('dark-mode');
        // Define o ícone de acordo com o tema escuro
        themeIcon.classList.replace('bi-moon-fill', 'bi-sun-fill');
    }

    // Adiciona um listener de clique ao botão que alterna os temas
    document.getElementById('theme-toggle').addEventListener('click', toggleTheme);
});
