import streamlit as st
import requests

# Custom Styling
st.set_page_config(page_title="Legal Document Analyzer", page_icon="⚖")

# Sidebar for navigation and guidance
st.sidebar.title("ℹ️ How It Works")
st.sidebar.write("""
1. Paste your legal text in the input box.
2. Click 'Analyze' to extract key insights.
3. View the results categorized into Summary, Key Clauses, and Named Entities.
""")
st.sidebar.write("🔗 **Backend Status:** Ensure the FastAPI server is running.")

# Main Title
st.title("⚖ Legal Document Analyzer")
st.markdown("📜 **Unlock insights from legal documents effortlessly.**")

# User Input
text_input = st.text_area("Paste legal text here:", height=300, placeholder="Enter legal text for analysis...")

# Analysis Button with Feedback
if st.button("Analyze"):
    if text_input.strip():
        with st.spinner("🔎 Analyzing legal document..."):
            try:
                response = requests.post(
                    "http://localhost:8000/analyze/", 
                    data={"text": text_input}
                )
                response.raise_for_status()
                results = response.json()

                # Display Results with Collapsible Sections
                st.subheader("📄 Summary")
                with st.expander("View Summary"):
                    st.write(results.get("summary", "No summary available."))

                st.subheader("📌 Key Clauses")
                with st.expander("View Key Clauses"):
                    st.write(results.get("clauses", "No key clauses detected."))

                st.subheader("🔍 Named Entities")
                with st.expander("View Named Entities"):
                    st.write(results.get("entities", "No named entities found."))

            except requests.exceptions.RequestException as e:
                st.error(f"🚨 Error contacting backend: {e}")
    else:
        st.warning("⚠ Please enter legal text before analyzing.")

# Footer
st.markdown("---")
st.markdown("⚖ Developed for legal insights")
