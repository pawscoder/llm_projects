from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, Union

@dataclass
class Groomer:
    """Data class representing a groomer."""
    name: str
    rating: float
    address: str
    city: str
    zip_code: str
    pricing: Dict[str, float]
    breed_specializations: List[str]
    special_needs_handling: List[str]
    availability: Dict[str, List[str]]
    techniques: List[str]
    id: str = ""
    # service_menu: List[Dict[str, Any]] = field(default_factory=list)
    # breed_experience: Dict[str, str] = field(default_factory=dict)
    # calming_techniques: List[str] = field(default_factory=list)
    # photos: List[str] = field(default_factory=list)
    # cancellation_policy: str = ""


MOCK_GROOMERS = [
    Groomer(
        name="Paws & Pamper",
        rating=4.8,
        address="123 Main St",
        city="San Francisco",
        zip_code="94102",
        pricing={"small": 45, "medium": 65, "large": 85},
        breed_specializations=["Poodle", "Labrador", "Golden Retriever"],
        special_needs_handling=["anxiety-prone", "senior dogs"],
        availability={"weekday": ["Mon-Fri 9am-5pm"], "weekend": ["Sat 10am-4pm"]},
        techniques=["hand scissoring", "dematting", "de-shedding"],
        id="groomer_01"
    ),
    Groomer(
        name="Fluffy Dreams Grooming",
        rating=4.6,
        address="456 Oak Ave",
        city="San Francisco",
        zip_code="94107",
        pricing={"small": 50, "medium": 70, "large": 90},
        breed_specializations=["Shih Tzu", "Maltese", "Pomeranian"],
        special_needs_handling=["anxiety-prone", "aggressive dogs"],
        availability={"weekday": ["Tue-Thu 10am-6pm"], "weekend": ["Sat-Sun 11am-5pm"]},
        techniques=["breed-standard cuts", "hand scissoring", "conditioning"],
        id="groomer_02"
    ),
    Groomer(
        name="Bark & Shine",
        rating=4.5,
        address="789 Elm St",
        city="Oakland",
        zip_code="94612",
        pricing={"small": 40, "medium": 60, "large": 75},
        breed_specializations=["German Shepherd", "Husky", "Malamute"],
        special_needs_handling=["senior dogs", "reactive dogs"],
        availability={"weekday": ["Mon-Fri 8am-4pm"], "weekend": ["Sun 12pm-4pm"]},
        techniques=["undercoat removal", "de-shedding", "sanitary trim"],
        id="groomer_03"
    ),
    Groomer(
        name="Grooming Grace",
        rating=4.7,
        address="321 Birch Ln",
        city="Berkeley",
        zip_code="94702",
        pricing={"small": 55, "medium": 75, "large": 95},
        breed_specializations=["Doodles", "Terriers", "Spaniels"],
        special_needs_handling=["anxiety-prone", "special medical needs"],
        availability={"weekday": ["Mon-Fri 9am-6pm"], "weekend": ["Sat-Sun 10am-3pm"]},
        techniques=["breed-specific grooming", "hypoallergenic products", "calming techniques"],
        id="groomer_04"
    ),
    Groomer(
        name="The Dog Spa",
        rating=4.9,
        address="654 Pine Rd",
        city="San Francisco",
        zip_code="94110",
        pricing={"small": 60, "medium": 80, "large": 100},
        breed_specializations=["Toy breeds", "Bichon Frise", "Pug"],
        special_needs_handling=["anxiety-prone", "senior dogs", "aggressive dogs"],
        availability={"weekday": ["Tue-Fri 10am-6pm"], "weekend": ["Sat-Sun 9am-5pm"]},
        techniques=["spa treatments", "hand scissoring", "nail art", "aromatherapy"],
        id="groomer_05"
    ),
    Groomer(
        name="Tail Wags & Cuts",
        rating=4.4,
        address="987 Cedar Dr",
        city="Oakland",
        zip_code="94601",
        pricing={"small": 35, "medium": 55, "large": 70},
        breed_specializations=["Mixed breeds", "Mutts"],
        special_needs_handling=["anxiety-prone"],
        availability={"weekday": ["Mon-Sat 8am-5pm"], "weekend": []},
        techniques=["basic grooming", "nail trimming", "ear cleaning"],
        id="groomer_06"
    ),
    Groomer(
        name="Royal Paws Grooming",
        rating=4.7,
        address="246 Spruce Ave",
        city="San Jose",
        zip_code="95110",
        pricing={"small": 45, "medium": 65, "large": 85},
        breed_specializations=["Poodle", "Doodles", "Pomeranian"],
        special_needs_handling=["senior dogs"],
        availability={"weekday": ["Wed-Fri 10am-5pm"], "weekend": ["Sat-Sun 10am-4pm"]},
        techniques=["breed cuts", "creative grooming", "conditioning treatments"],
        id="groomer_07"
    ),
    Groomer(
        name="Zen Dog Grooming",
        rating=4.6,
        address="512 Market St",
        city="San Francisco",
        zip_code="94102",
        pricing={"small": 55, "medium": 75, "large": 95},
        breed_specializations=["Doodles", "Poodle", "Schnauzer"],
        special_needs_handling=["anxiety-prone", "special medical needs", "aggressive dogs"],
        availability={"weekday": ["Mon-Fri 10am-6pm"], "weekend": ["Sat 11am-4pm"]},
        techniques=["calming techniques", "gentle handling", "therapeutic grooming"],
        id="groomer_08"
    ),
    Groomer(
        name="Pawsitively Perfect",
        rating=4.8,
        address="789 Valencia St",
        city="San Francisco",
        zip_code="94110",
        pricing={"small": 50, "medium": 70, "large": 90},
        breed_specializations=["Boxer", "Bulldog", "Pit Bull"],
        special_needs_handling=["aggressive dogs", "reactive dogs"],
        availability={"weekday": ["Tue-Fri 9am-5pm"], "weekend": ["Sat-Sun 10am-4pm"]},
        techniques=["muscle massage", "deshedding", "breed-specific cuts"],
        id="groomer_09"
    ),
    Groomer(
        name="Cozy Paws Salon",
        rating=4.5,
        address="834 Telegraph Ave",
        city="Oakland",
        zip_code="94609",
        pricing={"small": 45, "medium": 65, "large": 80},
        breed_specializations=["Chihuahua", "Toy breeds", "Pug"],
        special_needs_handling=["senior dogs", "anxiety-prone"],
        availability={"weekday": ["Mon-Fri 10am-5pm"], "weekend": ["Sat-Sun 12pm-4pm"]},
        techniques=["hand scissoring", "nail care", "dental cleaning"],
        id="groomer_10"
    ),
    Groomer(
        name="Happy Hound Grooming",
        rating=4.7,
        address="1250 Park Ave",
        city="Berkeley",
        zip_code="94710",
        pricing={"small": 48, "medium": 68, "large": 88},
        breed_specializations=["Labrador", "Golden Retriever", "Cocker Spaniel"],
        special_needs_handling=["senior dogs", "reactive dogs"],
        availability={"weekday": ["Wed-Fri 8am-4pm"], "weekend": ["Sat-Sun 9am-3pm"]},
        techniques=["double coat grooming", "de-shedding", "sanitary trim"],
        id="groomer_11"
    ),
    Groomer(
        name="Groom Elite",
        rating=4.9,
        address="456 First St",
        city="San Jose",
        zip_code="95113",
        pricing={"small": 65, "medium": 85, "large": 105},
        breed_specializations=["Poodle", "Doodles", "Bichon Frise"],
        special_needs_handling=["anxiety-prone", "special medical needs"],
        availability={"weekday": ["Mon-Fri 9am-6pm"], "weekend": ["Sat-Sun 10am-5pm"]},
        techniques=["show grooming", "creative styling", "breed-standard cuts"],
        id="groomer_12"
    ),
    Groomer(
        name="Tail Town Grooming",
        rating=4.4,
        address="567 South St",
        city="San Jose",
        zip_code="95112",
        pricing={"small": 42, "medium": 62, "large": 78},
        breed_specializations=["Mixed breeds", "Mutts", "Rescues"],
        special_needs_handling=["anxiety-prone", "special medical needs"],
        availability={"weekday": ["Mon-Sat 8am-5pm"], "weekend": ["Sun 11am-3pm"]},
        techniques=["gentle grooming", "mat removal", "basic care"],
        id="groomer_13"
    ),
    Groomer(
        name="Luxe Paws",
        rating=4.8,
        address="678 Mission St",
        city="San Francisco",
        zip_code="94103",
        pricing={"small": 58, "medium": 78, "large": 98},
        breed_specializations=["Maltese", "Shih Tzu", "Lhasa Apso"],
        special_needs_handling=["senior dogs", "anxiety-prone"],
        availability={"weekday": ["Tue-Fri 10am-5pm"], "weekend": ["Sat-Sun 11am-4pm"]},
        techniques=["show cuts", "breed grooming", "conditioning treatments"],
        id="groomer_14"
    ),
    Groomer(
        name="Bark's Best",
        rating=4.6,
        address="789 Webster St",
        city="Oakland",
        zip_code="94610",
        pricing={"small": 50, "medium": 70, "large": 85},
        breed_specializations=["Terrier", "Schnauzer", "Pomeranian"],
        special_needs_handling=["anxiety-prone"],
        availability={"weekday": ["Mon-Fri 9am-5pm"], "weekend": ["Sat 10am-3pm"]},
        techniques=["hand scissoring", "breed trims", "ear cleaning"],
        id="groomer_15"
    ),
    Groomer(
        name="Pawfect Cuts",
        rating=4.7,
        address="890 Grand Ave",
        city="Oakland",
        zip_code="94610",
        pricing={"small": 48, "medium": 68, "large": 88},
        breed_specializations=["Doodle", "Poodle", "Spaniel"],
        special_needs_handling=["anxiety-prone", "senior dogs", "reactive dogs"],
        availability={"weekday": ["Mon-Fri 10am-6pm"], "weekend": ["Sat-Sun 10am-4pm"]},
        techniques=["breed cuts", "de-shedding", "calming techniques"],
        id="groomer_16"
    ),
    Groomer(
        name="Shiny Coat Studio",
        rating=4.5,
        address="1001 California Ave",
        city="Berkeley",
        zip_code="94706",
        pricing={"small": 52, "medium": 72, "large": 92},
        breed_specializations=["German Shepherd", "Husky", "Belgian Malinois"],
        special_needs_handling=["reactive dogs", "aggressive dogs"],
        availability={"weekday": ["Wed-Fri 8am-4pm"], "weekend": []},
        techniques=["undercoat removal", "de-shedding", "conditioning"],
        id="groomer_17"
    ),
    Groomer(
        name="Puppy Paradise",
        rating=4.6,
        address="1112 Elm St",
        city="San Jose",
        zip_code="95126",
        pricing={"small": 40, "medium": 60, "large": 75},
        breed_specializations=["All breeds", "Puppies", "Young dogs"],
        special_needs_handling=["anxiety-prone", "puppies"],
        availability={"weekday": ["Mon-Sat 9am-5pm"], "weekend": ["Sun 10am-2pm"]},
        techniques=["puppy introduction", "gentle handling", "basic grooming"],
        id="groomer_18"
    ),
    Groomer(
        name="Elite Grooming Studio",
        rating=4.8,
        address="1223 Broadway",
        city="Oakland",
        zip_code="94612",
        pricing={"small": 60, "medium": 80, "large": 100},
        breed_specializations=["Poodle", "Doodle", "Bichon Frise", "Pomeranian"],
        special_needs_handling=["anxiety-prone", "senior dogs", "special medical needs"],
        availability={"weekday": ["Mon-Fri 9am-5pm"], "weekend": ["Sat-Sun 10am-4pm"]},
        techniques=["show grooming", "creative styling", "breed cuts", "spa treatments"],
        id="groomer_19"
    ),
    Groomer(
        name="Cuddle & Clip",
        rating=4.4,
        address="1334 Lincoln Ave",
        city="San Jose",
        zip_code="95125",
        pricing={"small": 38, "medium": 58, "large": 73},
        breed_specializations=["Chihuahua", "Toy breeds", "Small dogs"],
        special_needs_handling=["senior dogs", "anxiety-prone"],
        availability={"weekday": ["Tue-Sat 10am-5pm"], "weekend": []},
        techniques=["gentle grooming", "nail care", "sanitary trim"],
        id="groomer_20"
    ),
]