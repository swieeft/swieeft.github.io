---
layout: post
title: "커스텀 스위치(Custom Switch) 만들기"
subtitle: "[iOS]"
date: 2020-02-23 21:20
background: 
tags: [ios, swift]
---

안녕하세요. 오늘은 커스텀 스위치(Custom Switch)를 만들어 보려고 합니다. 애플에서는 이미 기본적으로 [UISwitch](https://developer.apple.com/documentation/uikit/uiswitch)라는 기본 컨트롤을 제공하지만 디자인 요구사항에 따라 커스텀을 해야 될 때 기본 UISwitch는 디자인 적인 요소에 많은 한계가 존재합니다. 

그래서 가장 좋은 것은 디자이너한테 기본 UISwitch 디자인으로 작업을 해달라고 요청하는 것이 좋지만 또 일이라는게 내 맘대로 되지 않다보니 결국 커스텀 스위치를 만들어야 합니다.

하지만 어떻게 만들어야 할지 막막하신 분들을 위해 간단한 커스텀 스위치 만드는 법을 포스팅합니다.

### 예제 프로젝트 동작 설명

---

스위치를 누르면 스위치 상태가 On/Off로 변하고, 현재 상태를 Label에 표시합니다. 또한 setOn 메서드와 isOn 프로퍼티를 변경 했을 때 스위치의 상태가 변하는 동작을 포함하고 있습니다.
  
  ![swieeftSwitch.gif](https://raw.githubusercontent.com/swieeft/SwieeftSwitch/master/Resource/swieeftSwitch.gif)

### 스위치 Custom Class 만들기

---

- **클래스에 UIButton 클래스를 상속 받기**

  <p>{% gist swieeft/a7525bef6e2d016fed1bd5fa7dd5771f CustomSwitch1.swift %}</p>

- **버튼에 들어갈 커스텀 뷰 초기화 하기**
  
  - **프로퍼티**

    <p>{% gist swieeft/a7525bef6e2d016fed1bd5fa7dd5771f CustomSwitch2.swift %}</p>

  - **메서드**

    <p>{% gist swieeft/a7525bef6e2d016fed1bd5fa7dd5771f CustomSwitch3.swift %}</p>

    > barView는 스위치의 뒤쪽 기다란 타원 모양의 뷰입니다. circleView는 스위치의 동그란 모양의 뷰이며, On/Off 시에 위치를 이동합니다.

    > barViewTopBottomMargin은 barView의 상하단 여백을 지정해주는 값입니다. 0을 지정하면 circleView와 높이 값이 같게 설정됩니다.

- **스위치 색상 설정하기**

  <p> {% gist swieeft/a7525bef6e2d016fed1bd5fa7dd5771f CustomSwitch4.swift %} </p>

  > On 상태의 색상을 설정하는 onColor과, Off 상태의 색상을 설정하는 offColor가 있습니다. 색상을 받는 데이터 타입은 Tuple 형태로 되어 있고 SwitchColor라는 type으로 명명되어 있습니다. 이 값은 외부에서도 설정할 수 있습니다.

  > bar는 barView의 색상을 지정해주며, circle은 circleView 색상을 지정해주게 됩니다.

- **커스텀 스위치 터치 이벤트 받기**

  - **프로퍼티**
  
    <p> {% gist swieeft/a7525bef6e2d016fed1bd5fa7dd5771f CustomSwitch5.swift %} </p>

  - **메서드**

    <p> {% gist swieeft/a7525bef6e2d016fed1bd5fa7dd5771f CustomSwitch6.swift %} </p>

    > 사용자가 스위치를 터치하면 setOn 메서드를 호출합니다. 그럼 setOn 메서드에서 isOn의 값을 변경시켜 줍니다.
      isOn이 변경되면 changeState 메서드를 통해 뷰의 상태를 업데이트하게 됩니다.

- **스위치 뷰 상태 업데이트하기**
    
  - **프로퍼티**

    <p> {% gist swieeft/a7525bef6e2d016fed1bd5fa7dd5771f CustomSwitch7.swift %} </p>

  - **메서드**

    <p> {% gist swieeft/a7525bef6e2d016fed1bd5fa7dd5771f CustomSwitch8.swift %} </p>

    > animationDuration 프로퍼티는 스위치가 이동하는 애니메이션을 실행하는 시간입니다. 외부에서도 변경 가능합니다.

### 스위치 상태 변경에 대한 Delegate 만들기

---

스위치 상태가 변경되면 호출되는 Delegate입니다. Delegate를 통해 사용자가 스위치 상태를 변경하면 체크할 수 있도록 해줍니다.

- **프로토콜 만들기**

  <p> {% gist swieeft/a7525bef6e2d016fed1bd5fa7dd5771f CustomSwitch9.swift %} </p>

- **Delegate 호출**

  <p> {% gist swieeft/a7525bef6e2d016fed1bd5fa7dd5771f CustomSwitch10.swift %} </p>

### ViewController에 커스텀 스위치 사용하기

---

- **커스텀 스위치 클래스 연결하기**

  ViewController에 추가 한 Button을 클릭한 후 Custom Class에 가서 커스텀 스위치 클래스를 입력합니다.

  ![customSwitch.png](/assets/images/posts/2020-02-23/customSwitch.png)

- **연결된 커스텀 스위치 ViewController 클래스에서 사용하기**

  <p> {% gist swieeft/a7525bef6e2d016fed1bd5fa7dd5771f CustomSwitch11.swift %} </p>

  > 스위치에 delegate를 설정해주어 SwieeftSwitchButtonDelegate의 isOnValueChange 메소드가 호출되어 상태값을 받을 수 있도록 해줍니다.

### 예제 프로젝트 링크

---

[https://github.com/swieeft/SwieeftSwitch](https://github.com/swieeft/SwieeftSwitch)

### 마무리

---

커스텀 스위치 만드는 법을 알아보았습니다. 생각보다 간단할 수도, 복잡할 수도 있지만 그래도 몇번 커스텀 뷰를 만들다 보면 자신만의 노하우 같은게 생길 것 같습니다.

커스텀 뷰 만드는 법이 익숙해지면 내가 개발한 앱이 다른 앱과는 다른 차별성을 둘 수 있어서 많이 선호들 하지만 개발자에겐 노가다가 필요한 작업이어서 고통이 따릅니다.

하지만 하나하나 만들어 나가다 보면 뷰에 대한 이해도 높아지고 자신만의 강점을 하나 더 만들 수 있는 부분이라 생각하지 때문에 커스텀 뷰 개발은 꾸준히 연습하고 여러가지 다른 앱들의 커스텀 뷰를 따라 만들어 보면서 자신의 강점으로 성장시키면 좋을 것 같습니다.
