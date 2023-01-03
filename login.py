import streamlit as st

userpass = {
    "aziz.basha@vcinfotech.ae": "Yamaha9394",
    "srinivas.harnoor@vcinfotech.ae": "Sri@123",
    "rajesh.singh@vcinfotech.ae": "Rajes@321"
}
username = st.text_input('Username')
password = st.text_input('Password', type="password")
for key in userpass:
    if key == username.lower() and userpass[key] == password:
        if username.lower() == "aziz.basha@vcinfotech.ae":
            st.write("Go to this [link](https://azizzbasha-greenbee-greenbee-wp0mzt.streamlit.app/)")
        elif username.lower() == "srinivas.harnoor@vcinfotech.ae":
            st.write("Go to this [link](https://azizzbasha-greenbee-2-greenbee-nmcrlc.streamlit.app/)")
        elif username.lower() == "rajesh.singh@vcinfotech.ae":
            st.write("Go to this [link](https://azizzbasha-greenbee-1-greenbee-ga2xrq.streamlit.app/)")
        else:
            pass