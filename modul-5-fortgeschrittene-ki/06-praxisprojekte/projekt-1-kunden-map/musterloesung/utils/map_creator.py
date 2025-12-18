"""Karten-Erstellung mit Folium."""

import folium


def create_customer_map(customers_df):
    """Erstellt eine Karte mit allen Kunden.

    Args:
        customers_df: DataFrame mit Kundendaten (inkl. latitude, longitude)

    Returns:
        folium.Map: Interaktive Karte
    """
    # Kunden mit Koordinaten filtern
    valid_customers = customers_df.dropna(subset=["latitude", "longitude"])

    if len(valid_customers) == 0:
        # Leere Karte (Schweiz zentriert)
        return folium.Map(location=[46.8182, 8.2275], zoom_start=7)

    # Zentrum berechnen (Durchschnitt aller Koordinaten)
    center_lat = valid_customers["latitude"].mean()
    center_lon = valid_customers["longitude"].mean()

    # Karte erstellen
    m = folium.Map(location=[center_lat, center_lon], zoom_start=7)

    # Marker für jeden Kunden
    for _, customer in valid_customers.iterrows():
        # Popup-Text
        popup_text = f"""
        <b>{customer["company"]}</b><br>
        {customer["street"]}<br>
        {customer["zip_code"]} {customer["city"]}<br>
        {customer["country"]}
        """

        # Marker hinzufügen
        folium.Marker(
            location=[customer["latitude"], customer["longitude"]],
            popup=folium.Popup(popup_text, max_width=200),
            tooltip=customer["company"],
            icon=folium.Icon(color="blue", icon="building", prefix="fa"),
        ).add_to(m)

    return m
