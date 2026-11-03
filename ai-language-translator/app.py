
import streamlit as st
from translator import translate_text

# Page configuration
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

# Application title
st.title("🌍 AI Language Translator")
st.write("Translate English text into French using Artificial Intelligence.")

st.markdown("---")

# Text input
text = st.text_area(
    "Enter English text:",
    placeholder="Type something in English...",
    height=150
)

# Initialize session state
if "translation" not in st.session_state:
    st.session_state.translation = ""

# Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Translate", use_container_width=True):
        if text.strip():
            try:
                with st.spinner("AI is translating..."):
                    st.session_state.translation = translate_text(text)
            except Exception as e:
                st.error(f"Translation failed: {e}")
        else:
            st.warning("Please enter some text.")

with col2:
    if st.button("🗑️ Clear", use_container_width=True):
        st.session_state.translation = ""
        st.rerun()

# Display translation ONCE
if st.session_state.translation:
    st.success("Translation completed!")
    st.subheader("🇫🇷 French Translation")
    st.code(st.session_state.translation, language=None)

# Footer
st.markdown("---")
st.caption(
    "Built with Python | PyTorch | Hugging Face Transformers | Streamlit"
)
