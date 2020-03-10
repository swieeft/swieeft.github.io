---
title: "[iOS] URL을 이용한 Image Download"
layout: post
date: 2020-03-10 13:45
tag:
    - iOS
    - Swift
headerImage: false
image:
description: URL을 이용한 Image Download
category: blog
author: swieeft
externalLink: true
published: true
comments: true
share: true
use_math: false
---
안녕하세요. 이번에는 URL을 이용한 Image Download를 알아보려고 합니다.

앱을 개발하다 보면 서버에서 프로필 이미지나 상품 이미지의 URL을 받은 후 해당 URL을 통해 이미지를 다운 받는 개발을 해야 될 때가 많이 있습니다.

그럴 때 어떻게 개발을 해야 될까요? 아래에 해당 내용을 정리하려고 합니다.

### URL을 통한 Image Download 구현하기

---

구현하는 방법은 생각보다 간단합니다. API 통신 하듯이 URLSession을 이용해서 다운로드 받아 주면 간단하게 이미지를 다운 받을 수 있습니다.

- **예제 코드**
    ```swift
    func imageDownload(url: URL) {
        var request = URLRequest(url: url)
        request.httpMethod = "GET"
    
        URLSession.shared.dataTask(with: request) { data, response, error in
            guard
                let httpURLResponse = response as? HTTPURLResponse, httpURLResponse.statusCode == 200,
                let mimeType = response?.mimeType, mimeType.hasPrefix("image"),
                let data = data, error == nil,
                let image = UIImage(data: data)
                else {
                    print("Download image fail : \(url)")
                    return
            }
    
            DispatchQueue.main.async() {[weak self] in
                print("Download image success \(url)")
    
                self?.imageView.image = image
            }
        }.resume()
    }
    ```

    url에는 다운로드 받을 이미지의 url을 넣어 주면 image를 다운 받아서 imageView에 이미지가 나오도록 해주는 메서드입니다.

- **코드 분석**

    URLSession을 통해 이미지 데이터를 받아 오면 현재 받아온 데이터가 이미지 데이터가 맞는지 확인하기 위해 mimeType을 체크 해줍니다.

    ```swift
    let mimeType = response?.mimeType, mimeType.hasPrefix("image")
    ```

    mimeType이 image인지 여부를 확인하여 이미지 데이터를 정상적으로 다운로드 받았는지 확인 합니다.

    그리고 받아온 데이터를 이용하여 UIImage를 생성해줍니다.

    ```swift
    let image = UIImage(data: data)
    ```

    만약 위의 과정들이 정상적으로 동작하지 않는다면 이미지 다운로드가 실패한 것을 판단합니다.

    다운로드가 성공적으로 완료 되면 imageView에 다운로드 받은 이미지를 넣어줍니다.

    ```swift
    DispatchQueue.main.async() {[weak self] in
        print("Download image success \(url)")
    
        self?.imageView.image = image
    }
    ```

    여기서 DispatchQueue.main.async()를 사용한 이유는 우리가 이미지 다운로드를 URLSession을 통해 비동기로 다운 받았기 때문에 메인 스레드에서 imageView를 업데이트 해주라고 명시 해주어야 정상적으로 이미지를 표시 해줄 수 있습니다.

### Extension을 활용하여 Image Download 구현하기

---

위에서 알아본 방법을 사용하면 필요한 ViewController마다 해당 함수를 구현 해주어야 하는 불편함이 있습니다.

그런 불편함을 없애기 위해 UIImageView를 Extension하여 Image Download를 구현 할 수 있습니다.

- **예제 코드**

    ```swift
    extension UIImageView {
        func imageDownload(url: URL, contentMode mode: UIView.ContentMode = .scaleAspectFit) {
            var request = URLRequest(url: url)
            request.httpMethod = "GET"
    
            URLSession.shared.dataTask(with: request) { data, response, error in
                guard
                    let httpURLResponse = response as? HTTPURLResponse, httpURLResponse.statusCode == 200,
                    let mimeType = response?.mimeType, mimeType.hasPrefix("image"),
                    let data = data, error == nil,
                    let image = UIImage(data: data)
                    else {
                        print("Download image fail : \(url)")
                        return
                }
    
                DispatchQueue.main.async() { [weak self] in
                    print("Download image success \(url)")
    
                    self?.contentMode = mode
                    self?.image = image
                }
            }.resume()
        }
    }
    ```

    위에서 알아본 코드를 그대로 UIImageView extension에 넣어서 사용하시면 됩니다. 여기에 UIImageView를 Extension하여 사용 했기 때문에 contentMode 파라메터를 추가 해주었습니다.

- **URL을 String으로 받아서 사용하기**

    예제 코드에서 보시면 파라메터로 URL을 받고 있습니다. 그러면 매번 URL 객체를 생성해서 값을 넘겨줘야 되는데 그러면 반복 작업들이 많아지게 되니깐 String으로 받아서 사용할 수 있는 메서드를 추가해서 사용하면 좀 더 코드를 깔끔하게 만들 수 있습니다.

    ```swift
    func imageDownload(link: String, contentMode mode: UIView.ContentMode = .scaleAspectFit) {
        guard let url = URL(string: link) else {
            return
        }
    
        imageDownload(url: url, contentMode: mode)
    }
    ```

    Extension 안에 위의 메소드를 만들어서 사용하면, String으로 이미지 다운로드를 할 수 있습니다.

### Image 캐싱(Caching) 처리하기

---

이제 이미지 다운로드 하는 방법은 전부 알아보았습니다. 근데 여기서 우리는 또 다른 문제를 보게 됩니다. 바로 이미지가 필요할 때마다 매번 이미지 다운로드를 하고 있다는 것입니다.

그럼 매번 이미지 다운로드를 안 받고 사용하려면 어떤 방법이 있을까요?

우리에겐 캐싱(Caching)이라는 것이 있습니다.

> 이미지 캐싱이란, 한번 다운로드 받은 이미지를 로컬에 저장하여 이미지가 필요할 때 매번 다운로드를 받는 것이 아니라 로컬에서 불러옴으로써 로딩 시간을 줄이고, 데이터 통신을 줄이는 방법입니다.

- **예제 코드**
    - Cache 클래스 만들기

        우선 캐싱을 위한 Cache 클래스를 만듭니다. Cache는 NSCache를 활용해 만들어 줍니다.

        ```swift
        class Cache {
            static let imageCache = NSCache<NSString, UIImage>()
        }
        ```

        NSCache 뒤에 들어가는 NSString은 캐싱 시 사용 될 키입니다. 뒤에 UIImage는 다운로드 받은 이미지 데이터가 들어가게 됩니다.

    - Cache에 이미지 저장하기

        ```swift
        Cache.imageCache.setObject(image, forKey: url.absoluteString as NSString)
        ```

        NSCache의 setObject를 이용해서 캐시에 저장합니다. 키 값은 이미지의 url로 해줍니다.

        > 키 값은 url이 아닌 다른 고유 값을 사용하셔도 됩니다.

    - Cache에서 이미지 불러오기

        ```swift
        let cacheImage = Cache.imageCache.object(forKey: url.absoluteString as NSString)
        ```

        NSCache의 object를 이용해서 캐시에 저장된 이미지를 불러옵니다. 만약 키 값이 존재하지 않으면 nil을 반환하게 됩니다.

    - 전체 코드

        캐싱이 적용된 다운로드 메서드 풀 코드입니다.

        ```swift
        func imageDownload(url: URL, contentMode mode: UIView.ContentMode = .scaleAspectFit) {
            if let cacheImage = Cache.imageCache.object(forKey: url.absoluteString as NSString) {
                DispatchQueue.main.async() { [weak self] in
                    self?.contentMode = mode
                    self?.image = cacheImage
                }
            }
            else {
                var request = URLRequest(url: url)
                request.httpMethod = "GET"
        
                URLSession.shared.dataTask(with: request) { data, response, error in
                    guard
                        let httpURLResponse = response as? HTTPURLResponse, httpURLResponse.statusCode == 200,
                        let mimeType = response?.mimeType, mimeType.hasPrefix("image"),
                        let data = data, error == nil,
                        let image = UIImage(data: data)
                        else {
                            print("Download image fail : \(url)")
                            return
                    }
        
                    DispatchQueue.main.async() { [weak self] in
                        print("Download image success \(url)")
        
                        Cache.imageCache.setObject(image, forKey: url.absoluteString as NSString)
        
                        self?.contentMode = mode
                        self?.image = image
                    }
                }.resume()
            }
        }
        ```

        먼저 캐싱 된 이미지가 있는지 확인 후에 캐싱 이미지가 있으면 바로 imageView에 넣어주고, 아니면 이미지 다운로드를 진행합니다.

        이미지 다운로드에 성공하면 해당 이미지를 캐시에 저장하도록 합니다.

- **캐싱 시 주의할 점**

    캐싱을 하면 많은 부분에서 이득이 있지만 한가지 주의할 점이 있습니다.

    캐싱을 하게 되면 로컬에 저장 된 이미지를 불러오기 때문에 만약 동일한 키 값의 이미지가 서버에서 변경이 되면 앱을 껏다 키기 전까진 변경된 이미지가 아닌 기존 이미지를 불러오게 되는 문제가 있습니다.

    이 부분만 주의하시면 캐싱을 사용해서 얻는 이득이 크니깐 개발 시 주의해서 적용하시면 될 것 같습니다.

### 마무리

---

지금까지 이미지 다운로드 받는 법을 알아보았습니다. 앱에서 이미지 다운로드는 흔하게 개발 되는 것 중에 하나이기 때문에 잘 기억해 두면 많은 곳에서 활용할 수 있습니다.

그럼 달콤한 코딩 되세요!