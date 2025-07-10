import streamlit as st
import requests
import datetime

# Backend API endpoint
BASE_URL = "https://tripwise-fumv.onrender.com"

# App Configuration
st.set_page_config(
    page_title="TripWise • Your AI Travel Concierge",
    page_icon="🧳",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Header Section
st.title("🧳 TripWise")
st.caption("Your AI Travel Concierge ✨")

st.markdown(
    """
    Welcome to **TripWise**, your intelligent assistant for planning personalized getaways!  
    Whether it’s a tropical escape, a city adventure, or a cultural dive — just describe your dream trip, and we’ll take care of the rest.  
    \n_Type something like:_  
    `“Plan a 4-day cultural trip to Istanbul with historic sites and local food experiences.”`
    """
)

# Chat History Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# User Input Form
with st.form(key="tripwise_form", clear_on_submit=True):
    st.subheader("📍 Where to next?")
    user_input = st.text_input(
        "Describe your ideal trip:",
        placeholder="e.g. 7-day road trip across Scotland with hiking and scenic views"
    )
    submit_button = st.form_submit_button("🌐 Create My Travel Plan")

# Handle Submission
if submit_button and user_input.strip():
    try:
        with st.spinner("🧠 Crafting your perfect journey..."):
            response = requests.post(f"{BASE_URL}/query", json={"question": user_input})

        if response.status_code == 200:
            plan = response.json().get("answer", "No plan returned.")
            timestamp = datetime.datetime.now().strftime('%A, %d %B %Y at %I:%M %p')

            st.success("🎉 Your itinerary is ready!")

            st.markdown(f"""
                ## 🗺️ Your TripWise Itinerary  
                **📅 Generated on:** {timestamp}  
                **🤖 Powered by:** TripWise AI Engine  

                ---
                {plan}
                ---
                _⚠️ Please verify accommodations, local guidelines, and activity availability before booking._
            """)
        else:
            st.error(f"❌ Failed to generate travel plan. Details: {response.text}")

    except Exception as e:
        st.error(f"⚠️ Something went wrong while fetching your itinerary: {e}")
