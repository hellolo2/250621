import streamlit as st
from streamlit_lottie import st_lottie
import requests

# ------------------------------------
# 🎬 애니메이션 로딩 함수
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ------------------------------------
# 🌈 페이지 설정
st.set_page_config(
    page_title="MBTI 진로 추천기 💼",
    page_icon="🧬",
    layout="wide"
)

# ------------------------------------
# 💖 타이틀
st.markdown("""
    <h1 style='text-align: center; color: #ff69b4;'>🌟 MBTI 기반 진로 추천 사이트 🌟</h1>
    <h3 style='text-align: center; color: #8a2be2;'>성격 유형에 맞는 꿈을 찾아볼까요? ✨</h3>
""", unsafe_allow_html=True)

# ------------------------------------
# 🎭 MBTI 선택
mbti_types = [
    'ISTJ 🛠️', 'ISFJ 🧸', 'INFJ 🌌', 'INTJ 🧠',
    'ISTP 🧪', 'ISFP 🎨', 'INFP 📚', 'INTP 🔍',
    'ESTP 🏍️', 'ESFP 🎤', 'ENFP 🚀', 'ENTP 💡',
    'ESTJ 📋', 'ESFJ 🤝', 'ENFJ 🕊️', 'ENTJ 👑'
]
mbti = st.selectbox("📌 당신의 MBTI를 선택하세요:", mbti_types)

# ------------------------------------
# 🔍 선택한 MBTI 코드 추출
selected_code = mbti.split(" ")[0]

# ------------------------------------
# 🎁 직업 추천 리스트
jobs = {
    "ISTJ": ["📊 회계사", "🏢 공무원", "🔧 엔지니어"],
    "ISFJ": ["🩺 간호사", "📚 사서", "👶 유치원 교사"],
    "INFJ": ["🧘‍♀️ 심리상담가", "✍️ 작가", "🌱 사회운동가"],
    "INTJ": ["💻 데이터 사이언티스트", "📈 전략 컨설턴트", "🧪 연구원"],
    "ISTP": ["🔧 정비사", "🕹️ 게임 디자이너", "🚔 경찰"],
    "ISFP": ["🎨 일러스트레이터", "🧵 패션 디자이너", "🎶 작곡가"],
    "INFP": ["📖 시인", "🧝‍♀️ 판타지 작가", "🎭 배우"],
    "INTP": ["🧬 과학자", "👨‍💻 개발자", "🔬 분석가"],
    "ESTP": ["🎯 마케터", "🧗 트레이너", "🎮 스트리머"],
    "ESFP": ["🎤 가수", "📸 유튜버", "🎉 이벤트 플래너"],
    "ENFP": ["🚀 창업가", "🎈 크리에이터", "🦄 브랜딩 디렉터"],
    "ENTP": ["💡 아이디어 뱅크", "📢 광고기획자", "🧠 컨셉 디자이너"],
    "ESTJ": ["📋 관리자", "🛠️ 프로젝트 매니저", "🏗️ 건축 관리자"],
    "ESFJ": ["👩‍🏫 교사", "🏥 병원 행정직", "👗 쇼핑몰 운영자"],
    "ENFJ": ["🕊️ NGO 활동가", "🎤 발표자", "👥 HR매니저"],
    "ENTJ": ["👑 CEO", "📈 투자 분석가", "⚖️ 법률가"],
}

recommended_jobs = jobs.get(selected_code, [])

# ------------------------------------
# ✨ 애니메이션 선택
if selected_code in ["INFP", "INFJ", "ISFP", "ENFP"]:
    lottie_url = "https://assets3.lottiefiles.com/packages/lf20_j1adxtyb.json"  # 감성적
elif selected_code in ["INTJ", "INTP", "ENTJ"]:
    lottie_url = "https://assets2.lottiefiles.com/packages/lf20_gnb0jsok.json"  # 분석적
else:
    lottie_url = "https://assets4.lottiefiles.com/packages/lf20_kkflmtur.json"  # 일반 환영

lottie_json = load_lottie_url(lottie_url)

# ------------------------------------
# 💫 애니메이션 출력
st_lottie(lottie_json, height=300, key="mbti_anim")

# ------------------------------------
# 🎯 추천 결과 출력
st.markdown("---")
st.subheader(f"💼 {mbti} 유형에게 어울리는 직업 추천")

for job in recommended_jobs:
    st.markdown(f"### {job}")

# ------------------------------------
# 👣 하단 안내
st.markdown("""
    <hr>
    <div style='text-align: center; font-size: 18px;'>
        Made with ❤️ by <b>진로마스터봇</b> | 당신의 미래를 함께 응원해요! 🌈
    </div>
""", unsafe_allow_html=True)
