const togglePassword = document.querySelector("#togglePassword");
const password = document.querySelector("#password");
const eyeIcon = document.querySelector("#eyeIcon");

togglePassword.addEventListener("click", function (e) {
  // Toggle the type attribute
  const type =
    password.getAttribute("type") === "password" ? "text" : "password";
  password.setAttribute("type", type);

  // Toggle the eye icon
  eyeIcon.setAttribute(
    "d",
    type === "password"
      ? "M10 3C6 3 2.73 5.11 1.14 8.25a1 1 0 000 .77C2.73 12.89 6 15 10 15c4 0 7.27-2.11 8.86-5.25a1 1 0 000-.77C17.27 5.11 14 3 10 3zM10 13a3 3 0 110-6 3 3 0 010 6zm0-4a1 1 0 100 2 1 1 0 000-2z"
      : "M10 3C6 3 2.73 5.11 1.14 8.25a1 1 0 000 .77C2.73 12.89 6 15 10 15c4 0 7.27-2.11 8.86-5.25a1 1 0 000-.77C17.27 5.11 14 3 10 3zM10 13a3 3 0 110-6 3 3 0 010 6zm0-4a1 1 0 100 2 1 1 0 000-2z"
  );
});
