import streamlit as st
from PIL import Image


st.title('キムホンアプリ')
st.caption('これはキムホンの動画用のテストアプリです')

st.subheader('自己紹介')
st.text('Pythonに関する情報をYouTube上で発信しているPython VTuber キムホンです\n''宜しければチャンネル登録よろしくお願いします！')
code = ''''''
import streamlit as st
st.title('キムホン')
st.code(code,language='python')

#画像
Image = Image.open('./data/写真.jpg')
st.image(Image,width=400)

#動画
video_file = open('./data/動画.mp4','rb')
video_bytes = video_file.read()
st.video(video_bytes)