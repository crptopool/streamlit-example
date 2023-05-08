from streamlit_extras.stateful_button import button

if button("Button 1", key="button1"):
    if button("Button 2", key="button2"):
        if button("Button 3", key="button3"):
            st.write("All 3 buttons are pressed")
