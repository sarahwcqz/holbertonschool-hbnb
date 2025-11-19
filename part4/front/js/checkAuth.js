/*=========================================================================================================*/
/*============================================= FUNCTIONS =====================================================*/


/* ================================= check user authentication ====================================== */
export function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.querySelector('.login-button');
    const logoutLink = document.querySelector('.logout-button');

    // display login-link only if user not connected 
    if (!token) {
        loginLink.style.display = 'block';
        logoutLink.style.display = 'none';
    } else {
        loginLink.style.display = 'none';
        logoutLink.style.display = 'block';
    }

    

    // logout handle
    if (logoutLink) {
        logoutLink.addEventListener('click', (e) => {
            e.preventDefault();
            // suppress cookie
            document.cookie = 'token=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT';

            window.location.reload();
        });
    }

    return token
}

/* =========================================getCookie ===============================================*/
// Function to get a cookie value by its name
export function getCookie(name) {
    return document.cookie
        .split("; ")
        .find((row) => row.startsWith(name + "="))  // finds the right pair
        ?.split("=")[1];    //returns the value or undefined ifnt found
    // ?. => avoid exception if find returns undefined, then the whole value becomes undefined
    // we split the result w/ =
    // take element [1] => the value
}


/* ==================================================================================================*/
/* =========================================== EXECUTION =========================================== */



