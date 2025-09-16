import streamlit as st

st.markdown(
    """
    <style>
    /* Center all vertical blocks (title, text input, button, etc.) */
    div[data-testid="stVerticalBlock"] {
        display: flex;
        flex-direction: column;
        align-items: center;  /* horizontal centering */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="Support Card", page_icon="⚡", layout="centered")

# Page title
st.markdown('<h1 style="text-align:center;">Zuper Assistant</h1>', unsafe_allow_html=True)


# Text input box
user_input = st.text_area(
    label="",
    height=100,
    width=500,
    placeholder="Type your message..."
)


# Read CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Process button
process_clicked = st.button("Process")

# Only render the card if Process is clicked and there is input
if process_clicked and user_input.strip():
    draft_text = user_input  # Use the input as the draft text
    # Card component
    st.markdown(
        f"""
        <div class="card">
            <div class="contextual-title">Request to Adjust Total for Increased Permit Fee</div>
            <div class="header-row">
                <span class="pill">Pricing Adjustment (Confirmation)</span>
                <span class="ticket-group-pill">Scoping Group</span>
                <span class="priority-pill">High priority</span>
            </div>
            <div class="installer-question"> 
              <div class="ticket-info">Installer Question:</div>
              {user_input}
            </div>
            <div class="draft-response">
              <div class="ticket-info">Draft Response:</div>
              {draft_text}
              <div class="draft-footer">
                <div class="draft-footer-icon copy-icon" title="Copy"></div>
                <div class="draft-footer-icon like-icon" title="Like"></div>
                <div class="draft-footer-icon dislike-icon" title="Dislike"></div>
                <div class="draft-footer-icon upload-icon" title="Upload"></div>
                <div class="draft-footer-icon regenerate-icon" title="Regenerate"></div>
              </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
