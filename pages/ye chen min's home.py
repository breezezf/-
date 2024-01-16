import streamlit as st


page = st.sidebar.radio('我的世界指令', ['设置', '基础指令知识', '/advancement:获取或移除成就', '/worldborder：世界边界', '/kill：清除实体', '/seed：种子', '/loacate：寻找遗迹'])
def option():
    with open('蕊蕊蕊蕊！ - 天堂岛之歌.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
def a_1():
    st.write('基础指令知识')
def a_2():
    st.write('获取或移除成就')
def a_3():
    st.write('世界边界')
def a_4():
    st.write('清除实体')
def a_5():
    st.write('世界种子')
def a_6():
    st.write('寻找遗迹')

if page == '设置':
    option()
if page == '基础指令知识':
    a_1()
if page == '/advancement:获取或移除成就':
    a_2()
if page == '/worldborder：世界边界':
    a_3()
if page == '/kill：清除实体':
    a_4()
if page == '/seed：种子':
    a_5()
if page =='/loacate：寻找遗迹':
    a_6()