# music_homepage
<aside>
💡 링크

</aside>

[뮤직뮤직](http://54.180.26.66:8000/ssac/main)

***서울산업진흥원 SBA (SSAC 3기) 교육***

- 🏆 ***개인프로젝트*** ***우수상 수상(4위)***

<aside>
💡 메인화면

</aside>

![스크린샷 2021-12-14 오후 10.18.24.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/998874f1-8947-4a83-90eb-0adefa487b34/스크린샷_2021-12-14_오후_10.18.24.png)

# Music **- 개인프로젝트**

> 음악 사이트를 만들어보았습니다.
> 

## **💡 프로젝트 구상 계기**

평소 노래듣기를 즐겨하기에, 나만의 음악사이트를 만들어보자 생각하였고, 만들어보았습니다.

## **📑 프로젝트 레이아웃**

- 뮤직 메인페이지
- 뮤직차트
- 최신음악
- 장르별
- 뮤직비디오
- 마이페이지

## **🛠 기술 스택**

- 프론트 : Html, Css, JavaScript
- 백앤드 : Python, Django
- 크롤링 : BeautifulSoup, Bs4

## **💎 미리보기**

1. 메인화면
    
    ![스크린샷 2021-12-14 오후 11.32.10.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/922b8fba-893a-4a31-89b8-b8c3c561a3ed/스크린샷_2021-12-14_오후_11.32.10.png)
    

→ 카드형식 앨범모양 호버시 해당 제목과 앨범이름 보이기.

1. 실시간 차트
    
    ![스크린샷 2021-12-14 오후 11.19.14.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/93722ea5-8f37-43eb-b944-d6932e9bad9c/스크린샷_2021-12-14_오후_11.19.14.png)
    

 → 멜론 차트에서 크롤링한 데이터를 DB에 넣은 후  실시간 차트에 반영.

 → audio태그를 이용해 해당 음악 플레이 가능.

1. 회원가입
    
    ![스크린샷 2021-12-14 오후 11.28.33.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fab2b944-c929-4827-a4f1-4b1a0adc80c0/스크린샷_2021-12-14_오후_11.28.33.png)
    

 → id 중복 시 DB에서 존재확인 후 메세지 출력.

 → password 일치 여부 확인.

1. 마이페이지
    
    ![스크린샷 2021-12-14 오후 11.40.34.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5cf26afb-b63e-49f0-b246-3b5abf4d8833/스크린샷_2021-12-14_오후_11.40.34.png)
    

  → 해당 섹션에 마우스 호버시 메뉴 텍스트 보이기

![스크린샷 2021-12-14 오후 11.27.05.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c71c3825-2eb0-433c-ac8c-c065d8f6f115/스크린샷_2021-12-14_오후_11.27.05.png)

 → 회원정보, 비밀번호 변경

 → 회원 탈퇴

1. Top 100
    
    ![스크린샷 2021-12-14 오후 11.27.54.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3c1227b1-c2f5-4838-ae0b-b9ca2d216e00/스크린샷_2021-12-14_오후_11.27.54.png)
    

 → DB에 있는 크롤링한 데이터를 받아와 출력

![스크린샷 2021-12-14 오후 11.27.32.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bf02e4b1-8306-4e14-9621-bf15e6901b20/스크린샷_2021-12-14_오후_11.27.32.png)

 → 곡 선택 후 추가하기 버튼 클릭 시 마이리스트에 담김

![스크린샷 2021-12-14 오후 11.28.00.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5782f0dd-6d89-4544-9548-33788c0612a1/스크린샷_2021-12-14_오후_11.28.00.png)

→ 추가된 것을 확인할 수 있다.
