---
layout: default
title: Awesome Android Keyboards
description: A curated Android keyboard and Android IME ecosystem index.
---

> This page is generated from the repository README. Edit `data/keyboards.yml`, then run `python scripts/generate_readme.py` and `python scripts/generate_pages.py`.

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re) [![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](https://github.com/ideas-no996/awesome-android-keyboards/blob/main/LICENSE) ![Last Updated](https://img.shields.io/badge/last%20updated-2026--06--29-blue) [![GitHub Stars](https://img.shields.io/github/stars/ideas-no996/awesome-android-keyboards?style=social)](https://github.com/ideas-no996/awesome-android-keyboards/stargazers)

> A curated, maintainable map of Android keyboard and input method ecosystems.

Awesome Android Keyboards is a professional index for the android keyboard ecosystem: Android IME apps, input method engines, privacy keyboard choices, open-source keyboard projects, Rime and Trime front-ends, F-Droid packages, commercial keyboards, developer keyboards, theme systems, and Android InputMethodService resources. It is built for users comparing daily keyboards, developers studying Android IME architecture, Chinese input method users evaluating Rime-based workflows, and maintainers looking for realistic open-source keyboard bases.

The list is intentionally conservative. It does not rank projects by hype, copy marketing text, or treat closed-source claims as implementation facts. Each entry is backed by structured data in YAML, source links, maintenance notes, privacy/network signals, theme suitability, Chinese input support, and a short original review.

Data file: [`data/keyboards.yml`](https://github.com/ideas-no996/awesome-android-keyboards/blob/main/data/keyboards.yml). Generated from structured data on 2026-06-29.

## Table of Contents

- [Quick Recommendations](#quick-recommendations)
- [Categories](#categories)
  - [Commercial Keyboards](#commercial-keyboards)
  - [Open Source Keyboards](#open-source-keyboards)
  - [Rime-based Keyboards](#rime-based-keyboards)
  - [Privacy-focused Keyboards](#privacy-focused-keyboards)
  - [AI-assisted Keyboards](#ai-assisted-keyboards)
  - [Developer / Hacker Keyboards](#developer--hacker-keyboards)
  - [Theme and Customization Resources](#theme-and-customization-resources)
  - [Android IME Development Resources](#android-ime-development-resources)

## Quick Recommendations

- **普通用户推荐:** [Gboard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin), [Microsoft SwiftKey](https://www.microsoft.com/swiftkey), [HeliBoard](https://github.com/Helium314/HeliBoard)
- **隐私优先推荐:** [HeliBoard](https://github.com/Helium314/HeliBoard), [FUTO Keyboard](https://github.com/futo-org/android-keyboard), [FlorisBoard](https://github.com/florisboard/florisboard), [Simple Keyboard](https://github.com/rkkr/simple-keyboard)
- **中文输入推荐:** [Trime](https://github.com/osfans/trime), [Fcitx5 for Android](https://github.com/fcitx5-android/fcitx5-android), [WeChat Keyboard](https://z.weixin.qq.com/), [Sogou IME](https://shurufa.sogou.com/)
- **适合二次开发推荐:** [FlorisBoard](https://github.com/florisboard/florisboard), [HeliBoard](https://github.com/Helium314/HeliBoard), [Simple Keyboard](https://github.com/rkkr/simple-keyboard), [Unexpected Keyboard](https://github.com/Julow/Unexpected-Keyboard)
- **适合 iOS-like 主题改造推荐:** [FlorisBoard](https://github.com/florisboard/florisboard), [HeliBoard](https://github.com/Helium314/HeliBoard), [AnySoftKeyboard](https://github.com/AnySoftKeyboard/AnySoftKeyboard), [Trime](https://github.com/osfans/trime)
- **适合 Glassmorphism 主题改造推荐:** [FlorisBoard](https://github.com/florisboard/florisboard), [HeliBoard](https://github.com/Helium314/HeliBoard), [FUTO Keyboard](https://github.com/futo-org/android-keyboard), [Trime](https://github.com/osfans/trime)

## Categories

The tables stay intentionally compact. Full evaluation fields live in `data/keyboards.yml`; the complete README contains the longer detail blocks.

### Commercial Keyboards

| Name | Source | License | Stars | Signals | Short review |
| --- | --- | --- | ---: | --- | --- |
| Baidu IME | [Baidu IME](https://shurufa.baidu.com/) | Proprietary | N/A | Chinese: excellent<br>Theme: advanced<br>Offline: partial<br>Privacy: medium | Worth tracking for Chinese input UX patterns, especially commercial theming and prediction. |
| Gboard | [Gboard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin) | Proprietary | N/A | Chinese: good<br>Theme: good<br>Offline: partial<br>Privacy: medium | Best baseline recommendation for users who want reliability and broad language support. |
| Microsoft SwiftKey | [Microsoft SwiftKey](https://www.microsoft.com/swiftkey) | Proprietary | N/A | Chinese: good<br>Theme: advanced<br>Offline: partial<br>Privacy: medium | Strong mainstream choice for users who value prediction quality and visual customization. |
| Sogou IME | [Sogou IME](https://shurufa.sogou.com/) | Proprietary | N/A | Chinese: excellent<br>Theme: advanced<br>Offline: partial<br>Privacy: medium | Useful reference point for Chinese commercial keyboard features and theme marketplaces. |
| WeChat Keyboard | [WeChat Keyboard](https://z.weixin.qq.com/) | Proprietary | N/A | Chinese: excellent<br>Theme: basic<br>Offline: partial<br>Privacy: medium | Practical option for Chinese users already living in Tencent services. |

### Open Source Keyboards

| Name | Source | License | Stars | Signals | Short review |
| --- | --- | --- | ---: | --- | --- |
| AnySoftKeyboard | [AnySoftKeyboard](https://github.com/AnySoftKeyboard/AnySoftKeyboard) | Apache-2.0 | 3,327 | Chinese: basic<br>Theme: advanced<br>Offline: Yes<br>Privacy: high | Strong candidate for studying plugin-like language and theme packaging. |
| FlorisBoard | [FlorisBoard](https://github.com/florisboard/florisboard) | Apache-2.0 | 8,441 | Chinese: basic<br>Theme: advanced<br>Offline: Yes<br>Privacy: high | Best candidate for serious UI experiments, Compose-based refactors, and custom themes. |
| HeliBoard | [HeliBoard](https://github.com/Helium314/HeliBoard) | GPL-3.0 | 5,520 | Chinese: basic<br>Theme: good<br>Offline: Yes<br>Privacy: high | Best starting point for privacy-minded users and theme-oriented forks. |
| OpenBoard | [OpenBoard](https://github.com/openboard-team/openboard) | GPL-3.0 | 2,726 | Chinese: basic<br>Theme: basic<br>Offline: Yes<br>Privacy: high | Good reference for minimal offline keyboard behavior, but check maintenance before forking. |
| Simple Keyboard | [Simple Keyboard](https://github.com/rkkr/simple-keyboard) | Apache-2.0 | 1,529 | Chinese: none<br>Theme: basic<br>Offline: Yes<br>Privacy: high | Good for learning Android IME basics or building a deliberately simple fork. |

### Rime-based Keyboards

| Name | Source | License | Stars | Signals | Short review |
| --- | --- | --- | ---: | --- | --- |
| Fcitx5 for Android | [Fcitx5 for Android](https://github.com/fcitx5-android/fcitx5-android) | LGPL-2.1 | 5,371 | Chinese: rime-based<br>Theme: good<br>Offline: Yes<br>Privacy: high | Best reference for bringing desktop IME architecture and Rime support to Android. |
| Trime | [Trime](https://github.com/osfans/trime) | GPL-3.0 | 4,435 | Chinese: rime-based<br>Theme: advanced<br>Offline: Yes<br>Privacy: high | Best Android choice for serious Chinese Rime users and schema-heavy workflows. |

### Privacy-focused Keyboards

| Name | Source | License | Stars | Signals | Short review |
| --- | --- | --- | ---: | --- | --- |
| Fcitx5 for Android | [Fcitx5 for Android](https://github.com/fcitx5-android/fcitx5-android) | LGPL-2.1 | 5,371 | Chinese: rime-based<br>Theme: good<br>Offline: Yes<br>Privacy: high | Best reference for bringing desktop IME architecture and Rime support to Android. |
| FlorisBoard | [FlorisBoard](https://github.com/florisboard/florisboard) | Apache-2.0 | 8,441 | Chinese: basic<br>Theme: advanced<br>Offline: Yes<br>Privacy: high | Best candidate for serious UI experiments, Compose-based refactors, and custom themes. |
| FUTO Keyboard | [FUTO Keyboard](https://github.com/futo-org/android-keyboard) | NOASSERTION | 2,777 | Chinese: basic<br>Theme: good<br>Offline: Yes<br>Privacy: high | Interesting bridge between mainstream prediction quality and privacy-first design. |
| HeliBoard | [HeliBoard](https://github.com/Helium314/HeliBoard) | GPL-3.0 | 5,520 | Chinese: basic<br>Theme: good<br>Offline: Yes<br>Privacy: high | Best starting point for privacy-minded users and theme-oriented forks. |
| Thumb-Key | [Thumb-Key](https://github.com/dessalines/thumb-key) | AGPL-3.0 | 1,497 | Chinese: none<br>Theme: good<br>Offline: Yes<br>Privacy: high | Good reference for alternative mobile typing mechanics and compact UI experiments. |
| Trime | [Trime](https://github.com/osfans/trime) | GPL-3.0 | 4,435 | Chinese: rime-based<br>Theme: advanced<br>Offline: Yes<br>Privacy: high | Best Android choice for serious Chinese Rime users and schema-heavy workflows. |

### AI-assisted Keyboards

| Name | Source | License | Stars | Signals | Short review |
| --- | --- | --- | ---: | --- | --- |
| Baidu IME | [Baidu IME](https://shurufa.baidu.com/) | Proprietary | N/A | Chinese: excellent<br>Theme: advanced<br>Offline: partial<br>Privacy: medium | Worth tracking for Chinese input UX patterns, especially commercial theming and prediction. |
| FUTO Keyboard | [FUTO Keyboard](https://github.com/futo-org/android-keyboard) | NOASSERTION | 2,777 | Chinese: basic<br>Theme: good<br>Offline: Yes<br>Privacy: high | Interesting bridge between mainstream prediction quality and privacy-first design. |
| Microsoft SwiftKey | [Microsoft SwiftKey](https://www.microsoft.com/swiftkey) | Proprietary | N/A | Chinese: good<br>Theme: advanced<br>Offline: partial<br>Privacy: medium | Strong mainstream choice for users who value prediction quality and visual customization. |
| Sogou IME | [Sogou IME](https://shurufa.sogou.com/) | Proprietary | N/A | Chinese: excellent<br>Theme: advanced<br>Offline: partial<br>Privacy: medium | Useful reference point for Chinese commercial keyboard features and theme marketplaces. |

### Developer / Hacker Keyboards

| Name | Source | License | Stars | Signals | Short review |
| --- | --- | --- | ---: | --- | --- |
| Hacker's Keyboard | [Hacker's Keyboard](https://github.com/klausw/hackerskeyboard) | Apache-2.0 | 2,349 | Chinese: none<br>Theme: basic<br>Offline: Yes<br>Privacy: high | Historically important hacker keyboard, but new projects should account for age and maintenance risk. |
| MessageEase | [MessageEase](https://www.exideas.com/ME/) | Proprietary | N/A | Chinese: none<br>Theme: basic<br>Offline: Yes<br>Privacy: medium | Included as a design reference for non-QWERTY mobile input methods. |
| Unexpected Keyboard | [Unexpected Keyboard](https://github.com/Julow/Unexpected-Keyboard) | GPL-3.0 | 3,095 | Chinese: none<br>Theme: good<br>Offline: Yes<br>Privacy: high | Excellent reference for non-mainstream layouts and dense gesture-accessible symbols. |

### Theme and Customization Resources

| Name | Source | License | Stars | Signals | Short review |
| --- | --- | --- | ---: | --- | --- |
| AnySoftKeyboard | [AnySoftKeyboard](https://github.com/AnySoftKeyboard/AnySoftKeyboard) | Apache-2.0 | 3,327 | Chinese: basic<br>Theme: advanced<br>Offline: Yes<br>Privacy: high | Strong candidate for studying plugin-like language and theme packaging. |
| Baidu IME | [Baidu IME](https://shurufa.baidu.com/) | Proprietary | N/A | Chinese: excellent<br>Theme: advanced<br>Offline: partial<br>Privacy: medium | Worth tracking for Chinese input UX patterns, especially commercial theming and prediction. |
| FlorisBoard | [FlorisBoard](https://github.com/florisboard/florisboard) | Apache-2.0 | 8,441 | Chinese: basic<br>Theme: advanced<br>Offline: Yes<br>Privacy: high | Best candidate for serious UI experiments, Compose-based refactors, and custom themes. |
| FUTO Keyboard | [FUTO Keyboard](https://github.com/futo-org/android-keyboard) | NOASSERTION | 2,777 | Chinese: basic<br>Theme: good<br>Offline: Yes<br>Privacy: high | Interesting bridge between mainstream prediction quality and privacy-first design. |
| HeliBoard | [HeliBoard](https://github.com/Helium314/HeliBoard) | GPL-3.0 | 5,520 | Chinese: basic<br>Theme: good<br>Offline: Yes<br>Privacy: high | Best starting point for privacy-minded users and theme-oriented forks. |
| Microsoft SwiftKey | [Microsoft SwiftKey](https://www.microsoft.com/swiftkey) | Proprietary | N/A | Chinese: good<br>Theme: advanced<br>Offline: partial<br>Privacy: medium | Strong mainstream choice for users who value prediction quality and visual customization. |
| Sogou IME | [Sogou IME](https://shurufa.sogou.com/) | Proprietary | N/A | Chinese: excellent<br>Theme: advanced<br>Offline: partial<br>Privacy: medium | Useful reference point for Chinese commercial keyboard features and theme marketplaces. |
| Trime | [Trime](https://github.com/osfans/trime) | GPL-3.0 | 4,435 | Chinese: rime-based<br>Theme: advanced<br>Offline: Yes<br>Privacy: high | Best Android choice for serious Chinese Rime users and schema-heavy workflows. |

### Android IME Development Resources

| Name | Source | License | Stars | Signals | Short review |
| --- | --- | --- | ---: | --- | --- |
| Android IME APIs | [Android IME APIs](https://developer.android.com/develop/ui/views/touch-and-input/creating-input-method) | Documentation | N/A | Chinese: none<br>Theme: none<br>Offline: Yes<br>Privacy: high | Start here before copying any existing keyboard architecture. |
| Rime | [Rime](https://github.com/rime/librime) | BSD-3-Clause | 4,463 | Chinese: rime-based<br>Theme: none<br>Offline: Yes<br>Privacy: high | Essential engine reference for Chinese IME developers and Rime-based Android projects. |

## More

- [View the full README and detailed entries](https://github.com/ideas-no996/awesome-android-keyboards)
- [Contribute a keyboard or correction](https://github.com/ideas-no996/awesome-android-keyboards/blob/main/CONTRIBUTING.md)
