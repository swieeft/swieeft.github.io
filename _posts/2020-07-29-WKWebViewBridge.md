---
layout: post
title: "WKWebView Bridge 연결하기"
subtitle: "[Swift]"
date: 2020-07-29 17:00
background: 
tags: [ios, swift]
---

이번 포스팅에서는 WKWebView에서 JavaScript를 Bridge로 연결하는 방법에 대해 알아보려고 합니다.

앱 개발을 하다보면 종종 웹뷰로 웹 페이지의 이벤트를 받아서 처리를 해주어야 하는데, 그때 사용하는 것이 바로 Bridge입니다.

뭔가 웹이랑 앱이랑 이벤트를 연결하고 어쩌고 하니 거창하고 어려워 보이지만 막상 작업을 하면 간단하게 되니 처음부터 겁먹지 마세요!

스크립트에는 안드로이드도 호출하는 부분이 있지만 여기서는 iOS에서 사용하는 방법에 대해서만 설명하겠습니다.

### Bridge 호출을 위한 JavaScript 만들기

---

JavaScript로 함수를 만들어 Bridge를 호출하는데요. Bridge 함수를 만드는 방법은 간단합니다.

<p> {% gist swieeft/14eeaacb6d53756b1a19cb6781658703 WKWebViewBridge1.js %} </p>

여기서 브릿지를 호출하는 부분을 잘 보셔야 합니다.

- webkit.messageHandlers.**outLink**.postMessage(link);

- webkit.messageHandlers.**back**.postMessage(link);

볼드 처리된 부분이 Bridge 이름으로 앱에서 호출 되었을 때 키가 되는 부분입니다. 이 부분은 앱과 웹에서 서로 맞추어서 전달해야 정상적으로 Bridge 사용이 가능합니다.


### 예제 HTML 코드

---

이제 Bridge 함수를 호출 할 HTML을 만들어줍니다. 저는 간단하게 버튼 3개를 만들어서 버튼 클릭 시 Bridge 함수가 호출 되도록 하였습니다.

<p> {% gist swieeft/14eeaacb6d53756b1a19cb6781658703 WKWebViewBridge2.html %} </p>

이제 웹에서 Bridge를 사용할 준비가 완료 되었습니다.

### WebView 초기화 및 Bridge 등록

---

이제 앱에서 작업을 해줘야 하는데요. 우선 WebView 생성 및 Bridge 설정하는 방법을 알아보겠습니다.

iOS 11 이상부터는 스토리보드에서도 WKWebView를 직접 추가할 수 있게 되었지만, Bridge를 설정하기 위해서는 WKWebViewConfiguration를 WKWebView 초기화 시에 넣어주어야 되는데 해당 기능을 스토리보드에서는 지원하지 않고 있어 코드로 웹뷰를 생성해줍니다.

- **Bridge 등록하기**

    <p> {% gist swieeft/14eeaacb6d53756b1a19cb6781658703 WKWebViewBridge3.swift %} </p>

    Bridge를 사용하기 위해서 우선 WKUserContentController를 생성하여 그 안에 사용할 Bridge 이름을 추가하여 줍니다.

    그 후 WKWebViewConfiguration을 생성하여 configuration.userContentController에 WKUserContentController를 넣어줍니다.

- **WKWebView 초기화**

    <p> {% gist swieeft/14eeaacb6d53756b1a19cb6781658703 WKWebViewBridge4.swift %} </p>

    웹뷰를 초기화 할 때 configuration 파라메터에 위에서 생성한 WKWebViewConfiguration을 넣어주도록 합니다.

- **페이지 로드**

    <p> {% gist swieeft/14eeaacb6d53756b1a19cb6781658703 WKWebViewBridge5.swift %} </p>

    이제 페이지를 로드 해줍니다. 저는 프로젝트에 html과 JavaScript 파일을 넣어두었기 때문에 위와 같은 코드를 사용하였습니다.

- **전체 코드**

    <p> {% gist swieeft/14eeaacb6d53756b1a19cb6781658703 WKWebViewBridge6.swift %} </p>

### 호출된 Bridge 처리하기

---

이제 Bridge를 사용할 모든 준비가 되었습니다. 그럼 실제 웹 페이지에서 Bridge를 호출 했을 때 처리하는 방법을 알아보도록 하겠습니다.

<p> {% gist swieeft/14eeaacb6d53756b1a19cb6781658703 WKWebViewBridge7.swift %} </p>

1. 우선 WKScriptMessageHandler 프로토콜을 위임 받은 후에 **userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage)** 메서드를 생성해줍니다. 이 메서드를 통해 Bridge가 들어오게 됩니다.

2. message.name으로 어떤 브릿지인지 확인하여 그에 맞는 로직을 작성하여 줍니다.

3. 파라메터는 message.body에 담겨서 내려오게 됩니다. message.body는 Any 타입으로 사용하고자 하는 타입으로 캐스팅한 후 사용하시면 됩니다.


### 결과화면

![WKWebViewBridge1.gif](/assets/images/posts/2020-07-29/WKWebViewBridge1.gif)

### 마무리

---

WKWebView에서 Bridge를 사용하는 방법에 대해서 알아보았습니다. 생각 보다 기능 구현이 어렵지는 않았는데요.

하지만 앱에서만 작업 되는 것이 아니라 웹에서도 함께 작업이 이루어져야 하기 때문에 서로 협력이 잘 되야 쉽게 기능을 구현할 수 있습니다.

그럼 달콤한 코딩 되세요!


### 예제 프로젝트

---

[swieeft/WKWebViewBridge](https://github.com/swieeft/WKWebViewBridge)

### 참고자료

--- 

[ClintJang/sample-swift-wkwebview-javascript-bridge-and-scheme](https://github.com/ClintJang/sample-swift-wkwebview-javascript-bridge-and-scheme)