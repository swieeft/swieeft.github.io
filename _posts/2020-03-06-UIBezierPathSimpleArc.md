---
title: "[iOS] UIBezierPath의 Arc 쉽게 그리는 방법"
layout: post
date: 2020-03-06 21:30
tag:
    - iOS
    - Swift
headerImage: false
image:
description: UIBezierPath의 Arc 쉽게 그리는 방법
category: blog
author: swieeft
externalLink: true
published: true
comments: true
share: true
use_math: false
---
안녕하세요. 오늘은 UIBezierPath의 Arc를 쉽게 그리는 방법에 대해 알아보려고 합니다.

UIBezierPath는 공식 문서에 이렇게 설명하고 있습니다.

> A path that consists of straight and curved line segments that you can render in your custom views. <br>
> [UIBezierPath](https://developer.apple.com/documentation/uikit/uibezierpath)

뷰에 렌더링 할 수 있는 직선 및 곡선으로 구성된 경로를 만들어 준다고 되어 있는데요. 

UIBezierPath 전부를 설명하는 글은 많아서 이 글에서는 UIBezierPath를 사용하면서 가장 까다로웠던 Arc를 좀 더 쉽게 그리는 방법을 알려 드리려고 합니다.

### 기본 Arc 그리는 방법

---

[공식문서](https://developer.apple.com/documentation/uikit/uibezierpath/1624358-init#1965853)를 보면 Arc를 그리기 위해 필요한 정보는 5가지입니다.

```swift
convenience init(arcCenter center: CGPoint, 
                radius: CGFloat, 
                startAngle: CGFloat, 
                endAngle: CGFloat, 
                clockwise: Bool)
```

각 파라메터에 대해 하나씩 살펴보면

- arcCenter : Arc의 중심점
- radius : Arc의 반지름
- startAngle : Arc의 시작 위치
- endAngle : Arc의 종료 위치
- clockwise : Arc를 그릴 방향 (true : 시계 방향, false : 시계 반대 방향)

여기서 startAngle과 endAngle에는 어떤 값을 넣어야 될지 난감해 하시는 분들이 계실겁니다. 일단 애플에서 제공하는 Angle 값의 이미지는 다음과 같습니다.

![UIBezierPathSimpleArc1.jpg](/assets/images/posts/2020-03-06/UIBezierPathSimpleArc1.jpg)

이미지를 보시면 감이 오시나요? 90도, 180도, 360도 같은 Arc를 그리는 것은 해당 이미지를 보면 감이 오는데 애매한 각도의 Arc를 그릴 땐 어떻게 해야 될지 난감합니다.

그럼 이제부터 쉽게 Angle 값을 만드는 방법을 알아보려고 합니다.

### 세 개의 Point를 이용해서 Arc 그리기

---

첫번째 방법은 세 개의 Point를 이용해서 그리는 방법입니다.

![UIBezierPathSimpleArc2.png](/assets/images/posts/2020-03-06/UIBezierPathSimpleArc2.png)

그림에서 보시는 바와 같이 **Center Point**와 **Start Point**, **End Point** 세 개의 Point를 이용해서 Arc를 그리는 방식입니다. 

여기서 Arc의 반지름(radius) 값은 Center Point와 Start Point 사이의 길이가 됩니다.

- **세 개의 Point 만들기**
    - Point 생성

        ```swift
        let centerPoint = view.center
        let startPoint = CGPoint(x: centerPoint.x + 100, y: centerPoint.y + 50)
        let endPoint = CGPoint(x: centerPoint.x - 100, y: centerPoint.y + 50)
        ```

        - centerPoint는 현재 뷰컨트롤러 있는 뷰의 Center Point로 해주었습니다.
        - startPoint는 centerPoint에서 x로 +100만큼, y로 +50 만큼 이동한 지점입니다.
        - endPoint는 centerPoint에서 x로 -100만큼, y로 +50 만큼 이동한 지점입니다.

    - 각 Point를 표시하는 점을 그리는 메서드

        ```swift
        func drawPointDot(centerPoint: CGPoint, startPoint: CGPoint, endPoint: CGPoint) {
            let path = UIBezierPath()
            path.move(to: CGPoint(x: centerPoint.x + 5, y: centerPoint.y))
            path.addArc(withCenter: centerPoint, radius: 5, startAngle: 0, endAngle: 2 * .pi, clockwise: true)
            path.move(to: CGPoint(x: startPoint.x + 5, y: startPoint.y))
            path.addArc(withCenter: startPoint, radius: 5, startAngle: 0, endAngle: 2 * .pi, clockwise: true)
            path.move(to: CGPoint(x: endPoint.x + 5, y: endPoint.y))
            path.addArc(withCenter: endPoint, radius: 5, startAngle: 0, endAngle: 2 * .pi, clockwise: true)
        
            let layer = CAShapeLayer()
            layer.path = path.cgPath
            layer.fillColor = UIColor.black.cgColor
            layer.fillMode = .forwards
        
            self.view.layer.addSublayer(layer)
        }
        ```

        해당 코드는 Arc가 제대로 그려지는지 확인하기 위한 코드로 실제 사용 시 필요하지는 않습니다.

    - 실행 결과

        세 개의 점이 정상적으로 만들어진 것을 확인할 수 있습니다.

        ![UIBezierPathSimpleArc3.png](/assets/images/posts/2020-03-06/UIBezierPathSimpleArc3.png)

- **Arc의 반지름(Radius) 구하기**

    이제 세 개의 Point를 만들었으니, Arc의 반지름을 구할 차례입니다. 반지름은 Center Point와 Start Point의 거리를 계산하여 구해줍니다. 

    - 반지름을 구하는 공식

        ![UIBezierPathSimpleArc4.png](/assets/images/posts/2020-03-06/UIBezierPathSimpleArc4.png)

    - 반지름 생성 메서드

        위의 공식을 코드로 옮겨 오면 다음과 같이 작성할 수 있습니다. 여기서 sqrt()는 제곱근을 구하는 함수 입니다.

        ```swift
        func getRadius(center: CGPoint, start: CGPoint) -> CGFloat {
            let xDist: CGFloat = start.x - center.x
            let yDist: CGFloat = start.y - center.y
        
            let radius: CGFloat = sqrt((xDist * xDist) + (yDist * yDist))
        
            return radius
        }
        ```

    - 결과 값

        위의 세 개의 Point로 반지름을 구하면 다음과 같은 결과가 나오게 됩니다.

        ```swift
        xDist = 100.0
        yDist = 50.0
        radius = 111.80339887498948
        ```

- **Arc의 Start/End Angle 구하기**

    반지름도 구했으니 이제 Start/End Angle을 구할 차례입니다. Start와 End Angle 구하는 공식은 동일합니다.

    Angle을 구할 때 사용하는 CGVector와 atan2는 아래 공식 문서를 확인 해보세요.

    > [CGVector](https://developer.apple.com/documentation/coregraphics/cgvector)<br>
    > [atan2(_:_:)](https://developer.apple.com/documentation/coregraphics/1455332-atan2)

    - Angle 구하는 방법
        1. Center Point에서 X를 반지름 만큼 이동한 위치에 Origin Point를 만듭니다. 
        2. Origin Point에서 Center Point의 거리를 구한 Vector(V1)를 만들어 줍니다. 
        3. Start/End Point에서 Center Point의 거리를 구한 Vector(V2)를 만들어 줍니다. 
        4. 이제 atan2를 사용하여 V1과 V2의 angle을 구합니다.
        5. V2 angle에서 V1 angle의 값 만큼을 빼주면 Start/End Angle을 구할 수 있습니다.

    - Angle 생성 메서드

        위에 설명한 방법을 코드로 옮기면 다음과 같습니다.

        ```swift
        func getAngle(center: CGPoint, point: CGPoint, radius: CGFloat) -> CGFloat {
            let origin = CGPoint(x: center.x + radius, y: center.y)
        
            let v1 = CGVector(dx: origin.x - center.x, dy: origin.y - center.y)
            let v2 = CGVector(dx: point.x - center.x, dy: point.y - center.y)
        
            let angle = atan2(v2.dy, v2.dx) - atan2(v1.dy, v1.dx)
        
            return angle
        }
        ```

- **Arc 그리기**

    이제 필요한 데이터는 전부 만들어 졌으니 Arc를 그리기만 하면 됩니다.

    - Arc 그리기 메서드

        ```swift
        func drawArc(centerPoint: CGPoint, startPoint: CGPoint, endPoint: CGPoint) {
            let radius = getRadius(center: centerPoint, start: startPoint)
            let start = getAngle(center: centerPoint, point: startPoint, radius: radius)
            let end = getAngle(center: centerPoint, point: endPoint, radius: radius)
        
            let arcPath = UIBezierPath()
            arcPath.move(to: startPoint)
            arcPath.addArc(withCenter: centerPoint, radius: radius, startAngle: start, endAngle: end, clockwise: true)
        
            let arcLayer = CAShapeLayer()
            arcLayer.path = arcPath.cgPath
            arcLayer.lineWidth = 3
            arcLayer.strokeEnd = 1
            arcLayer.strokeColor = UIColor.red.cgColor
            arcLayer.fillColor = UIColor.clear.cgColor
            arcLayer.fillMode = .forwards
        
            view.layer.addSublayer(arcLayer)
        }
        ```

    - 실행 결과

        실행 해보면 정확하게 두 개의 점을 이어주는 Arc가 그려진 것을 확인할 수 있습니다.

        ![UIBezierPathSimpleArc5.png](/assets/images/posts/2020-03-06/UIBezierPathSimpleArc5.png)

### 두 개의 Point와 각도를 이용해 Arc 그리기

---

이번엔 두 개의 Point와 각도를 이용해 Arc를 그리는 방법에 대해 알아보려고 합니다.

![UIBezierPathSimpleArc6.png](/assets/images/posts/2020-03-06/UIBezierPathSimpleArc6.png)

그림에서 보시는 바와 같이 Center Point, Start Point를 지정한 후 Angle 만큼 Arc를 그려 주는 방식입니다.

여기서도 위와 같이 Arc의 반지름(radius) 값은 Center Point와 Start Point 사이의 길이가 됩니다.

- **두 개의 Point 및 Angle 값 만들기**
    - 두 개의 Point 및 Angle 생성

        ```swift
        let centerPoint = view.center
        let startPoint = CGPoint(x: centerPoint.x + 100, y: centerPoint.y + 50)
        let angle: CGFloat = 180
        ```

        - centerPoint는 현재 뷰컨트롤러 있는 뷰의 Center Point로 해주었습니다.
        - startPoint는 centerPoint에서 x로 +100만큼, y로 +50 만큼 이동한 지점입니다.
        - angle은 180도로 설정하였습니다.

- **Arc의 반지름(Radius) 구하기, Arc의 Start Angle 구하기**

    **[세 개의 Point를 이용해서 Arc 그리기]**와 동일합니다.

- **Arc의 End Angle 구하기**

    이제 End Angle 구하는 방법을 알아보려고 합니다. 

    - End Angle 생성 메서드

        End Angle을 구하는건 공식만 알면 쉽습니다. 공식도 간단합니다.

        ```swift
        func getEndAngle(startAngle: CGFloat, angle: CGFloat) -> CGFloat {
            return (angle * (.pi / 180)) + startAngle
        }
        ```

        공식 **(angle * (.pi / 180))** 에서 나오는 Angle 값은 0도를 기준으로 계산 된 Angle 값이여서 startAngle 만큼을 더해주어야 제대로 된 End Angle 값을 얻을 수 있습니다.

- **Arc 그리기**
    - Arc 그리기 메서드

        ```swift
        func drawArc(centerPoint: CGPoint, startPoint: CGPoint, angle: CGFloat) {
            let radius = getRadius(center: centerPoint, start: startPoint)
            let start = getStartAngle(center: centerPoint, start: startPoint, radius: radius)
            let end = getEndAngle(startAngle: start, angle: angle)
        
            let arcPath = UIBezierPath()
            arcPath.move(to: startPoint)
            arcPath.addArc(withCenter: centerPoint, radius: radius, startAngle: start, endAngle: end, clockwise: true)
        
            let arcLayer = CAShapeLayer()
            arcLayer.path = arcPath.cgPath
            arcLayer.lineWidth = 3
            arcLayer.strokeEnd = 1
            arcLayer.strokeColor = UIColor.red.cgColor
            arcLayer.fillColor = UIColor.clear.cgColor
            arcLayer.fillMode = .forwards
        
            view.layer.addSublayer(arcLayer)
        }
        ```

- 실행 결과

    180도 만큼 Arc가 잘 그려진 것을 확인할 수 있습니다.

    ![UIBezierPathSimpleArc7.png](/assets/images/posts/2020-03-06/UIBezierPathSimpleArc7.png)

### 마무리

---

지금까지 좀 더 쉽게 UIBezierPath의 Arc 그리는 법을 알아 보았습니다.

처음 UIBezierPath를 이용해서 작업을 할 때 Arc 때문에 몇 일을 고생한 기억이 있어 자료를 찾아서 만들어 보게 되었습니다.

Arc 때문에 고생하고 계신 분들에게 조금이나마 도움이 되었으면 합니다.

그럼 달콤한 코딩 되세요!

### 예제 프로젝트

---

[swieeft/SimpleUIBezierPathArc](https://github.com/swieeft/SimpleUIBezierPathArc)