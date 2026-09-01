import streamlit as st
import pandas as pd

# App Title
st.set_page_config(page_title="Tempo | Find Your Rhythm", page_icon="⏱️")
st.title("⏱️ Tempo")
st.subheader("Find Your Rhythm")

# User Input
user_input = st.text_area("What's on your plate this week?", 
    placeholder="Example: I have a biology test Friday, soccer practice Tuesday, and I want to work out 3 times.")

if st.button("Generate My Schedule"):
    if user_input:
        st.success("Tempo Engine is processing your schedule...")
        
        # Mocking the AI Output for the prototype
        data = {
            "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "Activity": ["History Essay Due", "Soccer Practice", "Workout (Flex)", "Soccer Practice", "Biology Test", "Workout (Flex)", "Workout (Flex)"],
            "Type": ["Academic", "Fixed", "Personal", "Fixed", "Academic", "Personal", "Personal"]
        }
        df = pd.DataFrame(data)
        st.table(df)
        
        st.info("💡 Tip: Tempo found a 2-hour gap on Wednesday for your interests!")
    else:
        st.warning("Please enter your tasks first!")
