'''主页'''
import streamlit as st
page = st.sidebar.radio('主页',['科技普及','技术搜索','留言区(评价与建议)'])
def page1():
    '''科技普及'''
    st.write("航空航天-深空探测")
    st.write("离子推进器-星际之门的钥匙")
    with open('马一航_离子推进器.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    st.image('马一航_离子推进器.jpg')
    pass
if page == '科技普及':
    page1()
def page2():
    '''技术搜索'''
    pass

def page3():
    '''留言区(评价与建议)'''
    st.write("在这里留下你的痕迹吧，但请友善留言，恶语伤人心！")
    pass
if page == '留言区(评价与建议)':
    page3()