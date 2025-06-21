import streamlit as st
import gpxpy
import folium
from streamlit_folium import st_folium
import requests
from io import BytesIO

st.set_page_config(page_title="마라톤 코스 선택 & 지도 시각화", layout="wide")
st.title("📅년도 & 🏃‍♂️ 마라톤 코스 선택 후 지도 시각화")

# 예시: 구글 드라이브에 공개된 GPX 파일들의 URL과 파일명 딕셔너리 (실제 사용 시 여기에 직접 URL과 이름 넣기)
# 예) "파일명": "공개다운로드링크"
gpx_files_info = {
    "2024고양하프.gpx": "https://drive.google.com/uc?export=download&id=드라이브파일ID1",
    "2023서울마라톤.gpx": "https://drive.google.com/uc?export=download&id=드라이브파일ID2",
    "2024부산마라톤.gpx": "https://drive.google.com/uc?export=download&id=드라이브파일ID3",
    # 더 추가 가능
}

# 1. 파일명에서 년도, 마라톤 이름 추출
file_data = []
for fname in gpx_files_info.keys():
    if fname.lower().endswith(".gpx"):
        year = ''.join(filter(str.isdigit, fname[:4]))  # 앞 4글자 중 숫자만 추출, 예: 2024
        marathon_name = fname[4:].replace(".gpx", "")   # 나머지 부분에서 확장자 제거
        file_data.append((year, marathon_name, fname))

# 2. Streamlit 선택 UI
years = sorted(set([item[0] for item in file_data]))
selected_year = st.selectbox("📅 년도 선택", options=years)

marathon_names_for_year = [item[1] for item in file_data if item[0] == selected_year]
selected_marathon = st.selectbox("🏃‍♂️ 마라톤 선택", options=marathon_names_for_year)

# 3. 선택된 파일명 찾기
selected_file = None
for y, m_name, fname in file_data:
    if y == selected_year and m_name == selected_marathon:
        selected_file = fname
        break

if selected_file:
    # 4. GPX 파일 다운로드 & 파싱
    url = gpx_files_info[selected_file]
    response = requests.get(url)
    gpx = gpxpy.parse(BytesIO(response.content))

    coords = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                coords.append((point.latitude, point.longitude))

    if coords:
        # 지도 생성
        m = folium.Map(location=coords[0], zoom_start=13)
        folium.PolyLine(coords, color="blue", weight=5, opacity=0.8, tooltip=f"{selected_year} {selected_marathon}").add_to(m)

        st.subheader("🗺️ 마라톤 코스 지도")
        st_folium(m, width=800, height=600)
    else:
        st.warning("해당 GPX 파일에서 위치 정보를 찾을 수 없습니다.")
else:
    st.info("년도와 마라톤을 선택해주세요.")
