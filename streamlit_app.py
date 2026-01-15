import streamlit as st

from src.utils.answer import format_summary
from src.utils.router import route_query


st.set_page_config(page_title="WasteTrace", layout="wide")
st.title("WasteTrace")
st.write("Municipal waste stream analytics with MCP-ready tools.")

question = st.text_input("Ask a waste analytics question")
if question:
    route = route_query(question)
    summary = format_summary(question, route)
    st.subheader("Route")
    st.json(route)
    st.subheader("Summary")
    st.write(summary)

