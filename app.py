import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍱")

st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("버튼을 누르면 오늘 먹을 점심 메뉴를 랜덤으로 골라드립니다!")

# 추천할 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가/수정하세요)
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈까스",
    "초밥",
    "짜장면",
    "짬뽕",
    "국밥",
    "햄버거",
    "파스타",
    "쌀국수",
    "마라탕",
    "비빔밥",
    "칼국수",
    "샌드위치",
]

# 버튼을 눌렀을 때 실행될 동작
if st.button("🎲 점심 메뉴 추천받기", use_container_width=True):
  # 리스트에서 무작위로 하나 선택
  selected_menu = random.choice(lunch_menus)

  # 결과 출력
  st.success(f"오늘의 추천 메뉴는 **{selected_menu}**입니다! 맛있게 드세요 😋")
  st.balloons()  # 축하 풍선 효과
