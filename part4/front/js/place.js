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
        console.error('fetchPlaces error:', resp.status);
        return;
    }
    const placeDetails = await response.json();
    displayPlaceDetails(placeDetails)
}


/* ======================================== display place's details ========================== */
function displayPlaceDetails(place) {
    const placeDetails = document.querySelector('.place-details');
    // Clear the current content of the place details section
    placeDetails.innerHTML = "";

    // Create elements to display the place details (name, description, price, amenities and reviews)
    /* --------------------------- title ------------------------------ */
    const title = document.createElement('h1');
    title.classList.add("place-title");
    title.textContent = place.title;

    /* -------------------------------------- place-info --------------------------------- */
    const infoDiv = document.createElement('div');
    infoDiv.classList.add('place-info');

    /*....................................... host ....................................... */
    const fullName = place.owner.first_name + " " + place.owner.last_name;
    const host = document.createElement('p');
    host.innerHTML = `<strong>Host :</strong> ${fullName}`;

    /* ....................................... price ...................................... */
    const price = document.createElement('p');
    price.innerHTML = `<strong>Price per night :</strong> ${place.price} $`;

    /* ....................................... description ................................ */
    const descr = document.createElement('p');
    descr.innerHTML = `<strong>Description :</strong> ${place.description}`;

    /* ........................................ amenities ................................. */
    const amenities = document.createElement('p');
    amenities.innerHTML = `<strong>Amenities :</strong>`;

    const list = document.createElement('ul');
    place.amenities.forEach(am => {
        const li = document.createElement('li');
        li.textContent = am.name;
        list.appendChild(li);
    });


    /* --------------------------- reviews ------------------------------                       <= to be implemented (verif names)
    reviewsSection.classList.add("reviews-section");

    const reviewsTitle = document.createElement('h2');
    reviewsTitle.textContent = "Reviews";
    reviewsSection.appendChild(reviewsTitle);

    if (place.reviews.length === 0) {
        const noRev = document.createElement('p');
        noRev.textContent = "No reviews yet.";
        reviewsSection.appendChild(noRev);
    } else {
        place.reviews.forEach(rev => {
            const card = document.createElement('article');
            card.classList.add('review-card');

            const user = document.createElement('p');
            user.innerHTML = `<strong>User :</strong> ${rev.user.first_name} ${rev.user.last_name}`;

            const rating = document.createElement('p');
            rating.innerHTML = `<strong>Rating :</strong> ${rev.rating}`;

            const comment = document.createElement('p');
            comment.innerHTML = `<strong>Comment :</strong> ${rev.comment}`;

            card.appendChild(user);
            card.appendChild(rating);
            card.appendChild(comment);

            reviewsSection.appendChild(card);
        });  */

    // Append the created elements to the place details section
    infoDiv.appendChild(host);
    infoDiv.appendChild(price);
    infoDiv.appendChild(descr);
    infoDiv.appendChild(amenities);
    infoDiv.appendChild(list);

    placeDetails.appendChild(title);
    placeDetails.appendChild(infoDiv);
    /*
    placeDetails.appendChild(reviewsSection);                            <= to be implemented */

}

/* ==================================================================================================*/
/* =========================================== EXECUTION =========================================== */

document.addEventListener('DOMContentLoaded', () => {

    const token = checkAuthentication();

    const placeId = getPlaceIdFromURL();

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