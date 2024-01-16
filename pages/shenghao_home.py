'''我的主页'''
import streamlit as st
page = st.sidebar.radio('我的首页',['音乐推荐','GCK系列游玩','我的图片处理工具','我的智慧词典','我的留言区'])
def page_1():
    with open('不问别离.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    st.write('不问别离')
    
def page_2():
    st.write('GCK-训练场')
    st.image("GCK训练场封面.png")    
    st.write('https://shequ.codemao.cn/work/204769028'+ '   ↑')

    st.write('GCK-起源')
    st.write('https://shequ.codemao.cn/work/211624435')



if page=='音乐推荐':
    page_1()
if page=='GCK系列游玩':
    page_2()