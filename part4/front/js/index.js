/*=========================================================================================================*/
/*============================================= FUNCTIONS =====================================================*/

import { checkAuthentication } from './checkAuth.js';


/* ================================ fetch places ================================*/
// Make a GET request to fetch places data
// Include the token in the Authorization header
// Handle the response and pass the data to displayPlaces function
export async function fetchPlaces(token) {
    const resp = await fetch('http://localhost:5000/api/v1/places/', {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer ' + token
        }
    });
    if (!resp.ok) {
        console.error('fetchPlaces error:', resp.status);
        return;
    }
    const places = await resp.json();
    console.log('Places fetched:', places);
    displayPlaces(places);
}

/* ================================= display places ====================================== */
function displayPlaces(places) {
    const placesList = document.getElementById('places-list');


    // --- S'assurer que la div existe
    if (!placesList) {
        console.error('Element #places-list not found in DOM');
        return;
    }


    // empty places-list
    placesList.innerHTML = "";

    // loop over places
    places.forEach(place => {
        //------------------------------------------ article --------------------------------------
        const article = document.createElement("article");
        article.classList.add("place-card");
        article.dataset.price = place.price;  // creates attribute data-price="X" to article in html file

        //............................ titre ...............................
        const title = document.createElement("h2");
        title.textContent = place.title;

        //............................ content .........................
        const contentDiv = document.createElement("div");
        contentDiv.classList.add("content");

        // image
        if (place.image_path) {
            const img = document.createElement("img");
            img.src = place.image_path;
            img.alt = "place image";
            img.classList.add("place-image");
            contentDiv.appendChild(img);
        }


        // description
        const descr = document.createElement("p");
        descr.textContent = place.description;
        contentDiv.appendChild(descr);


        // ............................ buttons ..........................
        const buttonsDiv = document.createElement("div");
        buttonsDiv.classList.add("buttons");

        // price
        const price = document.createElement("p");
        price.classList.add("price");
        price.textContent = `${place.price} $`;
        buttonsDiv.appendChild(price);

        // details-button
        const detailsBtn = document.createElement("button");
        detailsBtn.classList.add("details-button");
        detailsBtn.textContent = "View Details";
        detailsBtn.addEventListener('click', () => {
            window.location.href = `place.html?id=${place.id}`;
        });
        buttonsDiv.appendChild(detailsBtn);

        // ---------------------------- building the article -------------------------
        article.appendChild(title);
        article.appendChild(contentDiv);
        article.appendChild(buttonsDiv);

        // adding it to list of places
        placesList.appendChild(article);
    });
}


/* ==================================================================================================*/
/* =========================================== EXECUTION =========================================== */

document.addEventListener('DOMContentLoaded', () => {

    //verif auth and gets token
    const token = checkAuthentication();

    const placesList = document.getElementById('places-list');

    if (!token) {
        // "not logged in"
        const card = document.createElement('article');
        card.classList.add('place-card', 'not-logged-in-card'); // ajoute une classe spécifique

        const p = document.createElement('p');
        p.textContent = "I see you there. Join the party and the rest of the content will follow. ;)";
        p.classList.add('not-logged-in-text');
        card.appendChild(p);

        const img = document.createElement('img');
        img.src = 'images/Loom.jpg';
        img.alt = 'Loom inviting you to join the partey';
        img.classList.add('not-logged-in-img');
        card.appendChild(img);

        const loginBtn = document.createElement('button');
        loginBtn.textContent = 'Login';
        loginBtn.classList.add('not-logged-in-btn');
        loginBtn.addEventListener('click', () => {
            window.location.href = 'login.html';
        });
        card.appendChild(loginBtn);

        placesList.appendChild(card);
        return;
    }

    // Fetch places data if connected
    fetchPlaces(token);


    /* =================================== filter by price ===================================== */
    document.getElementById('price-filter').addEventListener('change', (event) => {
        // Get the selected price value
        const selected = event.target.value;

        // Iterate over the places and show/hide them based on the selected price
        const articles = document.querySelectorAll('#places-list .place-card');
        articles.forEach(article => {
            const price = Number(article.dataset.price);
            if (selected == 'all' || price <= Number(selected)) {
                article.style.display = 'block';
            } else {
                article.style.display = 'none';
            }
        })

    });
})
