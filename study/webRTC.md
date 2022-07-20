# WebRTC

- [WebRTC? WebSockets? 5분 개념정리!]([WebRTC? WebSockets? 5분 개념정리! - YouTube](https://www.youtube.com/watch?v=5EhsjtBE7I4))

---

### WebRTC 기본개념

- Browser 와 Server는 HTTP를 이용해서 소통
  
  - ```
    HTTP
    - 인터넷 데이터 교환의 필수 요소
    - 업로드, 다운로드, 이미지, 문서 ...
    - HTTP request, HTTP response
    - 요청과 응답이 끝나면 브라우저-서버간 통신은 끝나게됨
    ```

- WebSockets
  
  - ```
    WebSockets
    - HTTP처럼 request-response가 있는 것이 아님
    - 커넥션이 Open-Close된 여부
    - 통신이 연결되어있고, 끊어져있는 개념
    - 통신이 열려있는 동안에는 자유롭게 메시지를 주고 받을 수 있음
    - 실시간 리얼타임을 위해 만들어짐
    - 모든 통신을 추적하기 위해, 메모리 파워가 중요함
    - 유저가 많으면 많을 수록 더 많은 메모리가 필요함, 서버 비용 증가
    - 메시지를 받으면 다른 유저에게 포워딩을 해야하므로, 서버를 빠르게 유지해야함
    ```

- WebRTC
  
  - ```
    WebRTC
    - 브라우저를 서버에 연결하는 것이 아니라, 브라우저끼리 연결
    - Web Real-Time Communication
    - 메시지가 서버를 통하지 않고 브라우저간 바로 전달
    - P2P : Peer to Peer, 직접 정보나 데이터를 주고받는 것
    - 사람이 많아지면 다운로드, 업로드 양이 많아져서 확장성에 제약이있음
    ```

---

WebRTC 시작하기

- ```
  $ mkdir zoom
  - zoom이라는 이름의 새폴더 만들기
  $ cd zoom
  - zoom이라는 폴더에 들어가기 ( 경로 이동 )
  $ npm init -y
  - package.json 생성
  $ code .
  - 코드 편집기 열기, vscode
  ```

- ```json
  {
    "name": "zoom",
    "version": "1.0.0",
    "description": "Zoom Clone using WebRTC and Websockets",
    "license": "JYP"
  }
  ```
  
  - package.json에 작성, license는 자기 마음대로 설정

- ```
  $ touch README.md
  - github 에 올릴 때 리드미를 작성해서 해당 프로젝트를 설명해주자!
  $ npm i nodemon -D
  ```

- ```
  npm WARN config global `--global`, `--local` are deprecated.
  Use `--location=global` instead.
  ```
  
  - 해당 경고 발생시
  
  - [여기 링크로 이동 후 따라 해보기!](https://yaongdaong.tistory.com/entry/Error-npm-WARN-config-global-global-local-are-deprecated-Use-locationglobal-instead)

- ```
  $ git init .
  $ npm i @babel/core @babel/cli @babel/node -D
      - 오류 발생시
      $ npm uninstall @babel/core @babel/cli @babel/node -D
      $ npm install -g babel@5
  $ npm i @babel/preset/env
  $ npm i @babel/preset-env -D
  ```

- ```json
  {
      "exec": "babel-node src/server.js"
  }
  ```
  
  - nodemon.json 에 작성

- ```json
  {
      "presets": ["babel/preset-env"]
  }
  ```
  
  - babel.config.json 에 작성

- 
