import streamlit as st

st.set_page_config(
    page_title="DYOR Agent",
    page_icon="🔎",
    layout="centered"
)

st.title("🔎 DYOR Agent")
st.subheader("Don't Trust the AI. Use AI to DYOR.")

st.write(
    "A beginner-first crypto research assistant "
    "that helps you understand an asset instead of "
    "telling you what to buy."
)

token = st.text_input(
    "Enter a crypto asset",
    placeholder="Example: BNB"
)

if st.button("Start DYOR"):
    if token:
        st.success(f"Research started for {token.upper()} 🚀")
    else:
        st.warning("Enter a crypto asset first.")
