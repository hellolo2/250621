import streamlit as st

# -------------------------------
# 🎨 스타일 설정
st.set_page_config(
    page_title="MBTI 직업 추천기 🎓",
    page_icon="🧬",
    layout="wide"
)

# -------------------------------
# 🌟 헤더
st.markdown("""
    <h1 style='text-align: center; color: #ff69b4;'>🌟 MBTI 기반 진로 추천 사이트 🌟</h1>
    <h3 style='text-align: center; color: #8a2be2;'>당신의 성격 유형에 딱 맞는 직업은 무엇일까요? 🤔</h3>
""", unsafe_allow_html=True)

# -------------------------------
# 🎯 MBTI 선택
mbti_types = [
    'ISTJ 🛠️', 'ISFJ 🧸', 'INFJ 🌌', 'INTJ 🧠',
    'ISTP 🧪', 'ISFP 🎨', 'INFP 📚', 'INTP 🔍',
    'ESTP 🏍️', 'ESFP 🎤', 'ENFP 🚀', 'ENTP 💡',
    'ESTJ 📋', 'ESFJ 🤝', 'ENFJ 🕊️', 'ENTJ 👑'
]
mbti = st.selectbox("🎭 당신의 MBTI를 선택하세요:", mbti_types)

# -------------------------------
# 📊 직업 추천 딕셔너리
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

# -------------------------------
# 🔍 선택한 MBTI에서 코드 추출
selected_code = mbti.split(" ")[0]
recommended_jobs = jobs.get(selected_code, [])

# -------------------------------
# 🎁 결과 출력
st.markdown("---")
st.subheader(f"✨ {mbti} 유형에게 어울리는 직업 ✨")

for job in recommended_jobs:
    st.markdown(f"### {job}")

# -------------------------------
# 🎨 하단 꾸미기
st.markdown("""
    <div style='text-align: center; font-size: 18px; margin-top: 50px;'>
        Made with ❤️ by <b>진로마스터봇</b> | MBTI로 나를 알아가요! 🌈
    </div>
""", unsafe_allow_html=True)
