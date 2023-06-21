In other languages: **English (WIP)**, [Русский](README.ru.md)

# Compose Table for Cyrillic Alphabets #

<p align="right">
<i>Every time a user is forced to switch input languages,</br>
God kills a kitten. Stop the slaughter!</i>
</p>

- [Introduction](#introduction)
- [Installation](#installation)
	- [Windows](#windows)
	- [Linux](#linux)
- [Usage](#usage)
- [List of sequences](#list-of-sequences)
- [Related projects](#related-projects)
- [Important information](#important-information)
- [License](#license)

## Introduction ##

This project is a table of [compose sequences](https://en.wikipedia.org/wiki/Compose_key) for Cyrillic alphabets, which allows to input hundreds of letters without installing several layouts.

It works as follows: say, your keyboard lacks letter Ғ (Cyrillic Г with stroke). So, to type it, press <kbd>⎄ Compose</kbd> <kbd>Г</kbd> <kbd>-</kbd>. The <kbd>⎄ Compose</kbd> key, which initiates the sequence, can be mapped to <kbd>Caps Lock</kbd>, right <kbd>Alt</kbd>, or any other key, whichever fits your typing habits. No key holding needed.

Default compose table in `en_US.UTF-8` and other layouts comprises mostly Latin letters, with some Greek, Cyrillic, and special symbols. This project greatly expands the coverage of Cyrillic letters, making it possible to type in many Cyrillic languages using standard keyboards and layout.

More information about compose input is available in [Wikipedia](https://en.wikipedia.org/wiki/Compose_key). List of default combos in `en_US.UTF-8` layout (included in most Linux distributions and WinCompose app) can be seen [here](https://gitlab.freedesktop.org/xorg/lib/libx11/-/blob/master/nls/en_US.UTF-8/Compose.pre). It has sequences for many useful symbols (proper typographic quotes and dashes, diacritic marks, math symbols, etc.)

## Installation ##

### Windows ###

1. Install [WinCompose](https://github.com/samhocevar/wincompose).
2. Download [`.XCompose`](/.XCompose) file.
3. Save it into the user profile folder (usually `C:\Users\user_name\`).
4. Restart WinCompose.
5. Redefine the compose key in the app settings, if needed (right <kbd>Alt</kbd> by default).

### Linux ###

1. Download [`.XCompose`](/.XCompose) file ("show hidden files" must be on).
2. Save it into the user home folder (usually `/home/user_name/`); if you have a custom `.XCompose` file there, append the contents of the downloaded file.
3. Choose the compose key (for example, in GNOME it is in `Settings > Keyboard > Special characters entry > Compose Key`).
4. Restart your text editor/app.

## Usage ##

TODO

## List of sequences ##

<details><summary>Expand</summary>

| Input                                                       | Letter |
| ----------------------------------------------------------- | ------ |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>г</kbd>              | ѕ      |
| <kbd>⎄ Compose</kbd> <kbd>с</kbd> <kbd>5</kbd>              | ѕ      |
| <kbd>⎄ Compose</kbd> <kbd>5</kbd> <kbd>с</kbd>              | ѕ      |
| <kbd>⎄ Compose</kbd> <kbd>е</kbd> <kbd>е</kbd>              | ә      |
| <kbd>⎄ Compose</kbd> <kbd>ё</kbd> <kbd>ё</kbd>              | ӛ      |
| <kbd>⎄ Compose</kbd> <kbd>з</kbd> <kbd>з</kbd>              | ԑ      |
| <kbd>⎄ Compose</kbd> <kbd>м</kbd> <kbd>м</kbd>              | ԝ      |
| <kbd>⎄ Compose</kbd> <kbd>у</kbd> <kbd>у</kbd>              | ү      |
| <kbd>⎄ Compose</kbd> <kbd>ц</kbd> <kbd>ц</kbd>              | џ      |
| <kbd>⎄ Compose</kbd> <kbd>ч</kbd> <kbd>ч</kbd>              | һ      |
| <kbd>⎄ Compose</kbd> <kbd>э</kbd> <kbd>э</kbd>              | є      |
| <kbd>⎄ Compose</kbd> <kbd>є</kbd> <kbd>є</kbd>              | э      |
| <kbd>⎄ Compose</kbd> <kbd>з</kbd> <kbd>3</kbd>              | ӡ      |
| <kbd>⎄ Compose</kbd> <kbd>3</kbd> <kbd>з</kbd>              | ӡ      |
| <kbd>⎄ Compose</kbd> <kbd>о</kbd> <kbd>о</kbd>              | ҩ      |
| <kbd>⎄ Compose</kbd> <kbd>с</kbd> <kbd>о</kbd>              | ҩ      |
| <kbd>⎄ Compose</kbd> <kbd>с</kbd> <kbd>0</kbd>              | ҩ      |
| <kbd>⎄ Compose</kbd> <kbd>0</kbd> <kbd>с</kbd>              | ҩ      |
| <kbd>⎄ Compose</kbd> <kbd>о</kbd> <kbd>0</kbd>              | ҩ      |
| <kbd>⎄ Compose</kbd> <kbd>0</kbd> <kbd>о</kbd>              | ҩ      |
| **Ligatures**                                               |        |
| <kbd>⎄ Compose</kbd> <kbd>а</kbd> <kbd>е</kbd>              | ӕ      |
| <kbd>⎄ Compose</kbd> <kbd>л</kbd> <kbd>ь</kbd>              | љ      |
| <kbd>⎄ Compose</kbd> <kbd>н</kbd> <kbd>г</kbd>              | ҥ      |
| <kbd>⎄ Compose</kbd> <kbd>н</kbd> <kbd>ь</kbd>              | њ      |
| <kbd>⎄ Compose</kbd> <kbd>т</kbd> <kbd>ц</kbd>              | ҵ      |
| **Digraphs**                                                |        |
| <kbd>⎄ Compose</kbd> <kbd>ь</kbd> <kbd>і</kbd>              | ы      |
| <kbd>⎄ Compose</kbd> <kbd>ъ</kbd> <kbd>і</kbd>              | ы      |
| <kbd>⎄ Compose</kbd> <kbd>ь</kbd> <kbd>\|</kbd>             | ы      |
| <kbd>⎄ Compose</kbd> <kbd>ъ</kbd> <kbd>\|</kbd>             | ы      |
| <kbd>⎄ Compose</kbd> <kbd>ь</kbd> <kbd>1</kbd>              | ы      |
| <kbd>⎄ Compose</kbd> <kbd>ъ</kbd> <kbd>1</kbd>              | ы      |
| <kbd>⎄ Compose</kbd> <kbd>¨</kbd> <kbd>ь</kbd> <kbd>і</kbd> | ӹ      |
| <kbd>⎄ Compose</kbd> <kbd>¨</kbd> <kbd>ъ</kbd> <kbd>і</kbd> | ӹ      |
| <kbd>⎄ Compose</kbd> <kbd>"</kbd> <kbd>ь</kbd> <kbd>і</kbd> | ӹ      |
| <kbd>⎄ Compose</kbd> <kbd>"</kbd> <kbd>ъ</kbd> <kbd>і</kbd> | ӹ      |
| <kbd>⎄ Compose</kbd> <kbd>а</kbd> <kbd>\|</kbd>             | аӀ     |
| <kbd>⎄ Compose</kbd> <kbd>а</kbd> <kbd>1</kbd>              | аӀ     |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>\|</kbd>             | гӀ     |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>1</kbd>              | гӀ     |
| <kbd>⎄ Compose</kbd> <kbd>к</kbd> <kbd>\|</kbd>             | кӀ     |
| <kbd>⎄ Compose</kbd> <kbd>к</kbd> <kbd>1</kbd>              | кӀ     |
| <kbd>⎄ Compose</kbd> <kbd>л</kbd> <kbd>\|</kbd>             | лІ     |
| <kbd>⎄ Compose</kbd> <kbd>л</kbd> <kbd>1</kbd>              | лІ     |
| <kbd>⎄ Compose</kbd> <kbd>о</kbd> <kbd>\|</kbd>             | оӀ     |
| <kbd>⎄ Compose</kbd> <kbd>о</kbd> <kbd>1</kbd>              | оӀ     |
| <kbd>⎄ Compose</kbd> <kbd>п</kbd> <kbd>\|</kbd>             | пӀ     |
| <kbd>⎄ Compose</kbd> <kbd>п</kbd> <kbd>1</kbd>              | пӀ     |
| <kbd>⎄ Compose</kbd> <kbd>т</kbd> <kbd>\|</kbd>             | тӀ     |
| <kbd>⎄ Compose</kbd> <kbd>т</kbd> <kbd>1</kbd>              | тӀ     |
| <kbd>⎄ Compose</kbd> <kbd>у</kbd> <kbd>\|</kbd>             | уӀ     |
| <kbd>⎄ Compose</kbd> <kbd>у</kbd> <kbd>1</kbd>              | уӀ     |
| <kbd>⎄ Compose</kbd> <kbd>ф</kbd> <kbd>\|</kbd>             | фӀ     |
| <kbd>⎄ Compose</kbd> <kbd>ф</kbd> <kbd>1</kbd>              | фӀ     |
| <kbd>⎄ Compose</kbd> <kbd>х</kbd> <kbd>\|</kbd>             | хӀ     |
| <kbd>⎄ Compose</kbd> <kbd>х</kbd> <kbd>1</kbd>              | хӀ     |
| <kbd>⎄ Compose</kbd> <kbd>ц</kbd> <kbd>\|</kbd>             | цӀ     |
| <kbd>⎄ Compose</kbd> <kbd>ц</kbd> <kbd>1</kbd>              | цӀ     |
| <kbd>⎄ Compose</kbd> <kbd>ч</kbd> <kbd>\|</kbd>             | чӀ     |
| <kbd>⎄ Compose</kbd> <kbd>ч</kbd> <kbd>1</kbd>              | чӀ     |
| <kbd>⎄ Compose</kbd> <kbd>ш</kbd> <kbd>\|</kbd>             | шІ     |
| <kbd>⎄ Compose</kbd> <kbd>ш</kbd> <kbd>1</kbd>              | шІ     |
| <kbd>⎄ Compose</kbd> <kbd>щ</kbd> <kbd>\|</kbd>             | щІ     |
| <kbd>⎄ Compose</kbd> <kbd>щ</kbd> <kbd>1</kbd>              | щІ     |
| <kbd>⎄ Compose</kbd> <kbd>ы</kbd> <kbd>\|</kbd>             | ыӀ     |
| <kbd>⎄ Compose</kbd> <kbd>ы</kbd> <kbd>1</kbd>              | ыӀ     |
| <kbd>⎄ Compose</kbd> <kbd>\|</kbd> <kbd>У</kbd>             | Іу     |
| <kbd>⎄ Compose</kbd> <kbd>1</kbd> <kbd>У</kbd>              | Іу     |
| <kbd>⎄ Compose</kbd> <kbd>\|</kbd> <kbd>у</kbd>             | Іу     |
| <kbd>⎄ Compose</kbd> <kbd>1</kbd> <kbd>у</kbd>              | Іу     |
| **Palochka**                                                |        |
| <kbd>⎄ Compose</kbd> <kbd>˙</kbd> <kbd>і</kbd>              | Ӏ      |
| <kbd>⎄ Compose</kbd> <kbd>і</kbd> <kbd>˙</kbd>              | Ӏ      |
| <kbd>⎄ Compose</kbd> <kbd>.</kbd> <kbd>і</kbd>              | Ӏ      |
| <kbd>⎄ Compose</kbd> <kbd>і</kbd> <kbd>.</kbd>              | Ӏ      |
| <kbd>⎄ Compose</kbd> <kbd>ь</kbd> <kbd>ы</kbd>              | Ӏ      |
| <kbd>⎄ Compose</kbd> <kbd>ъ</kbd> <kbd>ы</kbd>              | Ӏ      |
| <kbd>⎄ Compose</kbd> <kbd>ы</kbd> <kbd>ь</kbd>              | Ӏ      |
| <kbd>⎄ Compose</kbd> <kbd>ы</kbd> <kbd>ъ</kbd>              | Ӏ      |
| **Letters with dot[s] above, based on и & й**               |        |
| <kbd>⎄ Compose</kbd> <kbd>˙</kbd> <kbd>и</kbd>              | і      |
| <kbd>⎄ Compose</kbd> <kbd>и</kbd> <kbd>˙</kbd>              | і      |
| <kbd>⎄ Compose</kbd> <kbd>.</kbd> <kbd>и</kbd>              | і      |
| <kbd>⎄ Compose</kbd> <kbd>и</kbd> <kbd>.</kbd>              | і      |
| <kbd>⎄ Compose</kbd> <kbd>¨</kbd> <kbd>й</kbd>              | ї      |
| <kbd>⎄ Compose</kbd> <kbd>й</kbd> <kbd>¨</kbd>              | ї      |
| <kbd>⎄ Compose</kbd> <kbd>"</kbd> <kbd>й</kbd>              | ї      |
| <kbd>⎄ Compose</kbd> <kbd>й</kbd> <kbd>"</kbd>              | ї      |
| <kbd>⎄ Compose</kbd> <kbd>˙</kbd> <kbd>й</kbd>              | ј      |
| <kbd>⎄ Compose</kbd> <kbd>й</kbd> <kbd>˙</kbd>              | ј      |
| <kbd>⎄ Compose</kbd> <kbd>.</kbd> <kbd>й</kbd>              | ј      |
| <kbd>⎄ Compose</kbd> <kbd>й</kbd> <kbd>.</kbd>              | ј      |
| **Letters with vertical strokes**                           |        |
| <kbd>⎄ Compose</kbd> <kbd>\|</kbd> <kbd>к</kbd>             | ҝ      |
| <kbd>⎄ Compose</kbd> <kbd>1</kbd> <kbd>к</kbd>              | ҝ      |
| <kbd>⎄ Compose</kbd> <kbd>\|</kbd> <kbd>ч</kbd>             | ҹ      |
| <kbd>⎄ Compose</kbd> <kbd>1</kbd> <kbd>ч</kbd>              | ҹ      |
| **Letters with horizontal strokes**                         |        |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>о</kbd>              | ө      |
| <kbd>⎄ Compose</kbd> <kbd>о</kbd> <kbd>-</kbd>              | ө      |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>г</kbd>              | ғ      |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>-</kbd>              | ғ      |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>к</kbd>              | ҟ      |
| <kbd>⎄ Compose</kbd> <kbd>к</kbd> <kbd>-</kbd>              | ҟ      |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>ү</kbd>              | ұ      |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>у</kbd>              | ұ      |
| <kbd>⎄ Compose</kbd> <kbd>ү</kbd> <kbd>-</kbd>              | ұ      |
| <kbd>⎄ Compose</kbd> <kbd>у</kbd> <kbd>-</kbd>              | ұ      |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>х</kbd>              | ӿ      |
| <kbd>⎄ Compose</kbd> <kbd>х</kbd> <kbd>-</kbd>              | ӿ      |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>е</kbd>              | ҽ      |
| <kbd>⎄ Compose</kbd> <kbd>е</kbd> <kbd>-</kbd>              | ҽ      |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>һ</kbd>              | ћ      |
| <kbd>⎄ Compose</kbd> <kbd>һ</kbd> <kbd>-</kbd>              | ћ      |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>ч</kbd> <kbd>ч</kbd> | ћ      |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>ь</kbd>              | ҍ      |
| <kbd>⎄ Compose</kbd> <kbd>ь</kbd> <kbd>-</kbd>              | ҍ      |
| **Letters with diagonal strokes**                           |        |
| <kbd>⎄ Compose</kbd> <kbd>к</kbd> <kbd>\\</kbd>             | ԟ      |
| <kbd>⎄ Compose</kbd> <kbd>\\</kbd> <kbd>к</kbd>             | ԟ      |
| <kbd>⎄ Compose</kbd> <kbd>р</kbd> <kbd>\\</kbd>             | ҏ      |
| <kbd>⎄ Compose</kbd> <kbd>\\</kbd> <kbd>р</kbd>             | ҏ      |
| **Letters with top left bar**                               |        |
| <kbd>⎄ Compose</kbd> <kbd>7</kbd> <kbd>ь</kbd>              | ъ      |
| <kbd>⎄ Compose</kbd> <kbd>7</kbd> <kbd>ъ</kbd>              | ь      |
| <kbd>⎄ Compose</kbd> <kbd>7</kbd> <kbd>к</kbd>              | ҡ      |
| <kbd>⎄ Compose</kbd> <kbd>7</kbd> <kbd>ы</kbd>              | ꙑ      |
| **Letters with cedilla**                                    |        |
| <kbd>⎄ Compose</kbd> <kbd>,</kbd> <kbd>з</kbd>              | ҙ      |
| <kbd>⎄ Compose</kbd> <kbd>з</kbd> <kbd>,</kbd>              | ҙ      |
| <kbd>⎄ Compose</kbd> <kbd>¸</kbd> <kbd>з</kbd>              | ҙ      |
| <kbd>⎄ Compose</kbd> <kbd>з</kbd> <kbd>¸</kbd>              | ҙ      |
| <kbd>⎄ Compose</kbd> <kbd>,</kbd> <kbd>с</kbd>              | ҫ      |
| <kbd>⎄ Compose</kbd> <kbd>с</kbd> <kbd>,</kbd>              | ҫ      |
| <kbd>⎄ Compose</kbd> <kbd>¸</kbd> <kbd>с</kbd>              | ҫ      |
| <kbd>⎄ Compose</kbd> <kbd>с</kbd> <kbd>¸</kbd>              | ҫ      |
| **Letter with upturn**                                      |        |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>'</kbd>              | ґ      |
| **Letters with descenders to the right**                    |        |
| <kbd>⎄ Compose</kbd> <kbd>т</kbd> <kbd>с</kbd>              | ц      |
| <kbd>⎄ Compose</kbd> <kbd>ш</kbd> <kbd>,</kbd>              | щ      |
| <kbd>⎄ Compose</kbd> <kbd>ж</kbd> <kbd>,</kbd>              | җ      |
| <kbd>⎄ Compose</kbd> <kbd>к</kbd> <kbd>,</kbd>              | қ      |
| <kbd>⎄ Compose</kbd> <kbd>н</kbd> <kbd>,</kbd>              | ң      |
| <kbd>⎄ Compose</kbd> <kbd>х</kbd> <kbd>,</kbd>              | ҳ      |
| <kbd>⎄ Compose</kbd> <kbd>ч</kbd> <kbd>,</kbd>              | ҷ      |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>,</kbd>              | ӷ      |
| <kbd>⎄ Compose</kbd> <kbd>л</kbd> <kbd>,</kbd>              | ԯ      |
| <kbd>⎄ Compose</kbd> <kbd>п</kbd> <kbd>,</kbd>              | ԥ      |
| <kbd>⎄ Compose</kbd> <kbd>т</kbd> <kbd>,</kbd>              | ҭ      |
| <kbd>⎄ Compose</kbd> <kbd>һ</kbd> <kbd>,</kbd>              | ԧ      |
| <kbd>⎄ Compose</kbd> <kbd>'</kbd> <kbd>ч</kbd> <kbd>ч</kbd> | ԧ      |
| <kbd>⎄ Compose</kbd> <kbd>о</kbd> <kbd>,</kbd>              | ԛ      |
| **Letter with descender to the left**                       |        |
| <kbd>⎄ Compose</kbd> <kbd>,</kbd> <kbd>ч</kbd>              | ӌ      |
| **Letters with middle descenders**                          |        |
| <kbd>⎄ Compose</kbd> <kbd>,</kbd> <kbd>ц</kbd>              | џ      |
| <kbd>⎄ Compose</kbd> <kbd>ц</kbd> <kbd>,</kbd>              | џ      |
| <kbd>⎄ Compose</kbd> <kbd>е</kbd> <kbd>,</kbd>              | ҿ      |
| <kbd>⎄ Compose</kbd> <kbd>,</kbd> <kbd>е</kbd>              | ҿ      |
| **Letters with hooks**                                      |        |
| <kbd>⎄ Compose</kbd> <kbd>і</kbd> <kbd>9</kbd>              | ј      |
| <kbd>⎄ Compose</kbd> <kbd>к</kbd> <kbd>5</kbd>              | ӄ      |
| <kbd>⎄ Compose</kbd> <kbd>к</kbd> <kbd>9</kbd>              | ӄ      |
| <kbd>⎄ Compose</kbd> <kbd>к</kbd> <kbd>ј</kbd>              | ӄ      |
| <kbd>⎄ Compose</kbd> <kbd>л</kbd> <kbd>9</kbd>              | ԓ      |
| <kbd>⎄ Compose</kbd> <kbd>л</kbd> <kbd>ј</kbd>              | ԓ      |
| <kbd>⎄ Compose</kbd> <kbd>н</kbd> <kbd>9</kbd>              | ӈ      |
| <kbd>⎄ Compose</kbd> <kbd>н</kbd> <kbd>ј</kbd>              | ӈ      |
| <kbd>⎄ Compose</kbd> <kbd>х</kbd> <kbd>9</kbd>              | ӽ      |
| <kbd>⎄ Compose</kbd> <kbd>х</kbd> <kbd>ј</kbd>              | ӽ      |
| <kbd>⎄ Compose</kbd> <kbd>ғ</kbd> <kbd>9</kbd>              | ӻ      |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>9</kbd>              | ӻ      |
| **Letters with middle hooks**                               |        |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>5</kbd>              | ҕ      |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>ј</kbd>              | ҕ      |
| <kbd>⎄ Compose</kbd> <kbd>п</kbd> <kbd>5</kbd>              | ҧ      |
| <kbd>⎄ Compose</kbd> <kbd>п</kbd> <kbd>ј</kbd>              | ҧ      |
| <kbd>⎄ Compose</kbd> <kbd>ћ</kbd> <kbd>5</kbd>              | ђ      |
| <kbd>⎄ Compose</kbd> <kbd>һ</kbd> <kbd>5</kbd>              | ђ      |
| <kbd>⎄ Compose</kbd> <kbd>һ</kbd> <kbd>ј</kbd>              | ђ      |
| <kbd>⎄ Compose</kbd> <kbd>т</kbd> <kbd>5</kbd>              | ђ      |
| <kbd>⎄ Compose</kbd> <kbd>т</kbd> <kbd>ј</kbd>              | ђ      |
| **Letters with left hooks**                                 |        |
| <kbd>⎄ Compose</kbd> <kbd>9</kbd> <kbd>н</kbd>              | ԩ      |
| <kbd>⎄ Compose</kbd> <kbd>л</kbd> <kbd>н</kbd>              | ԩ      |
| <kbd>⎄ Compose</kbd> <kbd>ј</kbd> <kbd>н</kbd>              | ԩ      |
| **Letters with tails**                                      |        |
| <kbd>⎄ Compose</kbd> <kbd>л</kbd> <kbd>;</kbd>              | ӆ      |
| <kbd>⎄ Compose</kbd> <kbd>м</kbd> <kbd>;</kbd>              | ӎ      |
| <kbd>⎄ Compose</kbd> <kbd>н</kbd> <kbd>;</kbd>              | ӊ      |
| **Letters with multiple diacritics**                        |        |
| <kbd>⎄ Compose</kbd> <kbd>"</kbd> <kbd>-</kbd> <kbd>о</kbd> | ӫ      |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>"</kbd> <kbd>о</kbd> | ӫ      |
| **Letters absent from Macedonian & Serbian Cyrillic**       |        |
| <kbd>⎄ Compose</kbd> <kbd>ј</kbd> <kbd>и</kbd>              | й      |
| <kbd>⎄ Compose</kbd> <kbd>й</kbd> <kbd>о</kbd>              | ё      |
| <kbd>⎄ Compose</kbd> <kbd>ј</kbd> <kbd>о</kbd>              | ё      |
| <kbd>⎄ Compose</kbd> <kbd>й</kbd> <kbd>у</kbd>              | ю      |
| <kbd>⎄ Compose</kbd> <kbd>ј</kbd> <kbd>у</kbd>              | ю      |
| <kbd>⎄ Compose</kbd> <kbd>й</kbd> <kbd>а</kbd>              | я      |
| <kbd>⎄ Compose</kbd> <kbd>ј</kbd> <kbd>а</kbd>              | я      |
| **Currency symbols**                                        |        |
| <kbd>⎄ Compose</kbd> <kbd>=</kbd> <kbd>г</kbd>              | ₴      |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>=</kbd>              | ₴      |
| <kbd>⎄ Compose</kbd> <kbd>=</kbd> <kbd>р</kbd>              | ₽      |
| <kbd>⎄ Compose</kbd> <kbd>р</kbd> <kbd>=</kbd>              | ₽      |
| <kbd>⎄ Compose</kbd> <kbd>=</kbd> <kbd>т</kbd>              | ₮      |
| <kbd>⎄ Compose</kbd> <kbd>т</kbd> <kbd>=</kbd>              | ₮      |
| <kbd>⎄ Compose</kbd> <kbd>_</kbd> <kbd>т</kbd>              | ₸      |
| <kbd>⎄ Compose</kbd> <kbd>т</kbd> <kbd>_</kbd>              | ₸      |
| <kbd>⎄ Compose</kbd> <kbd>_</kbd> <kbd>с</kbd>              | ⃀¹     |
| <kbd>⎄ Compose</kbd> <kbd>с</kbd> <kbd>_</kbd>              | ⃀¹     |

¹: Kyrgyz som (underlined С) was introduced into Unicode in 2021 and is still absent from most fonts.

</details>

Compose sequences for Cyrillic letters with common diacritics (acute <kbd>´</kbd>, breve <kbd>˘</kbd>, macron <kbd>¯</kbd>, háček <kbd>ˇ</kbd>, etc.) are mostly present in Xorg (Linux) and WinCompose (Windows). They are usually entered as <kbd>⎄ Compose</kbd> <kbd>diacritic</kbd> <kbd>letter</kbd>. They can be viewed [here](https://gitlab.freedesktop.org/xorg/lib/libx11/-/blob/master/nls/en_US.UTF-8/Compose.pre#L1559) and [here](https://gitlab.freedesktop.org/xorg/lib/libx11/-/blob/master/nls/en_US.UTF-8/Compose.pre#L4874).

Some letters are still missing, though, so [they are included in our table too](blob/main/.XCompose#L567).

## Related projects ##

TODO

## Important information ##

[Queer Svit](https://queersvit.taplink.ws/) is an organization that helps queer and BAME people impacted by the war in Ukraine, and those whose lives are threated by rising authoritarianism in Russia and Belarus. We are a group of volunteers, providing financial assistance, housing, and transportation to LGBTQ+ and BAME people in need, along with guidance and connections to further resources.
Any donation helps, and we are always grateful to people who spread the word about our cause. Thank you!

## License ##

[MIT](blob/main/LICENSE)
