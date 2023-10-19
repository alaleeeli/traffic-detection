import streamlit as st

st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/home.png')
st.title('YOLO V5 Traffic Detection App')
st.caption('This web application will detect traffic objects.')

st.markdown("""
### This App detects objects from Images
- Automatically detects 5 Traffic objects from an image.
- [Click here for App](/YOLO_for_images/)  

Below give are the object the our model will detect:
1. Person
2. Car
3. Bus
4. Bicycle
5. Truck
            """)
