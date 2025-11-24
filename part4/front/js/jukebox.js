// ================== GLOBAL PLAYER ==================
const player = document.getElementById("player");

// ================== LOAD SAVED STATE ==================
window.addEventListener("DOMContentLoaded", () => {
    const savedTrack = localStorage.getItem("jukebox-track");
    const savedTime = localStorage.getItem("jukebox-time");
    const wasPlaying = localStorage.getItem("jukebox-playing") === "true";

    if (savedTrack) {
        player.src = savedTrack;

        player.addEventListener("loadedmetadata", () => {
            if (savedTime) player.currentTime = parseFloat(savedTime);

            if (wasPlaying) player.play().catch(() => { });
        });
    }
});

// ================== SAVE ON EXIT ==================
window.addEventListener("beforeunload", () => {
    localStorage.setItem("jukebox-time", player.currentTime);
    localStorage.setItem("jukebox-playing", !player.paused);
});

// ================== PLAY MUSIC ==================
function playMusic(file, btn) {
    const isSameTrack = player.src.endsWith(file);

    // Same track: toggle play/pause
    if (isSameTrack) {
        if (player.paused) {
            player.play();
            localStorage.setItem("jukebox-playing", true);
        } else {
            player.pause();
            localStorage.setItem("jukebox-playing", false);
        }
        return;
    }

    // New track: load & play
    player.src = file;
    localStorage.setItem("jukebox-track", file);
    localStorage.setItem("jukebox-time", 0);

    player.play();
    localStorage.setItem("jukebox-playing", true);
}

