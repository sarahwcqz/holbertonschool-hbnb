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

            if (wasPlaying) player.play().catch(() => {});
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
    // Change source only if new file
    if (player.src.includes(file) === false) {
        player.src = file;
        localStorage.setItem("jukebox-track", file);
        localStorage.setItem("jukebox-time", 0);
    }

    // Play
    player.play();

    // Save play state
    localStorage.setItem("jukebox-playing", true);
}
