import streamlit as st
import requests

# Set page configuration (must be the first Streamlit command)
st.set_page_config(page_title="🌍 Country Info Cards", layout="centered")

# Apply Custom CSS for Background Color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# API URL
API_URL = "https://restcountries.com/v3.1/name/"

st.title("🌍 Country Information Cards")
st.write("🔍 Get information about any country!")

# User Input
country = st.text_input("Enter country name:")

if st.button("🔍 Search"):
    if country:
        try:
            response = requests.get(API_URL + country)
            if response.status_code == 200:
                data = response.json()[0]

                # Extract Country Details
                name = data["name"]["common"]
                flag = data["flags"]["png"]
                capital = data.get("capital", ["N/A"])[0]
                region = data.get("region", "N/A")
                subregion = data.get("subregion", "N/A")
                population = data.get("population", "N/A")
                area = data.get("area", "N/A")
                currency = list(data["currencies"].keys())[0]
                language = ", ".join(data["languages"].values())

                # Display Country Card
                st.image(flag, width=150)
                st.markdown(f"## 📍 {name}")
                st.write(f"**🏛 Capital:** {capital}")
                st.write(f"**🌍 Region:** {region} | **📌 Subregion:** {subregion}")
                st.write(f"**👥 Population:** {population:,}")
                st.write(f"**📏 Area:** {area:,} km²")
                st.write(f"**💰 Currency:** {currency}")
                st.write(f"**🗣 Languages:** {language}")

            else:
                st.error("❌ Country not found! Please enter a valid name.")

        except Exception as e:
            st.error(f"⚠️ Error: {e}")

    else:
        st.warning("⚠️ Please enter a country name!")
