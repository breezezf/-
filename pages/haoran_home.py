'''我的主页'''
import streamlit as st
page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的电脑应用','我的游戏','我的留言区'])
def page_1():
    '''我的兴趣推荐'''
    with open('科目三.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    st.write('666')
    st.write('泰裤辣')
    st.write('科目三')
    st.write('画画')

if page == '我的兴趣推荐':
    page_1()
    
def page_2():
    '''我的电脑应用'''
    st.write('抖音，bilibili')

if page == '我的电脑应用':
    page_2()

def page_3():
    '''我的游戏'''
    st.write('暗区突围，香肠派对，火影忍者')

if page == '我的游戏':
    page_3()

def page_4():
    '''我的留言区'''
    st.write('无')

if page == '我的留言区':
    page_4()
    