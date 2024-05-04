// Función para añadir producto a favoritos
function addToFavorites(product) {
    // Obtén los favoritos actuales
    let favorites = JSON.parse(localStorage.getItem('favorites')) || [];

    // Verifica si el producto ya está en favoritos
    if (!favorites.some(fav => fav.id == product.id)) {
        favorites.push(product);
        localStorage.setItem('favorites', JSON.stringify(favorites));
    }
}

// Función para inicializar los botones
function initializeFavButtons() {
    let favorites = JSON.parse(localStorage.getItem('favorites')) || [];

    // Obtiene todos los botones de favoritos
    const favButtons = document.querySelectorAll('.fav-btn');

    favButtons.forEach(button => {
        const product = JSON.parse(button.dataset.producto);

        // Verifica si el producto ya está en favoritos
        if (favorites.some(fav => fav.id == product.id)) {
            button.disabled = true;
            button.innerText = 'Ya en favoritos';
        }

        button.addEventListener('click', () => {
            addToFavorites(product);
            button.disabled = true;
            button.innerText = 'Ya en favoritos';
        });
    });
}



// Inicializa los botones al cargar la página
document.addEventListener('DOMContentLoaded', initializeFavButtons);