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
            st.write("Go to this [link](https://abdurafeyf-greenbee-1-greenbee-7v3jtl.streamlit.app/)")
        elif username.lower() == "srinivas.harnoor@vcinfotech.ae":
            st.write("Go to this [link](https://abdurafeyf-greenbee-2-greenbee-p3nwxs.streamlit.app/)")
        elif username.lower() == "rajesh.singh@vcinfotech.ae":
            st.write("Go to this [link](https://abdurafeyf-greenbee-web-greenbee-gok6fp.streamlit.app/)")
        else:
            pass