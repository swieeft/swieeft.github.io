---
layout: post
title: "제플린(Zeplin)에서 Assets Export시 바로 Xcode 프로젝트에 적용하기"
subtitle: "[Tips]"
date: 2020-08-13 15:15
background: 
tags: [tips]
---

안녕하세요. 오늘은 간단한 팁을 하나 가지고 왔습니다.

디자인 가이드를 받으실 때 많은 분들이 제플린을 사용하실텐데요. 제플린에서 이미지를 다운 받아 프로젝트에 추가하실때 다들 어떻게 하시나요?

저 같은 경우엔 다운 받은 후에 직접 프로젝트 에셋에 추가하는 방법을 하였는데요.

최근에 알게된 사실로 인해 그 동안 쓸데 없는 작업을 하고 있었다는걸 깨닫게 되었습니다..... 아직도 충격적이네요...

그래서 혹시나 저 처럼 아직도 불필요한 작업을 하고 계시는 분들이 있을까봐 팁을 공유하려고 합니다.

### 제플린에서 바로 Xcode로 적용하기

---

제플린에서 바로 Xcode로 적용하는건 복잡한 설정도 필요하지 않습니다.

사실 Export할 때 제플린에 나온 메시지만 제대로 봤어도 금방 알아차릴 수 있는 팁입니다.

![ZeplinAssetsExportProject1.png](/assets/images/posts/2020-08-28/ZeplinAssetsExportProject1.png)

빨간색 박스 안에 메시지를 보시면 아래와 같은 문장이 있습니다.

> "Export the assets to your .xcodeproj or .xcassets directory, Zeplin will automatically add them to the asset catelog!"

아래와 같은 의미로 번역할 수 있습니다.

> "에셋을 .xcodeproj 또는 .xcassets 디렉토리로 내보내면 Zeplin이 에셋 카탈로그에 자동으로 추가합니다!"

결국 .xcodeproj 또는 .xcassets 디렉토리로 경로를 지정하고 이미지를 다운로드 하면 자동으로 Xcode 에셋에 맞는 형태로 이미지를 저장 시켜준다는 것을 의미합니다.

그럼 진짜로 자동으로 에셋 형태로 저장이 되는지 확인해보겠습니다.

### 디렉토리 지정하기

---

아래 이미지를 다운 받아 보는걸로 테스트 하겠습니다.

![ZeplinAssetsExportProject2.png](/assets/images/posts/2020-08-28/ZeplinAssetsExportProject2.png)

우선 이미지 Export 버튼을 클릭합니다.

![ZeplinAssetsExportProject2-1.png](/assets/images/posts/2020-08-28/ZeplinAssetsExportProject2-1.png)

그러면 디렉토리를 지정하는 화면이 나올텐데요. 여기서 .xcodeproj 또는 .xcassets 디렉토리를 저장 경로로 지정해줍니다. 이렇게 하면 디렉토리 지정은 끝납니다.

![ZeplinAssetsExportProject3.png](/assets/images/posts/2020-08-28/ZeplinAssetsExportProject3.png)

한번 .xcodeproj 또는 .xcassets를 디렉토리로 지정하면 다음에 Export 시에는 아래와 같은 화면으로 나오게 됩니다. 여러 개의 프로젝트를 지정하셨다면 여러개가 나오게 될겁니다.

![ZeplinAssetsExportProject3-1.png](/assets/images/posts/2020-08-28/ZeplinAssetsExportProject3-1.png)


### .png 파일 Export

---

우선 .png 파일을 Export를 한 후 Xcode에 Assets를 가보면 아래와 같은 상태로 Export가 되어 있는 것을 확인할 수 있습니다.

![ZeplinAssetsExportProject4.png](/assets/images/posts/2020-08-28/ZeplinAssetsExportProject4.png)

![ZeplinAssetsExportProject5.png](/assets/images/posts/2020-08-28/ZeplinAssetsExportProject5.png)

### .pdf 파일 Export

---

그럼 .png 파일 말고 .pdf 파일을 받으면 어떻게 될까요? .pdf 파일은 벡터이미지라서 scales를 Single Scale로 변경해서 저장 해주어야 하는데 확인 해보면 제대로 설정이 변경되서 저장 되는 것을 확인할 수 있습니다.

![ZeplinAssetsExportProject6.png](/assets/images/posts/2020-08-28/ZeplinAssetsExportProject6.png)


### 마무리

---

간단하게 제플린에서 Assets Export시 바로 Xcode 프로젝트에 적용하는 방법을 알아보았습니다.

너무 간단하게 설정해서 편하게 이미지를 프로젝트에 적용할 수 있었습니다.

오늘의 교훈은 툴을 사용할 때 사소한 문장이라도 일단 한번은 보고 사용하자라고 생각합니다.

조금만 시간을 들여서 확인 했더라면 몇배의 시간을 아낄 수 있었는데 그러지 못한게 많이 아쉽네요...

여러분도 조금이라도 불필요한 시간을 낭비하지 않게 되길 바랍니다.

그럼 달콤한 코딩 되세요!