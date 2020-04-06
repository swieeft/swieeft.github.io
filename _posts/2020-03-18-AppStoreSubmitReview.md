---
layout: post
title: "앱 스토어 심사 제출 및 배포하기"
subtitle: "[Tips]"
date: 2020-03-18 09:50
background: 
tags: [tips, ios]
---

iOS 앱 배포를 위해서 심사 제출 및 배포하는 방법에 대해 알아보도록 하겠습니다.

이 글은 이미 Xcode에서 빌드 된 바이너리가 업로드 된 후의 과정을 설명하고 있습니다. 신규 앱의 경우에는 생략 된 부분들이 있어 내용이 부족할 수 있음을 미리 알려드립니다.

또한 심사를 제출하기 전 미리 애플 심사 가이드 라인에 대한 문서를 숙지 하신 후에 배포를 진행하셔야 리젝을 최소화 할 수 있으니 심사 가이드를 아직 읽어보지 않으신 분들은 꼭 한번씩 읽고서 진행하세요. 

[App Store 심사 지침](https://developer.apple.com/kr/app-store/review/guidelines/)

### 배포할 앱으로 이동하기

---

1. **앱스토어 커넥트로 이동**

    [https://appstoreconnect.apple.com/](https://appstoreconnect.apple.com/)

2. **나의 앱 메뉴로 이동**

    ![AppStoreSubmitReview1.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview1.png)

3. **앱 선택**

    배포할 앱을 선택합니다. 만약 신규 등록 앱이라면 왼쪽 상단의 + 버튼을 눌러 앱을 추가하면 됩니다.

    ![AppStoreSubmitReview2.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview2.png)

### 배포 할 버전 생성 및 이동

---

1. **배포 할 버전 생성**

    버전 및 플랫폼을 클릭 후 iOS를 선택하면 버전 입력하는 창이 나타납니다. 그 창에서 배포 할 버전을 입력하시면 됩니다.

    ![AppStoreSubmitReview3.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview3.png)

2. **배포 할 버전 선택**

    배포 할 버전을 선택하시면 됩니다. 여기서는 1.6.1 버전이 업데이트 되는 버전이기 때문에 1.6.1을 선택하였습니다.

    ![AppStoreSubmitReview4.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview4.png)

### 앱 내용 입력

---

1. **업데이트 내용 입력**

    이번 버전에 업데이트 된 내용을 작성하시면 됩니다. 형식은 자유형식입니다.

    ![AppStoreSubmitReview5.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview5.png)

    > 신규 앱의 경우 업데이트 내용을 입력하는 화면이 없습니다.

2. **미리보기 추가**

    앱 스토어에 표시 될 미리보기 이미지를 업로드 하는 곳입니다. 기본적으로 이전 버전의 미리보기가 자동으로 들어가며, 이미지가 추가, 수정, 삭제 될 경우 이 곳에서 작업하시면 됩니다.

    ![AppStoreSubmitReview6.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview6.png)

3. **키워드 입력**

    앱스토어에서 검색 시 사용될 키워드입니다.

    ![AppStoreSubmitReview7.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview7.png)

4. **지원 URL 입력**

    앱 설명 URL이나 회사 URL을 입력하면 됩니다.

    ![AppStoreSubmitReview8.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview8.png)

5. **설명 입력**

    앱스토어에 표시 될 앱 설명을 입력하는 곳입니다.

    ![AppStoreSubmitReview9.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview9.png)

6. **빌드 선택**

    업데이트 할 앱의 빌드를 선택합니다. + 아이콘을 클릭하면 빌드를 선택할 수 있는 화면이 나타납니다.

    ![AppStoreSubmitReview10.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview10.png)

    빌드 선택 화면입니다. 원하는 빌드를 선택한 후 완료 버튼을 누르면 됩니다.

    > 괄호()는 앱의 빌드버전으로 하나의 앱 버전에 여러개의 빌드버전이 존재할 수 있습니다. (테스트 시에 문제 발생 시 빌드버전을 변경하여 다시 테스트 플라이트에 업로드 합니다.)

    ![AppStoreSubmitReview11.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview11.png)

    빌드를 선택하면 선택한 빌드가 표시됩니다.

    ![AppStoreSubmitReview12.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview12.png)

7. **앱 아이콘**

    앱 아이콘은 따로 설정하지 않아도 빌드 선택하면 자동으로 설정 됩니다.

    ![AppStoreSubmitReview13.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview13.png)

8. **저작권 입력**

    앱 저작권을 입력하는 곳입니다. 이전 버전에 입력 한 값을 그대로 가져오니 변경이 필요할 때만 수정하면 됩니다.

    ![AppStoreSubmitReview14.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview14.png)

9. **버전**

    버전을 입력하는 곳입니다. 이미 **버전 및 플랫폼**에서 입력한 버전으로 입력 되어 있습니다. 만약 버전이 잘못 입력 되었다면 이곳에서 수정하시면 됩니다.

    ![AppStoreSubmitReview15.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview15.png)

10. **로그인 정보**

    애플 리뷰어가 앱을 사용할 수 있게 제공한 테스트 계정 정보를 입력하는 곳입니다.

    ![AppStoreSubmitReview16.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview16.png)

11. **연락처 정보**

    앱 심사 중 문제 발생 시 연락할 담당자 번호를 입력합니다.

    ![AppStoreSubmitReview17.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview17.png)

12. **메모**

    앱 심사 시 리뷰어에게 전달해야 될 특이사항이나, 링크 등을 제공하는 목적의 메모란입니다.

    ![AppStoreSubmitReview18.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview18.png)

13. **첨부파일**

    앱 심사 시 필요한 파일을 첨부할 수 있습니다. (ex. 저작권 계약서, 데모 영상 등)

    ![AppStoreSubmitReview19.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview19.png)

14. **버전 출시 방법 선택**

    심사 완료 후 해당 버전을 앱 스토어에 배포하는 방법을 선택할 수 있습니다.

    - **수동으로 버전 출시** : 심사가 완료되면 직접 원하는 시기에 배포할 수 있습니다.
    - **자동으로 버전 출시** : 심사가 완료되는 즉시 배포를 시작합니다.
    - **다음 날짜 이후 앱 심사가 끝나면 자동으로 이 버전을 공개**
        - 설정한 날짜 이전 심사 완료 : 설정한 날짜에 배포 시작
        - 설정한 날짜 이후 심사 완료 : 심사 완료 후 즉시 배포 시작

    ![AppStoreSubmitReview20.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview20.png)

15. **자동 업데이트 점진적 출시**

    심사가 완료되면 모든 사용자에게 즉시 업데이트 배포를 하거나, 점진적으로 업데이트를 출시하는 방법을 선택할 수 있습니다.

    ![AppStoreSubmitReview21.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview21.png)

16. **iOS 평점 재설정**

    업데이트 시 평점을 리셋 시킬지 기존 평점을 유지할지 선택합니다.

    ![AppStoreSubmitReview22.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview22.png)

17. **기타사항**

위에서 언급되지 않은 항목들은 선택 사항이거나, 따로 건들이지 않아도 되는 내용이므로 작성하지 않았습니다.

### 심사 제출하기

---

1. **작성 내용 저장하기**

    위의 내용들이 전부 입력 되면 화면 오른쪽 상단에 저장 버튼을 눌러 입력한 내용을 저장합니다.

    ![AppStoreSubmitReview23.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview23.png)

2. **심사 제출하기**

    저장이 완료되면 **심사를 위해 제출** 버튼이 활성화 됩니다. 버튼을 눌러 심사를 시작합니다. 

    ![AppStoreSubmitReview24.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview24.png)

3. **광고 식별자 사용 여부 체크**

    광고 식별자를 사용하는지 묻는 화면이 나타납니다. 앱에서 광고 모듈을 사용하여 광고를 하고 있다면 예를 선택하고 사용하지 않으면 아니요를 선택하면 됩니다.

    ![AppStoreSubmitReview25.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview25.png)

4. **최종 제출하기**

    광고 식별자 사용 여부를 체크하면 오른쪽 상단의 **제출** 버튼이 활성화 되고 제출 버튼을 클릭하면 최종적으로 심사 제출이 완료 됩니다.

    ![AppStoreSubmitReview26.png](/assets/images/posts/2020-03-18/AppStoreSubmitReview26.png)

### 심사 프로세스

---

심사 프로세스는 아래와 같이 진행 됩니다.

1. **제출 준비 중** : 업데이트 대한 내용 입력 및 제출 준비 단계입니다.
2. **심사 대기 중** : 업데이트를 제출하여 리뷰어가 심사를 하기 전 상태입니다.
3. **심사 중** : 리뷰어가 앱에 대한 심사를 진행하고 있는 상태입니다.
4. **판매 준비됨** : 심사가 완료 되고 배포가 진행되고 있는 상태입니다.

    4-1. **개발자 출시 대기중** : 버전 출시 방법을 수동으로 선택한 경우 심사가 완료 되고, 아직 배포를 하지 않은 상태입니다. 

    4-2. **바이너리 거부 됨** : 심사 중 문제가 발견되어 리젝 된 상태입니다. 리젝에 대한 내용은 메일이나 앱스토어 커넥트에서 확인 가능합니다.

### 마무리

---

해당 내용은 신규앱 등록보단 앱 업데이트에 좀 더 초점을 맞추어 작성 되었습니다. 신규 앱 등록에 대한 부분은 더 많은 내용들이 들어가야 되서 이 글에서는 다루지 않으려고 합니다.

나중에 기회가 되면 신규 앱 생성 부터 등록까지 글을 작성하려고 합니다.

그럼 달콤한 코딩 되세요!