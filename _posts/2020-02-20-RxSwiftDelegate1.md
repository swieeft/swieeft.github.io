---
layout: post
title: "RxSwift에서 Delegate 패턴 사용하기 (1/2)"
subtitle: "[RxSwift]"
date: 2020-02-20 17:30
background: 
tags: [ios,rxswift]
---

현재 다니고 있는 회사 프로젝트에서 RxSwift를 사용하고 있습니다. 근데 Delegate를 사용해도 될 것 같은 부분에  전임자분은 Delegate 대신에 Notification으로 코드를 작성해놓았더군요... 무엇 때문에? 왜?라는 물음을 가지고 작업을 시작하였습니다.

작업을 하던 중에 Delegate를 연결해야 될 일이 있어서 보니 뭔가 기존 Swift 코드 처럼 Delegate를 적용하면 Rx스럽지 않은 스타일이 되어 Rx스러운 Delegate를 만들 수 없을까 찾아보다가 발견한 내용을 정리합니다.

RxSwift에서 Delegate 패턴 사용하기는 총 2개의 파트로 작성 될 예정입니다. 첫번째는 Delegate에서 Observable 메소드로 변경하여 사용하는 방식입니다.

### 예제 프로젝트 동작 설명

---

![RxSwiftDelegateExample](/assets/images/posts/2020-02-20/RxSwiftDelegateExample1.gif)

> Delegate를 만들어줄 InputViewController는 TextField에 입력 된 문자열을 Confirm 버튼 클릭 시 ViewController에 전달하고, 전달된 문자열은 ViewController의 Label에 설정되게 됩니다.

### InputViewController에 Delegate 선언하기

---

<p>{% gist swieeft/18cd1049db057324addc9b9d04ab076b RxSwiftDelegate1-1.swift %}</p>

> Protocol에 optional을 선언한 것은 이후에 ViewController에서 Delegate 사용 시 함수를 생성하지 않고 Observable 메소드 형태로 사용하기 위함입니다.

<p>{% gist swieeft/18cd1049db057324addc9b9d04ab076b RxSwiftDelegate1-2.swift %}</p>

### DelegateProxy 설정하기

---

DelegateProxy는 Delegate의 인터페이스 역할을 해줍니다. 기존 Swift의 Delegate와 Rx를 이어주는 역할이라고 생각하면 될 것 같습니다.

코드가 조금 복잡해 보일 수 있지만 위의 코드 내용을 본인의 클래스나 프로토콜 이름으로 바꿔서 사용하시면 됩니다.

<p>{% gist swieeft/18cd1049db057324addc9b9d04ab076b RxSwiftDelegate1-3.swift %}</p>

### Reactive로 Extension하기

---

이제 기나긴 delegate 설정의 마지막 단계인 Reactive로 Extension하기입니다. 이 작업을 통해서 Delegate 함수를 Observable 메소드 형태로 변환하여 사용할 수 있게 됩니다.

<p>{% gist swieeft/18cd1049db057324addc9b9d04ab076b RxSwiftDelegate1-4.swift %}</p>

### Delegate 구독하기

---

이제 만들어준 Delegate를 ViewController에서 구독하는 코드만 넣으면 Rx의 Observable 메소드 형태로 Delegate를 사용하는 과정이 끝납니다.

<p>{% gist swieeft/18cd1049db057324addc9b9d04ab076b RxSwiftDelegate1-5.swift %}</p>

setForwardToDelegate를 먼저 설정 해주어야 원하는 동작이 가능합니다. 아직 왜 설정을 해줘야 하는지  정확한 내용을 찾지 못하여 이 부분은 좀 더 리서치 후 추가하도록 하겠습니다.

### 마무리

---

Rx에서 Delegate 사용을 좀 더 Rx스럽게 하고자 찾은 내용을 정리하였습니다. 100% 코드를 이해하지는 못하여서 중간중간 왜 이렇게 해야되는지에 대한 설명이 미흡합니다. 이 부분은 차후 좀 더 다듬어 가도록하겠습니다.

Observable 메소드 형태로 사용하여 프로젝트에 적용을 해보았는데 한가지 제약사항이 걸리는게 있었습니다. 넘겨줄 수 있는 데이터형이 Objective-c에서 사용 가능한 데이터형만 넘길 수 있었는데, 이건 위에 코드에서 보셨듯이 Selector를 이용해 Delegate를 호출해서 그런것이 아닐까 합니다.

그래서 저는 네트워크로 받은 데이터를 JSON 디코더를 통해 Codable 모델에 담아 넘겨줄려고 했지만 위의 제약 때문에 사용하지 못하였습니다.

아마 전임자분도 이런 문제들로 인해서 이 방법의 사용을 포기하지 않았을까 생각이 되지만 뭐 물어볼 수 있는 방법이 없으니 그냥 그럴꺼다 생각하고 넘어가기로 했습니다...

이 문제를 해결할 수 있는 방법이 있다면 댓글로 알려주시면 감사하겠습니다. 다른 궁금한 점이나 잘못된 점도 댓글로 남겨주시면 감사하겠습니다.

### 예제 프로젝트 링크

---

[swieeft/RxSwiftDelegateExample](https://github.com/swieeft/RxSwiftDelegateExample)

### 참고자료

---

[[ReactiveX][RxSwift]Delegate 패턴을 Rx로 바꾸기](http://minsone.github.io/programming/reactive-swift-delegate)

[[RxSwift] 예제로 이해하는 Delegate Proxy](https://eunjin3786.tistory.com/28)

[RxSwift, delegate 와 Observable](https://brunch.co.kr/@tilltue/24)
