import random
import streamlit as st

st.title("🌐 나의 6주차 Open API 앱")
st.write("외부 데이터를 활용하여 정보를 보여주는 웹 서비스입니다.")

# 사용자 입력 받기
search_query = st.text_input("검색하고 싶은 키워드를 입력하세요:", "파이썬")

if st.button("데이터 조회하기"):
  st.success(f"'{search_query}'에 대한 검색 결과입니다!")

  # 예시 데이터 출력 (추후 Open API 연동 코드로 변경 가능)
  st.metric(label="조회된 데이터 수", value=f"{random.randint(10, 50)}건")
  st.write("---")
  st.write("1. 관련 트렌드 분석 완료")
  st.write("2. 실시간 API 연동 상태: 정상 작동 중")
