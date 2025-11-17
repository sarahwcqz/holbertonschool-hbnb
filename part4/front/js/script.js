document.addEventListener('DOMContentLoaded', () => {

    /*============================================= LOGIN =====================================================*/

    /* ------------------------- handle form -------------------------*/
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            console.log('JS submit caught'); //test, to remove

            //Get values from form
            const email = loginForm.elements['email'].value.trim();
            const password = loginForm.elements['password'].value.trim();

            //Validation not empty
            if (!email || !password) {
                alert('Dude you need to fill in both email and password...');
                return;
            }

            // Email format validation
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email)) {
                alert('Doll it needs to be a valid email.');
                return;
            }

            /* ------------------------ cookie + redir ------------------------*/
            // avoids redir if login fails
            try {
                const token = await loginUser(email, password);
                document.cookie = `token=${token}; path=/; secure; samesite=strict`;
                window.location.href = 'index.html';
            } catch (error) {
                alert(error.message);
            }


        });
    }

    /* ---------------------- AJAX request -------------------*/
    async function loginUser(email, password) {
        const response = await fetch('http://localhost:5000/api/v1/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        if (response.ok) {
            const data = await response.json();
            return data.access_token;
        } else {
            throw new Error('Login failed: ' + response.statusText);
        }
    }










    /*----------------------------- JUKEBOX ------------------------------*/
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

});
