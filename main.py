import streamlit as st
from streamlit_lottie import st_lottie
import requests

# ------------------------------------
# 🎬 Lottie 애니메이션 로더
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ------------------------------------
# 🌈 페이지 설정
st.set_page_config(page_title="MBTI 성격 & 궁합 분석기 💖", page_icon="🌟", layout="wide")

# ------------------------------------
# 🎉 타이틀
st.markdown("""
    <h1 style='text-align: center; color: #ff69b4;'>🌟 MBTI 성격 분석기 & 궁합 추천 🌟</h1>
    <h4 style='text-align: center; color: #8a2be2;'>MBTI로 나를 알고, 친구와의 궁합까지 확인해보세요! 🔍💞</h4>
""", unsafe_allow_html=True)

# ------------------------------------
# 🎭 MBTI 리스트
mbti_list = [
    "ISTJ 🛠️", "ISFJ 🧸", "INFJ 🌌", "INTJ 🧠",
    "ISTP 🧪", "ISFP 🎨", "INFP 📚", "INTP 🔍",
    "ESTP 🏍️", "ESFP 🎤", "ENFP 🚀", "ENTP 💡",
    "ESTJ 📋", "ESFJ 🤝", "ENFJ 🕊️", "ENTJ 👑"
]
mbti_selected = st.selectbox("📌 당신의 MBTI를 선택하세요:", mbti_list)
mbti_code = mbti_selected.split(" ")[0]

# ------------------------------------
# 📘 MBTI 성격 설명
mbti_traits = {
    "ISTJ": "💼 책임감 강하고 현실적인 관리자 스타일. 정해진 규칙과 시스템을 잘 따르며 계획적인 성격!",
    "ISFJ": "🧸 배려심 깊고 조용하지만 친절한 도우미. 타인을 챙기며 헌신적인 성향이 돋보여요!",
    "INFJ": "🌌 깊이 있는 사고와 통찰력을 가진 조용한 비전가. 이상주의자이며 사람들을 도우려는 성향이 강해요!",
    "INTJ": "🧠 논리적이고 전략적인 마스터마인드. 미래를 내다보는 계획 능력이 뛰어나요!",
    "ISTP": "🔧 즉흥적이지만 침착한 탐험가. 문제 해결에 강하고 손재주가 뛰어난 성격이에요!",
    "ISFP": "🎨 예술 감각이 풍부하고 조용한 자유인. 평화를 사랑하고 감정이 풍부해요!",
    "INFP": "📚 이상주의자이자 감성적인 중재자. 깊은 공감능력을 갖춘 아름다운 영혼!",
    "INTP": "🔍 호기심 많은 사색가. 새로운 아이디어와 이론 탐구를 좋아해요!",
    "ESTP": "🏍️ 에너지 넘치는 활동가. 현실적인 문제를 즉시 해결하며 모험을 즐겨요!",
    "ESFP": "🎤 무대 위 스타. 삶을 즐기고 주변에 긍정 에너지를 퍼뜨리는 분위기 메이커!",
    "ENFP": "🚀 자유로운 영혼의 열정가. 창의적이고 사람들과 함께할 때 에너지를 얻어요!",
    "ENTP": "💡 아이디어 뱅크. 빠른 사고와 논쟁을 즐기는 창의적인 혁신가!",
    "ESTJ": "📋 체계적이고 실용적인 리더. 조직적이고 책임감이 뛰어난 스타일!",
    "ESFJ": "🤝 친절하고 협동적인 사람. 조화를 중요시하고 타인을 잘 챙겨요!",
    "ENFJ": "🕊️ 따뜻한 카리스마 리더. 사람들을 이끄는 데 능숙하고 배려심이 깊어요!",
    "ENTJ": "👑 전략적이고 결단력 있는 지도자. 도전 정신과 야망이 넘치는 카리스마!"
}

# ------------------------------------
# 💞 궁합 추천
mbti_compatibility = {
    "ISTJ": ["ESFP 🎤", "ISFP 🎨"],
    "ISFJ": ["ESTP 🏍️", "ESFP 🎤"],
    "INFJ": ["ENFP 🚀", "INFP 📚"],
    "INTJ": ["ENFP 🚀", "ENTP 💡"],
    "ISTP": ["ESFJ 🤝", "ISFJ 🧸"],
    "ISFP": ["ESTJ 📋", "ESFJ 🤝"],
    "INFP": ["ENFJ 🕊️", "INFJ 🌌"],
    "INTP": ["ENTP 💡", "INTJ 🧠"],
    "ESTP": ["ISFJ 🧸", "ESFJ 🤝"],
    "ESFP": ["ISTJ 🛠️", "ISFJ 🧸"],
    "ENFP": ["INFJ 🌌", "INTJ 🧠"],
    "ENTP": ["INTP 🔍", "INFJ 🌌"],
    "ESTJ": ["ISFP 🎨", "INFP 📚"],
    "ESFJ": ["ISFP 🎨", "ISTP 🧪"],
    "ENFJ": ["INFP 📚", "ISFP 🎨"],
    "ENTJ": ["INTP 🔍", "ENFP 🚀"]
}

# ------------------------------------
# 🎨 애니메이션
lottie_url = "https://assets7.lottiefiles.com/packages/lf20_xlmz9xwm.json"
lottie_json = load_lottie_url(lottie_url)

st_lottie(lottie_json, height=300, key="mbti_lottie")

# ------------------------------------
# 📋 출력
st.markdown("---")
st.subheader(f"🧠 {mbti_selected}의 성격 분석")

st.markdown(f"""
### {mbti_traits[mbti_code]}  
""")

st.markdown("### 💞 어울리는 MBTI 궁합 추천:")
for pair in mbti_compatibility.get(mbti_code, []):
    st.markdown(f"- {pair}")

# ------------------------------------
# 👣 하단
st.markdown("""
    <hr>
    <div style='text-align: center; font-size: 18px;'>
        💡 <b>MBTI 궁합으로 관계를 더 가깝게!</b>  
        <br>🔮 나를 알고, 서로를 이해하는 시간 🌈
    </div>
""", unsafe_allow_html=True)
