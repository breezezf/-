import streamlit as st

page = st.sidebar.radio("我的首页",["s","c","d","e"])

def ps_1():
    '''我的推荐'''
    with open('霞光.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=1)
    st.image('slogan.png')
    st.write('我的s荐')
    st.write('-----------------------------')
    st.write('我的游戏推荐')
    st.write('-----------------------------')
    st.write('我的书籍推荐')
    st.write('-----------------------------')
    st.write('我的习题集推荐')
    st.write('-----------------------------')
if page == 'c':
    ps_1()