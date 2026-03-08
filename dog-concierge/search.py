"""Search for dog groomers by filters."""
from typing import Any, Dict, List, Optional

from mock_groomers import MOCK_GROOMERS


def search_groomers(
    city: Optional[str] = None,
    zip_code: Optional[str] = None,
    breed_specialization: Optional[str] = None,
    special_needs: Optional[str] = None,
    availability: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
) -> List[Dict[str, Any]]:
    """
    Search for dog groomers based on various filters.

    Args:
        city: Filter by city name (case-insensitive)
        zip_code: Filter by zip code
        breed_specialization: Filter by breed specialization (case-insensitive)
        special_needs: Filter by special needs handling capability (e.g., "anxiety-prone", "senior dogs")
        availability: Filter by availability ("weekday" or "weekend")
        min_price: Minimum price for small dogs
        max_price: Maximum price for small dogs

    Returns:
        List of groomer dicts with: id, name, rating, address, city, zip_code, pricing,
        breed_specializations, special_needs_handling, availability, techniques.
    """
    results = []

    for groomer in MOCK_GROOMERS:
        # City filter
        if city and groomer.city.lower() != city.lower():
            continue

        # Zip code filter
        if zip_code and groomer.zip_code != zip_code:
            continue

        # Breed specialization filter
        if breed_specialization:
            if not any(breed.lower() == breed_specialization.lower() for breed in groomer.breed_specializations):
                continue

        # Special needs handling filter
        if special_needs:
            if special_needs.lower() not in [need.lower() for need in groomer.special_needs_handling]:
                continue

        # Availability filter
        if availability:
            if availability.lower() == "weekend":
                if not groomer.availability.get("weekend"):
                    continue
            elif availability.lower() == "weekday":
                if not groomer.availability.get("weekday"):
                    continue

        # Price range filter (checking small dog price)
        small_price = groomer.pricing.get("small", 0)
        if min_price and small_price < min_price:
            continue
        if max_price and small_price > max_price:
            continue

        # Add matching groomer to results
        results.append({
            "id": groomer.id,
            "name": groomer.name,
            "rating": groomer.rating,
            "address": groomer.address,
            "city": groomer.city,
            "zip_code": groomer.zip_code,
            "pricing": groomer.pricing,
            "breed_specializations": groomer.breed_specializations,
            "special_needs_handling": groomer.special_needs_handling,
            "availability": groomer.availability,
            "techniques": groomer.techniques,
        })

    return results
