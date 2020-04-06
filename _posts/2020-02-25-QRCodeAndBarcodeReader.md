---
layout: post
title: "QR, Barcode 리더기 만들기"
subtitle: "[iOS]"
date: 2020-02-25 18:40
background: 
tags: [ios, swift]
---

흔히 사용되지는 않지만 종종 QRcode나 Barcode를 인식해서 나온 데이터로 상품을 등록하거나, 가계부를 작성하는 등 기능을 구현해야 되는 일이 있습니다.

저도 최근에 해당 기능을 구현할 기회가 있어 구현을 하면서 예제 프로젝트를 만들었는데요. 그냥 깃헙에 올려 두면 까먹을까봐 정리하기 위해 블로그를 작성합니다.

혹시나 구현을 위해 리서치 하시는 분들에게 도움이 되었으면 합니다.

### 예제 프로젝트 동작 설명

---

예제 프로젝트는 정말 간단하게 구현되어 있습니다. Start 버튼을 누르면 코드 인식을 시작하게 되고, 카메라가 활성화 됩니다. 

카메라에 코드가 인식되면 카메라가 비활성화 되면서 코드 인식을 멈춘 후 코드로 읽어드린 값을 Alert 창으로 표시 해줍니다.

![QRCodeAndBarcodeReader1.gif](/assets/images/posts/2020-02-25/QRCodeAndBarcodeReader1.gif)

### ReaderView 만들기

---

이 프로젝트의 핵심은 UIView를 커스텀하여 ReaderView를 만드는 것입니다. UIViewController를 이용하는 방법도 있고 여러가지 방법들이 있지만 저는 UIView 커스텀으로 개발을 하였습니다.

1. **ReaderView 초기화**

    ReaderView를 초기화 할 때 수행해야 될 작업은 AVCaptureSession을 생성하여 값을 설정해주는 작업을 하는 것입니다. 

    AVCaptureSession을 애플 공식문서에서는 아래와 같이 설명하고 있습니다.

    ![QRCodeAndBarcodeReader2.png](/assets/images/posts/2020-02-25/QRCodeAndBarcodeReader2.png)

    **캡처 활동을 관리하고 입력 장치의 데이터 흐름을 조정하여 출력을 캡처하는 객체입니다.** 라고 설명이 되어 있는데요. 아래 개요에 **객체를 인스턴스화하고 적절한 입력 및 출력을 추가합니다.** 라고 되어 있습니다.

    결국 AVCaptureSession을 사용하려면 우선 객체를 생성하고, 입력 및 출력 설정을 해주면 사용할 수 있는 준비가 된다는 얘기겠죠? 
    
    그럼 아래 코드를 보면서 하나씩 차근차근 초기화를 진행하도록 하겠습니다.

    - **UIView 기본 초기화**

      뷰를 초기화 하기 위해 기본적 초기화 메서드를 작성합니다.

      <p> {% gist swieeft/075acb44f906e0b9aa49e21c873eacdf QRCodeAndBarcodeReader1.swift %} </p>
    
    - **리더기로 인식 할 코드 종류 설정**

      리더기가 인식할 수 있는 코드 타입을 설정합니다. 본인의 프로젝트에 맞게 설정하시면 될 것 같습니다. 종류는 아래 링크에 자세히 나와 있으며, 코드 타입에 대한 설명은 각각 검색 해보시면 보다 자세한 내용을 확인하실 수 있습니다.

      [https://developer.apple.com/documentation/avfoundation/avmetadataobject/objecttype](https://developer.apple.com/documentation/avfoundation/avmetadataobject/objecttype)

      <p> {% gist swieeft/075acb44f906e0b9aa49e21c873eacdf QRCodeAndBarcodeReader2.swift %} </p>
                                                                                                            
    - **AVCaptureSession 초기화 및 RederView 초기화 하기**

      리더기의 핵심은 AVCaptureSession을 활용하여 코드를 인식하는 것입니다. 그러기 위해선 AVCaptureSession의 입,출력을 설정하는 작업이 필요합니다.

      <p> {% gist swieeft/075acb44f906e0b9aa49e21c873eacdf QRCodeAndBarcodeReader3.swift %} </p>

    - **AVCaptureVideoPreviewLayer 생성 및 초기화**

      AVCaptureVideoPreviewLayer은 실제 AVCaptureSession이 실행되어 보여지는 곳입니다. AVCaptureSession 설정을 완료한 후에 Layer를 생성하여 만들어진 AVCaptureSession를 넣어 초기화를 해주면 ReaderView 초기화 작업이 완료 됩니다.

      <p> {% gist swieeft/075acb44f906e0b9aa49e21c873eacdf QRCodeAndBarcodeReader4.swift %} </p>

    - **(선택) AVCaptureVideoPreviewLayer 중앙 가이드라인 만들기**

      이 부분은 필수 사항이 아닙니다. 편의를 위해 추가한 내용이기 때문에 필요하시면 추가하시거나, 다르게 사용하고 싶으시면 프로젝트에 맞게 변경해서 사용하시면 됩니다.

      <p> {% gist swieeft/075acb44f906e0b9aa49e21c873eacdf QRCodeAndBarcodeReader5.swift %} </p>

2. **AVCaptureSession 시작, 중지하기** 

    ReaderView 초기화가 완료 되었으면 이제 AVCaptureSession을 시작할 차례입니다. 예제 프로젝트에서는 ReaderView를 ViewController에 만들어 준 후 Button Action을 통해 시작을 합니다.

    - **ViewController 코드**

      AVCaptureSession이 현재 실행 중이지 않다면 세션을 시작하고, 실행 중이라면 세션을 중지합니다.

      <p> {% gist swieeft/075acb44f906e0b9aa49e21c873eacdf QRCodeAndBarcodeReader6.swift %} </p>

    - **AVCaptureSession 시작 - ReaderView 코드**

      <p> {% gist swieeft/075acb44f906e0b9aa49e21c873eacdf QRCodeAndBarcodeReader7.swift %} </p>    

    - **AVCaptureSession 중지 - ReaderView 코드**

      isButtonTap은 세션이 중지 된 이유가 Stop 버튼으로 중지 된 것인지 코드 인식이 완료 되어서 중지 된 것인지 확인하기 위한 것입니다.

      <p> {% gist swieeft/075acb44f906e0b9aa49e21c873eacdf QRCodeAndBarcodeReader8.swift %} </p>

3. **코드 인식한 결과 Delegate로 받기**

    코드 인식이 되면 AVCaptureMetadataOutputObjectsDelegate를 통해 인식 된 결과를 전달 받을 수 있습니다.

    <p> {% gist swieeft/075acb44f906e0b9aa49e21c873eacdf QRCodeAndBarcodeReader9.swift %} </p>

4. **ViewController에 결과를 전달할 Delegate 만들기**

    코드 인식이 완료되거나 실패, 중지 등의 이벤트가 발생하면 해당 이벤트를 ViewController에 전달할 Delegate 만들어야 합니다. 저는 success, fail, stop 3가지의 이벤트에 대해 처리 해주었습니다. 

    - **이벤트 상태**

      <p> {% gist swieeft/075acb44f906e0b9aa49e21c873eacdf QRCodeAndBarcodeReader10.swift %} </p>

    - **프로토콜 정의**

      <p> {% gist swieeft/075acb44f906e0b9aa49e21c873eacdf QRCodeAndBarcodeReader11.swift %} </p>

    - **Delegate 호출방법**

      <p> {% gist swieeft/075acb44f906e0b9aa49e21c873eacdf QRCodeAndBarcodeReader12.swift %} </p>

5. **ViewController에서 Delegate 처리**

    <p> {% gist swieeft/075acb44f906e0b9aa49e21c873eacdf QRCodeAndBarcodeReader13.swift %} </p>

### 마무리

---

QRcode, Barcode 리더기 만드는 법을 알아보았습니다. AVCaptureSession 생성만 잘 한다면 나머지 작업은 크게 어려운 부분이 없었던 것 같습니다.

꼭 UIView 커스텀으로만 사용하지 않고 UIViewController에서 사용도 가능하니 프로젝트 여러 곳에서 사용된다면 코드 리더기로만 활용되는 ViewController를 따로 만들어서 사용하셔도 될 것 같습니다.

아래 예제 프로젝트 링크를 확인하시면 전체 프로젝트를 확인하실 수 있습니다.

감사합니다. 달콤한 코딩 되세요!

### 예제 프로젝트 링크

---

[swieeft/QRCodeAndBarcodeReader](https://github.com/swieeft/QRCodeAndBarcodeReader)

### 참고자료

---

[How to create a simple QRCode / barcode scanner app in iOS swift?](https://medium.com/@abhimuralidharan/how-to-create-a-simple-qrcode-barcode-scanner-app-in-ios-swift-fd9970a70859)
