---
title: "[iOS] 아임포트 다날 SMS 본인인증 iOS에 연동하기"
layout: post
date: 2020-02-23 20:55
tag:
    - iOS
headerImage: false
image:
description: 아임포트 다날 SMS 본인인증 iOS에 연동하기
category: blog
author: swieeft
externalLink: true
published: true
comments: true
share: true
use_math: false
---
![importLogo.png](/assets/images/posts/2020-02-23/importLogo.png)

회사 프로젝트를 하면서 본인인증 기능을 추가해야 되서 아임포트에서 제공하는 다날 SMS 본인인증 기능을 사용하였습니다.

생각보다 문서 정리가 잘 안 되어 있어서 좀 놀랐고, iOS에 연동하는 방법이 정리되어 있는 글을 찾기가 힘들었습니다. 

연동을 하면서 보니 iOS에서는 웹뷰만 잘 실행 시켜주고, 브릿지만 연동 잘하면 되는 작업이라서 크게 문제 없었지만 웹 페이지와 백엔드 쪽 작업이 많이 있었습니다. 이 부분은 제 담당이 아니어서 자세한 부분은 모르겠지만 최대한 iOS 개발과 접점에 닿아 있는 부분은 같이 작성하도록 하겠습니다.

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

```html
<!DOCTYPE html>
<html>
<head>
<script type="text/javascript" src="https://code.jquery.com/jquery-1.12.4.min.js" ></script>
<script type="text/javascript" src="https://cdn.iamport.kr/js/iamport.payment-1.1.7.js" ></script>
</head>
<body>
<!-- 아임포트 자바스크립트는 jQuery 기반으로 개발되었습니다 -->

<script type="text/javascript">
// 모바일 에이전트 구분
var isMobile = {
    Android: function () {
        return navigator.userAgent.match(/Android/i) == null ? false : true;
    },
    IOS: function () {
        return navigator.userAgent.match(/iPhone|iPad|iPod/i) == null ? false : true;
    }
};

var IMP = window.IMP; // 생략가능
IMP.init('imp00000000'); // 'imp00000000' 대신 부여받은 "가맹점 식별코드"를 사용

/* 중략 */
IMP.certification({
    merchant_uid : 'merchant_' + new Date().getTime()
}, function(rsp) {
    console.log(JSON.stringify(rsp));
    if ( rsp.success ) {
        // 인증성공
        $.ajax({
                    url: "https://www.myservice.com/certifications", // 현재 서비스의 웹서버로 인증된 사용자 정보 요청
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    data: { imp_uid: rsp.imp_uid }
                }).done(function() {
                    // 이후 Business Logic 처리
                    takeResponseAndHandle(rsp)
                });
    } else {
        // 인증취소 또는 인증실패
        if(isMobile.IOS()){
            // 브릿지 연동 : authFail는 브릿지 네임 (프로젝트에 맞게 설정 필요)
            webkit.messageHandlers.authFail.postMessage(JSON.stringify(rsp));
        }
    }
});

function takeResponseAndHandle(rsp) {
    if ( rsp.success ) {
        // 인증성공
        if(isMobile.IOS()){
            // 브릿지 연동 : authSuccess는 브릿지 네임 (프로젝트에 맞게 설정 필요)
            webkit.messageHandlers.authSuccess.postMessage(JSON.stringify(rsp));
        }
    } else {
        // 인증취소 또는 인증실패
        if(isMobile.IOS()){
            // 브릿지 연동 : authFail는 브릿지 네임 (프로젝트에 맞게 설정 필요)
            webkit.messageHandlers.authFail.postMessage(JSON.stringify(rsp));
        }
    }
}

</script>
</body>
</html>
```

- 꼭 부여 받은 가맹점 식별번호를 입력하셔야 됩니다.

- IMP.certification에서 인증 성공 후 호출되는 API는 회사의 웹서버 API이고, 다날이나 아임포트의 API가 아닙니다. 본인인증 작업하면서 웹 개발자 분이 제일 헷갈려하셨던 부분입니다. 

- 회사 웹 서버에서 사용자 정보를 받는 로직을 수행 후 앱에 최종적으로 데이터를 전달 해주면 됩니다.(서버에서 아임포트의 API를 호출하도록 합니다.)

페이지가 정상적으로 잘 동작한다면 아래 이미지와 같은 페이지가 보여야 합니다.

![import2.png](/assets/images/posts/2020-02-23/import2.png)

만약 제대로 다 설정이 되어 있는데도 페이지가 열리지 않는다면 
info.plist에 App Transport Security 속성을 추가한 후 하위 속성에 Allow Arbitrary Loads를 추가하여 Value를 YES로 설정 해보세요.

### 본인인증 성공 후 사용자 정보 받아오기

---

이 부분은 백엔드 쪽에서 작업이 진행되는 부분이기 때문에 잘 정리되어 있는 예제 링크만 작성합니다.

- [[Android/연동방법] SMS 본인인증 연동 (with iamport, 아임포트) (2)](https://zladnrms.tistory.com/61)

아임포트 API를 호출해볼 수 있는 테스트 페이지입니다.

- [API-아임포트](https://api.iamport.kr)

### iOS 앱에서 본인인증 페이지 실행하기

---

본인인증 페이지를 실행하기 위해서 웹뷰 작업을 해주어야 합니다. 웹뷰 코드는 WKWebView 기반으로 작성합니다.

- **웹뷰 생성하기**

  ```swift  
  class AuthWebViewViewController: UIViewController {
    var webView: WKWebView?
  
    override func viewDidLoad() {
      super.viewDidLoad()
  
      // 브릿지 설정
      let contentController = WKUserContentController()
      contentController.add(self, name: "authSuccess")
      contentController.add(self, name: "authFail")
      
      let config = WKWebViewConfiguration()
      config.userContentController = contentController
  
      webView = WKWebView(frame: .zero, configuration: config)
      webView?.uiDelegate = self
      webView?.navigationDelegate = self
  
      self.view.addSubview(webView!)
  
      webView?.snp.makeConstraints({ maker in
          maker.top.equalTo(self.view.snp.topMargin)
          maker.bottom.equalTo(self.view.snp.bottomMargin)
          maker.left.equalTo(self.view.snp.left)
          maker.right.equalTo(self.view.snp.right)
      })
    }
  }
  ```

  웹뷰를 스토리보드에 직접 추가하여 작업할 수 있지만 브릿지 설정을 하기 위해 config를 추가하려면 직접 코드로 웹뷰를 생성해야 합니다. (이 부분은 아직 애플에서 스토리 보드로 지원하지 않는 것 같습니다)

  저는 웹뷰 오토 레이아웃을 SnapKit을 이용해서 잡았는데 편한 방법으로 사용하시면 됩니다.

- **웹 페이지 로드 하기**

  ```swift
  override func viewDidAppear(_ animated: Bool) {
    super.viewDidAppear(animated)
  
    if let url = URL(string: "본인인증 웹 페이지 주소 입력") {
      let urlRequest = URLRequest(url: url)
      webView?.load(urlRequest)
    }
  }
  ```

### 본인인증 완료 등의 이벤트 브릿지로 받아서 처리하기

---

본인인증 절차가 완료되거나 중간에 취소 및 에러가 발생 하면 html에서 설정해 주었던 브릿지가 호출 될 것입니다. 호출 된 브릿지는 아래와 같이 코드 작업을 해주시면 됩니다.

```swift
func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {

  if message.name == "authSuccess" {
    // 인증 성공 시 처리할 로직
  } else if message.name == "authFail" {
    // 인증 취소, 실패 시 처리할 로직
  }
}
```

### 웹 페이지 JavaScript Alert 처리하기

---

본인인증 페이지에서 발생하는 JavaScript Alert을 처리하는 로직이 추가 되어야 사용자가 잘못 된 동작을 했을 때 안내 해줄 수 있는 Alert을 발생시킬 수 있습니다.

- **확인만 있는 Alert 처리**

  ```swift
  func webView(_ webView: WKWebView, runJavaScriptAlertPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping () -> Swift.Void) {
    let alertController = UIAlertController(title: message, message: nil, preferredStyle: .alert)
  
    let cancelAction = UIAlertAction(title: "확인", style: .cancel) { _ in
      completionHandler()
    }
  
    alertController.addAction(cancelAction)
  
    DispatchQueue.main.async {
      self.present(alertController, animated: true, completion: nil)
    }
  }
  ```

- **확인/취소 가능한 Alert 처리**

  ```swift
  func webView(_ webView: WKWebView, runJavaScriptConfirmPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping (Bool) -> Void) {
    let alertController = UIAlertController(title: message, message: nil, preferredStyle: .alert)
  
    let cancelAction = UIAlertAction(title: "취소", style: .cancel) { _ in
      completionHandler(false)
    }
  
    let okAction = UIAlertAction(title: "확인", style: .default) { _ in
      completionHandler(true)
    }
  
    alertController.addAction(cancelAction)
    alertController.addAction(okAction)
  
    DispatchQueue.main.async {
      self.present(alertController, animated: true, completion: nil)
    }
  }
  ```

### 마무리

---

아임포트로 다날 SMS 본인인증 연동하는 법을 알아보았습니다. 생각보다 백엔드 쪽에서 해줘야 하는 작업이 많아서 앱단에서는 많은 처리가 필요가 없었는데요. 

연동하면서 iOS 연동 관련 문서나 공식 가이드 문서가 부실하다보니 여러가지 삽질을 많이 했습니다. 아직 해결 못한 부분도 몇군데 있습니다. 그 부분은 해결 되는대로 추가해서 글 작성하도록 하겠습니다.

이 글이 큰 도움이 될지는 모르겠지만 그래도 조금의 힌트는 될 수 있기를 바랍니다.

### 참고자료

---

[아임포트 결제연동 메뉴얼](https://docs.iamport.kr/tech/mobile-authentication)

[[아임포트] 아임포트로 다날 SMS 본인인증 개발 연동하기](https://m.blog.naver.com/PostView.nhn?blogId=iamport&logNo=221004352427&proxyReferer=https%3A%2F%2Fwww.google.com%2F)

[[Android/연동방법] SMS 본인인증 연동 (with iamport, 아임포트) (1)](https://zladnrms.tistory.com/60)

[WKWebView에서 Javascript Alert 띄우기](https://kka7.tistory.com/69)
