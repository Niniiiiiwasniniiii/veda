import streamlit as st
from groq import Groq

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="V3DA AI",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# GROQ CLIENT
# -----------------------------
client = Groq(
    api_key=st.secrets["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"]
)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🤖 V3DA AI")

mode = st.sidebar.radio(
    "Choose Mode",
    [
        "🧠 V3DA Chat",
        "💪 V3DA Fit",
        "🎓 V3DA Study"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Powered by Groq + Llama 3.3"
)

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# -----------------------------
# TITLE
# -----------------------------
st.title("🤖 V3DA AI")
st.caption("Your intelligent AI companion")

# -----------------------------
# CHAT HISTORY
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# SYSTEM PROMPTS
# -----------------------------
def get_system_prompt(mode):

    if mode == "💪 V3DA Fit":
        return """
You are V3DA Fit.

Rules:
- Be friendly and motivating.
- Keep answers practical.
- Suggest healthy workout plans.
- Suggest healthy diet plans.
- Keep responses concise.
- Never give dangerous medical advice.
"""

    elif mode == "🎓 V3DA Study":
        return """
You are V3DA Study.

Rules:
- Help students understand concepts.
- Explain step by step.
- Use simple language.
- Give examples whenever possible.
- Keep answers concise.
"""

    return """
You are V3DA AI.

Rules:
- Be helpful and professional.
- Give accurate answers.
- Keep answers easy to understand.
"""

# -----------------------------
# USER INPUT
# -----------------------------
prompt = st.chat_input("Ask V3DA anything...")

if prompt:

    if len(prompt) > 500:
        st.warning("Please keep messages under 500 characters.")
        st.stop()

    if not prompt.strip():
        st.stop()

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    try:

        messages = [
            {
                "role": "system",
                "content": get_system_prompt(mode)
            }
        ]

        for msg in st.session_state.messages:
            messages.append(
                {
                    "role": msg["role"],
                    "content": msg["content"]
                }
            )

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7
        )

        reply = response.choices[0].message.content

        with st.chat_message("assistant"):
            st.markdown(reply)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

    except Exception as e:
        st.error(
            f"Unable to connect to Groq AI: {e}"
        )



     
