---
title: "[Swift] 열거형(Enum) 고급편"
layout: post
date: 2020-03-02 17:00
tag:
    - iOS
    - Swift
headerImage: false
image:
description: 열거형(Enum) 고급편
category: blog
author: swieeft
externalLink: true
published: true
comments: true
share: true
use_math: false
---
오늘은 열거형의 고급 활용에 대해 알아보려고 합니다. 저번 기본편에서는 열거형을 만들고, 사용하는 법을 배웠는데 이번엔 좀 더 깊이 들어가 열거형을 어떻게 더 사용할 수 있는지 알아보려고 합니다.

혹시 열거형 기본편을 확인하고 싶으신 분들은 아래 링크를 참고 해주세요.

[[Swift] 열거형(Enum) 기본편](https://swieeft.github.io/EnumBasic/)

### 프로토콜

---

스위프트 열거형은 하나의 데이터 타입으로 정의 될 수 있는데요. 그 중에 구조체와 유사한 점들이 많이 있습니다. 일단 메서드나 프로퍼티(열거형은 연산 프로퍼티만 가능)를 정의할 수 있으며, 둘 다 Call by Value로 메모리 주소를 복사하지 않고 값이 복사되는 형태를 가지고 있습니다.

그리고 스위프트에서 가장 많이 활용 되는 프로토콜을 적용할 수 있다는 점이 유사합니다. 스위프트 문법을 공부하다 보면 POP에 대한 이야기가 많이 언급 되는 것을 확인할 수 있는데, 열거형에서도 프로토콜을 채택할 수 있어 프로토콜의 여러 장점을 활용할 수 있습니다.

- **프로토콜 선언**

    기본편에서는 메뉴판 하나만을 사용하였는데, 이번엔 분식집, 고기집, 양식집 메뉴판을 만들어 보려고 합니다. 모든 메뉴판에는 기본적으로 메뉴 이름을 보여줘야 되고, 다음 메뉴를 볼 수 있게 넘기는 기능이 필요합니다. 이 기능은 모든 메뉴판에 필수적으로 들어가야 되기 때문에 프로토콜로 선언 해주어 모든 메뉴판에서 채택하도록 합니다.

    ```swift
    protocol 메뉴판프로토콜 {
        var 메뉴이름: String { get }
        mutating func 다음메뉴() -> Self
    }
    ```

    메뉴이름 프로퍼티에 get만 있는 것은 열거형에서는 연산 프로퍼티만 사용할 수 있기 때문입니다.

- **열거형 프로토콜 채택**

    이제 메뉴판프로토콜을 각 메뉴판에 채택하여 메뉴이름, 다음메뉴를 구현하도록 합니다. 프로토콜 채택은 구조체, 클래스와 마찬가지로 열거형 이름 옆에 콜론(:)을 한 뒤 프로토콜을 입력하면 됩니다.

    ```swift
    enum 분식집메뉴판: 메뉴판프로토콜 {
        case 라면
        case 김밥
        case 떡볶이
    
        var 메뉴이름: String {
            switch self {
            case .라면:
                return "라면"
            case .김밥:
                return "김밥"
            case .떡볶이:
                return "떡볶이"
            }
        }
    
        func 다음메뉴() -> 분식집메뉴판 {
            switch self {
            case .라면:
                return .김밥
            case .김밥:
                return .떡볶이
            case .떡볶이:
                return .라면
            }
        }
    }
    
    enum 고기집메뉴판: 메뉴판프로토콜 {
        case 삼겹살
        case 목살
        case 냉면
    
        var 메뉴이름: String {
            switch self {
            case .삼겹살:
                return "삼겹살"
            case .목살:
                return "목살"
            case .냉면:
                return "냉면"
            }
        }
    
        func 다음메뉴() -> 고기집메뉴판 {
            switch self {
            case .삼겹살:
                return .목살
            case .목살:
                return .냉면
            case .냉면:
                return .삼겹살
            }
        }
    }
    
    enum 양식집메뉴판: 메뉴판프로토콜 {
        case 파스타
        case 피자
        case 스테이크
    
        var 메뉴이름: String {
            switch self {
            case .파스타:
                return "파스타"
            case .피자:
                return "피자"
            case .스테이크:
                return "스테이크"
            }
        }
    
        func 다음메뉴() -> 양식집메뉴판 {
            switch self {
            case .파스타:
                return .피자
            case .피자:
                return .스테이크
            case .스테이크:
                return .파스타
            }
        }
    }
    ```

- **사용하기**

    프로토콜을 채택하여 만든 프로퍼티와 메서드 사용하는 방법은 기존에 직접 정의 했을 때 처럼  사용하면 됩니다.

    ```swift
    var 분식집 = 분식집메뉴판.라면
    print(분식집.메뉴이름)
    분식집 = 분식집.다음메뉴()
    print(분식집.메뉴이름)
    분식집 = 분식집.다음메뉴()
    print(분식집.메뉴이름)
    /** 
    라면
    김밥
    떡볶이
    **/
    ```

### 익스텐션(extension)

---

열거형도 익스텐션을 사용하여 케이스와 메서드, 프로퍼티를 분리하여 가독성을 높일 수 있습니다.

- **익스텐션 사용하기**

    ```swift
    enum 분식집메뉴판 {
        case 라면
        case 김밥
        case 떡볶이
    }
    
    extension 분식집메뉴판: 메뉴판프로토콜 {
        var 메뉴이름: String {
            switch self {
            case .라면:
                return "라면"
            case .김밥:
                return "김밥"
            case .떡볶이:
                return "떡볶이"
            }
        }
    
        func 다음메뉴() -> 분식집메뉴판 {
            switch self {
            case .라면:
                return .김밥
            case .김밥:
                return .떡볶이
            case .떡볶이:
                return .라면
            }
        }
    }
    ```

    이렇게 케이스와  메서드, 프로퍼티를 익스텐션을 사용해서 분리할 수 있습니다. 또한 여러 프로토콜을 채택한 열거형이라면 각 프로토콜별로 익스텐션을 만들어서 관리할 수도 있습니다.

- **프로토콜 익스텐션 만들기**

    프로토콜 자체를 익스텐션하여 프로토콜이 요구하는 사항을 모두 한꺼번에 구현할 수 있는 방법이 프로토콜 익스텐션입니다. 

    프로토콜 익스텐션을 활용하면 중복되는 코드를 피할 수 있고, 프로토콜을 채택한 곳에서 프로토콜이 요구하는 사항을 모두 구현해 줄 필요가 없습니다.

    ```swift
    protocol 메뉴판프로토콜 {
        var 메뉴이름: String { get }
        func 다음메뉴() -> Self
    }
    
    extension 메뉴판프로토콜 {
        var 메뉴이름: String {
            return String(describing: self)
        }
    }
    
    enum 분식집메뉴판: 메뉴판프로토콜 {
        case 라면
        case 김밥
        case 떡볶이
    
        func 다음메뉴() -> 분식집메뉴판 {
            switch self {
            case .라면:
                return .김밥
            case .김밥:
                return .떡볶이
            case .떡볶이:
                return .라면
            }
        }
    }
    
    var 분식집 = 분식집메뉴판.라면
    print(분식집.메뉴이름)
    분식집 = 분식집.다음메뉴()
    print(분식집.메뉴이름)
    분식집 = 분식집.다음메뉴()
    print(분식집.메뉴이름)
    /**
    라면
    김밥
    떡볶이
    **/
    ```

    분식집메뉴판 열거형을 보시면 메뉴판프로토콜을 채택 한 후 메뉴이름을 구현하지 않았지만 오류가 나지 않는 것을 확인 할 수 있습니다.

- **프로토콜 익스텐션 재정의**

    만약 메뉴이름을 각 항목의 이름이 아닌 좀 더 멋진 메뉴 이름으로 바꾸고 싶다면 열거형 안에서 재정의 해주면 됩니다.

    ```swift
    enum 분식집메뉴판: 메뉴판프로토콜 {
        case 라면
        case 김밥
        case 떡볶이
    
        var 메뉴이름: String {
            switch self {
            case .라면:
                return "계란 하나 톡 들어간 파송송 라면"
            case .김밥:
                return "밥보다 햄이 더 많은 김밥"
            case .떡볶이:
                return "추억의 맵달맵달 떡볶이"
            }
        }
    
        func 다음메뉴() -> 분식집메뉴판 {
            switch self {
            case .라면:
                return .김밥
            case .김밥:
                return .떡볶이
            case .떡볶이:
                return .라면
            }
        }
    }
    
    var 분식집 = 분식집메뉴판.라면
    print(분식집.메뉴이름)
    분식집 = 분식집.다음메뉴()
    print(분식집.메뉴이름)
    분식집 = 분식집.다음메뉴()
    print(분식집.메뉴이름)
    /**
    계란 하나 톡 들어간 파송송 라면
    밥보다 햄이 더 많은 김밥
    추억의 맵달맵달 떡볶이
    **/
    ```

### 제네릭 열거형

---

제네릭을 적용한 열거형을 만들 수 있습니다. 스위프트 문법 중에 제네릭 열거형을 활용한 대표적인 예는 옵셔널(Optional)이라고 할 수 있습니다. 

- **옵셔널 구현 형태**

    [옵셔널(Optional) 공식문서](https://developer.apple.com/documentation/swift/optional)를 보시면 간단하게 아래와 같이 구현 되어 있는 것을 볼 수 있습니다.

    ```swift
    enum Optional<Wrapped> {
        case none          /** nil일 경우 **/
        case some(Wrapped) /** 값이 있을 경우 **/
    }
    ```

    여기서 <Wrapped>가 제네릭 파라메터이고 이 제네릭 파라메터로 다양한 타입의 옵셔널을 만들 수 있게 되는 것입니다.

- **옵셔널 열거형 사용**

    옵셔널을 구현할 때 단순하게 변수 타입에 ?를 붙이면 되지만 아래와 같이 사용이 가능합니다.

    ```swift
    let someValue = Optional<String>.some("some")
    let nilValue = Optional<String>.none
    
    print(someValue)
    print(nilValue)
    /**
    Optional("some")
    nil
    **/
    ```

    옵셔널 타입을 String으로 선언 해줬기 때문에 String 옵셔널 변수가 만들어 집니다. print 해보면 someValue에는 값으로 넣어준 "some"이 출력 되는 것을 볼 수 있고, nilValue에는 nil이 출력 되는 것을 확인할 수 있습니다.

### 재귀적 /간접 타입 열거형

---

재귀적 / 간접 타입을 사용하면 열거형의 각 항목의 연관 값으로 열거형 타입을 지정해줄 수  있습니다.  열거형은 구조체와 마찬가지로 크기가 일정한 데이터 타입이라고 볼 수 있습니다.

하지만 자기 자신을 참조하는 열거형은 잠재적으로 무한한 크기를 가지가 될 수 있어 컴파일러에게 해당 타입이 재귀적 / 간접 타입이라는 것을 명시 해주어야 합니다.

- **재귀적 / 간접 타입 열거형 선언**

    재귀적 / 간접 타입을 사용하기 위해서는 indirect를 사용해야 합니다. 열거형 전체 항목에 적용하려면 enum 앞에 선언하고, 특정 항목에만 적용하려면 case 앞에 선언 해주면 됩니다.

    - 전체에 적용

        ```swift
        indirect enum LinkedListItem<T> {
            case end(value: T)
            case node(value: T, next: LinkedListItem)
        }
        ```

    - 특정 항목에만 적용

        ```swift
        enum LinkedListItem<T> {
            case end(value: T)
            indirect case node(value: T, next: LinkedListItem)
        }
        ```

- **재귀적 / 간접 타입 열거형 사용**

    ```swift
    let cNode = LinkedListItem.end(value: "c")
    let bNode = LinkedListItem.node(value: "b", next: cNode)
    let aNode = LinkedListItem.node(value: "a", next: bNode)
    
    var current = aNode
    
    linkedListLoop: while true {
        switch current {
        case let .end(value):
            print(value)
            break linkedListLoop
        case let .node(value, next):
            print(value)
            current = next
        }
    }
    /**
    a
    b
    c
    **/
    ```

> 재귀적 / 간접 타입 열거형은 아직 저도 100% 이해한 부분이 아니라서 내용이 부실합니다. 좀 더 공부해서 내용을 더 추가하도록 하겠습니다.

### 열거형 연관 값으로 비교하기

---

열거형의 케이스만으로 비교를 할 경우엔 if T.a == T.b 처럼 쉽게 비교 연산을 할 수 있습니다. 하지만 연관 값이 들어 있을 경우 비교하는 로직이 복잡해질 수 있는데 이 때 직접 비교 연산자를 만들어서 사용하면 좀 더 간편하게 연관 값을 비교할 수 있습니다.

- **비교 연산자 만들기**

    비교 연산자를 만드는건 구조체나 다른 곳에서 만드는 방식과 동일하게 func ==() -> Bool을 사용하면 됩니다.

    ```swift 
    enum 주문서 {
        case 주문내역(메뉴: String, 인분: Int)
    }
    
    func ==(lhs: 주문서, rhs: 주문서) -> Bool {
        switch (lhs, rhs) {
        case let (.주문내역(메뉴1, 인분1), .주문내역(메뉴2, 인분2)) where 메뉴1 == 메뉴2 && 인분1 == 인분2:
            return true
        default:
            return false
        }
    }
    ```

    비교 연산자 메서드 안에서 switch 문을 이용해 연관 값을 추출한 후 where을 통해 비교하고자 하는 값을 비교하여 결과를 리턴 해주면 됩니다.

- **비교 연산자 사용하기**

    위에 비교 연산자를 만들었다면 사용하는 방법은 일반적인 비교 연산자와 동일합니다.

    ```swift
    let 주문1 = 주문서.주문내역(메뉴: "삼겹살", 인분: 5)
    let 주문2 = 주문서.주문내역(메뉴: "삼겹살", 인분: 5)
    
    print(주문1 == 주문2) /** true **/
    
    let 주문3 = 주문서.주문내역(메뉴: "목살", 인분: 5)
    let 주문4 = 주문서.주문내역(메뉴: "삼겹살", 인분: 5)
    
    print(주문3 == 주문4) /** false **/
    ```

### 커스텀 생성자

---

만약 API를 통해 문자열로 된 값을 받아 와서 열거형으로 변환을 하여 사용하려고 하면 어떻게 해야 될까요? 

기본편에서 배웠던 정적 메서드를 이용해서 하는 방법도 있지만 그것보다 더 깔끔하게 사용하는 방법이 커스텀 생성자를 이용하는 것입니다.

- **커스텀 생성자 만들기**

    생성자 만드는 방법은 구조체나 클래스의 생성자를 만드는 방법과 동일하게 init을 만들어 주면 됩니다. 아래는 서버에서 받은 에러 코드 값으로 에러 메시지를 찾는 열거형입니다.

    ```swift
    enum ErrorCode {
        case Code400
        case Code404
        case Code500
        case CodeNil
    
        init(errorCode: Int) {
            switch errorCode {
            case 400:
                self = .Code400
            case 404:
                self = .Code404
            case 500:
                self = .Code500
            default:
                self = .CodeNil
            }
        }
    
        var errorMessage: String {
            switch self {
            case .Code400:
                return "서버 요청 실패"
            case .Code404:
                return "페이지가 존재하지 않음"
            case .Code500:
                return "서버 응답 없음"
            case .CodeNil:
                return "알 수 없는 에러"
            }
        }
    }
    ```

- **커스텀 생성자 사용하기**

    생성자를 사용하려면 Enum.init()을 사용하면 됩니다.

    ```swift
    let errorCode = ErrorCode.init(errorCode: 404)
    print(errorCode.errorMessage)
    /** 페이지가 존재하지 않음 **/
    
    let errorCode2 = ErrorCode.init(errorCode: 700)
    print(errorCode2.errorMessage)
    /** 알 수 없는 에러 **/
    ```

- **실패할 수 있는 생성자 만들기**

    열거형에도 실패할 수 있는 생성자를 만들 수 있습니다. init 뒤에 ?만 붙여 주면 원하는 초기화 값이 없을 경우 nil을 반환하게 됩니다.

    ```swift
    enum ErrorCode {
        case Code400
        case Code404
        case Code500
    
        init?(errorCode: Int) {
            switch errorCode {
            case 400:
                self = .Code400
            case 404:
                self = .Code404
            case 500:
                self = .Code500
            default:
                return nil
            }
        }
    
        var errorMessage: String {
            switch self {
            case .Code400:
                return "서버 요청 실패"
            case .Code404:
                return "페이지가 존재하지 않음"
            case .Code500:
                return "서버 응답 없음"
            }
        }
    }
    
    let errorCode = ErrorCode.init(errorCode: 404)
    print(errorCode?.errorMessage)
    /** 페이지가 존재하지 않음 **/
    
    let errorCode2 = ErrorCode.init(errorCode: 700)
    print(errorCode2?.errorMessage)
    /** nil **/
    ```

### 마무리

---

기나긴 열거형 기본편과 고급편을 마무리하게 되었습니다. 저도 열거형에 대한 글을 정리하려고 검색을 하니 제가 알지 못 했던 사용 방법도 많이 있어서 쉽게 생각하고 글을 작성 했다가 장장 두 편에 걸쳐서 글을 작성하게 되었네요.

스위프트를 사용하면서 열거형은 잘 활용하면 더 좋고 직관적인 코드 작성이 가능한 것 같습니다. 저도 진행하고 있는 프로젝트에서 열거형을 사용하면 더 좋은 부분을 찾아서 바꿔 보려고 합니다.

여러분도 기존에 쓰던 방식이 편하다고 그냥 두지 마시고 바꿔 볼 수 있는 부분들을 찾아서 바꾸다 보면 열거형에 많이 익숙해지고 더 좋은 코드를 만들 수 있을 것 같습니다.

그럼 달콤한 코딩 되세요!

### 참고자료

---

[열거형의 고급 활용과 모범 사례](https://outofbedlam.github.io/swift/2016/04/05/EnumBestPractice/)

[What are indirect enums?](https://www.hackingwithswift.com/example-code/language/what-are-indirect-enums)

[indirect enums and structs](https://stackoverflow.com/questions/37533006/indirect-enums-and-structs/37533442)

[Swift - 프로토콜 지향 프로그래밍 - yagom's blog](https://blog.yagom.net/531/)