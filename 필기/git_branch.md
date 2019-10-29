브랜치(나뭇가지의 비유적 표현)

git 브랜치는 매우 가볍다.

순식간에 브랜치를 만들고 브랜치 사이를 이동할 수 있다.

git  이 가지고온 혁신 중 하나는 브랜치 기능을 매우 쓸만한 수준까지 만들었다는 것.



`feature branch workflow`

Pull request

- 기능 개발을 끝내고 master에 바로 병합시키는게 아니라, 브랜치를 중앙 원격 저장소에 올리고(push) master 에 병합을 요청(merge)

- 주의 사항
  - 중앙에서 병합을 했다면 , 다른 팀원들은 master 브랜치를 pull 받아야 한다.



## 상황 1.fast-forwark

1. feature/test branch 이동

   ```bash
   $ git checkout -b feature/test
   $ (feature/test)
   ```

2. 작업 완료 후 commit

   ```bash
   touch test.md
   git add .
   git commit -m "Complete test.md"
   ```

3. master 이동

   ```bash
   git checkout master
   $ (master)
   ```

4. master에 병합

   ```bash
   git merge feature/test
   ```

5. 결과

   - 단순히 HEAD 가 최신 COMMIT 으로 이동
   - feature/test branch 생성 이후 master branch 의 이력에 변화가 없었기 때문

6. branch 삭제

   ```bash
   $ git branch -d feature/test
   ```

------

### 2. merge commit 

1. feature/login branch 이동

   ```bash
   $ git checkout -b feature/login 
   ```

2. 작업 완료 후 commit

   ```bash
   $ touch login.md
   $ git add .
   $ git commit -m "complete login.md"
   ```

3. master 로 이동

   ```bash
   $ git checkout master
   ```

4. master 에 추가 commit 생성

   ```bash
   $ touch master.md
   $ git add .
   $ git commit -m "fix master.md"
   ```

5. master 에 병합

   ```bash
   $ git merge feature/login
   ```

6. 자동으로 merge commit 발생

   ```bash
   Merge branch 'feature/login'
   
   # Please enter a commit ...
   ...
   ```

   - Vim 에디터로 열림
   - 메세지를 수정하고자하면 `i` 로 편집 모드로 바꾼다음에 COMMIT 을 수정하고
   - `esc` + `:wq` 를 통해 저장 및 종료

7. commit 그래프 확인하기

   ```bash
   $ git log --oneline --graph
   ```

   ```bash
   *   2743900 Merge branch 'feature/login'
   |\
   | * 29a92c0 Complete login.txt
   | * 38e2723 Complete signout.txt
   * | 278eaf5 Make master.txt
   |/
   * a52a916 complete test.txt
   * 8988463 first commit
   ```

8. branch 삭제

   ```bash
   $ git branch -d feature/login
   ```

------

### 3. merge conflict

1. feature/article branch 생성 및 이동

   ```bash
   $ git checkout -b feature/article
   ```

2. 작업 완료 후  commit

   ```bash
   # 충돌을 만들어 낼 파일에 코드를 작성
   $ git add .
   $ git commit -m "fixed minor update"
   ```

3. master 로 이동

   ```bash
   $ git checkout master
   ```

4. master 에 추가 commit 만들기

   ```bash
   # feature/article branch 에서 수정한 파일과 동일 파일의 같은 위치를 수정
   $ git add .
   $ git commit -m "fixed master update"
   ```

5. master 에 병합

   ```bash
   $ git merge feature/article
   ```

6. merge confict 발생

   ```bash
   $ git merge feature/article
   Auto-merging a.txt
   CONFLICT ...
   Automatic merge faild; fix conflicts and then commit result.
   ```

7. 충돌 확인 및 해결

   ```bash
   # 충돌이 일어난 파일 열기
   # 그럼 아래와 같은 내용이 있다.
   
   <<<<<<<< HEAD
   master 에서 작성한 내용
   ========
   feature/article 에서 작성한 내용
   >>>>>>>> feature/article
   
   # 원하는 코드로 수정
   ```

8. merge commit 진행

   ```bash
   $ git add .
   $ git commit
   ```

   - commit 메세지는 미리 작성되어 있음

9. commit 그래프 확인

   ```bash
   $ git log --oneline --graph
   *   7238aa2 (HEAD -> master) Merge branch 'feature/article'
   |\
   | * 8e84920 (feature/article) fix a.txt
   * | 28faf63 fix a.txt in master
   |/
   *   2743900 Merge branch 'feature/login'
   |\
   | * 29a92c0 Complete login.txt
   | * 38e2723 Complete signout.txt
   * | 278eaf5 Make master.txt
   |/
   * a52a916 complete test.txt
   * 8988463 first commit
   ```

10. branch 삭제

    ```bash
    $ git branch -d feature/article
    ```

    





