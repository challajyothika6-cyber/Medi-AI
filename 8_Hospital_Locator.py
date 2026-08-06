import streamlit as st
import folium
from streamlit_folium import st_folium


st.set_page_config(
    page_title="Hospital Locator",
    page_icon="🏥",
    layout="wide"
)


st.title("🏥 Hospital Locator")
st.caption("Find nearby hospitals using Google Maps")


st.warning(
    "📍 Enter your location coordinates to find hospitals on the map."
)


col1, col2 = st.columns(2)


with col1:

    latitude = st.number_input(
        "Latitude",
        value=15.4786,
        format="%.6f"
    )


with col2:

    longitude = st.number_input(
        "Longitude",
        value=78.4836,
        format="%.6f"
    )


if st.button("🔍 Find Hospitals"):

    hospital_map = folium.Map(
        location=[latitude, longitude],
        zoom_start=13
    )


    # User Location

    folium.Marker(
        [latitude, longitude],
        popup="📍 Your Location",
        icon=folium.Icon(
            color="blue"
        )
    ).add_to(hospital_map)


    # Sample Hospitals

    hospitals = [
        {
            "name":"Government Hospital",
            "lat":latitude+0.005,
            "lon":longitude+0.004
        },
        {
            "name":"City Care Hospital",
            "lat":latitude-0.004,
            "lon":longitude+0.006
        },
        {
            "name":"Apollo Hospital",
            "lat":latitude+0.003,
            "lon":longitude-0.005
        }
    ]


    for hospital in hospitals:

        folium.Marker(
            [
                hospital["lat"],
                hospital["lon"]
            ],
            popup="🏥 "+hospital["name"],
            icon=folium.Icon(
                color="red",
                icon="plus"
            )
        ).add_to(hospital_map)


    st_folium(
        hospital_map,
        width=900,
        height=500
    )


st.markdown("---")


st.subheader("🏥 Emergency Contact")

st.info(
    """
    🚑 Ambulance: 108

    🏥 Emergency Services: Contact nearest hospital

    📞 Always consult qualified healthcare professionals.
    """
)


st.caption(
    "© 2026 Medi-AI Healthcare Platform | Developed by Jyothika"
)