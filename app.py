import streamlit as st
from rag import load_rag

st.set_page_config(
    page_title="pgRAG",
    layout = "wide"
)

st.title("pgRAG")
st.caption("Ask anything about PostgreSQL!")

@st.cache_resource(show_time="Loading docs...")
def get_rag_chain():
    return load_rag()

rag_chain = load_rag()

if "messages" not in st.session_state:
    st.session_state.messages=[]

for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

    # Read user message and call rag pipeline

user_input = st.chat_input("Ask..")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        answer = ""

        try:
            for chunk in rag_chain.stream(user_input):
                answer += chunk
                placeholder.markdown(answer)
        except Exception as e:
            answer = f"Error: {e}"
            placeholder.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

