from flask_restx import Namespace, Resource, fields
from app.services import facade
from app.api.v1.users import user_model
from app.api.v1.amenities import amenity_model
api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'owner': fields.Nested(user_model, description='Owner of the place'),
    'amenities': fields.List(fields.Nested(amenity_model), description='List of amenities'),
    'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(404, 'Place not found')
    @api.response(404, 'User not found')
    def post(self):
        """Register a new review"""
        review_data = api.payload
        place = facade.get_place(review_data.get("place_id"))
        if not place:
            return {"error": "Place not found"}, 404
        review_owner = facade.get_user(review_data.get("user_id"))
        if not review_owner:
            return {"error": "User not found"}, 404
        try:
            new_review = facade.create_review(review_data)
        except:
            return {"error": "Invalid input data"}, 400
        place.add_review(new_review)
        return {'id': new_review.id, 'text': new_review.text, 'rating': new_review.rating, 'user_id': new_review.user_id, 'place_id': new_review.place_id}, 201

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        all_review = facade.get_all_reviews()
        return [
            {
                "id": all_review_items.id,
                "text": all_review_items.text,
                "rating": all_review_items.rating
            }
            for all_review_items in all_review
        ], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        return {'id': review.id, 'text': review.text, 'rating': review.rating, 'user_id': review.user_id, 'place_id': review.place_id}, 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        review_inDB = facade.get_review(review_id)
        if not review_inDB:
            return {"error": "Review not found"}, 404
        updated_review = api.payload
        try:
            review_inDB.text = updated_review.get('text', review_inDB.text)
        except:
            return {"error": "Invalid input data"}, 400
        try:
            review_inDB.rating = updated_review.get('rating', review_inDB.rating)
        except:
            return {"error": "Invalid input data"}, 400
        return {"message": "Review updated successfully"}, 200
    

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        existing_review = facade.get_review(review_id)
        if not existing_review:
            return {"error": "Review not found"}, 404
        facade.delete_review(review_id)
        return {"message": "Review deleted successfully"}, 200
