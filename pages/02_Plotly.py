
import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="🌍 글로벌 시가총액 TOP10 주가 분석", layout="wide")

st.markdown("""
# 🌍 글로벌 시가총액 TOP10 💹
지난 1년간 주요 기업 주가 변화 시각화
""")

# 🏆 TOP10 기업 리스트 (2025년 기준)
top10 = {
    "AAPL": "Apple",
    "MSFT": "Microsoft",
    "NVDA": "Nvidia",
    "AMZN": "Amazon",
    "GOOGL": "Alphabet",
    "META": "Meta Platforms",
    "BRK-B": "Berkshire Hathaway",
    "TSLA": "Tesla",
    "AVGO": "Broadcom",
    "LLY": "Eli Lilly"
}

st.sidebar.header("🔧 설정")
start_date = st.sidebar.date_input("시작일", datetime.today() - timedelta(days=365))
end_date = st.sidebar.date_input("종료일", datetime.today())

if start_date >= end_date:
    st.sidebar.error("👉 시작일은 종료일보다 빨라야 합니다!")
    st.stop()

# 📊 데이터 다운로드
@st.cache_data
def fetch_data(tickers, start, end):
    data = yf.download(list(tickers), start=start, end=end)["Adj Close"]
    return data

data = fetch_data(top10.keys(), start_date, end_date)

# ✅ Plotly 라인차트 생성
fig = px.line(data, labels={'value': '주가(USD)', 'Date': '날짜'}, title="📈 최근 1년간 종가 추이")

fig.update_layout(legend_title_text="기업", legend=dict(orientation="h", y=-0.2), hovermode="x unified")

st.plotly_chart(fig, use_container_width=True)

# 📋 요약 테이블 (최근 주가, 1년 전 대비 성과)
latest = data.iloc[-1]
one_year_ago = data.iloc[0]
change = (latest - one_year_ago) / one_year_ago * 100
summary = pd.DataFrame({
    "기업": [top10[t] for t in data.columns],
    "티커": data.columns,
    "최근 종가": latest.values,
    "1년 전 대비 상승률 (%)": change.values
}).round(2).sort_values("1년 전 대비 상승률 (%)", ascending=False)

st.header("📋 요약 성과")
st.dataframe(summary, use_container_width=True)
