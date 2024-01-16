import streamlit as st
page = st.sidebar.radio("我的首页",["我感兴趣的","我的工具","我的智能词典","我的留言区"])
def page_1():
    st.write("666")
    
    if page =="我感兴趣的":
        page_1()

def page_2():
    st.write("666")
    if page =="我的工具":
        page_2()

def page_3():
    st.write("666")
    if page =="我的智能词典":
        page_3()

