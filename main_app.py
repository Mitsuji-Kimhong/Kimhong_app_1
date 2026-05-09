import streamlit as st
from PIL import Image
import datetime
import pandas as pd

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

with st.form(key='profile_form'):

    #テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')

    #セレクトボックス または　ラジオ ボタン
    age_category = st.radio('年齢層',('子供(18歳未満)','大人(18歳以上)')) 
    #st.selectbox or st.radio

    #複数選択
    hobby = st.multiselect('趣味',('スポーツ','読書','プログラム','アニメ・映画','釣り','料理'))

    #チェックボックス
    mail_subscribe = st.checkbox('メールマガジンを購読する')

    #スライダー
    height = st.slider('身長',min_value=110,max_value=210)

    #日付
    start_date = st.date_input('開始日', datetime.date(2026,5,6))

    #カラーピッカー
    color = st.color_picker('テーマカラー','#00f900')

    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'ようこそ！{name}さん！{address}に書籍を送りました！')
        st.text(f'年齢層:{age_category}')
        st.text(f'趣味:{",".join(hobby)}')


#データ分析関連

df = pd.read_csv('./data/Test.csv')
st.dataframe(df)  #st.line_chart(df) 　# st.bar_chart(df['建築設計']) も可能