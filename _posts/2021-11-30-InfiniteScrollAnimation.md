---
layout: post
title: "무한 스크롤 애니메이션 구현하기 (Infinite Scroll Animation)"
subtitle: "[iOS, Swift]"
date: 2021-11-30 14:00
background: 
tags: [ios, swift]
---

![InfiniteScrollAnimation1.gif](/assets/images/posts/2021-11-30/InfiniteScrollAnimation1.gif)

오늘은 위에 보시는 것 처럼 하늘 이미지가 계속 스크롤? 되는 것처럼 보이게 하는 애니메이션 구현 방법을 알아보려고 합니다.

많이 쓰이는 애니메이션은 아니지만 최근에 회사 프로젝트를 진행하면서 카드 모양의 긴 이미지를 계속해서 흘러가도록 구현 해야 되는 요구사항이 있어서 찾아보다가 정리를 해놓으면 좋겠다고 생각 되서 이렇게 글을 작성하게 되었습니다.

생각보다 원리만 알면 구현하는건 어렵지 않으니 하나하나 따라오시면 금방 이해 하실 수 있습니다.

<br>

### 이미지 만들기

---

이 애니메이션을 구현할 때 핵심은 이미지입니다.

아래에서 자세히 설명을 드릴테지만 간단하게 구현 방법에 대해 설명하면 2개의 동일한 이미지를 이어 붙여서 위치를 조정해주는 것이기 때문에 

이미지가 이어지는 부분이 자연스럽게 연결되어 있는 이미지를 써야지 계속해서 이미지가 스크롤 되는 것처럼 구현할 수 있습니다.

![InfiniteScrollAnimation2.png](/assets/images/posts/2021-11-30/InfiniteScrollAnimation2.png)

위의 이미지를 보시면 좌우 간격을 동일하게 만들어 주어, 이미지 2개를 붙였을때 그림 간의 여백 등이 자연스럽게 이어지도록 되어 있습니다.

이렇게 이미지를 자연스럽게 만들어 주어야 애니메이션을 제대로 구현할 수 있는데요.

위의 이미지를 애니메이션으로 구현하면 다음과 같이 동작하는 것을 볼 수 있습니다.

![InfiniteScrollAnimation3.gif](/assets/images/posts/2021-11-30/InfiniteScrollAnimation3.gif)

<br>

### 이미지 뷰 만들기

--- 

이제 본격적으로 애니메이션을 구현 해보겠습니다. 

그냥 위의 네모 이미지로 만들어도 되지만 그래도 그럴싸하게 보여주고 싶어서 저는 직접 아이패드(아이패드 산거 자랑 중)로 하늘 이미지를 그려주었습니다.

>> 샘플 이미지 및 샘플 프로젝트는 아래에 예제 프로젝트 링크로 들어가시면 다운로드 받으실 수 있습니다.

- **샘플 이미지**

    ![InfiniteScrollAnimation4.png](/assets/images/posts/2021-11-30/InfiniteScrollAnimation4.png)

- **UI 예제 코드**

    >> 이번 프로젝트에서는 UI가 간단하기도 하고 이미지 뷰의 경우 코드로 넣어주는게 좋아서, 직접 코드로 작성하였습니다.

    <p> {% gist swieeft/c464cfb70b541134d148dfdd5f84c5fd InfiniteScrollAnimation1.swift %} </p>

    <p> {% gist swieeft/c464cfb70b541134d148dfdd5f84c5fd InfiniteScrollAnimation2.swift %} </p>

    <p> {% gist swieeft/c464cfb70b541134d148dfdd5f84c5fd InfiniteScrollAnimation3.swift %} </p>

- **실행 결과**

    위의 예제 코드만 넣으면 가만히 멈춰 있는 하늘 이미지를 확인 할 수 있습니다.

<br>

### 애니메이션 구현하기

---

이제 본격적으로 애니메이션을 구현해보려고 합니다. 

애니메이션 구현 방법은 2가지 방법이 있는데요. UIView.animate를 이용한 방법과 Core Animation을 이용한 방법이 있습니다.

각각의 장단점이 있으니 만들어 보시고 앱에 맞는 방법으로 구현 해보시면 될 것 같습니다.

- **UIView.animate를 이용한 구현**

    <p> {% gist swieeft/c464cfb70b541134d148dfdd5f84c5fd InfiniteScrollAnimation4.swift %} </p>

    frame offsetBy를 이용해 x 좌표를 이동하는 방식으로 개발 된 애니메이션입니다. 

    옵션으로 .repect를 주어서 애니메이션이 계속 반복 되도록 하였습니다.

- **Core Animation을 이용한 구현**

    <p> {% gist swieeft/c464cfb70b541134d148dfdd5f84c5fd InfiniteScrollAnimation5.swift %} </p>

    CABasicAnimation을 이용해서 구현 했으며, keyPath "position.x"는 x 좌표의 위치를 변경하는 애니메이션을 뜻합니다.

    byValue로 이미지 뷰를 이동할 만큼의 x 좌표값을 입력 해준 후 해당 이미지 뷰 레이어에 애니메이션을 추가해주면 구현이 완료 됩니다.

- **UIView.animate 대신 Core Animation을 선택한 이유**

    원래는 UIView.animate를 이용해서 개발을 먼저 했었는데, 앱이 Background로 내려 갔다가 다시 Foreground로 다시 올라 올때 애니메이션이 멈추는 현상이 있었습니다.

    그래서 다시 애니메이션을 재실행하고 하면 제대로 동작이 되서 괜찮은 줄 알았는데, 제 프로젝트가 이상한건지 다른 버그가 있는건지 Background로 몇번 더 왔다 갔다 하다보면 어느 순간 애니메이션을 실행 중인 뷰가 사라지는 현상이 있었습니다.

    메모리 문제인지 뭔지 원인을 파악 해보려고 해도 찾을 수가 없어서 Core Animation을 이용해서 해보면 어떨까하고 작업을 하게 되었습니다.

    Core Animation도 Background로 내려가면 애니메이션이 멈추기는 하지만 여러 번 왔다갔다 해도 문제 없이 애니메이션을 재실행 할 수 있어 최종적으로 Core Animation을 채택하게 되었습니다.

<br>

### 애니메이션 원리

---

지금까지 무한 스크롤 애니메이션을 구현하는 방법에 대해서 알아보았습니다. 

여기까지 보셨으면 눈치 채신 분들도 계실테지만 대체 이게 왜 이렇게 되는거지? 라고 생각 하시는 분들도 계실까봐 간단하게 원리를 설명하려고 합니다.

애니메이션 순서대로 설명을 드리면

1. imageView1, imageView2를 각각의 위치에 둔다.

2. imageView1, imageView2의 넓이 값 만큼 x 좌표를 이동시켜 준다.

3. imageView1, imageView2의 넓이 값 만큼 x 좌표가 이동이 되었다면 애니메이션을 종료한다.

4. 애니메이션이 종료 되면 자동으로 imageView1, imageView2의 위치는 초기 위치로 돌아간다.

5. 1번부터 계속 반복한다.

아래의 gif 이미지는 애니메이션 원리를 보여주고 있습니다.

![InfiniteScrollAnimation5.gif](/assets/images/posts/2021-11-30/InfiniteScrollAnimation5.gif)

<br>

### 마무리

---

지금까지 무한 스크롤 애니메이션 구현하는 방법에 대해 알아보았습니다.

어떤가요? 처음 원리를 몰랐을 때는 어떻게 구현해야 되는지 막막 했는데 막상 구현하고 보니 단순한 원리를 이용한 애니메이션이지 않았나요?

저도 처음 해당 기능을 만들어 달라고 했을땐 어려웠는데 원리를 알고보니 오히려 다양한 곳에 활용할 수 있을 것 같은 유용한 애니메이션이었습니다.

애니메이션을 구현하다보면 항상 느끼는거지만 보여지는 그대로를 생각할 것이 아니라 사용자의 눈속임을 통한 구현 방법을 연구해야지 원하는 결과물이 나오는 것 같습니다.

저는 이 방법을 이용해서 이미지가 한장 한장 넘어가는 애니메이션도 구현을 했습니다.

원래는 스크롤 뷰를 이용해서 전체 이미지를 스크롤 뷰에 넣어 놓고 작업을 했었는데, 이 방법을 이용해서 약간의 트릭을 더해 2개의 이미지 뷰 많을 이용해서 구현 할 수 있었습니다.

여러분도 해당 기능만을 생각하지 마시고, 이 원리를 이용해서 다양한 곳에 활용 방법을 찾아보시면 좋을 것 같습니다.

그럼 달콤한 코딩 되세요!

<br>

### 예제 프로젝트

---

[swieeft/InfiniteRollingAnimation](https://github.com/swieeft/InfiniteRollingAnimation)

<br>

### 참고자료

--- 
[Creating infinite background scroll right to left](https://stackoverflow.com/a/30423963)

