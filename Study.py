import streamlit as st
import pandas as pd
import time

st.title('Welcome to Indian Startup Analysis')
st.header('Startup Sectors')
st.subheader('Sector Analysis !')
st.write('Lets go...!')
st.markdown(""" ### My Favorite Startup
    - Zomato
    - Swige
    - Tomato
    - Dunzo
 """)

st.code(""" 
def fun(input):
    return fun**2

x = fun(2)
""")
st.latex('x^2 + y^2 + 4 = 0')

df = pd.DataFrame({
    'name': ['Mayur','Amit','Saket'],
    'marks': [50,80,70],
    'package': [10,20,14]
})
st.dataframe(df)
st.metric('Revenue','Rs 3L','3%')

st.json({
    'name': ['Mayur','Amit','Saket'],
    'marks': [50,80,70],
    'package': [10,20,14]
})
st.image('images/new-tata-tiago-price-in-india.jpg')
st.video('images/VID_20191102_183319.mp4')
st.audio('images/Dil-Se-Re-(RaagSong.Com).mp3')
st.sidebar.title('Select Category')
st.sidebar.markdown(""" ### My Favorite Startup
    - Zomato
    - Swige
    - Tomato
    - Dunzo
 """)

col1, col2 = st.columns(2)

with col1:
    st.image("images/new-tata-tiago-price-in-india.jpg")
    st.image("images/67d54c6b-5771-4694-b7bb-3d9cdfd85ca9.jpg")
    st.metric('Redme10s','Rs 13,720(Rs 14,000)','-20%')

with col2:
    st.image("images/new-tata-tiago-price-in-india.jpg")
    st.image("images/kv-last-239572.jpg.webp")
    st.metric('One Plus Nord 5','Rs 28,000(Rs 35,000)','-20%')  

st.sidebar.audio("images/VID_20191102_183319.mp4")  

st.error('Login Failed')
st.success('Login is Successful')
st.info('Change your email')
st.warning('3 unsuccessful attempts')

bar = st.progress(0)

for i in range(1,101):
    bar.progress(i)

#email = st.text_input('Enter email')
#number = st.number_input('Enter your age')
#st.date_input('Enter your birthdate')


email = st.text_input('Enter your email',placeholder='must have @ and .com')
password = st.text_input('Enter your password', type='password',placeholder='one capital atleast and no special charc')
gender = st.selectbox('Select Gender',['male','female','other'])

btn = st.button('Login')

# if button is pressed.
if btn:
    if email == 'abc@xyz.com' and  password == '1234':
        st.success('Login Successful')
        st.write(gender)
        st.balloons()
    else:
        st.error('Login Failed')

file = st.file_uploader('chose your csv file')
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())





