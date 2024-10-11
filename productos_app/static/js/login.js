document.addEventListener("DOMContentLoaded", function () {
  const togglePassword = document.querySelector('#togglePassword');
  const passwordField = document.querySelector('#{{ form.password.id_for_label }}');
  const eyeIcon = document.querySelector('#eyeIcon');

  togglePassword.addEventListener('click', function () {
      // Alternar el tipo de input entre password y text
      const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
      passwordField.setAttribute('type', type);

      // Alternar el ícono del ojo (opcional)
      if (type === 'password') {
          eyeIcon.setAttribute('d', 'M10 3C6.13 3 2.61 5.92 1 9.5c1.61 3.58 5.13 6.5 9 6.5s7.39-2.92 9-6.5C17.39 5.92 13.87 3 10 3zM10 12c-1.11 0-2-.89-2-2s.89-2 2-2 2 .89 2 2-.89 2-2 2zm0-10C6.13 2 2.61 4.92 1 8.5c1.61 3.58 5.13 6.5 9 6.5s7.39-2.92 9-6.5C17.39 4.92 13.87 2 10 2z');
      } else {
          eyeIcon.setAttribute('d', 'M10 3C6.13 3 2.61 5.92 1 9.5c1.61 3.58 5.13 6.5 9 6.5s7.39-2.92 9-6.5C17.39 5.92 13.87 3 10 3zM10 12c-1.11 0-2-.89-2-2s.89-2 2-2 2 .89 2 2-.89 2-2 2zM1 9.5c1.61 3.58 5.13 6.5 9 6.5s7.39-2.92 9-6.5c-1.61-3.58-5.13-6.5-9-6.5S2.61 5.92 1 9.5z');
      }
  });
});
