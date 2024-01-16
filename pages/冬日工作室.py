'''我的主页'''
import streamlit as st

page = st.sidebar.radio('雪球 Snow Ball', ['热门视频', '游戏分区', '生活分区', '学习分区', '我的视频网站账号'])
def page_1():
    #热门视频
    st.write('雪球的游戏视频推荐')

def page_2():
    #游戏分区
    st.write('雪球的太空杀')
    st.write('-------------------------------------------------------------')
    st.write('雪球的我的世界')
    st.write('-------------------------------------------------------------')
    st.write('雪球的忍者必须死3')
    st.write('-------------------------------------------------------------')
    st.write('雪球的其他游戏')

def page_3():
    #生活分区
    st.write('雪球的生活频道')

def page_4():
    #学习分区
    st.write('雪球的学习频道')
    st.write('猫武士')

def page_5():
    #我的视频网站账号
    st.write('网站账号：')
    st.write('bilibili游戏和生活频道：爱过圣诞的雪球')
    st.write('bilibili学习频道：一颗量子爱摸鱼')
    st.write('bilibili猫武士频道：木寸民的农场主')
    
if page == '热门视频':
    page_1()
elif page == '游戏分区':
    page_2()
elif page == '生活分区':
    page_3()
elif page == '学习分区':
    page_4()
else:
    page_5()