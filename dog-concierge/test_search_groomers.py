"""Tests for search_groomers."""
import pytest

from search import search_groomers


def test_search_groomers_by_city_and_breed():
    """Filter by city and breed_specialization returns matching groomers."""
    results = search_groomers(city="San Francisco", breed_specialization="Poodle")
    assert len(results) >= 1
    for r in results:
        assert r["city"] == "San Francisco"
        assert "Poodle" in r["breed_specializations"]
    # Paws & Pamper is SF and has Poodle
    names = [r["name"] for r in results]
    assert "Paws & Pamper" in names


def test_search_groomers_rejects_nonexistent_parameter():
    """Passing a non-existent keyword argument raises TypeError."""
    with pytest.raises(TypeError, match="unexpected keyword argument"):
        search_groomers(city="Oakland", fake_param="should not exist")
