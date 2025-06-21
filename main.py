import streamlit as st

# 🌈 페이지 설정
st.set_page_config(page_title="MBTI 성격 & 궁합 분석기 💖", page_icon="🌟", layout="wide")

# 🎉 타이틀
st.markdown("""
    <h1 style='text-align: center; color: #ff69b4;'>✨ MBTI 성격 분석 & 궁합 추천 ✨</h1>
    <h4 style='text-align: center; color: #6a0dad;'>MBTI로 나를 알고, 찰떡 궁합도 확인해보세요! 💫</h4>
""", unsafe_allow_html=True)

# 🎭 MBTI 선택
mbti_list = [
    "ISTJ 🛠️", "ISFJ 🧸", "INFJ 🌌", "INTJ 🧠",
    "ISTP 🧪", "ISFP 🎨", "INFP 📚", "INTP 🔍",
    "ESTP 🏍️", "ESFP 🎤", "ENFP 🚀", "ENTP 💡",
    "ESTJ 📋", "ESFJ 🤝", "ENFJ 🕊️", "ENTJ 👑"
]
mbti_selected = st.selectbox("📌 당신의 MBTI를 선택하세요:", mbti_list)
mbti_code = mbti_selected.split(" ")[0]

# 📘 성격 설명
mbti_traits = {
    "ISTJ": "📚 조용하고 신중하며 책임감이 강해요. 체계적이고 신뢰할 수 있는 관리자 스타일!",
    "ISFJ": "🧸 따뜻하고 헌신적인 보호자예요. 남을 잘 챙기고 협력적인 성향이 강해요!",
    "INFJ": "🌌 통찰력 있고 창의적인 조용한 이상주의자예요. 세상을 더 좋게 만들고 싶어 해요!",
    "INTJ": "🧠 독립적이고 분석적인 전략가예요. 목표 지향적이고 효율성을 중요시해요!",
    "ISTP": "🛠️ 현실적이고 논리적인 탐험가예요. 즉흥적이며 손재주가 뛰어나요!",
    "ISFP": "🎨 감성적이고 조용한 예술가예요. 감정이 풍부하고 자연을 사랑해요!",
    "INFP": "📚 이상과 가치 중심의 중재자예요. 깊이 있는 감성과 상상력을 갖고 있어요!",
    "INTP": "🔍 지적인 탐험가예요. 호기심이 많고 새로운 아이디어를 추구해요!",
    "ESTP": "🏍️ 활동적이고 에너지 넘치는 해결사예요. 직접 뛰어드는 걸 좋아해요!",
    "ESFP": "🎤 삶을 즐기며 사람들과 어울리는 걸 좋아하는 자유로운 영혼이에요!",
    "ENFP": "🚀 창의적이고 열정적인 활동가예요. 새로운 것에 대한 열망이 넘쳐요!",
    "ENTP": "💡 아이디어가 넘치는 토론가예요. 빠르게 사고하고 말도 잘해요!",
    "ESTJ": "📋 조직적이고 현실적인 리더예요. 책임감 있고 실용적이에요!",
    "ESFJ": "🤝 따뜻하고 친절한 외교관이에요. 모두가 잘 지내도록 도와줘요!",
    "ENFJ": "🕊️ 리더십 있고 헌신적인 사람입니다. 타인의 잠재력을 끌어내요!",
    "ENTJ": "👑 대담하고 효율적인 지휘관이에요. 야망 있고 목표 중심이에요!"
}

# 💕 궁합 추천
mbti_compatibility = {
    "ISTJ": ["ISFP 🎨", "ESFP 🎤"],
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

# 📋 출력
st.markdown("---")
st.subheader(f"🔍 {mbti_selected}의 성격 분석")

st.markdown(f"""
### {mbti_traits[mbti_code]}
""")

st.markdown("### 💞 어울리는 궁합 MBTI:")

for pair in mbti_compatibility.get(mbti_code, []):
    st.markdown(f"- {pair}")

# 👣 하단
st.markdown("""
    <hr>
    <div style='text-align: center; font-size: 18px;'>
        🎯 <b>MBTI 궁합으로 친구, 연인, 동료까지 더 잘 이해해요!</b><br>  
        💖 심리 기반 소통으로 행복한 관계를 만들어보세요!
    </div>
""", unsafe_allow_html=True)
