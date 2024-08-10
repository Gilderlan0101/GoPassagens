function mostra_senha() {
    var inputpass = document.getElementById('senha');
    var showpassword = document.getElementById('mostra_senha');

    if (inputpass.type === 'password') {
        inputpass.setAttribute('type', 'text');
        showpassword.classList.replace('bi-eye-fill', 'bi-eye-slash-fill');
    } else {
        inputpass.setAttribute('type', 'password');
        showpassword.classList.replace('bi-eye-slash-fill', 'bi-eye-fill');
    }
}
