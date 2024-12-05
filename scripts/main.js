// Toggle and responsive nav
const navSlide = () => {
    const burger = document.querySelector(".burger");
    const navLists = document.querySelector("nav");

    burger.addEventListener("click", () => {
        navLists.classList.toggle("nav-active");
        burger.classList.toggle("toggle-burger");
    });
};

navSlide();

// Theme Switch
const themeToggle = document.getElementById('theme-toggle');
const root = document.documentElement;

themeToggle.addEventListener('change', () => {
  if (themeToggle.checked) {
    // Dark theme
    root.style.setProperty('--primaryTextColor', '#fff');
    root.style.setProperty('--secondaryTextColor', '#f1f1f1');
    root.style.setProperty('--borderColor', '#f1f1f1');
    root.style.setProperty('--lineColor', '#d9d9d9');
    root.style.setProperty('--primaryBackgroundColor', '#000');
    root.style.setProperty('--secondaryBackgroundColor', '#121212');
    root.style.setProperty('--thirdBackgroundColor', '#f5f3fe');
    root.style.setProperty('--primaryIconColor', '#BB86FC');
    root.style.setProperty('--primaryIconColorHover', '#3700B3');
    root.style.setProperty('--secondaryIconColor', '#03DAC6');
  } else {
    // Light theme
    root.style.setProperty('--primaryTextColor', '#232e35');
    root.style.setProperty('--secondaryTextColor', '#656d72');
    root.style.setProperty('--borderColor', '#f1f1f1');
    root.style.setProperty('--lineColor', '#d9d9d9');
    root.style.setProperty('--primaryBackgroundColor', '#fff');
    root.style.setProperty('--secondaryBackgroundColor', '#fbfbfb');
    root.style.setProperty('--thirdBackgroundColor', '#f5f3fe');
    root.style.setProperty('--primaryIconColor', '#7e74f1');
    root.style.setProperty('--primaryIconColorHover', '#5d51e8');
    root.style.setProperty('--secondaryIconColor', '#03DAC6');
  }
});
