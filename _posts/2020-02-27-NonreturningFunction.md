---
title: "[Swift] 비반환 함수에 대해 알아보기"
layout: post
date: 2020-02-27 11:15
tag:
    - iOS
    - Swift
headerImage: false
image:
description: 비반환 함수에 대해 알아보기
category: blog
author: swieeft
externalLink: true
published: true
comments: true
share: true
use_math: false
---
비반환 함수란, 또 다른 뜻으로 종료(return)되지 않는 함수라고 합니다. 종료 되지 않는 다는 것은 정상적으로 함수가 끝나지 않았다는 것을 의미하고, 이 함수가 실행 되면 프로세스가 끝났다고 볼 수 있습니다.

그렇다면 비반환 함수는 언제 사용 될까요? 바로 앱 실행을 계속 유지할 수 없는 오류가 발생할 경우 이를 사용자에게 안내하고, 서버에 오류를 보고하는 등의 일을 한 후 프로세스를 종료시킬 때 사용됩니다.

### 비반환 함수 정의 및 사용하기

---

비반환 함수는 일반적인 함수 작성 방법과 동일합니다. 다른 점은 반환 값(return type)으로 **"Never"**를 사용한다는 것입니다.  

또한 비반환 함수는 어디서든 호출 가능하며, 재정의도 가능합니다. 하지만 재정의 시에도 반환 타입은 Never가 되어야 합니다.

- **예제 코드**

    ```swift
    func mineExplosion() -> Never {
        fatalError("지뢰찾기에 실패하였습니다.")
    }
    
    func minesweeper(isMine: Bool) {
        print("== isMine : \(isMine) ==")
        guard isMine else {
            print("지뢰가 터졌습니다!")
            mineExplosion()
        }
    
        print("지뢰를 발견하였습니다.")
    }
    
    minesweeper(isMine: true)
    minesweeper(isMine: false)
    ```

- **실행 결과**

    ![NonreturningFunction1.png](/assets/images/posts/2020-02-27/NonreturningFunction1.png)

    isMine이 false일 경우 mineExplosion 메서드가 호출됩니다. mineExplosion 메서드는 반환 타입이 Never이므로 비반환함수가 되어 fatalError 메시지 출력 후 프로세스가 종료되게 됩니다.

### 마무리

---

비반환 함수를 보면 일반적인 앱 실행 상황에서는 잘 사용 되지 않을 것 같습니다. 어떻게 보면 앱이 강제로 종료된다는 것은 사용자에게는 치명적인 오류로 받아들여질 수 있고, 앱의 완성도 면에서 떨어져 보일 수도 있습니다.

그럼 강제로 앱을 종료해야 되는 상황에서는 사용 되야 하는데 대표적으로 불법 사용자를 감지하고 앱을 종료 시킬 때 사용할 수 있을 것 같습니다.

불법 사용자로 감지 되면 사용자에게 불법 사용자임을 안내하고, 서버에 사용자 블랙리스트 등록 한 뒤 앱을 강제 종료 시켜 앱 사용을 차단하는 방법 등이 있을 것 같네요.

저도 아직까지 딱 여기에 사용되면 최고다! 라는 곳은 찾지는 못 했는데요. 혹시 괜찮은 예시가 있다면 댓글로 알려주시면 감사하겠습니다.

그럼 달콤한 개발 되세요!

### 참고자료

---

- [스위프트 프로그래밍 2판](http://www.hanbit.co.kr/store/books/look.php?p_code=B2206901403)
    - 저자 : 야곰
    - 출판사 : 한빛 미디어
    - 158쪽 7.4 종료되지 않는 함수를 참고하였습니다.