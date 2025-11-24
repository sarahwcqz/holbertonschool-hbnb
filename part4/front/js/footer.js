document.addEventListener('DOMContentLoaded', () => {


    /* ======================================================================================= */
    /* ========================================== FOOTER ===================================== */
    /* ======================================================================================= */


    /* ========================================== JUKEBOX =============================== */
    const player = document.getElementById('player');
    const buttons = document.querySelectorAll('.jukebox-btn');

    function playMusic(src, btn) {
        // Si même son → pause
        if (player.src.includes(src) && !player.paused) {
            player.pause();
            btn.classList.remove('active');
            return;
        }

        // Mettre à jour le visuel des boutons
        buttons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        // Charger et jouer la musique
        player.src = src;
        player.play();
    }
})