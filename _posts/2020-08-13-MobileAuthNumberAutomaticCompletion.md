---
layout: post
title: "TextField 휴대폰 인증번호 자동완성 기능 구현하기"
subtitle: "[iOS]"
date: 2020-08-13 15:15
background: 
tags: [ios, swift]
---

안녕하세요. 오늘은 간단한 포스팅이 될 것 같은데요. 

iOS 12부터는 문자인증을 받을 때 인증 번호를 수신하면 문자 메시지에 가서 확인하지 않아도 키보드에 자동완성을 보여주는 기능을 제공해줍니다.

그래서 오늘은 자동완성을 보이게 하기 위한 간단한 설정 및 문자 내용에 대해 알아보도록 하겠습니다. 

![MobileAuthNumberAutomaticCompletion1.jpeg](/assets/images/posts/2020-08-13/MobileAuthNumberAutomaticCompletion1.jpeg)

### TextField 설정

---

TextField에서 인증번호를 자동완성으로 띄우기 위해서는 **textContentType**을 **oneTimeCode**로 설정해주어야 합니다.

- **스토리 보드에서 설정하기**

    스토리 보드에서는 아래 설정 창에서 Text Input traits -> ContentType을 One Time Code로 변경해주면 됩니다.

    ![MobileAuthNumberAutomaticCompletion2.png](/assets/images/posts/2020-08-13/MobileAuthNumberAutomaticCompletion2.png)    

- **코드로 설정하기**

    코드에서는 TextField에 textContentType을 oneTimeCode로 설정하면 됩니다.

    <p> {% gist swieeft/a2efa61b193257171f2f24d0135d87c1 MobileAuthNumberAutomaticCompletion1.swift %} </p>
    
### 문자 메시지(SMS) 형식

---

설정은 간단하지만 문자 메시지 형식을 맞춰서 보내야 제대로 자동완성 기능이 작동을 합니다.

저도 설정은 다 했는데 자동완성이 뜨지 않아서 여러가지 삽질을 했는데 결국 문자 메시지 형식이 달라서 제대로 작동을 하지 않았었습니다.

제가 발견한 형식은 크게 4가지 입니다.

1. **인증번호 + 조사 + 인증번호 텍스트**

    - ex) 0000은 인증번호, 0000을 인증번호 등

2. **인증번호 텍스트 + 조사 + 인증번호**

    - ex) 인증번호는 0000, 인증번호를 0000 등

3. **인증번호 + 특수문자 + 인증번호 텍스트**
 
    - ex) 0000 : 인증번호, 0000 - 인증번호 등

4. **인증번호 텍스트 + 특수문자 + 인증번호**

    - ex) 인증번호 : 0000, 인증번호 - 0000 등

제가 테스트 해본 형식은 위와 같은데 이것보다 더 많은 형식이 있을 수 있습니다. 그 외의 형식은 여러가지로 테스트 해보시면 될 것 같습니다.

### 마무리

---

지금까지 인증번호 자동 완성 기능 구현에 대해서 알아보았습니다.

저희는 개발하면서 삽질 한 것 중에 하나가 **인증번호는 0000**이라고 문자를 보내야 되는데 인증번호는과 0000 사이에 띄어쓰기를 하나 더 추가 했더니 자동완성이 작동하지 않았습니다.

띄어쓰기 하나에도 동작을 할 수도 안 할 수도 있으니 개발하실 때 유의하셔서 개발하세요.

그럼 달콤한 코딩 되세요!

### 참고자료

--- 

[AppleDeveloper - oneTimeCode](https://developer.apple.com/documentation/uikit/uitextcontenttype/2980930-onetimecode)

[iOS 12 SMS Reading API](https://stackoverflow.com/a/50791536)