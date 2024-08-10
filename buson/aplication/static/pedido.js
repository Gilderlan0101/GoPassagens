document.addEventListener('DOMContentLoaded', () => {
    const emailOption = document.getElementById('emailOption');
    const documentoOption = document.getElementById('documentoOption');
    const extraFieldContainer = document.getElementById('extraFieldContainer');

    function updateExtraField() {
        extraFieldContainer.innerHTML = ''; // Limpa o conteúdo atual

        if (emailOption.checked) {
            extraFieldContainer.innerHTML = `
                <label for="emailInput">E-mail</label>
                <input type="email" name="email" id="emailInput" placeholder="example@example.com">
            `;
        } else if (documentoOption.checked) {
            extraFieldContainer.innerHTML = `
                <label for="cpfInput">CPF</label>
                <input type="text" name="cpf" id="cpfInput" placeholder="___.___.___-__">
            `;
        }
    }

    emailOption.addEventListener('change', updateExtraField);
    documentoOption.addEventListener('change', updateExtraField);
});
