/*=========================================================================================================*/
/*============================================= FUNCTIONS =====================================================*/

import { checkAuthentication } from './checkAuth.js';
import { getPlaceIdFromURL } from './IdFromURL.js';



/* ==================================================================================================*/
/* =========================================== EXECUTION =========================================== */

document.addEventListener('DOMContentLoaded', () => {

    //verif auth and gets token
    const token = checkAuthentication();

    //get place_id
    const placeId = getPlaceIdFromURL();


    if (!token) {
        document.getElementById('review-form').style.display = 'none';
        document.getElementById('not-logged-in').style.display = 'block';
    }

    const review = document.getElementById('review-form');

    review.addEventListener('submit', async (event) => {
        event.preventDefault();

        const comment = document.getElementById('review').value;
        const rating = document.getElementById('rating').value;

        // DEBUG===================================================
        console.log("Submitting review", { comment, rating });
        console.log('Token from checkAuthentication:', token);
        console.log('place id from getPlaceIdFrom URL:', placeId)

        const payload = {
            text: comment,
            rating: parseInt(rating),
            place_id: placeId
        };

        try {
            const resp = await fetch('http://localhost:5000/api/v1/reviews', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token
                },
                body: JSON.stringify(payload)
            });

            const data = await resp.json();

            if (!resp.ok) {
                console.error(data);
                alert("Error: " + data.error);
                return;
            }

            alert("Review created!");
            window.location.href = `place.html?id=${placeId}`;
        } catch (err) {
            console.error(err);
            alert("Network error");
        }
    });
})