'''我的主页'''
import streamlit as st

page = st.sidebar.radio('音游人の首页', ['观看视频', '公告', '帖群', '游戏推荐', '曲目推荐'])
def page_1():
    '''观看视频'''
    st.write('假设这里有一个视频.gif')
    dividing_line()
    st.write('该功能还未制作，敬请期待！！！')

def page_2():
    '''公告'''
    The_format_of_the_announcement('一只老咸鱼', '1.15', '15','50', '目前公告、帖群、游戏推荐以及曲目推荐已完全完成，有待补充，观看视频还未制作。这里的公告是写明制作进度以及音游新闻的。')
    The_format_of_the_announcement('一只老咸鱼', '1.15', '15','50', 'Phigros与Rataeno的再次联动将于19号开启。')

def page_3():
    '''帖群'''
    The_format_of_the_post('一只老咸鱼', '1.15', '15','50', '终于把帖子部分内容做好了我好高兴啊哈哈哈哈哈哈哈哈哈哈')
    The_format_of_the_post('一只老咸鱼', '1.15', '16','10', '目前除了观看视频以外其他项目均已完成。')
    
def page_4():
    '''游戏推荐'''
    st.write('非商业音游')
    Phigros()

def page_5():
    '''曲目推荐'''
    song_open('Nhelv', 'Silentroom', 'Silentroom - Nhelv.mp3', '静室的著名牛肉饭，是BOF:ET冠军曲，混乱的曲风配上BGA拥有十分独特的感受')
    song_open("Le Porteur d'Ombre", '黒皇帝、AKA', "黒皇帝、AKA - Le Porteur d'Ombre.mp3", '空灵的歌声加上较强烈的压迫感，不愧为黑皇帝的好速核')
    song_open('TECHNOPOLIS 2085', 'PRASTIK DANCEFLOOR', 'PRASTIK DANCEFLOOR - TECHNOPOLIS 2085.mp3', '魔性的人声采样让人欲罢不能')
    song_open("DESTRUCTION 3,2,1", 'Supa7onyz', "Supa7onyz - DESTRUCTION 3,2,1.mp3", '激烈的速核，谁家好歌每秒BPM3秒以上')
    song_open("Rrhar'il", 'Team Grimoire', "Team Grimoire - Rrhar'il.mp3", 'Phigros里最难的魔王曲，虽然听上去有种模板曲的感觉但仍然不失为一首好曲')
    # song_open("R.I.P", 'eicateve', "eicateve - R.I.P.", '无冕之王，歌曲旋律十分の优美')
    # song_open("NightTheater", 'わかどり', "わかどり - NightTheater.mp3", '曲师第一次参加BOF便获得了冠军，可以看出曲子的质量之高，是一首十分优美の钢琴曲')


# '''帖群函数库'''
def The_format_of_the_post(name, day, hour, minute, content):
    st.write('发帖人：',name)
    st.write('发帖时间：', day, hour, minute)
    st.write(content)
    dividing_line()

# '''公告函数库'''
def The_format_of_the_announcement(name, day, hour, minute, content):
    st.write('发布人：',name)
    st.write('公告发送时间：', day, hour, minute)
    st.write(content)
    dividing_line()

# '''游戏推荐函数库'''
def Phigros():
    st.write('Phigros')
    st.image('咕の封面图.jpg')
    st.write('《Phigros》是由南京鸽游网络有限公司（Pigeon Games）开发的一款非商业音乐节奏类游戏，可在 TapTap 和 App store下载。')
    st.write('游戏完全免费，无任何内购收费物品。运营方式为售卖游戏周边与玩家主动向开发者捐赠（也就是俗称的“用爱发电”）游戏的总策划"CN_115"（杜锐）在自己的捐赠渠道官方主页上表示：“《Phigros》是完全免费的游戏，每个成员用爱发电，并且游戏发布之后，不会向玩家收一分钱。”')
    st.write('《Phigros》的评分较高。截至2023/12/31，《Phigros》在App store平台上的12.2万个评价中，取得了4.7分（满分5分）的平均分 。即使是玩家较严格的TapTap平台，它也在7.6万个评价中，获得了9.7分 （满分10分）的平均分。')
    dividing_line()  

# '''曲目推荐函数库'''
def song_open(name, singer, music_file, reason):
    st.write('曲名：', name, '曲师：', singer)
    with open(music_file, 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write('推荐理由：', reason)
    dividing_line()


# '''通用函数库'''
def dividing_line():
    st.write('————————————————————————————————————————————————————')


if page == '观看视频':
    page_1()
elif page == '公告':
    page_2()
elif page == '帖群':
    page_3()
elif page == '游戏推荐':
    page_4()
elif page == '曲目推荐':
    page_5()