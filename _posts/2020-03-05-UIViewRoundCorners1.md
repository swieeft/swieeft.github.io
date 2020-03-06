---
title: "[iOS] UIView 특정 모서리만 둥글게 만들기(Round Corners)"
layout: post
date: 2020-03-05 17:45
tag:
    - iOS
    - Swift
headerImage: false
image:
description: UIView 특정 모서리만 둥글게 만들기(Round Corners)
category: blog
author: swieeft
externalLink: true
published: true
comments: true
share: true
use_math: false
---
오늘은 UIView에서 특정 모서리만 둥글게 처리하는 방법을 알아보려고 합니다.

개발을 하다보면 "뷰의 상단만 둥글게 해주세요", "왼쪽 상단만 둥글게 해주세요" 등의 요구사항을 받을 때가 있는데 그때 사용 하시면 될 것 같습니다.

### iOS 11 이상에서 둥글게 만들기

---

iOS 11 이상에서는 애플에서 CACornerMask라는 녀석을 제공 해주어 이전보다 더 쉽게 특정 모서리만 둥글게 처리하는 것이 가능해졌습니다.

- **예제 코드**

    빨간색 배경의 직사각형의 상단을 둥글게 만드는 코드입니다.

    ```swift
    class ViewController: UIViewController {
    
        @IBOutlet weak var cornerView: UIView!
    
        override func viewDidLoad() {
            super.viewDidLoad()
    
            cornerView.clipsToBounds = true
            cornerView.layer.cornerRadius = 50
            cornerView.layer.maskedCorners = CACornerMask(arrayLiteral: .layerMinXMinYCorner, .layerMaxXMinYCorner)
        }
    }
    ```

    여기서 CACornerMask를 통해 둥글게 만들려는 포인트를 설정할 수 있습니다.

    여러 모서리를 둥글게 처리하기 위해선 위의 코드처럼 초기화를 arrayLiteral로 선택해서 원하는 모서리의 위치를 지정 해주면 됩니다.

    한 곳의 모서리만 둥글게 하고 싶으면 아래와 같이 사용하시면 됩니다.

    ```swift
    cornerView.layer.maskedCorners = CACornerMask.layerMaxXMaxYCorner
    ```

- **모서리의 값**

    위의 예제 코드를 보다 보면 layerMaxXMaxYCorner 같이 알아 먹기 힘든 코드를 볼 수 있는데, 이게 각 모서리의 위치입니다.

    - 선언 된 형태

        ```swift
        public struct CACornerMask : OptionSet {
        
            public init(rawValue: UInt)
        
            public static var layerMinXMinYCorner: CACornerMask { get }
            public static var layerMaxXMinYCorner: CACornerMask { get }
            public static var layerMinXMaxYCorner: CACornerMask { get }
            public static var layerMaxXMaxYCorner: CACornerMask { get }
        }
        ```

    - 모서리 값 분석

        layer와 Corner는 공통적으로 사용 되기 때문에 무시하셔도 됩니다.

        - layerMinXMinYCorner = layer, **MinX**, **MinY**, Corner
            - MinX : 뷰의 최소 X 좌표 값 (뷰의 왼쪽)
            - MinY : 뷰의 최소 Y 좌표 값 (뷰의 상단)
            - **뷰의 왼쪽 상단 모서리**
        - layerMaxXMinYCorner = layer, **MaxX**, **MinY**, Corner
            - MaxX : 뷰의 최대 X 좌표 값 (뷰의 오른쪽)
            - MinY :  뷰의 최소 Y 좌표 값 (뷰의 상단)
            - **뷰의 오른쪽 상단 모서리**
        - layerMinXMaxYCorner = layer, **MinX**, **MaxY**, Corner
            - MinX : 뷰의 최소 X 좌표 값 (뷰의 왼쪽)
            - MaxY : 뷰의 최대 Y 좌표 값 (뷰의 하단)
            - **뷰의 왼쪽 하단 모서리**
        - layerMaxXMaxYCorner = layer, **MaxX**, **MaxY**, Corner
            - MaxX : 뷰의 최대 X 좌표 값 (뷰의 오른쪽)
            - MaxY : 뷰의 최대 Y 좌표 값 (뷰의 하단)
            - **뷰의 오른쪽 하단 모서리**

    - 각 값의 위치

    ![UIViewRoundCorners1.png](/assets/images/posts/2020-03-05/UIViewRoundCorners1.png)

- **실행 결과**

    첫번째 예제 코드를 실행 해보면 뷰의 상단만 둥글게 처리 된 것을 확인할 수 있습니다.

    ![UIViewRoundCorners2.png](/assets/images/posts/2020-03-05/UIViewRoundCorners2.png)

- **익스텐션(Extension)으로 만들어서 공용으로 사용하기**

    위의 예제 코드는 하나의 뷰에서만 사용할 수 있도록 하였는데, UIView를 익스텐션하여 메서드를 만들어서 여러 곳에서 공용으로 사용할 수 있게 만들 수 있습니다.

    - 익스텐션 만들기

        ```swift
        extension UIView {
        func roundCorners(cornerRadius: CGFloat, maskedCorners: CACornerMask) {
                clipsToBounds = true
                layer.cornerRadius = cornerRadius
                layer.maskedCorners = CACornerMask(arrayLiteral: maskedCorners)
            }
        }
        ```

    - 익스텐션 메서드 사용하기

        ```swift
        cornerView.roundCorners(cornerRadius: 50, maskedCorners: [.layerMinXMinYCorner, .layerMaxXMinYCorner])
        ```

### iOS 10 이하에서 둥글게 만들기

---

요즘은 대부분의 앱들이 iOS 11 이상을 지원하고 있어 많이 사용되진 않지만 그래도 필요로 하는 경우가 있어 iOS 10 이하에서 둥글게 만드는 법도 알아보겠습니다.

- **예제 코드**

    예제는 아까와 똑같이 빨간색 배경을 가진 뷰의 상단 모서리를 둥글게 처리하는 것입니다.

    하지만 CACornerMask는 iOS 11 이상에서 지원 해주기 때문에 UIBezierPath를 이용해서 둥글게 만들어 주어야 합니다.

    ```swift
    class ViewController: UIViewController {
    
        @IBOutlet weak var cornerView: UIView!
    
        override func viewDidLoad() {
            super.viewDidLoad()
    
            let path = UIBezierPath(roundedRect: cornerView.bounds, 
                                    byRoundingCorners: [.topLeft, .topRight], 
                                    cornerRadii: CGSize(width: 50, height: 50))
    
            let maskLayer = CAShapeLayer()
            maskLayer.frame = cornerView.bounds
            maskLayer.path = path.cgPath
    
            cornerView.layer.mask = maskLayer
        }
    }
    ```

    UIBezierPath를 이용해 둥근 사각형의 Path를 만들어 줍니다. byRoundingCorners에 모서리를 둥글게 만들고 싶은 곳을 배열로 입력 해주면 됩니다.

- **모서리의 값**
    - 선언된 형태

        ```swift
        public struct UIRectCorner : OptionSet {
        
            public init(rawValue: UInt)
        
            
            public static var topLeft: UIRectCorner { get }
            public static var topRight: UIRectCorner { get }
            public static var bottomLeft: UIRectCorner { get }
            public static var bottomRight: UIRectCorner { get }
            public static var allCorners: UIRectCorner { get }
        }
        ```

    - 모서리 값 분석

        UIBezierPath에서 사용하는 모서리의 값은 CACornerMask의 값 보다 명확하게 되어 있습니다. 
        
        (왜 CACornerMask는 복잡하게 만들었을까요? 아시는 분 있으면 답글 좀 남겨주세요)

        - topLeft : 상단 왼쪽 모서리
        - topRight : 상단 오른쪽 모서리
        - bottomLeft : 하단 왼쪽 모서리
        - bottomRight : 하단 오른쪽 모서리
        - allCorners : 네개의 모든 모서리

- **실행 결과**

    실행 결과는 **iOS 11 이상에서 둥글게 만들기**의 결과와 동일합니다.

- **익스텐션(Extension)으로 만들어서 공용으로 사용하기**
    - 익스텐션 만들기

        ```swift
        extension UIView {
            func roundCorners(cornerRadius: CGFloat, byRoundingCorners: UIRectCorner) {
                let path = UIBezierPath(roundedRect: self.bounds, 
                                        byRoundingCorners: byRoundingCorners, 
                                        cornerRadii: CGSize(width:cornerRadius, height: cornerRadius))
        
                let maskLayer = CAShapeLayer()
                maskLayer.frame = self.bounds
                maskLayer.path = path.cgPath
        
                layer.mask = maskLayer
            }
        }
        ```

    - 익스텐션 메서드 사용하기

        ```swift
        cornerView.roundCorners(cornerRadius: 50, byRoundingCorners: [.topLeft, .topRight])
        ```

### 모든 버전에서 사용 가능하도록 익스텐션(Extension) 만들기

---

타겟 버전은 iOS 10 이하 이지만 iOS 11 이상을 쓰는 사용자들에게는 CACornerMask를 사용하도록 하고 싶다면 두개의 코드를 분기 처리하면 됩니다.

```swift
func roundCorners(cornerRadius: CGFloat, byRoundingCorners: UIRectCorner) {
    if #available(iOS 11.0, *) {
        clipsToBounds = true
        layer.cornerRadius = cornerRadius
        layer.maskedCorners = CACornerMask(rawValue: byRoundingCorners.rawValue)
    } else {
        let path = UIBezierPath(roundedRect: self.bounds, 
                                byRoundingCorners: byRoundingCorners, 
                                cornerRadii: CGSize(width:cornerRadius, height: cornerRadius))

        let maskLayer = CAShapeLayer()
        maskLayer.frame = self.bounds
        maskLayer.path = path.cgPath

        layer.mask = maskLayer
    }
}
```

### 마무리

---

이렇게 UIView의 특정 모서리를 둥글게 만드는 법을 알아보았습니다. 저도 지금까지 계속 UIBezierPath를 사용해서 만드는 방법만 사용하고 있었는데 CACornerMask라는게 있는 줄 이 글을 작성하면서 처음 보았습니다.

역시 개발자는 계속 해서 새로운 것을 찾아서 공부해야 되는 직업이라는 것을 새삼 깨닫는 순간이었습니다.

익숙한 것만 찾다가는 순식간에 도태되어 버리는 것 같네요. iOS 11부터 지원한거라면 시간이 꽤 지났는데도 매번 똑같은 코드만 사용 했던 제가 좀 부끄럽네요.

여러분도 익숙함에 빠지지 마세요! 그럼 달콤한 코딩 되세요!

### 참고자료

---

[Round Top Corners of a UIView in Swift](https://stackoverflow.com/questions/46179735/round-top-corners-of-a-uiview-in-swift)