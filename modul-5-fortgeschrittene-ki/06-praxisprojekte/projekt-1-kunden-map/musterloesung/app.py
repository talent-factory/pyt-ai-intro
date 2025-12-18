"""Kunden-Adressen Visualisierung mit Streamlit.

Eine vollständige Streamlit-App zur Verwaltung und Visualisierung
von Kundenadressen auf einer interaktiven Karte.
"""

import streamlit as st
import pandas as pd
from pathlib import Path
from streamlit_folium import st_folium

from utils.geocoder import geocode_address
from utils.map_creator import create_customer_map

# Konstanten
DATA_FILE = Path("data/customers.csv")


def load_customers():
    """Lädt Kundendaten aus CSV-Datei.

    Returns:
        pd.DataFrame: Kundendaten oder leerer DataFrame
    """
    if DATA_FILE.exists():
        return pd.read_csv(DATA_FILE)
    else:
        # Leerer DataFrame mit Spalten
        return pd.DataFrame(
            columns=["company", "street", "zip_code", "city", "country", "latitude", "longitude"]
        )


def save_customer(company, street, zip_code, city, country):
    """Speichert einen neuen Kunden mit Geocoding.

    Args:
        company: Firmenname
        street: Strasse
        zip_code: PLZ
        city: Ort
        country: Land
    """
    # Geocoding durchführen
    with st.spinner("Ermittle Koordinaten..."):
        lat, lon = geocode_address(street, zip_code, city, country)

    if lat is None or lon is None:
        st.warning(
            "⚠️ Koordinaten konnten nicht ermittelt werden. "
            "Kunde wird ohne Koordinaten gespeichert."
        )

    # Bestehende Daten laden
    df = load_customers()

    # Neuen Kunden hinzufügen
    new_customer = pd.DataFrame(
        [
            {
                "company": company,
                "street": street,
                "zip_code": zip_code,
                "city": city,
                "country": country,
                "latitude": lat,
                "longitude": lon,
            }
        ]
    )

    df = pd.concat([df, new_customer], ignore_index=True)

    # Speichern
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(DATA_FILE, index=False)


def delete_customer(index):
    """Löscht einen Kunden.

    Args:
        index: Index des zu löschenden Kunden
    """
    df = load_customers()
    df = df.drop(index).reset_index(drop=True)
    df.to_csv(DATA_FILE, index=False)


# Seitenkonfiguration
st.set_page_config(
    page_title="Kunden-Map",
    page_icon="🗺️",
    layout="wide",
)

# Titel
st.title("🗺️ Kunden-Adressen Visualisierung")

# Sidebar für Dateneingabe
st.sidebar.header("Neuen Kunden hinzufügen")

with st.sidebar.form("customer_form"):
    # Eingabefelder
    company = st.text_input("Firmenname*", placeholder="z.B. Acme GmbH")
    street = st.text_input("Strasse*", placeholder="z.B. Bahnhofstrasse 1")
    zip_code = st.text_input("PLZ*", placeholder="z.B. 8001")
    city = st.text_input("Ort*", placeholder="z.B. Zürich")
    country = st.selectbox(
        "Land*",
        options=["Schweiz", "Deutschland", "Österreich", "Frankreich", "Italien"],
    )

    # Submit-Button
    submitted = st.form_submit_button("Kunde hinzufügen")

    if submitted:
        # Validierung
        if not company or not street or not zip_code or not city:
            st.error("Bitte füllen Sie alle Pflichtfelder aus!")
        else:
            # Speichern
            save_customer(company, street, zip_code, city, country)
            st.success(f"✅ Kunde '{company}' erfolgreich hinzugefügt!")
            st.rerun()

# Hauptbereich
st.header("Kundenliste")

# Daten laden
customers_df = load_customers()

if len(customers_df) == 0:
    st.info("Noch keine Kunden vorhanden. Fügen Sie den ersten Kunden hinzu!")
else:
    st.write(f"**Anzahl Kunden:** {len(customers_df)}")

    # Filter
    col1, col2 = st.columns([2, 1])

    with col1:
        # Länder-Filter
        countries = ["Alle"] + sorted(customers_df["country"].unique().tolist())
        selected_country = st.selectbox("Filter nach Land:", countries)

    with col2:
        # Statistiken
        st.metric("Länder", customers_df["country"].nunique())

    # Daten filtern
    if selected_country != "Alle":
        filtered_df = customers_df[customers_df["country"] == selected_country]
    else:
        filtered_df = customers_df

    st.write(f"**Angezeigte Kunden:** {len(filtered_df)}")

    # Erweiterte Statistiken
    with st.expander("📊 Statistiken"):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Gesamt Kunden", len(customers_df))

        with col2:
            st.metric("Länder", customers_df["country"].nunique())

        with col3:
            geocoded = customers_df["latitude"].notna().sum()
            st.metric("Geocodiert", f"{geocoded}/{len(customers_df)}")

        # Kunden pro Land
        st.subheader("Kunden pro Land")
        country_counts = customers_df["country"].value_counts()
        st.bar_chart(country_counts)

    # Tabs für Tabelle und Karte
    tab1, tab2 = st.tabs(["📋 Tabelle", "🗺️ Karte"])

    with tab1:
        # Tabelle mit Export
        st.dataframe(filtered_df, use_container_width=True)

        # CSV-Export
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="📥 Als CSV exportieren",
            data=csv,
            file_name="kunden_export.csv",
            mime="text/csv",
        )

    with tab2:
        # Karte erstellen und anzeigen
        customer_map = create_customer_map(filtered_df)
        st_folium(customer_map, width=1200, height=600)

