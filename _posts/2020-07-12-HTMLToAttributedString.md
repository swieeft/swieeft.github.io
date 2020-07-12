---
layout: post
title: "HTML을 AttributedString으로 변환하기"
subtitle: "[Swift]"
date: 2020-07-12 14:15
background: 
tags: [ios, swift]
---

안녕하세요. 요즘 프로젝트 기간의 압박으로 인해 열심히 달리고 있어 포스팅을 몇 달 동안 못하고 있었네요.

포스팅을 하려면 새로운 것을 공부도 해야되고, 자료도 찾아보고 해야 되는데 그럴 시간이 없었다는 변명과 함께 포스팅을 시작합니다.

---

오늘은 HTML을 AttributedString으로 변환하는 방법을 알아보려고 합니다.

앱을 개발하다보면 API에서 HTML로 데이터를 내려주면 HTML을 문자열로 바꿔서 보여줘야 되는 경우가 있습니다.

이번 프로젝트에서도 필요했던 기능이라서 찾아보았는데 생각보단 간단하게 개발을 할 수 있어서 해당 내용을 간단하게 정리해보려고 합니다.

### HTML을 AttributedString으로 변환하기

---

HTMl을 AttributedString으로 변환하는 방법은 생각보다 간단합니다. 이미 AttributedString에서 옵션으로 제공하고 있습니다.

- **예제코드**

    <p> {% gist swieeft/9a2ff3ac26b7007e742ef6d1e2071193 HTMLToAttributedString1.swift %} </p>

    - 우선 String 형태로 내려온 HTML을 data로 변환 시켜줍니다.
    - 그 후 NSAttributedString를 생성할 때 변환된 data를 넣어준 후 options에 아래 두가지 옵션을 추가해줍니다.
        - .documentType: NSAttributedString.DocumentType.html
        - .characterEncoding:String.Encoding.utf8.rawValue

    이렇게 하면 HTML이 AttributedString으로 잘 변환 된 것을 확인 할 수 있습니다.


- **결과화면**

    ![HTMLToAttributedString1.png](/assets/images/posts/2020-07-12/HTMLToAttributedString1.png)


### 기본 Font, Font Size, Color, Line Height 설정하기

---

앱 개발을 하다보면 기본적으로 제공하는 시스템 폰트 외에 앱 자체적으로 사용되는 커스텀 폰트로 변환해야 되는 경우도 있고, 기본 텍스트 색상이 검정색이 아닌 경우도 많이 있습니다.

이럴 경우에는 간단하게 기본으로 설정되는 값을 HTML로 작성하여 감싸주기만 하면 됩니다.

- **Font 설정하기**

    <p> {% gist swieeft/9a2ff3ac26b7007e742ef6d1e2071193 HTMLToAttributedString2.swift %} </p>

    - 위의 코드에서 font.fontName 부분에 사용할 폰트의 이름을 적어주시면 해당 폰트로 설정할 수 있습니다.
        - ex) AppleSDGothicNeo-Regular, AppleSDGothicNeo-Bold 등

- **Font Size 설정하기**

    <p> {% gist swieeft/9a2ff3ac26b7007e742ef6d1e2071193 HTMLToAttributedString3.swift %} </p>

    - 위의 코드에서 font.pointSize 부분에 설정할 폰트 크기를 지정해주면 됩니다.

- **Font Color 설정하기**

    <p> {% gist swieeft/9a2ff3ac26b7007e742ef6d1e2071193 HTMLToAttributedString4.swift %} </p>

    - 변경하고자 하는 컬러의 RGB 값을 추출해서 "rgb(red, green, blue)"로 만들어서 색상을 지정해주면 됩니다.

- **Line Height 설정하기**

    <p> {% gist swieeft/9a2ff3ac26b7007e742ef6d1e2071193 HTMLToAttributedString5.swift %} </p>

    - 여러 줄의 텍스트를 표시할 때 지정된 Line Height를 설정해주려면 lineHeight에 값을 넣어주어야 합니다. 
    - 주의할 점은 제플린에서의 Line Height가 아닌 현재 폰트 높이의 배수로 설정을 해주어야 하기 때문에 제플린의 Line Height를 적용하고 싶으다면 아래와 같이 계산하여 넣어주어야 합니다.
        - 계산식 : lineHeight / font.pointSize

### Extension을 활용하여 여러 곳에서 사용할 수 있게 만들기

---

이제 위에 내용들을 합쳐서 Extension으로 만들어 여러 곳에서 접근하여 사용할 수 있게 전체 코드를 작성해보겠습니다.

- **전체 코드**

    <p> {% gist swieeft/9a2ff3ac26b7007e742ef6d1e2071193 HTMLToAttributedString6.swift %} </p>

- **사용 방법**

    <p> {% gist swieeft/9a2ff3ac26b7007e742ef6d1e2071193 HTMLToAttributedString7.swift %} </p>

    - 여기서 UILabel 대신에 UITextView를 사용한 이유는 하이퍼링크 사용 시 UITextView에서는 링크를 사파리로 오픈 하는 것을 자동으로 해주지만 UILabel에서는 여러가지 번거로운 작업을 거쳐야 되서 UITextView를 사용하는 것을 권장합니다.

### Tip. UITextView를 UILabel 처럼 사용하기 위한 설정 방법

--- 

위에서 UITextView를 사용하는 이유를 설명 드렸는데요. UITextView를 UILabel 처럼 수정하지도 못하고, 스크롤 되지도 않게 하기 위한 방법을 알려 드리겠습니다.

![HTMLToAttributedString2.png](/assets/images/posts/2020-07-12/HTMLToAttributedString2.png)

- **Editable 체크 해제** : Editable 항목은 사용자가 수정할 수 있게 해줄지 여부를 설정하는 항목입니다.
- **Show Horizontal indicator, Show Vertical indicator 체크 해제** : 스크롤 할 때 나타나는 스크롤바를 보이지 않게 합니다.
- **Scrolling Enabled 체크 해제** : UITextView가 스크롤 가능하게 할지 여부를 설정합니다. 이 옵션을 꺼야 동적으로 텍스트 줄 수 만큼 텍스트뷰의 높이가 조절되고, 선택 되어 있으면 설정 된 크기 이상 텍스트가 늘어날 경우 스크롤이 되게 됩니다.


### 마무리

---

지금까지 HTML을 AttributedString으로 변환하는 방법에 대해 알아보았습니다. 

오랜만에 포스팅을 하려니 뭔가 내용 정리도 잘 안 되는거 같고 글을 쓰기가 어렵네요. 역시 주기적으로 작성을 해야 실력도 유지가 되는 것 같습니다.

다음번 포스팅은 비교적 짧은 시간 안에 업로드 되길 바라며 이만 마치겠습니다.

그럼 달콤한 코딩 되세요!

### 참고자료

--- 

[stack overflow - Swift: Display HTML data in a label or textView](https://stackoverflow.com/a/47230632)

[[iOS] HTML 태그에 UIFont 적용 하기](https://gogorchg.tistory.com/entry/iOS-HTML-%ED%83%9C%EA%B7%B8%EC%97%90-UIFont-%EC%A0%81%EC%9A%A9-%ED%95%98%EA%B8%B0)