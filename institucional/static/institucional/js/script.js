
const menuButton = document.getElementById("menu-button");
const mobileMenu = document.getElementById("mobile-menu");

menuButton.addEventListener("click", () => {
    const isHidden = mobileMenu.classList.toggle("hidden");

    menuButton.setAttribute("aria-expanded", String(!isHidden));
});

document.querySelectorAll("#mobile-menu a").forEach(link => {
    link.addEventListener("click", () => {
        mobileMenu.classList.add("hidden");
        menuButton.setAttribute("aria-expanded", "false");
    });
});

document.getElementById("ano").textContent =
    new Date().getFullYear();