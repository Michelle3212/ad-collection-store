document.addEventListener("DOMContentLoaded", () => {
  const searchInput = document.getElementById("product-search");
  const filterButtons = [...document.querySelectorAll(".filter-button")];
  const cards = [...document.querySelectorAll(".product-card")];
  const noResults = document.getElementById("no-results");
  let activeCategory = "All";

  function updateProducts() {
    const searchTerm = searchInput.value.trim().toLowerCase();
    let visibleCount = 0;

    cards.forEach((card) => {
      const matchesSearch = card.dataset.name.includes(searchTerm);
      const matchesCategory =
        activeCategory === "All" || card.dataset.category === activeCategory;
      const show = matchesSearch && matchesCategory;
      card.hidden = !show;
      if (show) visibleCount += 1;
    });

    noResults.hidden = visibleCount !== 0;
  }

  searchInput.addEventListener("input", updateProducts);

  filterButtons.forEach((button) => {
    button.addEventListener("click", () => {
      activeCategory = button.dataset.category;
      filterButtons.forEach((item) => item.classList.toggle("active", item === button));
      updateProducts();
    });
  });

  document.getElementById("year").textContent = new Date().getFullYear();
});
