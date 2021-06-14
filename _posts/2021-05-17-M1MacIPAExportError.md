---
layout: post
title: "M1 Mac에서 IPA 내보내기 에러 해결방법"
subtitle: "[iOS, Swift]"
date: 2021-05-17 15:00
background: 
tags: [ios, swift]
---

최근에 M1 Mac mini를 구입하여 회사에서 업무용으로 사용하고 있습니다. 아직 코코아팟 이슈나 몇몇 문제점들이 있기는 하지만 업무에 큰 지장은 없고 빌드 속도는 문제점들을 상쇄하기에 충분한 것 같네요.

이번에 포스팅할 내용은 M1 Mac으로 작업하면서 발생 했던 이슈 중에 IPA 내보내기 할 때 발생하는 에러에 대해서 해결방법을 포스팅하려고 합니다.

쉽게 해결할 수 있어서 간단한 포스팅이 될 것 같네요.

---

IPA는 테스트 버전 배포를 위해 위해 url 링크를 제공하거나, Firebase의 앱 배포를 이용하거나 할 때 사용하게 됩니다. IPA 추출 방법이나 테스트 버전 링크 배포 내용은 아래 링크에 자세히 작성하였으니 아래 링크를 참고바랍니다.

[Development로 Archive하여 테스트 버전 배포하기](https://swieeft.github.io/2020/02/20/DevelopmentArchive.html)

### IPA 내보내기 에러

--- 

위에 링크에서 보셨듯이 IPA를 추출하는 과정은 그렇게 어렵지 않습니다.

하지만 M1 Mac에서 IPA 추출을 하려고 하면 그 동안 잘 되면 것이 아래 이미지와 같은 에러와 함께 내보내기가 되지 않습니다. 참 당황스럽네요...

![M1MacIPAExportError1.png](/assets/images/posts/2021-05-17/M1MacIPAExportError1.png)

### 해결방법

---

처음에는 인증서 문제인지, 아니면 프로젝트 설정이 잘못 된건지 엄청 헤매었는데 해결 방법은 간단했습니다. 바로 Xcode를 Rosetta로 실행해주면 되는 것이었습니다.

- **Xcode 정보창 실행**

![M1MacIPAExportError2.png](/assets/images/posts/2021-05-17/M1MacIPAExportError2.png)

- **Rosetta 활성화**

![M1MacIPAExportError3.png](/assets/images/posts/2021-05-17/M1MacIPAExportError3.png)

이렇게 하고 Xcode를 실행해서 IPA 내보내기를 하면 정상적으로 동작하는 것을 확인할 수 있습니다.

### 마무리

---

간단하게 M1 Mac IPA 내보내기 에러에 대한 해결 방법을 알아보았습니다.

해당 이슈는 앱 타겟버전을 iOS 13.0 이상으로 설정하면 발생하지 않는다고 하는 답변들이 많이 있습니다. 

저 같은 경우에는 회사에서 작업하는 프로젝트의 타겟버전이 iOS 11.0이었어서 발생했던 것 같습니다.

이 이슈 때문에 몇 시간은 삽질한 것 같네요... 저 같은 삽질의 희생양이 나타나지 않길 바랍니다...

그럼 달콤한 코딩 되세요!

> 최근에 Xcode 12.5로 업데이트를 하니 Rosetta로 실행하지 않아도 정상적으로 IPA를 Export 할 수 있었습니다.


### 참고자료

--- 

[How to fix “IPA processing failed” in Xcode 12.2 with MAC M1](https://stackoverflow.com/questions/64916429/how-to-fix-ipa-processing-failed-in-xcode-12-2-with-mac-m1) 

