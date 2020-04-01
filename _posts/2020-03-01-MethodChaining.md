---
layout: post
title: "함수 체이닝(Method Chaining) 만들기"
subtitle: "[Swift]"
date: 2020-03-01 11:15
background: 
tag: [iOS, Swift]
---

이번엔 함수 체이닝(Method Chaining)에 대한 글을 작성 해보려고 합니다. 우리는 흔히 코딩을 하면서 같은 대상에 대한 여러가지 작업을 처리해야 되는 경우가 생깁니다.

기본적인 라이브러리에서는 한줄 한줄 입력을 해야만 하는 경우가 생기는데, 이 부분을 계속 연결해 가면서 설정 하는 방식을 체이닝이라고 합니다.

우리가 일반적으로 무의식 중에도 체이닝을 사용하고 있고, 또 체이닝을 사용하고 싶지만 지원을 안 해서 못 하는 경우도 발생합니다. 그래서 일반적으로 사용하는 체이닝은 어떤 것이 있는지, 또 체이닝을 사용하고 싶은데 어떻게 만들어서 사용할 수 있는지 알아보려고 합니다.

### 일반적으로 사용되는 함수 체이닝

---

ReactiveX라던가 Alamofire 같은 라이브러리 코드를 보면 코드를 점(.)으로 이어가면서 한번에 쭉 기술하는 것을 볼 수 있습니다. 바로 체이닝을 사용한 것인데요. 

라이브러리 뿐만 아니라 Swift에서도 기본적으로 사용할 수 있는 체이닝들이 있습니다.

- **예제 코드**

    문자열을 split한 후 filter를 통해 걸러진 데이터의 개수를 구하는 방법 입니다. 
    
    체이닝으로 연결이 안 된다면 split, filter, count를 각각 따로 입력 받아서 처리해야 되지만 체이닝을 통해 한 줄로 구현이 되었습니다.

    <p> {% gist swieeft/57ba3439b14138b3b63309ad9685c86c MethodChaining1.swift %} </p>

- **코드 분석**

    위의 예제 코드를 하나씩 뜯어보도록 하겠습니다.

    우선 "aaa\|bbb\|ccc"가 반복되는 문자열을 string이란 상수로 생성하였습니다.

    <p> {% gist swieeft/57ba3439b14138b3b63309ad9685c86c MethodChaining2.swift %} </p>

    위에 선언 된 string을 "\|"를 기준으로 split을 합니다. 그 후 값이 "aaa"인 것만 filter를 통해 걸러 내어 "aaa"의 갯수가 총 몇 개 인지 확인하고 있습니다.

    <p> {% gist swieeft/57ba3439b14138b3b63309ad9685c86c MethodChaining3.swift %} </p>

    위의 코드가 어떻게 체이닝이 가능한 것 일까요? 그건 메서드 하나하나 찾아 들어가보면 답이 나옵니다.

    - split

        split 메서드를 보면 반환 타입이 **[Substring]**으로 되어 있습니다. 
        
        우리는 이것을 통해 문자열을 split 하면 배열이 나온다는 것을 유추할 수 있고, 배열에서 사용 가능한 메서드를 체이닝 할 수 있다는 것을 알게 됩니다.

        그래서 split를 사용한 후 배열에서 사용 가능한 filter 메서드 체이닝을 할 수 있게 되었습니다.

        <p> {% gist swieeft/57ba3439b14138b3b63309ad9685c86c MethodChaining4.swift %} </p>

    - filter

        filter 메서드도 확인 해보면 Array<T> 타입을 반환하는 것을 볼 수 있습니다. T라는건 제네릭 타입입니다. 

        그럼 여기서 유추할 수 있는 것은 Split을 통해 만들어진 배열은 [Substring]이므로, filter를 통해 반환 되는 배열도 [Substring]이란 것을 알 수 있게 됩니다.

        그래서 filter 후에 배열의 갯수를 확인하는 count 프로퍼티를 사용할 수 있게 됩니다.

        <p> {% gist swieeft/57ba3439b14138b3b63309ad9685c86c MethodChaining5.swift %} </p>

        > 제네릭 타입은 어떤 타입으로도 사용 가능한 타입입니다. Int가 들어오면 Int 타입이 되고 String이 들어오면 String 타입이 됩니다. (내용이 좀 많아 간략하게만 설명하고 넘어갑니다. 궁금하신 분들은 따로 검색 해보시면 좋은 글들이 많이 있습니다.)

### 함수 체이닝 만들기

---

위에서는 이미 Swift에서 지원하고 있는 함수 체이닝을 보았습니다. 근데 체이닝 방식은 지원해주는 것만 쓸 수 있을까요? 당연히 아닙니다. 

우리에겐 Extension이라는 아주 매력적인 것이 있죠. Extension을 통해 우리가 만들고 싶은 체이닝을 만들어서 사용할 수 있습니다.

제가 체이닝으로 많이 활용하는 것이 UIBezierPath여서, 예제도 간단하게 UIBezierPath를 활용하여 작성하도록 하겠습니다.

- **UIBezierPath로 삼각형 그리기**

    - 기존 방식으로 그린 삼각형

        삼각형을 그리는데 move, addLine의 반환 값이 Void여서 path를 하나 그릴 때마다 **path.** 를 계속 입력하면서 한 줄씩 작성해야 됩니다.

        <p> {% gist swieeft/57ba3439b14138b3b63309ad9685c86c MethodChaining6.swift %} </p>

    - 체이닝을 위한 extension 만들기

        UIBezierPath를 extension하여 기존에 반환 타입이 Void인 move와 addLine에 **Self**를 반환하는 메서드를 만들어 주었습니다. 

        Self 반환은 자기자신을 반환 하는 것을 의미합니다. 기본 move, addLine을 호출 후 자기 자신을 반환하여 이후 작업을 계속 이어갈 수 있도록 만들어 주는 것입니다.

        <p> {% gist swieeft/57ba3439b14138b3b63309ad9685c86c MethodChaining7.swift %} </p>

    - 체이닝을 이용해 그린 삼각형

        move, addLine을 점(.)으로 연결해서 계속 작성해 나가는 것을 볼 수 있습니다.

        <p> {% gist swieeft/57ba3439b14138b3b63309ad9685c86c MethodChaining8.swift %} </p>

- **CAShapeLayer 설정도 체이닝으로 변경하기**

    UIBezierPath 뿐만 아니라 생성 중인 CAShapeLayer도 **layer.** 으로 한 줄씩 입력을 하고 있는 것을 확인할 수 있습니다. 이 부분도 체이닝으로 바꿔서 적용 해보도록 하겠습니다.

    - 기존 방식으로 설정한 CAShapeLayer

        <p> {% gist swieeft/57ba3439b14138b3b63309ad9685c86c MethodChaining9.swift %} </p>

    - 체이닝을 위한 extension 만들기

        CAShapeLayer의 extension을 만들었습니다. 각각의 프로퍼티 입력을 받는 함수를 만들고 Self를 리턴 시켜 체이닝을 사용할 수 있도록 해주었습니다.

        그리고 마지막에 add 메서드를 이용하여 layer를 추가하는 메서드까지 추가해 레이어 생성, 설정, 추가를 한 줄로 입력할 수 있도록 하였습니다.

        <p> {% gist swieeft/57ba3439b14138b3b63309ad9685c86c MethodChaining10.swift %} </p>

    - 체이닝을 이용해 설정한 CAShapeLayer

        <p> {% gist swieeft/57ba3439b14138b3b63309ad9685c86c MethodChaining11.swift %} </p>

### 마무리

---

체이닝 만드는 법을 알아보았습니다. 어떤가요? 그 전 코드보다 좀 더 직관적이고 깔끔하게 코드가 정리 되지 않았나요? 

예제에서 알려드린 것 외에도 여러 곳에 함수 체이닝을 사용할 수 있는데요. 개발을 하시다 보면 이 부분은 체이닝을 만들어서 사용하면 깔끔 하겠다고 생각 되는 부분들이 있을 겁니다. 그 부분들을 하나하나 바꿔 보시면 좀 더 퀄리티 있고 가독성이 높은 코드를 짤 수 있을 것 같습니다.

그럼 달콤한 코딩 하세요!

### 참고자료

---

[[Swift]Method Chaining](http://minsone.github.io/mac/ios/method-chaining-in-swift)

[Types - The Swift Programming Language (Swift 5.2)](https://docs.swift.org/swift-book/ReferenceManual/Types.html#grammar_self-type)