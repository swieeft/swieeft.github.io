---
layout: post
title: "디자인 가이드와 내 앱의 컬러가 달라요😟"
subtitle: "[Tips]"
date: 2020-03-17 15:35
background: 
tags: [tips, ios, xcode]
---

안녕하세요. 오랜만에 글을 업데이트 하는 것 같습니다.

앱을 개발하다보면 디자이너 분이 주신 디자인 가이드의 색상과 내 앱의 색상이 다르게 보일 때가 있습니다. 분명히 똑같은 RGB 값을 입력해 주었는데도 말이죠.

아래 이미지는 **R 200, G 50, B 100**으로 동일한 값의 배경색을 가진 뷰입니다. 하지만 이미지에서는 왼쪽 뷰의 색상이 더 어둡게 보이고 있습니다.

![ColorProfile1.png](/assets/images/posts/2020-03-17/ColorProfile1.png)

왜 동일한 값인데 색상의 차이가 발생하는 것일까요? 그 이유는 선택된 Color Profile 때문에 그렇습니다.

### sRGB와 Adobe RGB

---

Color Profile에는 여러가지 종류가 있지만 대표적으로 sRGB와 Adobe RGB를 사용합니다. 이 두가지는 RGB 색 공간의 표준인데, 색을 표현할 수 있는 범위가 다릅니다.

아래 이미지를 보시면 sRGB와 Adobe RGB의 색상 표현 범위가 다른 것을 볼 수 있습니다.

![ColorProfile2.png](/assets/images/posts/2020-03-17/ColorProfile2.png)

- **sRGB란**

    국제전기표준회의(IEC)가 지정한 RGB 색 공간 표준입니다.

    sRGB는 디스플레이, 프린터, 디지털 카메라 등의 일반 소프트웨어와 하드웨어가 채택한 국제 표준입니다.

    sRGB 호환 장치로 입출력할 경우, 서로 다른 장치 사이에도 색 차이를 최소화할 수 있어서 원하는 색상이 재현됩니다. 그러나 표현할 수 있는 색상 범위가 다소 제한적 입니다.

- **Adobe RGB란**

    Adobe Systems가 제안한 표준입니다.

    sRGB보다 재현 영역이 넓어 더욱 섬세하게 색상을 표현할 수 있습니다. 따라서 인쇄 산업 등의 분야에 많이 사용 됩니다.

    Adobe RGB 색상을 이미지로 올바르게 출력하기 위해서는 디스플레이, 프린터 등의 호환 하드웨어와 호환 소프트웨어가 필요합니다.

### Xcode에서 Color Profile 변경하기

---

위에서 Color Profile의 대표적인 두가지를 알아보았습니다. 개발을 하면서 디자인 가이드 보다 색상이 밝다면 sRGB인데 Adobe RGB로 사용하고 있을 가능성이 높습니다. 반대일 경우도 있겠죠.

그럼 디자인 가이드에 맞춰서 Color Profile을 변경해주는 방법을 알아보도록 하겠습니다.

- **컬러 팔레트 열기**

    컬러 팔레트를 열은 후 빨간 박스에 있는 톱니바퀴 아이콘을 선택합니다.

    ![ColorProfile3.png](/assets/images/posts/2020-03-17/ColorProfile3.png)

- **컬러 프로필 선택하기**

    톱니바퀴 아이콘을 누르면 이미지 처럼 컬러 프로필이 나옵니다. 여기서 원하는 프로필을 선택하시면 됩니다.

    ![ColorProfile4.png](/assets/images/posts/2020-03-17/ColorProfile4.png)

### 코드로 컬러 설정 시 Color Profile

---

코드로 동일한 컬러 값을 설정하면 어떤 Color Profile로 나타날지 확인을 해보았습니다.

![ColorProfile5.png](/assets/images/posts/2020-03-17/ColorProfile5.png)

이미지에서 보시는 것 처럼 sRGB Color Profile과 동일한 색상이 나타나는 것을 확인 할 수 있습니다.

그러므로 스토리보드에서 Adobe RGB를 사용하고 코드로 색상을 적용한다면 동일한 색상도 달라지게 될 수 있습니다.

### 마무리

---

지금까지 Color Profile에 대해 알아보았습니다. 저도 앱 개발하면서 자꾸 색상이 이상하다는 피드백을 받으면서 원인을 알지 못해 고생했던 적이 있었습니다.

만약 디자인 가이드와 개발하는 앱의 색상이 다를 경우 한번 씩 확인해보시면 금방 해결할 수 있을 것 같습니다.

참고로 Xcode에서 뷰의 Color Profile을 바꿔도 다른 뷰나 컨트롤들의 Color Profile은 그대로여서 노가다 작업을 해야 되는 경우가 있으니 처음 개발을 시작할 때부터 맞추고 시작하는 것이 나중에 노가다 작업을 줄일 수 있습니다.

그럼 달콤한 코딩 되세요!

### 참고자료

---

[sRGB와 Adobe RGB의 차이는 무엇입니까?](https://www.sony.co.kr/electronics/support/articles/00031635)