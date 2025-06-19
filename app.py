import streamlit as st
import requests

# Set page config
st.set_page_config(page_title="KnowYourCountry", layout="centered")

# App title
st.title("🌍 KnowYourCountry")
st.subheader("Get instant info about any country on Earth!")

# Input
country_name = st.text_input("Enter a country name (e.g. India, France, Japan):")

# When button is clicked
if st.button("🔍 Search") and country_name:
    with st.spinner("Fetching country info..."):
        try:
            response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}?fullText=true")

            data = response.json()
            
            if isinstance(data, list):
                country = data[0]

                # Display basic info
                st.success(f"✅ Info for **{country['name']['common']}**")

                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"**Capital**: {country.get('capital', ['N/A'])[0]}")
                    st.write(f"**Region**: {country.get('region', 'N/A')}")
                    st.write(f"**Subregion**: {country.get('subregion', 'N/A')}")
                    st.write(f"**Population**: {country.get('population', 'N/A')}")
                    st.write(f"**Area (km²)**: {country.get('area', 'N/A')}")

                with col2:
                    flag_url = country['flags']['png']
                    st.image(flag_url, caption=f"{country['name']['common']} Flag", width=200)

                # Currency and languages
                currencies = list(country.get('currencies', {}).keys())
                langs = list(country.get('languages', {}).values())

                st.write(f"**Currency**: {', '.join(currencies) if currencies else 'N/A'}")
                st.write(f"**Languages**: {', '.join(langs) if langs else 'N/A'}")

            else:
                st.error("⚠️ Country not found. Please check the spelling.")
        except Exception as e:
            st.error("Something went wrong while fetching data.")
