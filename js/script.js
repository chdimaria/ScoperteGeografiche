const navToggle = document.querySelector(".nav-toggle");
const mainNav = document.querySelector(".main-nav");

if (navToggle && mainNav) {
  navToggle.addEventListener("click", () => {
    const isOpen = mainNav.classList.toggle("open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
  });
}

const themeToggle = document.querySelector(".theme-toggle");
const savedTheme = localStorage.getItem("sitostoria-theme");

if (savedTheme === "dark") {
  document.documentElement.dataset.theme = "dark";
}

if (themeToggle) {
  themeToggle.addEventListener("click", () => {
    const isDark = document.documentElement.dataset.theme === "dark";
    if (isDark) {
      delete document.documentElement.dataset.theme;
      localStorage.setItem("sitostoria-theme", "light");
    } else {
      document.documentElement.dataset.theme = "dark";
      localStorage.setItem("sitostoria-theme", "dark");
    }
  });
}

const progressBar = document.querySelector(".progress-bar");

window.addEventListener("scroll", () => {
  const scrollTop = window.scrollY;
  const docHeight = document.documentElement.scrollHeight - window.innerHeight;
  const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
  if (progressBar) progressBar.style.width = `${progress}%`;
});

document.querySelectorAll("[data-quiz]").forEach((quiz) => {
  const feedback = quiz.parentElement.querySelector(".quiz-feedback");

  quiz.querySelectorAll("button").forEach((button) => {
    button.addEventListener("click", () => {
      const correct = button.dataset.correct === "true";
      feedback.textContent = correct
        ? "Risposta corretta: Colombo cercava una rotta occidentale verso l’Asia."
        : "Non proprio: l’obiettivo iniziale era raggiungere l’Asia navigando verso ovest.";
      feedback.style.color = correct ? "var(--accent)" : "var(--brand)";
    });
  });
});

document.querySelectorAll("[data-timeline]").forEach((timeline) => {
  const buttons = timeline.querySelectorAll(".timeline-item");
  const panels = document.querySelectorAll(".timeline-panel");

  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      buttons.forEach((item) => item.classList.remove("active"));
      panels.forEach((panel) => panel.classList.remove("active"));

      button.classList.add("active");
      const panel = document.getElementById(button.dataset.panel);
      if (panel) panel.classList.add("active");
    });
  });
});

document.querySelectorAll("[data-accordion]").forEach((accordion) => {
  accordion.querySelectorAll("button").forEach((button) => {
    button.addEventListener("click", () => {
      const expanded = button.getAttribute("aria-expanded") === "true";
      button.setAttribute("aria-expanded", String(!expanded));
    });
  });
});
