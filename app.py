import streamlit as st
from rag_pipeline import get_rag_qa

st.set_page_config(page_title="📚 Personal Notes Search Assistant", layout="wide")
st.title("📚 Personal Notes Search Assistant (Offline RAG)")

qa = get_rag_qa()

query = st.text_input("Ask something from your notes:")

if query:
    with st.spinner("Searching your notes..."):
        result = qa.invoke(query)

    st.subheader("📘 Answer:")

    # ---- Correct text extractor ----
    if hasattr(result, "content"):            
        # AIMessage object
        answer_text = result.content

    elif isinstance(result, dict):
        answer_text = (
            result.get("output")
            or result.get("answer")
            or result.get("content")
            or str(result)
        )

    else:
        answer_text = str(result)

    # --------------------------------

    st.write(answer_text)
