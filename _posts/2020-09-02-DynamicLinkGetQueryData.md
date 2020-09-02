---
layout: post
title: "Firebase DynamicLink에서 데이터 받기"
subtitle: "[iOS, Swift]"
date: 2020-09-02 15:50
background: 
tags: [ios, swift]
---

안녕하세요. 오늘은 Firebase DynamicLink에서 데이터를 받기는 방법에 대해 알아보려고 합니다.

우선 DynamicLink가 무엇인지 잘 모르시는 분들을 위해 Firebase 문서에서는 간단하게 이렇게 소개하고 있습니다.

> Firebase 동적 링크는 앱 설치 여부에 관계없이 여러 플랫폼에서 원하는 대로 작동하는 링크입니다.

소개대로 여러 플랫폼 (iOS, Android 등)에서 링크를 클릭하면 앱이 설치 되어 있다면 앱이 실행이 되고, 앱이 설치 되지 않았다면 앱스토어나 플레이스토어, 또는 설정한 특정 URL로 이동시킬 수 있는 링크입니다.

자세한 설명은 링크를 참고하세요. [Firebase DynamicLink](https://firebase.google.com/docs/dynamic-links?hl=ko)

그럼 DynamicLink가 무엇인지 알아보았는데요. 사실 DynamicLink로 앱 설치 유/무에 따라 스토어나 앱을 실행하도록 하는 것은 크게 어렵지 않습니다.

또한 많은 분들이 작업을 하시면서 작성하신 글들이 많습니다. 아래는 저도 DynamicLink를 적용하면서 참고했던 블로그 링크입니다.

[[Swift][iOS] Firebase Dynamic Link를 이용한 Deep Link](https://m.blog.naver.com/PostView.nhn?blogId=greatsk553&logNo=221397462709&proxyReferer=https:%2F%2Fwww.google.com%2F)

### DynamicLink에서 데이터를 받는 이유

--- 

자. 그럼 서론은 이 정도만 하고 본격적으로 이 포스팅에서 쓰고자 하는 내용에 대한 설명을 본격적으로 들어가보도록 하겠습니다.

우리는 DynamicLink를 이용해서 미설치 고객을 앱스토어로 유도하는 목적도 있을 수 있지만 그 보다는 인스타그램이나 카카오톡, 기타 여러 플랫폼에 링크를 공유하여 앱의 여러 기능을 활용하기 위한 수단으로 사용하려고 합니다.

대표적으로 사용되어지는 것은 아래와 같습니다.

- 추천인 보상
- 이벤트 상세 페이지 이동
- 상품 상세화면 공유
- 게시물 공유
- 위치 공유

근데 이런 기능은 단순 링크만 가지고는 사용할 수 없는 기능입니다. 특정 데이터를 이용해서 조회를 하거나 보상을 지급하는 등의 기능이 추가적으로 필요하죠. 

그럼 DynamicLink에 어떻게 데이터를 넣을 수 있을까요? 오늘은 이 부분에 대해 알아보려고 합니다.

### 데이터가 담긴 DynamicLink 생성하기

---

우선 DynamicLink를 생성할 때 어떻게 데이터를 담는지 보도록 하겠습니다.

- **Firebase 콘솔에서 생성하기**

    Firebase 콘솔에서 링크를 생성하는건 대부분 특정 유저에게 보내거나 유동적인 데이터가 아니라 이벤트, 공지사항 같은 전체에게 보내거나 인스타그램, 페이스북 같은 곳에 광고용 링크를 만들기 위해 주로 사용됩니다.

    그럼 간단하게 오픈 이벤트를 위한 링크를 생성 해보도록 하겠습니다.

    1. 새 동적 링크 생성하기 버튼 클릭

        ![DynamicLinkGetQueryData1.png](/assets/images/posts/2020-09-02/DynamicLinkGetQueryData1.png)

    2. 단축 URL 링크 설정하기

        오픈 이벤트 링크를 만들고 있기 떄문에 링크는 openevent로 해주었습니다.

        ![DynamicLinkGetQueryData2.png](/assets/images/posts/2020-09-02/DynamicLinkGetQueryData2.png)

    3. 동적 링크 설정

        여기가 데이터를 받는 핵심적인 부분입니다. 딥 링크 URL에 넣은 URL 파라메터를 빼내서 그 데이터를 활용해 원하는 동작을 수행하도록 할 수 있습니다.

        저는 여기서 eventId라는 파라메터를 추가하여 거기에 id값을 1로 지정해주었습니다.

        ![DynamicLinkGetQueryData3.png](/assets/images/posts/2020-09-02/DynamicLinkGetQueryData3.png)

    4. 그 외 설정

        그 외에 iOS용 링크 동작 정의, Android용 링크 동작 정의, 캠페인 추적, 소셜 태그, 고급 옵션 항목은 원래 설정하는 방식대로 설정하시면 됩니다.

- **iOS 앱에서 생성하기**

    iOS 앱에서 링크를 생성하는 이유는 추천인 보상을 위해 링크 공유 시 사용자 고유 값을 함께 지정해서 보내기 위함이거나, 네이버 지도와 같이 특정 위치에 대한 정보를 공유하거나, 쇼핑몰에서 특정 상품 정보를 공유하는 등 사용자가 다른 사람에게 정보를 공유하기 위해 주로 사용됩니다.

    간단하게 쇼핑몰에서 특정 상품에 대한 정보를 공유하는 링크를 만들도록 하겠습니다.

    1. Dynamic Link 생성 코드

        <p> {% gist swieeft/ef47967f8a4ac3f8750bc143027204d8 DynamicLinkGetQueryData1.swift %} </p>

        > 리다이렉트 URL은 사용자가 모바일이 아닌 PC에서 링크를 클릭 했을 경우 보여줄 페이지 주소입니다.

    2. 단축 URL 확인하기

        코드를 실행해보면 **https://리다이렉트URL/nTUoNJwAAuLJkCnT6** 처럼 뒤에 난수로 된 단축 URL이 만들어 지는 것을 확인할 수 있습니다.

> Firebase에서 제공하는 API를 통해 관리자 웹 등에서도 Dynamic Link를 생성해서 사용할 수 있습니다. [동적 링크 만들기](https://firebase.google.com/docs/dynamic-links/create-links?hl=ko)

### Dynamic Link에서 데이터 받기

---

이제 생성된 링크를 클릭 했을 때 앱에서 해당 링크의 데이터를 받아오는 방법을 알아보도록 하겠습니다.

- **Info.plist에 커스텀 도메인 추가하기**

    Firebase에서 제공하는 문서대로 했는데도 제대로 데이터를 받아오지 못했는데 알고 보니 커스텀 도메인을 추가하지 않아서 발생한 문제였습니다.

    커스텀 도메인을 추가하는 방법은 간단합니다

    - Property List에서 추가하기

        Property List에서 **FirebaseDynamicLinksCustomDomains**를 추가한 후 Array Type으로 설정합니다. 그리고 Dynamic Link에 URL 프리픽스를 입력합니다.

        ![DynamicLinkGetQueryData4.png](/assets/images/posts/2020-09-02/DynamicLinkGetQueryData4.png)

    - Source Code로 추가하기

        <p> {% gist swieeft/ef47967f8a4ac3f8750bc143027204d8 DynamicLinkGetQueryData4.xml %} </p>    

- **Associated Domains에 원하는 도메인 추가하기**

    Associated Domains에 설정한 딥링크의 도메인을 추가해줍니다.

    만약에 사용하는 URL 프리픽스가 test.domain.com인데 리다이렉트 할 URL은 www.domain.com을 사용하는 중이라면 Associated Domains에 www.domain.com도 추가를 해주어야 데이터를 받을 수 있습니다.

    ![DynamicLinkGetQueryData6.png](/assets/images/posts/2020-09-02/DynamicLinkGetQueryData6.png)


- **AppDelegate에 콜백 메서드 만들기**

    우선 Dynamic Link를 받을 수 있게 AppDelegate에 아래 코드를 추가합니다.

    <p> {% gist swieeft/ef47967f8a4ac3f8750bc143027204d8 DynamicLinkGetQueryData2.swift %} </p>

- **Link에서 데이터 받기**

    콜백 메서드로 들어온 DynamicLink에서 데이터를 빼내는 메서드를 만듭니다.

    <p> {% gist swieeft/ef47967f8a4ac3f8750bc143027204d8 DynamicLinkGetQueryData3.swift %} </p>

- **결과 화면**

    코드를 전부 추가 한 뒤 생성된 DynamicLink를 클릭 해보면 콘솔창에 아래와 같이 데이터를 정상적으로 받아오는 것을 확인 할 수 있습니다.

    ![DynamicLinkGetQueryData5.png](/assets/images/posts/2020-09-02/DynamicLinkGetQueryData5.png)

### 마무리

---

지금까지 Firebase Dynamic Link를 통해 데이터를 얻는 방법에 대해서 알아보았습니다.

데이터를 얻어서 여러가지 마케팅이나 이벤트에 활용할 수도 있을거 같은데요. 

적절하게 이용한다면 간단한 방법으로 서비스에 큰 효과를 얻을 수 있을 것 같습니다.

그럼 달콤한 코딩 되세요!

### 참고자료

--- 

[Firebase 동적링크 사용사례 - 사용자 추천에 대한 보상](https://firebase.google.com/docs/dynamic-links/use-cases/rewarded-referral?hl=ko)