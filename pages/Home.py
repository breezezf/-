'''终龙の秘密基地'''
import streamlit as st
page = st.sidebar.radio('空间主页',['Furry','图像处理区','悄悄话'])

def Furry():
    '''Furry'''
    st.write('Furry，字面意思是穿戴毛皮的，毛茸茸的。')
    st.write('在亚文化层面，Furry特指“拟人化动物”同时也代指“兽迷”')
    st.image('Furry_1.png')
    with open('Music_1.mp3','rb') as f:
        Music_1 = f.read()
    st.audio(Music_1,format='audio/mp3',start_time=0)
def Image_Processing_Page():
    '''图像处理区'''
    pass

def Whisper_Page():
    '''悄悄话'''
    pass
             
if page == 'Furry':
    Furry()

if page == '图像处理区':
    Image_Processing_Page()

if page == '悄悄话':
    Whisper_Page()