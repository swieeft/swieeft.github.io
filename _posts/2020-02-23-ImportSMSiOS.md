---
layout: post
title: "아임포트 다날 SMS 본인인증 iOS에 연동하기"
subtitle: "[iOS]"
date: 2020-02-23 20:55
background: 
tags: [ios]
---

회사 프로젝트에 본인인증 기능을 추가하기 위해 아임포트에서 제공하는 다날 SMS 본인인증 기능을 사용하였습니다.

생각보다 iOS 앱에 연동하는 방법을 찾기가 힘들어서 연동하는 과정에 대해 정리 해보려고 합니다.

### 아임포트에 다날 CPID와 CPPWD 연동하기

---

제일 먼저 선행되어야 될 작업은 당연히 아임포트 회원가입을 마치고, 다날 SMS 본인인증 사용 심사를 완료해야 합니다. 

심사 기간은 정확하게 가이드 되어 있는 부분은 없었는데 저희 회사는 2주 만에 심사가 끝났습니다. 다른 업체는 몇일 안 되서 끝난다고 하니 심사 담당 업체 사정에 따라 기간이 좀 들쭉날쭉인 것 같습니다.

심사가 완료되면 다날에서 CPID와 CPPWD를 메일로 보내줍니다. 만약 메일이 오지 않았다면 아임포트나 다날에 문의해서 전달 받으셔야 됩니다.

CPID와 CPPWD를 전달 받으셨으면 아임포트 관리자 페이지([http://admin.iamport.kr/](http://admin.iamport.kr/))에 로그인하여 [시스템 설정 → 본인인증 서비스] 항목으로 이동합니다.

이동 후에 아래 이미지와 같이 PG사를 다날(문자인증)로 선택하신 후 전달 받은 CPID와 CPPWD를 입력 후 저장하면 됩니다.

![import1.png](/assets/images/posts/2020-02-23/import1.png)

### 본인인증 웹 페이지 만들기

---

CPID와 CPPWD 연동이 잘 되어 있다면 아래 HTML 스크립트로 웹 페이지를 만들면 본인인증 화면에 나오게 됩니다. 

<p> {% gist swieeft/1c0ebfb228e955d8655f28049bcb1a2e ImportSMSiOS1.html %} </p>

- **주의할 점**

  - 꼭 부여 받은 가맹점 식별번호를 입력하셔야 됩니다.

  - IMP.certification에서 인증 성공 후 호출되는 API는 회사의 웹서버 API이고, 다날이나 아임포트의 API가 아닙니다. 본인인증 작업하면서 웹 개발자 분이 제일 헷갈려하셨던 부분입니다. 

  - 회사 웹 서버에서 사용자 정보를 받는 로직을 수행 후 앱에 최종적으로 데이터를 전달 해주면 됩니다.(서버에서 아임포트의 API를 호출하도록 합니다.)

페이지가 정상적으로 잘 동작한다면 아래 이미지와 같은 페이지가 보여야 합니다.

![import2.png](/assets/images/posts/2020-02-23/import2.png)

> 만약 제대로 다 설정이 되어 있는데도 페이지가 열리지 않는다면 info.plist에 App Transport Security 속성을 추가한 후 하위 속성에 Allow Arbitrary Loads를 추가하여 Value를 YES로 설정 해보세요.

### 본인인증 성공 후 사용자 정보 받아오기

---

이 부분은 백엔드 쪽에서 작업이 진행되는 부분이기 때문에 잘 정리되어 있는 예제 링크만 작성합니다.

- [연동방법 가이드 블로그](https://zladnrms.tistory.com/61)

- [아임포트 API를 테스트 페이지](https://api.iamport.kr)

### iOS 앱에서 본인인증 페이지 실행하기

---

본인인증 페이지를 실행하기 위해서 웹뷰 작업을 해주어야 합니다.

iOS 11부터는 WKWebView를 스토리보드에 직접 추가하여 작업할 수 있지만 브릿지 설정을 하기 위해 config를 추가하려면 직접 코드로 웹뷰를 생성해야 합니다.

- **웹뷰 생성하기**

  <p> {% gist swieeft/1c0ebfb228e955d8655f28049bcb1a2e ImportSMSiOS2.swift %} </p>

  > 웹뷰 오토 레이아웃을 SnapKit을 이용해서 설정 했는데 이 부분은 편한 방법으로 사용하시면 됩니다.

- **웹 페이지 로드 하기**

  <p> {% gist swieeft/1c0ebfb228e955d8655f28049bcb1a2e ImportSMSiOS3.swift %} </p>

### 본인인증 완료 등의 이벤트 브릿지로 받아서 처리하기

---

본인인증 절차가 완료되거나 중간에 취소 및 에러가 발생 하면 html에서 설정해 주었던 브릿지가 호출 됩니다. 호출 된 브릿지에 대한 처리는 아래와 같이 개발 해주시면 됩니다.

<p> {% gist swieeft/1c0ebfb228e955d8655f28049bcb1a2e ImportSMSiOS4.swift %} </p>

### JavaScript Alert 처리하기

---

본인인증 페이지에서 발생하는 JavaScript Alert을 처리하는 로직이 추가 되어야 사용자가 잘못 된 동작을 했을 때 안내 해줄 수 있는 Alert을 발생시킬 수 있습니다.

- **확인만 있는 Alert 처리**

  <p> {% gist swieeft/1c0ebfb228e955d8655f28049bcb1a2e ImportSMSiOS5.swift %} </p>

- **확인/취소 가능한 Alert 처리**

  <p> {% gist swieeft/1c0ebfb228e955d8655f28049bcb1a2e ImportSMSiOS6.swift %} </p>

### 마무리

---

아임포트로 다날 SMS 본인인증 연동하는 법을 알아보았습니다. iOS 연동 관련 정보가 많이 없어서 여러가지 삽질을 많이 했는데요.

백엔드 쪽에서 해줘야 하는 작업이 많아서 앱단에서는 생각보다 많은 작업이 필요하지는 않았습니다. 그래도 웹뷰나 브릿지에 대한 개념은 익히시고 작업을 하셔야 수월하게 작업이 가능할 것 같습니다.

이 글이 큰 도움이 될지는 모르겠지만 그래도 조금의 힌트는 될 수 있기를 바랍니다.

### 참고자료

---

[아임포트 결제연동 메뉴얼](https://docs.iamport.kr/tech/mobile-authentication)

[[아임포트] 아임포트로 다날 SMS 본인인증 개발 연동하기](https://m.blog.naver.com/PostView.nhn?blogId=iamport&logNo=221004352427&proxyReferer=https%3A%2F%2Fwww.google.com%2F)

[[Android/연동방법] SMS 본인인증 연동 (with iamport, 아임포트) (1)](https://zladnrms.tistory.com/60)

[WKWebView에서 Javascript Alert 띄우기](https://kka7.tistory.com/69)
