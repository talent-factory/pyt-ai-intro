"""Geocoding-Funktionen für Adress-Umwandlung."""

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

# Geocoder initialisieren
geolocator = Nominatim(user_agent="customer_map_app")


def geocode_address(street, zip_code, city, country):
    """Wandelt Adresse in Koordinaten um.

    Args:
        street: Strasse
        zip_code: PLZ
        city: Ort
        country: Land

    Returns:
        tuple: (latitude, longitude) oder (None, None) bei Fehler
    """
    # Adresse zusammensetzen
    address = f"{street}, {zip_code} {city}, {country}"

    try:
        # Geocoding durchführen
        location = geolocator.geocode(address, timeout=10)

        if location:
            return location.latitude, location.longitude
        else:
            # Fallback: Nur Stadt und Land
            location = geolocator.geocode(f"{city}, {country}", timeout=10)
            if location:
                return location.latitude, location.longitude

        return None, None

    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Geocoding-Fehler: {e}")
        return None, None

