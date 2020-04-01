---
layout: post
title: "RxSwift에서 Delegate 패턴 사용하기 (2/2)"
subtitle: "[RxSwift]"
date: 2020-02-20 17:40
background: 
tag: [iOS, RxSwift]
---

RxSwift에서 Delegate 패턴 사용하기 두번째 방법은 Subject와 Obervable을 활용하여 사용하는 방식입니다. 첫번째 방법에서는 Delegate를 만들기 위해 여러 복잡한 작업과 Objective-C에서 사용 가능한 데이터형만을 사용할 수 있었다면 두번째 방법은 좀 더 간단하면서 더 많은 데이터형을 사용할 수 있다는 장점이 있습니다.  

첫번째 방법은 아래 링크를 참고해주세요.
  
[RxSwift에서 Delegate 패턴 사용하기 (1/2)](/RxSwiftDelegate1)

### 예제 프로젝트 동작 설명

---

![RxSwiftDelegateExample](/assets/images/posts/2020-02-20/RxSwiftDelegateExample2.gif)

> Subject를 만들어줄 InputViewController는 TextField에 입력 된 문자열을 Confirm<Subject> 버튼 클릭 시 ViewController에 전달하고, 전달된 문자열은 ViewController의 Label에 설정되게 됩니다.

### InputViewController에 Subject 선언하기

---

InputViewController에 Subject와 Observable을 선언하여 줍니다. 여기서 Subject는 내부에서 호출되어지고, Observable은 외부에서 호출하는 역할을 하게 됩니다.

<p> {% gist swieeft/a2806b7e4d59d2b5ed70acf99f810492 RxSwiftDelegate2-1.swift %} </p>

### Subject 호출하기

---

선언된 Subject를 이벤트 발생 시 호출하도록 합니다. 

Subject 호출 후 바로 onCompleted()를 호출해야 Subject가 disposed 되어 Subject로 인한 메모리 누수가 발생하는 것을 방지합니다.

<p> {% gist swieeft/a2806b7e4d59d2b5ed70acf99f810492 RxSwiftDelegate2-2.swift %} </p>

### ViewController에서 Subject 구독하기

---

flatMap으로 ViewController를 호출한 후 선언 된 Observable을 리턴합니다.
그 후에 bind 또는 subscribe로 리턴 받은 Observable의 값으로 데이터를 처리하시면 됩니다.

<p> {% gist swieeft/a2806b7e4d59d2b5ed70acf99f810492 RxSwiftDelegate2-3.swift %} </p>

### 마무리

---

Subject를 활용하여 Delegate 패턴처럼 사용하는 방법을 알아보았는데요. 첫번째 방법에 비해 코드도 간결해지고 한 곳에서 코드를 쭉 확인할 수 있어서 간단하고 가독성도 좋아진 것 같습니다.

하지만 모든 것들이 장점이 있다면 단점이 있듯이 Subject를 활용한 방법은 하나의 Subject만 만들어서 사용할 수 있다는 단점이 있습니다. 한마디로 여러 개의 Delegate 메소드가 필요한 경우에는 사용하기 힘들다는 것이죠.

이 부분은 제가 아직 RxSwift에 대한 이해도가 낮아서 방법이 있지만 찾지 못한 것일 수도 있기 때문에 100% 사용하지 못한다고는 할 수 없겠습니다.

이렇게 총 2개의 게시글로 RxSwift에서 Delegate 패턴 사용하기를 마무리하게 되었습니다. 

감사합니다. 달콤한 코딩 되세요~!

### 예제 프로젝트 링크

---

[swieeft/RxSwiftDelegateExample](https://github.com/swieeft/RxSwiftDelegateExample)

### 참고자료

---

[[RxSwift][Swift3] Closure, Delegate 대신 Observable을 사용해서 응답값을 쉽게 처리하기 - 이상한모임](https://blog.weirdx.io/post/42023)
