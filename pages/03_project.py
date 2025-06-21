import streamlit as st
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import gpxpy
import simplekml
import tempfile
import re

# 구글 드라이브 인증
def authenticate():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # OAuth 인증
    drive = GoogleDrive(gauth)
    return drive

# '마라톤 코스' 폴더 ID 찾기 (폴더명으로 검색)
def find_marathon_folder_id(drive):
    file_list = drive.ListFile({'q': "mimeType='application/vnd.google-apps.folder' and title='마라톤 코스' and trashed=false"}).GetList()
    if len(file_list) == 0:
        return None
    return file_list[0]['id']

# 폴더 내 GPX 파일 목록 가져오기
def get_gpx_files_in_folder(drive, folder_id):
    query = f"'{folder_id}' in parents and trashed=false and title contains '.gpx'"
    file_list = drive.ListFile({'q': query}).GetList()
    return file_list

# 파일명에서 년도와 마라톤 이름 분리 (예: '2024고양하프.gpx' -> ('2024', '고양하프'))
def parse_filename(filename):
    # 확장자 제거
    base = filename.replace('.gpx', '')
    # 숫자(년도)와 문자(이름) 분리 (첫 숫자 시퀀스 + 나머지)
    match = re.match(r'(\d+)(.+)', base)
    if match:
        year, marathon_name = match.groups()
        return year, marathon_name
    else:
        return None, None

# GPX 파일을 KML로 변환
def gpx_to_kml(gpx_content):
    gpx = gpxpy.parse(gpx_content)
    kml = simplekml.Kml()
    for track in gpx.tracks:
        for segment in track.segments:
            coords = [(point.longitude, point.latitude) for point in segment.points]
            kml.newlinestring(name="Marathon Route", coords=coords)
    return kml.kml()

def main():
    st.title("마라톤 코스 GPX to Google Earth KML 변환기")

    drive = authenticate()
    folder_id = find_marathon_folder_id(drive)
    if not folder_id:
        st.error("구글 드라이브에 '마라톤 코스' 폴더를 찾을 수 없습니다.")
        return

    gpx_files = get_gpx_files_in_folder(drive, folder_id)
    if not gpx_files:
        st.warning("폴더에 GPX 파일이 없습니다.")
        return

    # 파일명에서 년도와 마라톤 이름 리스트 만들기
    data = []
    for f in gpx_files:
        year, marathon_name = parse_filename(f['title'])
        if year and marathon_name:
            data.append({'file': f, 'year': year, 'name': marathon_name})

    # 중복 제거 후 년도와 이름 선택 UI 만들기
    years = sorted(set(item['year'] for item in data))
    selected_year = st.selectbox("년도 선택", years)

    names = sorted(set(item['name'] for item in data if item['year'] == selected_year))
    selected_name = st.selectbox("마라톤 이름 선택", names)

    # 선택한 년도와 이름에 맞는 파일 찾기
    selected_files = [item['file'] for item in data if item['year'] == selected_year and item['name'] == selected_name]

    if selected_files:
        file = selected_files[0]
        # 파일 다운로드 및 읽기
        downloaded = drive.CreateFile({'id': file['id']})
        gpx_content = downloaded.GetContentString()

        # GPX -> KML 변환
        kml_str = gpx_to_kml(gpx_content)

        # KML 다운로드 버튼
        st.download_button(label="KML 파일 다운로드", data=kml_str, file_name=f"{selected_year}_{selected_name}.kml", mime="application/vnd.google-earth.kml+xml")

        # 구글 어스 웹 버전 링크로 KML 경로 보기 안내
        st.markdown("""
        **구글 어스 웹에서 KML 보기 방법**  
        1. [Google Earth 웹](https://earth.google.com/web/) 접속  
        2. 좌측 메뉴에서 '프로젝트' 선택  
        3. '불러오기' 클릭 후 다운로드한 KML 파일 업로드  
        """)

    else:
        st.warning("선택한 년도와 이름에 해당하는 파일이 없습니다.")

if __name__ == "__main__":
    main()
