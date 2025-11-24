/*=========================================================================================================*/
/*============================================= FUNCTIONS =====================================================*/

/* =========================== loginUser ======================= */
async function loginUser(email, password) {
    const response = await fetch('http://localhost:5000/api/v1/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
    });

    console.log('Response status:', response.status);
    const text = await response.text();
    console.log('Response body:', text);

    if (response.ok) {
        const data = JSON.parse(text);
        return data.access_token;
    } else {
        throw new Error('Login failed: ' + response.status + ' - ' + text);
    }
}


/* ==================================================================================================*/
/* =========================================== EXECUTION =========================================== */


document.addEventListener('DOMContentLoaded', () => {


    /* ======================================= handle login form ==========================================*/
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

});
