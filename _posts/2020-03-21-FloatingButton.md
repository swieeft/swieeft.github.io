---
title: "[iOS] 간단한 플로팅 버튼(Floating Button) 만들기"
layout: post
date: 2020-03-21 23:20
tag:
    - iOS
    - Swift
headerImage: false
image:
description: 간단한 플로팅 버튼(Floating Button) 만들기
category: blog
author: swieeft
externalLink: true
published: true
comments: true
share: true
use_math: false
---
안녕하세요. 오늘은 간단한 플로팅 버튼을 만들어 보려고 합니다. 

플로팅 버튼에 관한 라이브러리도 많이 있지만 라이브러리를 사용하지 않고 심플하고 빠르게 개발하는 방법을 소개 하려고 합니다.

### 예제 프로젝트 실행 화면

---

![example.gif](https://raw.githubusercontent.com/swieeft/SampleFloatingButton/master/Resource/example.gif)

### 스토리보드 작업

---

우리가 만들 플로팅 버튼은 스택 뷰를 이용해 구현합니다. 스택뷰를 사용하는 이유는 대부분의 플로팅 버튼 특징상 메뉴를 Show / Hide 시킬 때 메뉴가 쭉 나타났다가 쭉 사라지도록 구현이 되기 때문입니다.

- **메뉴 버튼 만들기**

    처음 해야 될 작업은 각각의 메뉴 버튼을 만들어 주는 작업입니다. 예제는 아침, 점심, 저녁을 선택할 수 있도록 버튼을 만들어 주었고, 메뉴 Show / Hide 기능을 수행할 + 버튼도 만들어 주었습니다.

    ![FloatingButton1.png](/assets/images/posts/2020-03-21/FloatingButton1.png)

- **버튼 스택 뷰로 감싸기**

    이제 만들어진 4개의 버튼을 모두 선택한 후 스택뷰로 감싸 주는 작업을 하면 됩니다.

    1. 버튼 모두 선택

        ![FloatingButton2.png](/assets/images/posts/2020-03-21/FloatingButton2.png)

    2. 스택뷰 만들기

        스토리보드 화면 오른쪽 하단에 아래 이미지 메뉴를 선택하면 선택된 4개의 버튼이 스택뷰로 감싸지게 됩니다.

        ![FloatingButton3.png](/assets/images/posts/2020-03-21/FloatingButton3.png)

    3. 스택뷰 위치 지정하기

        만들어진 스택뷰의 위치를 오토레이아웃으로 지정해줍니다. 저는 오른쪽 하단으로 버튼 위치를 지정해주었습니다.

        ![FloatingButton4.png](/assets/images/posts/2020-03-21/FloatingButton4.png)

- **메뉴 버튼 Hidden 상태로 변경**

    이제 플로팅 버튼의 초기 상태를 만들기 위해 아침, 점심, 저녁 메뉴 버튼은 Hidden 상태로 변경해줍니다.

    ![FloatingButton5.png](/assets/images/posts/2020-03-21/FloatingButton5.png)

- **최종 스토리보드 화면**

    아래 이미지는 플로팅 버튼을 만들기 위한 작업이 완료 된 화면입니다.

    근데 여기서 신기한 점은 일반적으로 컨트롤을 Hidden 시켰을 때와 다르게 버튼들이 사라져 있는 것을 확인 할 수 있습니다.

    바로 이게 스택뷰를 사용하는 이유인데요. 스택뷰의 특징 중 하나가 스택뷰 안에 있는 컨트롤을 Hidden 시키면 그 자리에서 컨트롤이 숨겨지는게 아니라 그 영역 만큼이 줄어들게 되어 있습니다.

    마치 스택에 데이터를 push 하면 스택이 늘어나고, pop 하면 스택이 줄어드는 것 같은거죠. 

    그래서 우리가 원하는 애니메이션을 구현하기 위해 스택뷰를 사용하는 것입니다.

    ![FloatingButton6.png](/assets/images/posts/2020-03-21/FloatingButton6.png)

### 코드 작업

---

스토리보드 작업이 완료 되었으니 이제 코드 작업을 해보려고 합니다. 코드 작업의 핵심은 애니메이션입니다.

플로팅 버튼을 누르면 쭈르륵 메뉴 버튼이 올라왔다가, 다시 누르면 쭈르륵 내려가도록 보여주기 위해서는 애니메이션을 적용 해줘야 합니다.

- **스택뷰, 버튼 IBOutlet 연결**

    ```swift
    @IBOutlet weak var floatingStackView: UIStackView!
    @IBOutlet weak var floatingButton: UIButton!
    @IBOutlet weak var morningButton: UIButton!
    @IBOutlet weak var afternoonButton: UIButton!
    @IBOutlet weak var eveningButton: UIButton!
    ```

- **메뉴버튼 배열 만들기**

    ```swift
    lazy var buttons: [UIButton] = [self.morningButton, self.afternoonButton, self.eveningButton]
    ```

- **플로팅 버튼 상태에 대한 Flag**

    ```swift
    var isShowFloating: Bool = false
    ```

    > 상태 Flag는 따로 만들지 않고 Button의 isSelected나 다른 방법으로 사용하셔도 됩니다. 여기서는 이해하기 쉽도록 따로 상태 Flag를 만들어 주었습니다.

- **플로팅 버튼 Show / Hide 애니메이션**

    플로팅 버튼 Show / Hide에 대한 애니메이션 코드입니다. 

    - Show 애니메이션

        메뉴버튼 배열을 순차적으로 돌면서 제일 아래에 있는 메뉴버튼 부터 차례대로 Hidden을 false로 바꿔준 후 alpha 애니메이션을 통해 이미지가 자연스럽게 나오도록 개발 하였습니다.

        ```swift
        buttons.forEach { [weak self] button in
            button.isHidden = false
            button.alpha = 0
        
            UIView.animate(withDuration: 0.3) {
                button.alpha = 1
                self?.view.layoutIfNeeded()
            }
        }
        ```

    - Hide 애니메이션

        Show 애니메이션과 반대로 맨 위에 있는 메뉴부터 차례대로 Hidden을 true로 바꾸어 주고 있습니다.

        ```swift
        buttons.reversed().forEach { button in
            UIView.animate(withDuration: 0.3) {
                button.isHidden = true
                self.view.layoutIfNeeded()
            }
        }
        ```

- **플로팅 버튼 Show 상태에서 배경 Dim 처리 방법**

    Show 상태가 되면 배경이 어둡게 처리 되도록 하는 코드입니다.

    - floatingDimView 생성

        어둡게 처리 되도록 하기 위해 View를 하나 만들어 줍니다. 

        ```swift
        lazy var floatingDimView: UIView = {
            let view = UIView(frame: self.view.frame)
            view.backgroundColor = UIColor(red: 0, green: 0, blue: 0, alpha: 0.5)
            view.alpha = 0
            view.isHidden = true
            
            self.view.insertSubview(view, belowSubview: self.floatingStackView)
            
            return view
        }()
        ```

        > 플로팅 버튼을 사용하지 않으면 생성 될 필요가 없으므로 lazy를 이용해 호출이 되면 초기화 하도록 합니다.

    - Show / Hide 애니메이션

        ```swift
        /** DimView Show 애니메이션 **/
        UIView.animate(withDuration: 0.5, animations: {
            self.floatingDimView.alpha = 0
        }) { (_) in
            self.floatingDimView.isHidden = true
        }
        
        /** DimView Hide 애니메이션 **/
        self.floatingDimView.isHidden = false
        
        UIView.animate(withDuration: 0.5) {
            self.floatingDimView.alpha = 1
        }
        ```

- **상태 Flag값 변경**

    ```swift
    isShowFloating = !isShowFloating
    ```

    > Flag 값은 이전 상태의 반대로만 바꿔 주시면 됩니다.

- **플로팅 상태에 따른 버튼 이미지 변경**

    메뉴가 Show 되었을 때와, Hide 되었을 때의 버튼 이미지를 변경해주는 코드입니다.

    ```swift
    let image = isShowFloating ? UIImage(named: "Hide") : UIImage(named: "Show")
    UIView.animate(withDuration: 0.3) {
        sender.setImage(image, for: .normal)
    }
    ```

- **(선택) 버튼 아이콘 회전 애니메이션**

    버튼 이미지가 바뀔 때 회전 하는 애니메이션은 다음과 같이 구현하시면 됩니다.

    ```swift
    let roatation = isShowFloating ? CGAffineTransform(rotationAngle: .pi - (.pi / 4)) : CGAffineTransform.identity
    UIView.animate(withDuration: 0.3) {
        sender.transform = roatation
    }
    ```

- **전체 코드**

    ```swift
    class ViewController: UIViewController {
    
        @IBOutlet weak var floatingStackView: UIStackView!
        @IBOutlet weak var floatingButton: UIButton!
        @IBOutlet weak var morningButton: UIButton!
        @IBOutlet weak var afternoonButton: UIButton!
        @IBOutlet weak var eveningButton: UIButton!
        
        lazy var floatingDimView: UIView = {
            let view = UIView(frame: self.view.frame)
            view.backgroundColor = UIColor(red: 0, green: 0, blue: 0, alpha: 0.5)
            view.alpha = 0
            view.isHidden = true
            
            self.view.insertSubview(view, belowSubview: self.floatingStackView)
            
            return view
        }()
        
        var isShowFloating: Bool = false
        
        lazy var buttons: [UIButton] = [self.morningButton, self.afternoonButton, self.eveningButton]
        
        override func viewDidLoad() {
            super.viewDidLoad()
        }
        
        @IBAction func floatingButtonAction(_ sender: UIButton) {
            
            if isShowFloating {
                buttons.reversed().forEach { button in
                    UIView.animate(withDuration: 0.3) {
                        button.isHidden = true
                        self.view.layoutIfNeeded()
                    }
                }
                
                UIView.animate(withDuration: 0.5, animations: {
                    self.floatingDimView.alpha = 0
                }) { (_) in
                    self.floatingDimView.isHidden = true
                }
            } else {
                
                self.floatingDimView.isHidden = false
                
                UIView.animate(withDuration: 0.5) {
                    self.floatingDimView.alpha = 1
                }
                
                buttons.forEach { [weak self] button in
                    button.isHidden = false
                    button.alpha = 0
    
                    UIView.animate(withDuration: 0.3) {
                        button.alpha = 1
                        self?.view.layoutIfNeeded()
                    }
                }
            }
            
            isShowFloating = !isShowFloating
            
            let image = isShowFloating ? UIImage(named: "Hide") : UIImage(named: "Show")
            let roatation = isShowFloating ? CGAffineTransform(rotationAngle: .pi - (.pi / 4)) : CGAffineTransform.identity
            
            UIView.animate(withDuration: 0.3) {
                sender.setImage(image, for: .normal)
                sender.transform = roatation
            }
            
        }
    }
    ```

### 개발 시 주의사항

---

스택뷰를 이용해서 작업 할 때 버튼의 크기를 지정해주지 않으면 Hidden 시 Frame이 0으로 바뀌어 버립니다. 그렇게 되면 예상하지 못했던 방식으로 동작을 하게 됩니다.

예제 프로젝트에서는 Width 100을 주고, 1:1 비율로 버튼을 만들어 주어 버튼 모양 그대로 올라오는 느낌의 애니메이션을 구현할 수 있었는데요. 다른 식으로 값을 주면 어떻게 되는지 확인 해보도록 하겠습니다.

![FloatingButton7.gif](/assets/images/posts/2020-03-21/FloatingButton7.gif)

위의 예시는 Width 100만 준 결과입니다. 뭔가 이상하지 않나요? 메뉴가 차곡차곡 쌓이고 없어지고 하는 느낌보단 메뉴가 늘어나고 줄어주는 느낌이 강합니다. 

이렇게 오토레이아웃 제약 조건을 수정하는 것만으로도 애니메이션 결과가 달라 질 수 있으니 개발 시 주의하셔서 작업 하셔야 합니다.

### 예제 프로젝트 링크

---

[swieeft/SampleFloatingButton](https://github.com/swieeft/SampleFloatingButton)

### 마무리

---

지금까지 간단하게 플로팅 버튼 구현하는 방법을 알아보았습니다.

예제 프로젝트는 간단하게 한곳에서 전부 구현을 하였지만 좀 더 응용해서 범용적으로 재사용할 수 있도록 모듈화 시켜서 사용해도 좋을 것 같습니다.

그럼 달콤한 코딩 되세요!