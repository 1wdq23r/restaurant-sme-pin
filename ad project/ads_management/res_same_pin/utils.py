from .models import Restaurant

def find_restaurants_with_same_pincode(restaurant_id):
    try:
        # Get the restaurant by ID
        restaurant = Restaurant.objects.get(id=restaurant_id)
        # Get the pincode of the restaurant
        pincode = restaurant.pincode
        # Find all restaurants with the same pincode, excluding the given restaurant
        restaurants_with_same_pincode = Restaurant.objects.filter(pincode=pincode).exclude(id=restaurant_id)
        return restaurants_with_same_pincode
    except Restaurant.DoesNotExist:
        # Handle the case where the restaurant does not exist
        return None
