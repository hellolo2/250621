import streamlit as st
import pandas as pd

st.title("대기질 데이터 간단 탐색기")

# CSV 파일 URL (로그인 없이 바로 접근 가능한 공개 URL)
csv_url = "https://github.com/250621/seoul cultural space.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(csv_url)
    return df

df = load_data()

st.write("### 데이터 미리보기")
st.dataframe(df.head())

# 컬럼 선택
column = st.selectbox("분석할 컬럼 선택", df.columns)

st.write(f"### '{column}' 컬럼 통계 정보")
st.write(df[column].describe())

st.write(f"### '{column}' 컬럼 값 분포")
st.bar_chart(df[column].value_counts().sort_index())
