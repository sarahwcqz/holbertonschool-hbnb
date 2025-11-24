/*=========================================================================================================*/
/*============================================= FUNCTIONS =====================================================*/

import { checkAuthentication } from './checkAuth.js';
import { getPlaceIdFromURL } from './IdFromURL.js';


/* ===================================fetch place details ==================================== */
async function fetchPlaceDetails(token, placeId) {
    // Make a GET request to fetch place details
    const response = await fetch(`http://localhost:5000/api/v1/places/${placeId}`, {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer ' + token
        }
    });
    if (!response.ok) {
        console.error('fetchPlaces error:', response.status);
        return;
    }
    const placeDetails = await response.json();
    // DEBUG
    console.log(placeDetails);
    displayPlaceDetails(placeDetails)
}


/* ======================================== display place's details ========================== */
function displayPlaceDetails(place) {
    const placeDetails = document.querySelector('.place-details');
    const reviewsSection = document.getElementById('reviews');

    // Clear previous content
    placeDetails.innerHTML = "";
    reviewsSection.innerHTML = "";

    /* --------------------------------------- PLACE ------------------------------- */
    /* ....................................... Title ............................... */
    const title = document.createElement('h1');
    title.classList.add("place-title");
    title.textContent = `✨ ${place.title} ✨`;


    /* ........................................ Image .............................. */
    const img = document.createElement('img');
    img.src = place.image_path;
    img.alt = "place image";
    img.classList.add('place-image');


    /* ....................................... Place info ........................... */
    const infoDiv = document.createElement('div');
    infoDiv.classList.add('place-info');

    const fullName = place.owner.first_name + " " + place.owner.last_name;
    const host = document.createElement('p');
    host.innerHTML = `<strong>Host:</strong> ${fullName}`;

    const price = document.createElement('p');
    price.innerHTML = `<strong>Price per night:</strong> ${place.price} $`;

    const descr = document.createElement('p');
    descr.innerHTML = `${place.description}`;

    const amenities = document.createElement('p');
    amenities.innerHTML = `<strong>What you'll find there:</strong>`;

    const list = document.createElement('ul');
    place.amenities.forEach(am => {
        const li = document.createElement('li');
        li.textContent = am.name;
        list.appendChild(li);
    });

    // Append info to infoDiv
    infoDiv.appendChild(host);
    infoDiv.appendChild(price);
    infoDiv.appendChild(descr);
    infoDiv.appendChild(amenities);
    infoDiv.appendChild(list);

    // Append title and infoDiv to main place details section
    placeDetails.appendChild(title);
    placeDetails.appendChild(img);
    placeDetails.appendChild(infoDiv);


    /* ------------------------------------- REVIEWS -------------------------------------- */
    const reviewsTitle = document.createElement('h2');
    reviewsTitle.textContent = "Reviews";
    reviewsSection.appendChild(reviewsTitle);

if (!place.reviews || place.reviews.length === 0) {
    // If no reviews container
    const noRevContainer = document.createElement('div');
    noRevContainer.classList.add('review-card');
    // Image
    const img = document.createElement('img');
    img.src = 'images/hidding-head.jpg';
    img.alt = "No reviews";
    img.classList.add('no-reviews-image');
    noRevContainer.appendChild(img);

    // Message
    const noRev = document.createElement('p');
    noRev.classList.add('no-review-comment');
    noRev.textContent = "No reviews yet...";
    noRevContainer.appendChild(noRev);

    reviewsSection.appendChild(noRevContainer);

    } else {
        place.reviews.forEach(rev => {
            const card = document.createElement('article');
            card.classList.add('review-card');

            const topRow = document.createElement('div');
            topRow.classList.add('top-row');

            const user = document.createElement('h3');
            user.classList.add('review-user');
            user.textContent = `👁️ ${rev.user.first_name} ${rev.user.last_name}`;

            const ratingEmojis = {
                1: "💀",
                2: "🤮",
                3: "🫠",
                4: "🤡",
                5: "✨"
            };

            const rating = document.createElement('p');
            const ratingValue = Number(rev.rating);
            rating.classList.add('review-rating');
            rating.textContent = `Rating: ${ratingEmojis[ratingValue] || rev.rating}`;


            topRow.appendChild(user);
            topRow.appendChild(rating);

            const comment = document.createElement('p');
            comment.classList.add('review-comment');
            comment.textContent = rev.text;

            card.appendChild(topRow);
            card.appendChild(comment);

            reviewsSection.appendChild(card);
        });
    }
}


/* ==================================================================================================*/
/* =========================================== EXECUTION =========================================== */

document.addEventListener('DOMContentLoaded', () => {

    const token = checkAuthentication();
    // DEBUG
    console.log("Token:", token);

    const placeId = getPlaceIdFromURL();
    //DEBUG
    console.log("Place ID:", placeId);

    const addReview = document.getElementById('add-review');
    const addReviewBtn = document.getElementById('add-review-btn');

    fetchPlaceDetails(token, placeId);

    // If the user is authenticated, display the add review form
    if (!token) {
        addReview.style.display = 'none';
    } else {
        addReview.style.display = 'block';
    }

    addReviewBtn.addEventListener('click', () => {
        window.location.href = `add_review.html?id=${placeId}`;
    });

})