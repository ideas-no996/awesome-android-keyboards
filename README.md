# Awesome Android Keyboards

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re) [![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](LICENSE) ![Last Updated](https://img.shields.io/badge/last%20updated-2026--07--06-blue) [![GitHub Stars](https://img.shields.io/github/stars/ideas-no996/awesome-android-keyboards?style=social)](https://github.com/ideas-no996/awesome-android-keyboards/stargazers)

> A curated, maintainable map of Android keyboard and input method ecosystems.

Awesome Android Keyboards is a professional index for the android keyboard ecosystem: Android IME apps, input method engines, privacy keyboard choices, open-source keyboard projects, Rime and Trime front-ends, F-Droid packages, commercial keyboards, developer keyboards, theme systems, and Android InputMethodService resources. It is built for users comparing daily keyboards, developers studying Android IME architecture, Chinese input method users evaluating Rime-based workflows, and maintainers looking for realistic open-source keyboard bases.

The list is intentionally conservative. It does not rank projects by hype, copy marketing text, or treat closed-source claims as implementation facts. Each entry is backed by structured data in YAML, source links, maintenance notes, privacy/network signals, theme suitability, Chinese input support, and a short original review.

Data file: [`data/keyboards.yml`](data/keyboards.yml). Generated from structured data on 2026-07-06.

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
- [Detailed Entries](#detailed-entries)
- [Maintenance](#maintenance)

## Quick Recommendations

- **普通用户推荐:** [Gboard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin), [Microsoft SwiftKey](https://www.microsoft.com/swiftkey), [HeliBoard](https://github.com/Helium314/HeliBoard)
- **隐私优先推荐:** [HeliBoard](https://github.com/Helium314/HeliBoard), [FUTO Keyboard](https://github.com/futo-org/android-keyboard), [FlorisBoard](https://github.com/florisboard/florisboard), [Simple Keyboard](https://github.com/rkkr/simple-keyboard)
- **中文输入推荐:** [Trime](https://github.com/osfans/trime), [Fcitx5 for Android](https://github.com/fcitx5-android/fcitx5-android), [WeChat Keyboard](https://z.weixin.qq.com/), [Sogou IME](https://shurufa.sogou.com/)
- **适合二次开发推荐:** [FlorisBoard](https://github.com/florisboard/florisboard), [HeliBoard](https://github.com/Helium314/HeliBoard), [Simple Keyboard](https://github.com/rkkr/simple-keyboard), [Unexpected Keyboard](https://github.com/Julow/Unexpected-Keyboard)
- **适合 iOS-like 主题改造推荐:** [FlorisBoard](https://github.com/florisboard/florisboard), [HeliBoard](https://github.com/Helium314/HeliBoard), [AnySoftKeyboard](https://github.com/AnySoftKeyboard/AnySoftKeyboard), [Trime](https://github.com/osfans/trime)
- **适合 Glassmorphism 主题改造推荐:** [FlorisBoard](https://github.com/florisboard/florisboard), [HeliBoard](https://github.com/Helium314/HeliBoard), [FUTO Keyboard](https://github.com/futo-org/android-keyboard), [Trime](https://github.com/osfans/trime)

## Categories

The tables stay intentionally compact. Full evaluation fields live in `data/keyboards.yml` and the collapsible detail blocks below.

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
| AnySoftKeyboard | [AnySoftKeyboard](https://github.com/AnySoftKeyboard/AnySoftKeyboard) | Apache-2.0 | 3,330 | Chinese: basic<br>Theme: advanced<br>Offline: Yes<br>Privacy: high | Strong candidate for studying plugin-like language and theme packaging. |
| FlorisBoard | [FlorisBoard](https://github.com/florisboard/florisboard) | Apache-2.0 | 8,452 | Chinese: basic<br>Theme: advanced<br>Offline: Yes<br>Privacy: high | Best candidate for serious UI experiments, Compose-based refactors, and custom themes. |
| HeliBoard | [HeliBoard](https://github.com/Helium314/HeliBoard) | GPL-3.0 | 5,550 | Chinese: basic<br>Theme: good<br>Offline: Yes<br>Privacy: high | Best starting point for privacy-minded users and theme-oriented forks. |
| OpenBoard | [OpenBoard](https://github.com/openboard-team/openboard) | GPL-3.0 | 2,728 | Chinese: basic<br>Theme: basic<br>Offline: Yes<br>Privacy: high | Good reference for minimal offline keyboard behavior, but check maintenance before forking. |
| Simple Keyboard | [Simple Keyboard](https://github.com/rkkr/simple-keyboard) | Apache-2.0 | 1,533 | Chinese: none<br>Theme: basic<br>Offline: Yes<br>Privacy: high | Good for learning Android IME basics or building a deliberately simple fork. |

### Rime-based Keyboards

| Name | Source | License | Stars | Signals | Short review |
| --- | --- | --- | ---: | --- | --- |
| Fcitx5 for Android | [Fcitx5 for Android](https://github.com/fcitx5-android/fcitx5-android) | LGPL-2.1 | 5,398 | Chinese: rime-based<br>Theme: good<br>Offline: Yes<br>Privacy: high | Best reference for bringing desktop IME architecture and Rime support to Android. |
| Trime | [Trime](https://github.com/osfans/trime) | GPL-3.0 | 4,456 | Chinese: rime-based<br>Theme: advanced<br>Offline: Yes<br>Privacy: high | Best Android choice for serious Chinese Rime users and schema-heavy workflows. |

### Privacy-focused Keyboards

| Name | Source | License | Stars | Signals | Short review |
| --- | --- | --- | ---: | --- | --- |
| Fcitx5 for Android | [Fcitx5 for Android](https://github.com/fcitx5-android/fcitx5-android) | LGPL-2.1 | 5,398 | Chinese: rime-based<br>Theme: good<br>Offline: Yes<br>Privacy: high | Best reference for bringing desktop IME architecture and Rime support to Android. |
| FlorisBoard | [FlorisBoard](https://github.com/florisboard/florisboard) | Apache-2.0 | 8,452 | Chinese: basic<br>Theme: advanced<br>Offline: Yes<br>Privacy: high | Best candidate for serious UI experiments, Compose-based refactors, and custom themes. |
| FUTO Keyboard | [FUTO Keyboard](https://github.com/futo-org/android-keyboard) | NOASSERTION | 2,820 | Chinese: basic<br>Theme: good<br>Offline: Yes<br>Privacy: high | Interesting bridge between mainstream prediction quality and privacy-first design. |
| HeliBoard | [HeliBoard](https://github.com/Helium314/HeliBoard) | GPL-3.0 | 5,550 | Chinese: basic<br>Theme: good<br>Offline: Yes<br>Privacy: high | Best starting point for privacy-minded users and theme-oriented forks. |
| Thumb-Key | [Thumb-Key](https://github.com/dessalines/thumb-key) | AGPL-3.0 | 1,496 | Chinese: none<br>Theme: good<br>Offline: Yes<br>Privacy: high | Good reference for alternative mobile typing mechanics and compact UI experiments. |
| Trime | [Trime](https://github.com/osfans/trime) | GPL-3.0 | 4,456 | Chinese: rime-based<br>Theme: advanced<br>Offline: Yes<br>Privacy: high | Best Android choice for serious Chinese Rime users and schema-heavy workflows. |

### AI-assisted Keyboards

| Name | Source | License | Stars | Signals | Short review |
| --- | --- | --- | ---: | --- | --- |
| Baidu IME | [Baidu IME](https://shurufa.baidu.com/) | Proprietary | N/A | Chinese: excellent<br>Theme: advanced<br>Offline: partial<br>Privacy: medium | Worth tracking for Chinese input UX patterns, especially commercial theming and prediction. |
| FUTO Keyboard | [FUTO Keyboard](https://github.com/futo-org/android-keyboard) | NOASSERTION | 2,820 | Chinese: basic<br>Theme: good<br>Offline: Yes<br>Privacy: high | Interesting bridge between mainstream prediction quality and privacy-first design. |
| Microsoft SwiftKey | [Microsoft SwiftKey](https://www.microsoft.com/swiftkey) | Proprietary | N/A | Chinese: good<br>Theme: advanced<br>Offline: partial<br>Privacy: medium | Strong mainstream choice for users who value prediction quality and visual customization. |
| Sogou IME | [Sogou IME](https://shurufa.sogou.com/) | Proprietary | N/A | Chinese: excellent<br>Theme: advanced<br>Offline: partial<br>Privacy: medium | Useful reference point for Chinese commercial keyboard features and theme marketplaces. |

### Developer / Hacker Keyboards

| Name | Source | License | Stars | Signals | Short review |
| --- | --- | --- | ---: | --- | --- |
| Hacker's Keyboard | [Hacker's Keyboard](https://github.com/klausw/hackerskeyboard) | Apache-2.0 | 2,355 | Chinese: none<br>Theme: basic<br>Offline: Yes<br>Privacy: high | Historically important hacker keyboard, but new projects should account for age and maintenance risk. |
| MessageEase | [MessageEase](https://www.exideas.com/ME/) | Proprietary | N/A | Chinese: none<br>Theme: basic<br>Offline: Yes<br>Privacy: medium | Included as a design reference for non-QWERTY mobile input methods. |
| Unexpected Keyboard | [Unexpected Keyboard](https://github.com/Julow/Unexpected-Keyboard) | GPL-3.0 | 3,112 | Chinese: none<br>Theme: good<br>Offline: Yes<br>Privacy: high | Excellent reference for non-mainstream layouts and dense gesture-accessible symbols. |

### Theme and Customization Resources

| Name | Source | License | Stars | Signals | Short review |
| --- | --- | --- | ---: | --- | --- |
| AnySoftKeyboard | [AnySoftKeyboard](https://github.com/AnySoftKeyboard/AnySoftKeyboard) | Apache-2.0 | 3,330 | Chinese: basic<br>Theme: advanced<br>Offline: Yes<br>Privacy: high | Strong candidate for studying plugin-like language and theme packaging. |
| Baidu IME | [Baidu IME](https://shurufa.baidu.com/) | Proprietary | N/A | Chinese: excellent<br>Theme: advanced<br>Offline: partial<br>Privacy: medium | Worth tracking for Chinese input UX patterns, especially commercial theming and prediction. |
| FlorisBoard | [FlorisBoard](https://github.com/florisboard/florisboard) | Apache-2.0 | 8,452 | Chinese: basic<br>Theme: advanced<br>Offline: Yes<br>Privacy: high | Best candidate for serious UI experiments, Compose-based refactors, and custom themes. |
| FUTO Keyboard | [FUTO Keyboard](https://github.com/futo-org/android-keyboard) | NOASSERTION | 2,820 | Chinese: basic<br>Theme: good<br>Offline: Yes<br>Privacy: high | Interesting bridge between mainstream prediction quality and privacy-first design. |
| HeliBoard | [HeliBoard](https://github.com/Helium314/HeliBoard) | GPL-3.0 | 5,550 | Chinese: basic<br>Theme: good<br>Offline: Yes<br>Privacy: high | Best starting point for privacy-minded users and theme-oriented forks. |
| Microsoft SwiftKey | [Microsoft SwiftKey](https://www.microsoft.com/swiftkey) | Proprietary | N/A | Chinese: good<br>Theme: advanced<br>Offline: partial<br>Privacy: medium | Strong mainstream choice for users who value prediction quality and visual customization. |
| Sogou IME | [Sogou IME](https://shurufa.sogou.com/) | Proprietary | N/A | Chinese: excellent<br>Theme: advanced<br>Offline: partial<br>Privacy: medium | Useful reference point for Chinese commercial keyboard features and theme marketplaces. |
| Trime | [Trime](https://github.com/osfans/trime) | GPL-3.0 | 4,456 | Chinese: rime-based<br>Theme: advanced<br>Offline: Yes<br>Privacy: high | Best Android choice for serious Chinese Rime users and schema-heavy workflows. |

### Android IME Development Resources

| Name | Source | License | Stars | Signals | Short review |
| --- | --- | --- | ---: | --- | --- |
| Android IME APIs | [Android IME APIs](https://developer.android.com/develop/ui/views/touch-and-input/creating-input-method) | Documentation | N/A | Chinese: none<br>Theme: none<br>Offline: Yes<br>Privacy: high | Start here before copying any existing keyboard architecture. |
| Rime | [Rime](https://github.com/rime/librime) | BSD-3-Clause | 4,476 | Chinese: rime-based<br>Theme: none<br>Offline: Yes<br>Privacy: high | Essential engine reference for Chinese IME developers and Rime-based Android projects. |

## Detailed Entries

### Commercial Keyboards Entry Details

<details>
<summary><strong>Baidu IME</strong> details</summary>

- **Name:** Baidu IME
- **Repository / Website:** [Website](https://shurufa.baidu.com/)
- **License:** Proprietary
- **Stars:** N/A
- **Last commit:** N/A
- **Last release:** N/A
- **Tech stack:** Proprietary Android IME
- **Chinese support:** excellent
- **Theme system:** advanced
- **Offline support:** partial
- **Privacy:** medium
- **Development feasibility:** low
- **Recommended use case:** Worth tracking for Chinese input UX patterns, especially commercial theming and prediction.
- **Short review:** Feature-rich Chinese IME with a large skin and service ecosystem.
- **Sources:** [Source 1](https://shurufa.baidu.com/)
- **Last verified:** 2026-06-09

</details>

<details>
<summary><strong>Gboard</strong> details</summary>

- **Name:** Gboard
- **Repository / Website:** [Website](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin); [Play Store](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin)
- **License:** Proprietary
- **Stars:** N/A
- **Last commit:** N/A
- **Last release:** N/A
- **Tech stack:** Proprietary Android IME
- **Chinese support:** good
- **Theme system:** good
- **Offline support:** partial
- **Privacy:** medium
- **Development feasibility:** low
- **Recommended use case:** Best baseline recommendation for users who want reliability and broad language support.
- **Short review:** Proprietary mainstream keyboard with strong multilingual coverage.
- **Sources:** [Source 1](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin); [Source 2](https://support.google.com/gboard/)
- **Last verified:** 2026-06-09

</details>

<details>
<summary><strong>Microsoft SwiftKey</strong> details</summary>

- **Name:** Microsoft SwiftKey
- **Repository / Website:** [Website](https://www.microsoft.com/swiftkey); [Play Store](https://play.google.com/store/apps/details?id=com.touchtype.swiftkey)
- **License:** Proprietary
- **Stars:** N/A
- **Last commit:** N/A
- **Last release:** N/A
- **Tech stack:** Proprietary Android IME
- **Chinese support:** good
- **Theme system:** advanced
- **Offline support:** partial
- **Privacy:** medium
- **Development feasibility:** low
- **Recommended use case:** Strong mainstream choice for users who value prediction quality and visual customization.
- **Short review:** Commercial keyboard with mature prediction and rich theme support.
- **Sources:** [Source 1](https://www.microsoft.com/swiftkey); [Source 2](https://play.google.com/store/apps/details?id=com.touchtype.swiftkey)
- **Last verified:** 2026-06-09

</details>

<details>
<summary><strong>Sogou IME</strong> details</summary>

- **Name:** Sogou IME
- **Repository / Website:** [Website](https://shurufa.sogou.com/)
- **License:** Proprietary
- **Stars:** N/A
- **Last commit:** N/A
- **Last release:** N/A
- **Tech stack:** Proprietary Android IME
- **Chinese support:** excellent
- **Theme system:** advanced
- **Offline support:** partial
- **Privacy:** medium
- **Development feasibility:** low
- **Recommended use case:** Useful reference point for Chinese commercial keyboard features and theme marketplaces.
- **Short review:** Long-running Chinese IME with strong phrase prediction and skin culture.
- **Sources:** [Source 1](https://shurufa.sogou.com/)
- **Last verified:** 2026-06-09

</details>

<details>
<summary><strong>WeChat Keyboard</strong> details</summary>

- **Name:** WeChat Keyboard
- **Repository / Website:** [Website](https://z.weixin.qq.com/)
- **License:** Proprietary
- **Stars:** N/A
- **Last commit:** N/A
- **Last release:** N/A
- **Tech stack:** Proprietary Android IME
- **Chinese support:** excellent
- **Theme system:** basic
- **Offline support:** partial
- **Privacy:** medium
- **Development feasibility:** low
- **Recommended use case:** Practical option for Chinese users already living in Tencent services.
- **Short review:** Chinese-first keyboard tied closely to the WeChat ecosystem.
- **Sources:** [Source 1](https://z.weixin.qq.com/)
- **Last verified:** 2026-06-09

</details>

### Open Source Keyboards Entry Details

<details>
<summary><strong>AnySoftKeyboard</strong> details</summary>

- **Name:** AnySoftKeyboard
- **Repository / Website:** [Repository](https://github.com/AnySoftKeyboard/AnySoftKeyboard); [Website](https://anysoftkeyboard.github.io/); [F-Droid](https://f-droid.org/packages/com.menny.android.anysoftkeyboard/); [Play Store](https://play.google.com/store/apps/details?id=com.menny.android.anysoftkeyboard)
- **License:** Apache-2.0
- **Stars:** 3,330
- **Last commit:** 2026-05-17
- **Last release:** 2026-02-08
- **Tech stack:** Kotlin, Java, Android
- **Chinese support:** basic
- **Theme system:** advanced
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** medium
- **Recommended use case:** Strong candidate for studying plugin-like language and theme packaging.
- **Short review:** Mature modular keyboard with language packs and theme infrastructure.
- **Sources:** [Source 1](https://github.com/AnySoftKeyboard/AnySoftKeyboard); [Source 2](https://anysoftkeyboard.github.io/)
- **Last verified:** 2026-07-06

</details>

<details>
<summary><strong>FlorisBoard</strong> details</summary>

- **Name:** FlorisBoard
- **Repository / Website:** [Repository](https://github.com/florisboard/florisboard); [Website](https://florisboard.org/); [F-Droid](https://f-droid.org/packages/dev.patrickgold.florisboard/)
- **License:** Apache-2.0
- **Stars:** 8,452
- **Last commit:** 2026-07-01
- **Last release:** 2025-11-28
- **Tech stack:** Kotlin, Jetpack Compose, Android
- **Chinese support:** basic
- **Theme system:** advanced
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** high
- **Recommended use case:** Best candidate for serious UI experiments, Compose-based refactors, and custom themes.
- **Short review:** Modern open-source keyboard with strong theming direction and active architecture work.
- **Sources:** [Source 1](https://github.com/florisboard/florisboard); [Source 2](https://florisboard.org/)
- **Last verified:** 2026-07-06

</details>

<details>
<summary><strong>HeliBoard</strong> details</summary>

- **Name:** HeliBoard
- **Repository / Website:** [Repository](https://github.com/Helium314/HeliBoard); [F-Droid](https://f-droid.org/packages/helium314.keyboard/)
- **License:** GPL-3.0
- **Stars:** 5,550
- **Last commit:** 2026-07-02
- **Last release:** 2026-03-29
- **Tech stack:** Kotlin, Java, Android
- **Chinese support:** basic
- **Theme system:** good
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** high
- **Recommended use case:** Best starting point for privacy-minded users and theme-oriented forks.
- **Short review:** Active privacy-friendly fork in the LatinIME/OpenBoard lineage.
- **Sources:** [Source 1](https://github.com/Helium314/HeliBoard); [Source 2](https://f-droid.org/packages/helium314.keyboard/)
- **Last verified:** 2026-07-06

</details>

<details>
<summary><strong>OpenBoard</strong> details</summary>

- **Name:** OpenBoard
- **Repository / Website:** [Repository](https://github.com/openboard-team/openboard); [F-Droid](https://f-droid.org/packages/org.dslul.openboard.inputmethod.latin/)
- **License:** GPL-3.0
- **Stars:** 2,728
- **Last commit:** 2022-12-17
- **Last release:** 2022-08-05
- **Tech stack:** Java, Android
- **Chinese support:** basic
- **Theme system:** basic
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** medium
- **Recommended use case:** Good reference for minimal offline keyboard behavior, but check maintenance before forking.
- **Short review:** Clean AOSP-derived keyboard, useful historically and as a simpler code base.
- **Sources:** [Source 1](https://github.com/openboard-team/openboard); [Source 2](https://f-droid.org/packages/org.dslul.openboard.inputmethod.latin/)
- **Last verified:** 2026-07-06

</details>

<details>
<summary><strong>Simple Keyboard</strong> details</summary>

- **Name:** Simple Keyboard
- **Repository / Website:** [Repository](https://github.com/rkkr/simple-keyboard); [F-Droid](https://f-droid.org/packages/rkr.simplekeyboard.inputmethod/); [Play Store](https://play.google.com/store/apps/details?id=rkr.simplekeyboard.inputmethod)
- **License:** Apache-2.0
- **Stars:** 1,533
- **Last commit:** 2026-06-22
- **Last release:** 2026-05-23
- **Tech stack:** Kotlin, Java, Android
- **Chinese support:** none
- **Theme system:** basic
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** high
- **Recommended use case:** Good for learning Android IME basics or building a deliberately simple fork.
- **Short review:** Minimal keyboard with a small scope and few moving parts.
- **Sources:** [Source 1](https://github.com/rkkr/simple-keyboard); [Source 2](https://f-droid.org/packages/rkr.simplekeyboard.inputmethod/)
- **Last verified:** 2026-07-06

</details>

### Rime-based Keyboards Entry Details

<details>
<summary><strong>Fcitx5 for Android</strong> details</summary>

- **Name:** Fcitx5 for Android
- **Repository / Website:** [Repository](https://github.com/fcitx5-android/fcitx5-android); [Website](https://fcitx5-android.github.io/); [F-Droid](https://f-droid.org/packages/org.fcitx.fcitx5.android/)
- **License:** LGPL-2.1
- **Stars:** 5,398
- **Last commit:** 2026-07-04
- **Last release:** 2025-11-01
- **Tech stack:** Kotlin, C++, Fcitx5, Rime
- **Chinese support:** rime-based
- **Theme system:** good
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** medium
- **Recommended use case:** Best reference for bringing desktop IME architecture and Rime support to Android.
- **Short review:** Android port of the Fcitx5 input method framework with addon-oriented design.
- **Sources:** [Source 1](https://github.com/fcitx5-android/fcitx5-android); [Source 2](https://fcitx5-android.github.io/)
- **Last verified:** 2026-07-06

</details>

<details>
<summary><strong>Trime</strong> details</summary>

- **Name:** Trime
- **Repository / Website:** [Repository](https://github.com/osfans/trime); [Website](https://github.com/osfans/trime); [F-Droid](https://f-droid.org/packages/com.osfans.trime/)
- **License:** GPL-3.0
- **Stars:** 4,456
- **Last commit:** 2026-07-06
- **Last release:** 2026-07-01
- **Tech stack:** Kotlin, Java, C++, Rime
- **Chinese support:** rime-based
- **Theme system:** advanced
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** medium
- **Recommended use case:** Best Android choice for serious Chinese Rime users and schema-heavy workflows.
- **Short review:** Android Rime frontend with deep schema and theme customization.
- **Sources:** [Source 1](https://github.com/osfans/trime); [Source 2](https://f-droid.org/packages/com.osfans.trime/)
- **Last verified:** 2026-07-06

</details>

### Privacy-focused Keyboards Entry Details

<details>
<summary><strong>Fcitx5 for Android</strong> details</summary>

- **Name:** Fcitx5 for Android
- **Repository / Website:** [Repository](https://github.com/fcitx5-android/fcitx5-android); [Website](https://fcitx5-android.github.io/); [F-Droid](https://f-droid.org/packages/org.fcitx.fcitx5.android/)
- **License:** LGPL-2.1
- **Stars:** 5,398
- **Last commit:** 2026-07-04
- **Last release:** 2025-11-01
- **Tech stack:** Kotlin, C++, Fcitx5, Rime
- **Chinese support:** rime-based
- **Theme system:** good
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** medium
- **Recommended use case:** Best reference for bringing desktop IME architecture and Rime support to Android.
- **Short review:** Android port of the Fcitx5 input method framework with addon-oriented design.
- **Sources:** [Source 1](https://github.com/fcitx5-android/fcitx5-android); [Source 2](https://fcitx5-android.github.io/)
- **Last verified:** 2026-07-06

</details>

<details>
<summary><strong>FlorisBoard</strong> details</summary>

- **Name:** FlorisBoard
- **Repository / Website:** [Repository](https://github.com/florisboard/florisboard); [Website](https://florisboard.org/); [F-Droid](https://f-droid.org/packages/dev.patrickgold.florisboard/)
- **License:** Apache-2.0
- **Stars:** 8,452
- **Last commit:** 2026-07-01
- **Last release:** 2025-11-28
- **Tech stack:** Kotlin, Jetpack Compose, Android
- **Chinese support:** basic
- **Theme system:** advanced
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** high
- **Recommended use case:** Best candidate for serious UI experiments, Compose-based refactors, and custom themes.
- **Short review:** Modern open-source keyboard with strong theming direction and active architecture work.
- **Sources:** [Source 1](https://github.com/florisboard/florisboard); [Source 2](https://florisboard.org/)
- **Last verified:** 2026-07-06

</details>

<details>
<summary><strong>FUTO Keyboard</strong> details</summary>

- **Name:** FUTO Keyboard
- **Repository / Website:** [Repository](https://github.com/futo-org/android-keyboard); [Website](https://keyboard.futo.org/); [Play Store](https://play.google.com/store/apps/details?id=org.futo.inputmethod.latin)
- **License:** NOASSERTION
- **Stars:** 2,820
- **Last commit:** 2026-07-02
- **Last release:** 2026-06-22
- **Tech stack:** Kotlin, Java, Android
- **Chinese support:** basic
- **Theme system:** good
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** medium
- **Recommended use case:** Interesting bridge between mainstream prediction quality and privacy-first design.
- **Short review:** Privacy-oriented keyboard with local-first ambitions and richer prediction features.
- **Sources:** [Source 1](https://github.com/futo-org/android-keyboard); [Source 2](https://keyboard.futo.org/)
- **Last verified:** 2026-07-06

</details>

<details>
<summary><strong>HeliBoard</strong> details</summary>

- **Name:** HeliBoard
- **Repository / Website:** [Repository](https://github.com/Helium314/HeliBoard); [F-Droid](https://f-droid.org/packages/helium314.keyboard/)
- **License:** GPL-3.0
- **Stars:** 5,550
- **Last commit:** 2026-07-02
- **Last release:** 2026-03-29
- **Tech stack:** Kotlin, Java, Android
- **Chinese support:** basic
- **Theme system:** good
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** high
- **Recommended use case:** Best starting point for privacy-minded users and theme-oriented forks.
- **Short review:** Active privacy-friendly fork in the LatinIME/OpenBoard lineage.
- **Sources:** [Source 1](https://github.com/Helium314/HeliBoard); [Source 2](https://f-droid.org/packages/helium314.keyboard/)
- **Last verified:** 2026-07-06

</details>

<details>
<summary><strong>Thumb-Key</strong> details</summary>

- **Name:** Thumb-Key
- **Repository / Website:** [Repository](https://github.com/dessalines/thumb-key); [F-Droid](https://f-droid.org/packages/com.dessalines.thumbkey/); [Play Store](https://play.google.com/store/apps/details?id=com.dessalines.thumbkey)
- **License:** AGPL-3.0
- **Stars:** 1,496
- **Last commit:** 2026-07-05
- **Last release:** 2026-07-04
- **Tech stack:** Kotlin, Jetpack Compose, Android
- **Chinese support:** none
- **Theme system:** good
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** high
- **Recommended use case:** Good reference for alternative mobile typing mechanics and compact UI experiments.
- **Short review:** Thumb-oriented keyboard inspired by compact gesture-based layouts.
- **Sources:** [Source 1](https://github.com/dessalines/thumb-key); [Source 2](https://f-droid.org/packages/com.dessalines.thumbkey/)
- **Last verified:** 2026-07-06

</details>

<details>
<summary><strong>Trime</strong> details</summary>

- **Name:** Trime
- **Repository / Website:** [Repository](https://github.com/osfans/trime); [Website](https://github.com/osfans/trime); [F-Droid](https://f-droid.org/packages/com.osfans.trime/)
- **License:** GPL-3.0
- **Stars:** 4,456
- **Last commit:** 2026-07-06
- **Last release:** 2026-07-01
- **Tech stack:** Kotlin, Java, C++, Rime
- **Chinese support:** rime-based
- **Theme system:** advanced
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** medium
- **Recommended use case:** Best Android choice for serious Chinese Rime users and schema-heavy workflows.
- **Short review:** Android Rime frontend with deep schema and theme customization.
- **Sources:** [Source 1](https://github.com/osfans/trime); [Source 2](https://f-droid.org/packages/com.osfans.trime/)
- **Last verified:** 2026-07-06

</details>

### AI-assisted Keyboards Entry Details

<details>
<summary><strong>Baidu IME</strong> details</summary>

- **Name:** Baidu IME
- **Repository / Website:** [Website](https://shurufa.baidu.com/)
- **License:** Proprietary
- **Stars:** N/A
- **Last commit:** N/A
- **Last release:** N/A
- **Tech stack:** Proprietary Android IME
- **Chinese support:** excellent
- **Theme system:** advanced
- **Offline support:** partial
- **Privacy:** medium
- **Development feasibility:** low
- **Recommended use case:** Worth tracking for Chinese input UX patterns, especially commercial theming and prediction.
- **Short review:** Feature-rich Chinese IME with a large skin and service ecosystem.
- **Sources:** [Source 1](https://shurufa.baidu.com/)
- **Last verified:** 2026-06-09

</details>

<details>
<summary><strong>FUTO Keyboard</strong> details</summary>

- **Name:** FUTO Keyboard
- **Repository / Website:** [Repository](https://github.com/futo-org/android-keyboard); [Website](https://keyboard.futo.org/); [Play Store](https://play.google.com/store/apps/details?id=org.futo.inputmethod.latin)
- **License:** NOASSERTION
- **Stars:** 2,820
- **Last commit:** 2026-07-02
- **Last release:** 2026-06-22
- **Tech stack:** Kotlin, Java, Android
- **Chinese support:** basic
- **Theme system:** good
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** medium
- **Recommended use case:** Interesting bridge between mainstream prediction quality and privacy-first design.
- **Short review:** Privacy-oriented keyboard with local-first ambitions and richer prediction features.
- **Sources:** [Source 1](https://github.com/futo-org/android-keyboard); [Source 2](https://keyboard.futo.org/)
- **Last verified:** 2026-07-06

</details>

<details>
<summary><strong>Microsoft SwiftKey</strong> details</summary>

- **Name:** Microsoft SwiftKey
- **Repository / Website:** [Website](https://www.microsoft.com/swiftkey); [Play Store](https://play.google.com/store/apps/details?id=com.touchtype.swiftkey)
- **License:** Proprietary
- **Stars:** N/A
- **Last commit:** N/A
- **Last release:** N/A
- **Tech stack:** Proprietary Android IME
- **Chinese support:** good
- **Theme system:** advanced
- **Offline support:** partial
- **Privacy:** medium
- **Development feasibility:** low
- **Recommended use case:** Strong mainstream choice for users who value prediction quality and visual customization.
- **Short review:** Commercial keyboard with mature prediction and rich theme support.
- **Sources:** [Source 1](https://www.microsoft.com/swiftkey); [Source 2](https://play.google.com/store/apps/details?id=com.touchtype.swiftkey)
- **Last verified:** 2026-06-09

</details>

<details>
<summary><strong>Sogou IME</strong> details</summary>

- **Name:** Sogou IME
- **Repository / Website:** [Website](https://shurufa.sogou.com/)
- **License:** Proprietary
- **Stars:** N/A
- **Last commit:** N/A
- **Last release:** N/A
- **Tech stack:** Proprietary Android IME
- **Chinese support:** excellent
- **Theme system:** advanced
- **Offline support:** partial
- **Privacy:** medium
- **Development feasibility:** low
- **Recommended use case:** Useful reference point for Chinese commercial keyboard features and theme marketplaces.
- **Short review:** Long-running Chinese IME with strong phrase prediction and skin culture.
- **Sources:** [Source 1](https://shurufa.sogou.com/)
- **Last verified:** 2026-06-09

</details>

### Developer / Hacker Keyboards Entry Details

<details>
<summary><strong>Hacker's Keyboard</strong> details</summary>

- **Name:** Hacker's Keyboard
- **Repository / Website:** [Repository](https://github.com/klausw/hackerskeyboard); [Website](https://code.google.com/archive/p/hackerskeyboard/); [F-Droid](https://f-droid.org/packages/org.pocketworkstation.pckeyboard/); [Play Store](https://play.google.com/store/apps/details?id=org.pocketworkstation.pckeyboard)
- **License:** Apache-2.0
- **Stars:** 2,355
- **Last commit:** 2024-10-09
- **Last release:** 2018-11-26
- **Tech stack:** Java, Android
- **Chinese support:** none
- **Theme system:** basic
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** medium
- **Recommended use case:** Historically important hacker keyboard, but new projects should account for age and maintenance risk.
- **Short review:** Classic five-row keyboard for terminal and remote-desktop workflows.
- **Sources:** [Source 1](https://github.com/klausw/hackerskeyboard); [Source 2](https://f-droid.org/packages/org.pocketworkstation.pckeyboard/)
- **Last verified:** 2026-07-06

</details>

<details>
<summary><strong>MessageEase</strong> details</summary>

- **Name:** MessageEase
- **Repository / Website:** [Website](https://www.exideas.com/ME/)
- **License:** Proprietary
- **Stars:** N/A
- **Last commit:** N/A
- **Last release:** N/A
- **Tech stack:** Proprietary Android IME
- **Chinese support:** none
- **Theme system:** basic
- **Offline support:** Yes
- **Privacy:** medium
- **Development feasibility:** low
- **Recommended use case:** Included as a design reference for non-QWERTY mobile input methods.
- **Short review:** Alternative one-finger keyboard layout with historical design value.
- **Sources:** [Source 1](https://www.exideas.com/ME/)
- **Last verified:** 2026-06-09

</details>

<details>
<summary><strong>Unexpected Keyboard</strong> details</summary>

- **Name:** Unexpected Keyboard
- **Repository / Website:** [Repository](https://github.com/Julow/Unexpected-Keyboard); [F-Droid](https://f-droid.org/packages/juloo.keyboard2/); [Play Store](https://play.google.com/store/apps/details?id=juloo.keyboard2)
- **License:** GPL-3.0
- **Stars:** 3,112
- **Last commit:** 2026-07-04
- **Last release:** 2026-05-24
- **Tech stack:** Kotlin, Java, Android
- **Chinese support:** none
- **Theme system:** good
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** high
- **Recommended use case:** Excellent reference for non-mainstream layouts and dense gesture-accessible symbols.
- **Short review:** Symbol-heavy keyboard optimized for programmers, terminals, and power users.
- **Sources:** [Source 1](https://github.com/Julow/Unexpected-Keyboard); [Source 2](https://f-droid.org/packages/juloo.keyboard2/)
- **Last verified:** 2026-07-06

</details>

### Theme and Customization Resources Entry Details

<details>
<summary><strong>AnySoftKeyboard</strong> details</summary>

- **Name:** AnySoftKeyboard
- **Repository / Website:** [Repository](https://github.com/AnySoftKeyboard/AnySoftKeyboard); [Website](https://anysoftkeyboard.github.io/); [F-Droid](https://f-droid.org/packages/com.menny.android.anysoftkeyboard/); [Play Store](https://play.google.com/store/apps/details?id=com.menny.android.anysoftkeyboard)
- **License:** Apache-2.0
- **Stars:** 3,330
- **Last commit:** 2026-05-17
- **Last release:** 2026-02-08
- **Tech stack:** Kotlin, Java, Android
- **Chinese support:** basic
- **Theme system:** advanced
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** medium
- **Recommended use case:** Strong candidate for studying plugin-like language and theme packaging.
- **Short review:** Mature modular keyboard with language packs and theme infrastructure.
- **Sources:** [Source 1](https://github.com/AnySoftKeyboard/AnySoftKeyboard); [Source 2](https://anysoftkeyboard.github.io/)
- **Last verified:** 2026-07-06

</details>

<details>
<summary><strong>Baidu IME</strong> details</summary>

- **Name:** Baidu IME
- **Repository / Website:** [Website](https://shurufa.baidu.com/)
- **License:** Proprietary
- **Stars:** N/A
- **Last commit:** N/A
- **Last release:** N/A
- **Tech stack:** Proprietary Android IME
- **Chinese support:** excellent
- **Theme system:** advanced
- **Offline support:** partial
- **Privacy:** medium
- **Development feasibility:** low
- **Recommended use case:** Worth tracking for Chinese input UX patterns, especially commercial theming and prediction.
- **Short review:** Feature-rich Chinese IME with a large skin and service ecosystem.
- **Sources:** [Source 1](https://shurufa.baidu.com/)
- **Last verified:** 2026-06-09

</details>

<details>
<summary><strong>FlorisBoard</strong> details</summary>

- **Name:** FlorisBoard
- **Repository / Website:** [Repository](https://github.com/florisboard/florisboard); [Website](https://florisboard.org/); [F-Droid](https://f-droid.org/packages/dev.patrickgold.florisboard/)
- **License:** Apache-2.0
- **Stars:** 8,452
- **Last commit:** 2026-07-01
- **Last release:** 2025-11-28
- **Tech stack:** Kotlin, Jetpack Compose, Android
- **Chinese support:** basic
- **Theme system:** advanced
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** high
- **Recommended use case:** Best candidate for serious UI experiments, Compose-based refactors, and custom themes.
- **Short review:** Modern open-source keyboard with strong theming direction and active architecture work.
- **Sources:** [Source 1](https://github.com/florisboard/florisboard); [Source 2](https://florisboard.org/)
- **Last verified:** 2026-07-06

</details>

<details>
<summary><strong>FUTO Keyboard</strong> details</summary>

- **Name:** FUTO Keyboard
- **Repository / Website:** [Repository](https://github.com/futo-org/android-keyboard); [Website](https://keyboard.futo.org/); [Play Store](https://play.google.com/store/apps/details?id=org.futo.inputmethod.latin)
- **License:** NOASSERTION
- **Stars:** 2,820
- **Last commit:** 2026-07-02
- **Last release:** 2026-06-22
- **Tech stack:** Kotlin, Java, Android
- **Chinese support:** basic
- **Theme system:** good
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** medium
- **Recommended use case:** Interesting bridge between mainstream prediction quality and privacy-first design.
- **Short review:** Privacy-oriented keyboard with local-first ambitions and richer prediction features.
- **Sources:** [Source 1](https://github.com/futo-org/android-keyboard); [Source 2](https://keyboard.futo.org/)
- **Last verified:** 2026-07-06

</details>

<details>
<summary><strong>HeliBoard</strong> details</summary>

- **Name:** HeliBoard
- **Repository / Website:** [Repository](https://github.com/Helium314/HeliBoard); [F-Droid](https://f-droid.org/packages/helium314.keyboard/)
- **License:** GPL-3.0
- **Stars:** 5,550
- **Last commit:** 2026-07-02
- **Last release:** 2026-03-29
- **Tech stack:** Kotlin, Java, Android
- **Chinese support:** basic
- **Theme system:** good
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** high
- **Recommended use case:** Best starting point for privacy-minded users and theme-oriented forks.
- **Short review:** Active privacy-friendly fork in the LatinIME/OpenBoard lineage.
- **Sources:** [Source 1](https://github.com/Helium314/HeliBoard); [Source 2](https://f-droid.org/packages/helium314.keyboard/)
- **Last verified:** 2026-07-06

</details>

<details>
<summary><strong>Microsoft SwiftKey</strong> details</summary>

- **Name:** Microsoft SwiftKey
- **Repository / Website:** [Website](https://www.microsoft.com/swiftkey); [Play Store](https://play.google.com/store/apps/details?id=com.touchtype.swiftkey)
- **License:** Proprietary
- **Stars:** N/A
- **Last commit:** N/A
- **Last release:** N/A
- **Tech stack:** Proprietary Android IME
- **Chinese support:** good
- **Theme system:** advanced
- **Offline support:** partial
- **Privacy:** medium
- **Development feasibility:** low
- **Recommended use case:** Strong mainstream choice for users who value prediction quality and visual customization.
- **Short review:** Commercial keyboard with mature prediction and rich theme support.
- **Sources:** [Source 1](https://www.microsoft.com/swiftkey); [Source 2](https://play.google.com/store/apps/details?id=com.touchtype.swiftkey)
- **Last verified:** 2026-06-09

</details>

<details>
<summary><strong>Sogou IME</strong> details</summary>

- **Name:** Sogou IME
- **Repository / Website:** [Website](https://shurufa.sogou.com/)
- **License:** Proprietary
- **Stars:** N/A
- **Last commit:** N/A
- **Last release:** N/A
- **Tech stack:** Proprietary Android IME
- **Chinese support:** excellent
- **Theme system:** advanced
- **Offline support:** partial
- **Privacy:** medium
- **Development feasibility:** low
- **Recommended use case:** Useful reference point for Chinese commercial keyboard features and theme marketplaces.
- **Short review:** Long-running Chinese IME with strong phrase prediction and skin culture.
- **Sources:** [Source 1](https://shurufa.sogou.com/)
- **Last verified:** 2026-06-09

</details>

<details>
<summary><strong>Trime</strong> details</summary>

- **Name:** Trime
- **Repository / Website:** [Repository](https://github.com/osfans/trime); [Website](https://github.com/osfans/trime); [F-Droid](https://f-droid.org/packages/com.osfans.trime/)
- **License:** GPL-3.0
- **Stars:** 4,456
- **Last commit:** 2026-07-06
- **Last release:** 2026-07-01
- **Tech stack:** Kotlin, Java, C++, Rime
- **Chinese support:** rime-based
- **Theme system:** advanced
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** medium
- **Recommended use case:** Best Android choice for serious Chinese Rime users and schema-heavy workflows.
- **Short review:** Android Rime frontend with deep schema and theme customization.
- **Sources:** [Source 1](https://github.com/osfans/trime); [Source 2](https://f-droid.org/packages/com.osfans.trime/)
- **Last verified:** 2026-07-06

</details>

### Android IME Development Resources Entry Details

<details>
<summary><strong>Android IME APIs</strong> details</summary>

- **Name:** Android IME APIs
- **Repository / Website:** [Website](https://developer.android.com/develop/ui/views/touch-and-input/creating-input-method)
- **License:** Documentation
- **Stars:** N/A
- **Last commit:** N/A
- **Last release:** N/A
- **Tech stack:** Android SDK, InputMethodService
- **Chinese support:** none
- **Theme system:** none
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** high
- **Recommended use case:** Start here before copying any existing keyboard architecture.
- **Short review:** Official Android documentation for building custom input methods.
- **Sources:** [Source 1](https://developer.android.com/develop/ui/views/touch-and-input/creating-input-method); [Source 2](https://developer.android.com/reference/android/inputmethodservice/InputMethodService)
- **Last verified:** 2026-06-09

</details>

<details>
<summary><strong>Rime</strong> details</summary>

- **Name:** Rime
- **Repository / Website:** [Repository](https://github.com/rime/librime); [Website](https://rime.im/)
- **License:** BSD-3-Clause
- **Stars:** 4,476
- **Last commit:** 2026-07-04
- **Last release:** 2026-06-06
- **Tech stack:** C++, Rime schemas
- **Chinese support:** rime-based
- **Theme system:** none
- **Offline support:** Yes
- **Privacy:** high
- **Development feasibility:** medium
- **Recommended use case:** Essential engine reference for Chinese IME developers and Rime-based Android projects.
- **Short review:** Cross-platform input engine powering many Chinese schema-based IMEs.
- **Sources:** [Source 1](https://github.com/rime/librime); [Source 2](https://rime.im/)
- **Last verified:** 2026-07-06

</details>

## Maintenance

- Update GitHub stats with `python scripts/update_github_stats.py`.
- Regenerate this README with `python scripts/generate_readme.py`.
- Use `GITHUB_TOKEN` for higher GitHub API limits; never commit tokens.
- See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`docs/evaluation-criteria.md`](docs/evaluation-criteria.md) before adding entries.

## License

Released under CC0-1.0. See [`LICENSE`](LICENSE).
