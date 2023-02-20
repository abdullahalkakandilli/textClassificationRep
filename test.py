new_line = "\n"
shows_list = shows.iloc[:, 0].tolist()
shows_list_head = shows.iloc[:, 0].head(3).tolist()

pre_defined_keyphrases = shows_list_head



with st.form("my_form"):
    with st.expander("test expander"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

with st.form("my_form"):
    st.write("Inside the form")
    with st.expander("test expander"):
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")