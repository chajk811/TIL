html 은 프로그래밍 언어가 아님

단순히 텍스트를 보여주기 위한 markup 이다.(css도)

브라우져 언어중에 자바스크립트만 프로그래밍 언어



웹 표준 W3C/ WHATWG



익스플로러를 웹 브라우져로 인정하지 않는 이유

웹표준을 지키지 않음

모바일 대응 하지 않음

성능 개선 X, 느림



모든 사용자가 같은 브라우져를 사용하는게 아니기 때문에 IE에도 어느정도 대응을 해야 함.

=> Cross Browsing



빠른 설정

! + Tab



1. 들여쓰기 2칸

2. 속성값에는 반드시 큰 따옴표 사용

3. 태그, 속성, 속성값 등에는 모두 소문자만 사용

4. 최상위 html 태그에는 lang  속성을 주어 문서의 기본 언어를 지정한다.(스크린리더는 lang을 통해 언어를 인식하여 자동으로 음성을 변환하거나 해당 언어에 적합한 발음을 제공한다.)

5. IE 는 특정 META 태그를 사용해 페이지가 특정 버전에 맞게 세팅 되도록 지정한다.

   ```html
   <meta http-equiv="X-UA-Compatible" content="ie=edge">
   ```

6.  = 사이는 띄우지 않는다.

7. <!--주석내용--> ctrl +/

8.  ctrl + l : 한줄 선택

9. crtl + alt +b : beautify 익스텐션 키설정 해놓음
   1. 익스텐션 beautify 설치
   2. ctrl + Alt + p
   3. Keyword shortcuts

10. h1 태그는 한페이지에 한개만

11. strong => semantic 강조의 의미 부여

12. Alt + Shift + 아래위 방향키

13. 멀티커서 : ctrl + alt 아래위 방향키 

14. boolean 속성 값은 따로 명시하지 않는다.

    ```html
    <!-- good -->
    <input type="radio" checked>
    
    <!-- bad -->
    <input type="radio" checked="true">
    ```

    

검색 엔진 최적화 (SEO)  시메틱 테그 잘 지켜서 작성했을 시
