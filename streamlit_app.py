import streamlit as st
import requests
import datetime
import pandas as pd
import re

# Backend API endpoint
BASE_URL = "https://tripwise-fumv.onrender.com"

# App Configuration
st.set_page_config(
    page_title="TripWise • Your AI Travel Concierge",
    page_icon="🧳",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Header
st.title("🧳 TripWise")
st.caption("Your AI Travel Concierge ✨")

st.markdown("""
Welcome to **TripWise**, your intelligent assistant for planning personalized getaways!  
Describe your dream trip — we'll take care of the rest.

_Example:_  
`“Plan a 4-day cultural trip to Istanbul with historic sites and local food experiences.”`
""")

# Session setup
if "messages" not in st.session_state:
    st.session_state.messages = []
if "last_prompt" not in st.session_state:
    st.session_state.last_prompt = ""
if "last_plan" not in st.session_state:
    st.session_state.last_plan = ""

# --------- 🧾 Budget Filter & Input Form -----------
with st.form(key="tripwise_form", clear_on_submit=True):
    st.subheader("📍 Where to next?")
    user_input = st.text_input("Describe your ideal trip:")

    budget = st.radio(
        "Select your travel budget:",
        ["No preference", "Budget-friendly ($)", "Mid-range ($$)", "Luxury ($$$$)"],
        index=0,
        horizontal=True
    )

    submit_button = st.form_submit_button("🌐 Create My Travel Plan")

# --------- ✏️ Prompt Mod -----------------
def apply_budget_to_prompt(prompt, budget_pref):
    if budget_pref == "No preference":
        return prompt
    elif "budget" in budget_pref.lower():
        return f"Plan a {budget_pref.lower()} trip. {prompt}"
    elif "luxury" in budget_pref.lower():
        return f"Plan a luxurious and premium trip. {prompt}"
    return prompt

# --------- 🧠 Query Function ---------------
def generate_itinerary(prompt):
    try:
        with st.spinner("🧠 Crafting your perfect journey..."):
            response = requests.post(f"{BASE_URL}/query", json={"question": prompt})
        if response.status_code == 200:
            plan = response.json().get("answer", "No plan returned.")
            st.session_state.last_prompt = prompt
            st.session_state.last_plan = plan
            return plan
        else:
            st.error(f"❌ Failed to generate travel plan. Details: {response.text}")
            return None
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
        return None

# --------- 📤 Main Output ---------------
if submit_button and user_input.strip():
    full_prompt = apply_budget_to_prompt(user_input, budget)
    itinerary = generate_itinerary(full_prompt)

    if itinerary:
        timestamp = datetime.datetime.now().strftime('%A, %d %B %Y at %I:%M %p')
        st.success("🎉 Your itinerary is ready!")

        st.markdown(f"""
        ## 🗺️ Your TripWise Itinerary  
        **📅 Generated on:** {timestamp}  
        **💸 Budget Type:** {budget}  
        **🤖 Powered by:** TripWise AI Engine  
        ---
        {itinerary}
        ---
        _⚠️ Please verify accommodations, local guidelines, and activity availability before booking._
        """)

        # --------- 📊 Summary Table (Simple Extract) ------------
        st.subheader("📊 Trip Summary")
        summary = []
        pattern = r"(Day\s*\d+).*?:?\s*(.*)"
        for match in re.findall(pattern, itinerary, re.IGNORECASE):
            day, activity = match
            summary.append((day.strip(), activity.strip()[:100]))

        if summary:
            df = pd.DataFrame(summary, columns=["Day", "Activity Highlight"])
            st.table(df)
        else:
            st.info("Could not auto-extract summary. Try including 'Day 1', 'Day 2' style formatting in prompt.")

# --------- 📎 Extras (Download, Map, etc.) ---------------
if st.session_state.last_plan:
    itinerary = st.session_state.last_plan


    # 📄 Download Itinerary
    st.download_button("📄 Download as TXT", itinerary, file_name="tripwise_plan.txt")

   

    # 🔁 Regenerate Option
    if st.button("🔁 Regenerate Plan"):
        itinerary = generate_itinerary(st.session_state.last_prompt)
        if itinerary:
            st.session_state.last_plan = itinerary
            st.rerun()

# --------- ❓ FAQ Section ---------------
with st.expander("❓ Frequently Asked Questions (FAQs)"):
    st.markdown("""
    **Q1: Is the travel plan accurate and bookable?**  
    A: The itinerary is AI-generated and meant as inspiration. Always verify transportation, accommodation, and activity details before booking.

    **Q2: Can I plan trips for multiple destinations?**  
    A: Yes! Just include all destinations in your prompt (e.g., “Plan a 10-day trip from Rome to Paris with stops in Switzerland”).

    **Q3: Does TripWise consider budget preferences?**  
    A: Not yet, but we're working on budget filters soon! For now, feel free to include budget info in your prompt (e.g., “a low-cost trip to Thailand”).

    **Q4: Can I customize trip themes (adventure, culture, food)?**  
    A: Absolutely! Tailor your prompt with preferences like “adventure activities”, “historic landmarks”, or “local food experiences”.

    **Q5: Is my personal data stored or shared?**  
    A: No. TripWise does not collect or store personal data. All queries are processed securely and anonymously.

    **Q6: What powers TripWise's travel recommendations?**  
    A: TripWise uses an agentic AI framework combining OpenAI's LLMs, prompt engineering, and modular tools for smart itinerary generation.

    **Q7: Can I use TripWise on mobile?**  
    A: Yes! The app is responsive and works smoothly on mobile browsers — perfect for travel planning on the go. 📱
    """)
