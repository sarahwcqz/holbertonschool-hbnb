function playMusic(file, btn) {
    const player = document.getElementById('player');

    // pause if button clicked 2nd time
    if (player.src.endsWith(file) && !player.paused) {
        player.pause();
        btn.classList.remove('active');
        return;
    }

    // change source and play music
    player.src = file;
    player.play();

    // update active state of btn
    document.querySelectorAll('.jukebox-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
}
