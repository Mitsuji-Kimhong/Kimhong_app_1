import streamlit as st
import pandas as pd


#データ分析関連

df = pd.read_csv('./data/Test.csv')
st.dataframe(df)  #st.line_chart(df) 　# st.bar_chart(df['建築設計']) も可能