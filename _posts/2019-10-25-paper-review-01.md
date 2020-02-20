---
title: "논문 읽기 01: 'Atomic layer deposition: An overview', Chem. Rev. (2010), 110, 111-131"
layout: post
date: 2019-10-25 21:45
tag:
    - Chemical Engineering
    - Atomic Layer Deposition
    - ALD
    - Thin Film Deposition
    - Semiconductor
    - Paper
    - Study
    - Note
headerImage: false
image:
description: 191025 `Atomic layer deposition, An overview` paper review
category: blog
author: hsj00
externalLink: true
published: true
comments: true
share: true
use_math: false
---

# Atomic Layer Deposition: An Overview

해당 논문은 2010년에 콜로라도 대학 `Steven M. George`가 쓴 논문으로, [원자층증착법(`Atomic Layer Deposition`, `ALD`)][wiki]에 대한 개괄적인 내용을 담고있다. 학부생 연구원 시작하면서 가장 먼저 읽은 논문이다. 나온지 10년 가까이 됐지만 다양한 사례를 들어 `ALD`의 개념을 설명하는 논문이라 지금 읽어도 좋은 것 같다.

예전에 읽고 제대로 백업/관리를 안해서 다시 찾다보니 옛 기억이 새록새록 떠오른다. 논문 내용과 내가 아는 내용을 정리해서 노트로 만들어 정리해두고자 한다.

## Atomic Layer Deposition?

### History of ALD
`ALE`/`ALD`의 역사는 1970년대 핀란드의 [Tuomo Suntola]의 ZnS의 `ALE` 시스템 개발<sup>[^1]</sup>에서 시작됐다. 그 이후로 후속 연구들이 진행되어 학술 논문과 특허들이 나왔고, `ALE`가 처음으로 적용된 전자발광식 디스플레이가 1983년부터 1998년까지 헬싱키 공항에 전시되었다. 첫 상용 `ALE` 반응기인 `F-120`가 1988년에 판매되었다. 제조사인 `Microchemistry`는 나중에 `ASM`이 된다.<sup>[^2],[^3]</sup> 2000년대 이전에는 `ALE`(`Atomic Layer Eptaxy`)로 불리기도 했는데, 기판 위에서 대부분의 박막 성장이 에피택셜하게 성장하지 않는다는 결과 이후로 `ALD`란 용어가 더 널리 쓰이게 됐다.

### What is ALD?
`ALD`는 화학기상증착법(`CVD`)의 일종으로, 전구체(`precursor`)를 순차적 단계에 따라 반응기에 공급하여 박막을 성장시키는 기술이다. `Binary sequence ALD`가 가장 기본적인 형태로, Al<sub>2</sub>O<sub>3</sub>를 예로 들면, 금속 원소 Al을 포함하는 유기 금속 전구체와 반응 자리를 새로 만들어주는 `oxygen source`가 번갈아 공급되며 박막을 성장시킨다. 각 단계별로 공급된 전구체는 기판 표면의 반응자리와 전부 반응할 때까지 화학 흡착을 일으키고, 과량 공급되어도 `reactive site`가 포화 상태라면 더이상 반응이 일어나지 않는다. 이것을 `ALD`의 가장 큰 특징중 하나인 자기 제한적 거동(`Self-limiting growth behavior`)라고 부른다. 일반적인 `CVD`는 반응이 동시에, 연속적으로 일어나는 반면에 `ALD`는 전구체 공급 단계와 배출 단계가 들어가있는 것이 가장 큰 차이다. `ALD`의 자기 제한적 거동과 전구체의 순차적 공급 때문에 박막의 두께를 옹스트롬(`Å`) 단위로 조절할 수 있다. 옹스트롬 단위는 `1/10nm`로, 원자 수준으로 두께를 조절할 수 있어서 원자층증착법이라고 부른다. 이런 특징 때문에 높은 종횡비(`high aspect ratio`)를 갖는 구조에서도 균일한 두께로 박막을 성장시킬 수 있고, 초미세공정으로 돌입한 반도체 산업에서 중요한 공정으로 자리잡고 있는 것이다.

전구체는 기체 상태로 반응기에 공급되고, 기판의 기하학적 형상과 무관하게 모든 공간을 채운다. 전구체 공급 라인을 기판을 향해 직결할 필요도 없다. 오직 반응기 크기에 의한 제약만이 존재한다. 기판 표면에서의 반응도 순차적으로 진행되기 때문에 전구체끼리 반응을 일으키지 않는다.

다음 그림은 `ALD`의 순차적인 반응 단계를 도식화 한 것이다.

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/ALD_schematics.jpg/300px-ALD_schematics.jpg" alt="Schematic image of ALD" title="Schematic image of ALD">
<br>
<figure><figcaption><b>Schematic image of ALD (from wikipedia)</b></figcaption></figure>
</center>

## Thermal or Plasma-Enhanced ALD

`ALD`는 기본적으로 `CVD`와 연관이 깊어서 `Thermal ALD`의 경우 `CVD`의 `binary reaction`에 기반을 두고 있다. `CVD`와 같은 베이스를 갖는 반응물들은 다음과 같다.

| Type                     | Compound                                                                                                         |
| :----------------------- | :--------------------------------------------------------------------------------------------------------------- |
| **Binary Metal Oxide**   | Al<sub>2</sub>O<sub>3</sub>, TiO<sub>2</sub>, ZnO, ZrO<sub>2</sub>, HfO<sub>2</sub>, Ta<sub>2</sub>O<sub>5</sub> |
| **Binary Metal Nitride** | TiN, TaN, W<sub>2</sub>N                                                                                         |
| **Others**               | ZnS, CdS, GaP, InP                                                                                               |


`Plasma`/`Radical`을 이용할 경우 `Thermal ALD`로는 어려운 단일 성분의 `ALD` 박막을 증착<sup>[^3]</sup>할 수 있다. H<sub>2</sub> 플라즈마를 이용한 Ti<sup>[^4]</sup>, Ta<sup>[^5]</sup> `ALD`가 있다. `PE-ALD`(`Plasma Enhanced-ALD`)는 `Themal ALD`보다 훨씬 낮은 온도에서 박막을 증착할 수 있고, 이러한 특성은 열에 약한 기판이나 폴리머에도 `ALD` 박막을 증착<sup>[^6]</sup>할 수 있는 가능성을 제공한다.

## ALD reactor

다음 그림은 실험실 수준의 `viscous flow reactor` 구조를 개략적으로 나타낸 것이다.<sup>[^7]</sup> 기본적인 구성은 아래 그림과 같고, 필요에 따라 반응기 디자인이 달라지거나 `RF generator`, `QCM`, `in situ FT-IR`과 같은 부수적인 장비들이 추가된다. 

<center>
<img src="https://www.mdpi.com/inorganics/inorganics-06-00034/article_deploy/html/images/inorganics-06-00034-g001.png" alt="Viscous flow ALD reactor" title="Viscous flow ALD reactor">
<br>
<figure><figcaption><b>Viscous flow ALD reactor</b></figcaption></figure>
</center>

전구체의 증기압에 따라서 `carrier gas` 유무를 선택할 수 있다. 증기압이 낮은 전구체의 경우, 펌프가 끌어올리는데 긴 시간을 필요로 할 것이다. 그런 경우 `carrier gas`를 사용하면 효과적으로 증착 단계를 진행할 수 있다. `Viscous flow reactor`에서 전구체의 비말 동반과 기체의 상호 확산 사이에서 `carrier gas`의 최적 증기압은 약 ~1 `Torr`다 (N<sub>2</sub> 기준). 만약 증기압이 ~1 `Torr` 이하일 경우 기체의 평균 자유 경로(`mean free path`)가 멀어져서 `carrier gas`의 비말 동반 효과가 덜할 것이다.

다음 그림은 다양한 종류의 `ALD reactor`를 개략적으로 나타낸 그림이다.<sup>[^8]</sup> 전구체의 공급 방식에 따라 `flow-type`과 `showerhead`로 나뉘고, 반응기의 기판 용량에 따라 `single wafer`와 `batch`로 구분할 수 있다. 반응에 필요한 에너지원에 따라 `thermal` 또는 `energy enhanced`로 구분할 수 있고, 반응이 공간의 제약이 있느냐 전구체 공급 시간에 제약이 있느냐로 `temporal`과 `spatial`로 구분할 수 있다.

|     Reactor type     |
| :------------------: | :---------------------------: |
| **Precursor dosing** |         **variation**         |
|     `Flow-type`      |   `single wafer` / `batch`    |
|     `Showerhead`     | `thermal` / `energy enhanced` |
|                      |    `temporal` / `spatial`     |

<br>
<center>
<img src="https://ars.els-cdn.com/content/image/3-s2.0-B9780444633040000275-f27-14-9780444633040.jpg" alt="A schematic of the various types of ALD reactor" title="A schematic of the various types of ALD reactor">
<br>
<figure><figcaption><b>A schematic of the various types of ALD reactor</b></figcaption></figure>
</center>

----------
<!-- link -->
[wiki]: https://en.wikipedia.org/wiki/Atomic_layer_deposition
[Tuomo Suntola]: <https://en.wikipedia.org/wiki/Tuomo_Suntola>

<!-- references -->
[^1]: <https://doi.org/10.1002/cvde.201402012>
[^2]: <https://www.asm.com/about/strategy-and-focus-areas/breakthrough-technology>
[^3]: <https://doi.org/10.1016/0040-6090(92)90874-B>
[^4]: <https://doi.org/10.1116/1.1622676>
[^5]: <https://doi.org/10.1116/1.1305809>
[^6]: <https://doi.org/10.1116/1.1486233>
[^7]: <https://doi.org/10.1063/1.2338776>
[^7]: <https://doi.org/10.3390/inorganics6010034>
[^8]: <https://doi.org/10.1016/B978-0-444-63304-0.00027-5>