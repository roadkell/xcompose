# Compose-таблица для кириллических алфавитов / Compose Table for Cyrillic Alphabets #

*Every time a user is forced to needlessly switch input languages, God kills a kitten. Stop the slaughter!*

- [Что это](#что-это)
- [Как установить](#как-установить)
  - [Windows](#windows)
  - [Linux](#linux)
- [Как пользоваться](#как-пользоваться)
- [Список комбинаций](#список-комбинаций)
- [Похожие проекты](#похожие-проекты)
- [Важное](#важное)
- [Лицензия](#лицензия)

## Что это ##

Таблица compose-последовательностей, упрощающая ввод букв кириллических алфавитов без необходимости устанавливать несколько раскладок. Аналог `Compose` из `en_US.UTF-8`, только для кириллицы.

Например, если в вашей раскладке нет буквы Ғ (Г со штрихом), её можно ввести, нажав по очереди клавиши <kbd>⎄ Compose</kbd> <kbd>Г</kbd> <kbd>-</kbd> (а саму клавишу <kbd>⎄ Compose</kbd> можно назначить, например, на <kbd>Caps Lock</kbd> или на правый <kbd>Alt</kbd>). Удерживать клавиши не нужно. Полный список доступных символов [см. ниже](#список-комбинаций).

Подробнее об использовании compose-клавиши можно прочитать в Википедии ([Ру](https://ru.wikipedia.org/wiki/Compose) / [En](https://en.wikipedia.org/wiki/Compose_key)). Там же можно посмотреть комбинации, по умолчанию входящие в состав Xorg (Linux) и WinCompose (Windows). Например, там есть комбинации для длинного тире, различных кавычек, диакритических знаков [и т. д.]((https://gitlab.freedesktop.org/xorg/lib/libx11/-/blob/master/nls/en_US.UTF-8/Compose.pre))

## Как установить ##

### Windows ###

1. Установить [WinCompose](https://github.com/samhocevar/wincompose).
2. Скачать файл [.XCompose](/.XCompose).
3. Сохранить его в папке пользовательского профиля (обычно это `C:\Users\имя_пользователя\`).
4. Перезапустить WinCompose.
5. Если нужно, переназначить compose-клавишу в настройках приложения (по умолчанию это правый <kbd>Alt</kbd>).

### Linux ###

1. Скачать файл
   [.XCompose](/.XCompose)
   (включите показ скрытых файлов).
2. Сохранить его в домашней папке пользователя (обычно это
   `/home/имя_пользователя/`); если у вас уже установлен собственный
   `.XCompose`-файл, добавьте к нему содержимое скачанного файла.
3. Выбрать и назначить compose-клавишу (например, в GNOME это `Настройки >
   Клавиатура > Ввод специальных символов > Compose Key`).
4. Перезапустить приложение, в котором вы набираете текст.

## Как пользоваться ##

Буквы с диакритическими знаками вводятся по схеме <kbd>⎄ Compose</kbd> <kbd>буква</kbd> <kbd>знак</kbd>. Можно и наоборот: <kbd>⎄ Compose</kbd> <kbd>знак</kbd> <kbd>буква</kbd>. Например чтобы ввести букву **ѓ**, нужно набрать <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>´</kbd>. В стандартных раскладках обычно нет типографских диакритиков (умлаута <kbd>¨</kbd>, седили <kbd>¸</kbd> и др.), поэтому вместо них можно использовать более доступные символы:

| Диакритический знак                    | Замена                          | Пример комбинации                               | Буква |
| -------------------------------------- | ------------------------------- | ----------------------------------------------- | ----- |
| акут <kbd>´</kbd> (или подъём в Ґ)     | апостроф <kbd>'</kbd>           | <kbd>⎄ Compose</kbd> <kbd>к</kbd> <kbd>'</kbd>  | ќ     |
| двойной акут <kbd>˝</kbd>              | равенство <kbd>=</kbd>          | <kbd>⎄ Compose</kbd> <kbd>у</kbd> <kbd>=</kbd>  | ӳ     |
| гравис <kbd>\`</kbd>                   | обратный апостроф <kbd>\`</kbd> | <kbd>⎄ Compose</kbd> <kbd>е</kbd> <kbd>`</kbd>  | ѐ     |
| умлаут <kbd>¨</kbd>                    | кавычки <kbd>"</kbd>            | <kbd>⎄ Compose</kbd> <kbd>и</kbd> <kbd>"</kbd>  | ӥ     |
| макрон <kbd>¯</kbd>                    | подчёркивание <kbd>_</kbd>      | <kbd>⎄ Compose</kbd> <kbd>у</kbd> <kbd>_</kbd>  | ӯ     |
| гачек <kbd>ˇ</kbd>                     | меньше <kbd><</kbd>             | <kbd>⎄ Compose</kbd> <kbd><</kbd> <kbd>р</kbd>  | р̌     |
| кратка <kbd>˘</kbd>                    | скобка <kbd>(</kbd>             | <kbd>⎄ Compose</kbd> <kbd>ж</kbd> <kbd>(</kbd>  | ӂ     |
| седиль <kbd>¸</kbd> (или нижний вынос) | запятая <kbd>,</kbd>            | <kbd>⎄ Compose</kbd> <kbd>х</kbd> <kbd>,</kbd>  | ҳ     |
| нижний вынос слева                     | запятая перед буквой            | <kbd>⎄ Compose</kbd> <kbd>,</kbd> <kbd>ч</kbd>  | ӌ     |
| хвостик <kbd>ˏ</kbd>                   | точка с запятой <kbd>;</kbd>    | <kbd>⎄ Compose</kbd> <kbd>м</kbd> <kbd>;</kbd>  | ӎ     |
| горизонтальный штрих                   | дефис <kbd>-</kbd>              | <kbd>⎄ Compose</kbd> <kbd>о</kbd> <kbd>-</kbd>  | ө     |
| вертикальный штрих                     | <kbd>1</kbd>                    | <kbd>⎄ Compose</kbd> <kbd>1</kbd> <kbd>ч</kbd>  | ҹ     |
| диагональный штрих                     | бэкслэш <kbd>\\</kbd>           | <kbd>⎄ Compose</kbd> <kbd>р</kbd> <kbd>\\</kbd> | ҏ     |
| штрих сверху слева                     | <kbd>7</kbd> перед буквой       | <kbd>⎄ Compose</kbd> <kbd>7</kbd> <kbd>к</kbd>  | ҡ     |
| крюк <kbd> ̡</kbd>                      | <kbd>9</kbd>                    | <kbd>⎄ Compose</kbd> <kbd>л</kbd> <kbd>9</kbd>  | ԓ     |
| крюк слева                             | <kbd>9</kbd> перед буквой       | <kbd>⎄ Compose</kbd> <kbd>9</kbd> <kbd>н</kbd>  | ԩ     |
| крюк посередине                        | <kbd>5</kbd>                    | <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>5</kbd>  | ҕ     |

Если буква имеет уникальное начертание, её можно получить, набрав похожую внешне букву дважды:

| Ввод                                           | Буква |
| ---------------------------------------------- | ----- |
| <kbd>⎄ Compose</kbd> <kbd>е</kbd> <kbd>е</kbd> | ә     |
| <kbd>⎄ Compose</kbd> <kbd>у</kbd> <kbd>у</kbd> | ү     |
| <kbd>⎄ Compose</kbd> <kbd>ц</kbd> <kbd>ц</kbd> | џ     |

Или соединив с цифрой с похожим начертанием:

| Ввод                                           | Буква |
| ---------------------------------------------- | ----- |
| <kbd>⎄ Compose</kbd> <kbd>с</kbd> <kbd>5</kbd> | ѕ     |
| <kbd>⎄ Compose</kbd> <kbd>з</kbd> <kbd>3</kbd> | ӡ     |

С лигатурами всё просто:

| Ввод                                           | Буква |
| ---------------------------------------------- | ----- |
| <kbd>⎄ Compose</kbd> <kbd>а</kbd> <kbd>е</kbd> | ӕ     |
| <kbd>⎄ Compose</kbd> <kbd>л</kbd> <kbd>ь</kbd> | љ     |

Диграфы с палочкой (буква <kbd>Ӏ</kbd> в алфавитах кавказских языков) можно ввести, заменив палочку единицей или вертикальной чертой. Аналогично можно ввести и букву <kbd>Ы</kbd>:

| Ввод                                            | Буква |
| ----------------------------------------------- | ----- |
| <kbd>⎄ Compose</kbd> <kbd>а</kbd> <kbd>1</kbd>  | аӀ    |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>\|</kbd> | гӀ    |
| <kbd>⎄ Compose</kbd> <kbd>ь</kbd> <kbd>1</kbd>  | ы     |

Знаки валют — это буква и знак равенства (иногда подчёркивания):

| Ввод                                           | Буква |
| ---------------------------------------------- | ----- |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>=</kbd> | ₴     |
| <kbd>⎄ Compose</kbd> <kbd>т</kbd> <kbd>_</kbd> | ₸     |

## Список комбинаций ##

<details><summary>Развернуть</summary>

| Ввод                                                        | Буква |
| ----------------------------------------------------------- | ----- |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>г</kbd>              | ѕ     |
| <kbd>⎄ Compose</kbd> <kbd>с</kbd> <kbd>5</kbd>              | ѕ     |
| <kbd>⎄ Compose</kbd> <kbd>5</kbd> <kbd>с</kbd>              | ѕ     |
| <kbd>⎄ Compose</kbd> <kbd>е</kbd> <kbd>е</kbd>              | ә     |
| <kbd>⎄ Compose</kbd> <kbd>ё</kbd> <kbd>ё</kbd>              | ӛ     |
| <kbd>⎄ Compose</kbd> <kbd>з</kbd> <kbd>з</kbd>              | ԑ     |
| <kbd>⎄ Compose</kbd> <kbd>м</kbd> <kbd>м</kbd>              | ԝ     |
| <kbd>⎄ Compose</kbd> <kbd>у</kbd> <kbd>у</kbd>              | ү     |
| <kbd>⎄ Compose</kbd> <kbd>ц</kbd> <kbd>ц</kbd>              | џ     |
| <kbd>⎄ Compose</kbd> <kbd>ч</kbd> <kbd>ч</kbd>              | һ     |
| <kbd>⎄ Compose</kbd> <kbd>э</kbd> <kbd>э</kbd>              | є     |
| <kbd>⎄ Compose</kbd> <kbd>є</kbd> <kbd>є</kbd>              | э     |
| <kbd>⎄ Compose</kbd> <kbd>з</kbd> <kbd>3</kbd>              | ӡ     |
| <kbd>⎄ Compose</kbd> <kbd>3</kbd> <kbd>з</kbd>              | ӡ     |
| <kbd>⎄ Compose</kbd> <kbd>о</kbd> <kbd>о</kbd>              | ҩ     |
| <kbd>⎄ Compose</kbd> <kbd>с</kbd> <kbd>о</kbd>              | ҩ     |
| <kbd>⎄ Compose</kbd> <kbd>с</kbd> <kbd>0</kbd>              | ҩ     |
| <kbd>⎄ Compose</kbd> <kbd>0</kbd> <kbd>с</kbd>              | ҩ     |
| <kbd>⎄ Compose</kbd> <kbd>о</kbd> <kbd>0</kbd>              | ҩ     |
| <kbd>⎄ Compose</kbd> <kbd>0</kbd> <kbd>о</kbd>              | ҩ     |
| **Лигатуры**                                                |       |
| <kbd>⎄ Compose</kbd> <kbd>а</kbd> <kbd>е</kbd>              | ӕ     |
| <kbd>⎄ Compose</kbd> <kbd>л</kbd> <kbd>ь</kbd>              | љ     |
| <kbd>⎄ Compose</kbd> <kbd>н</kbd> <kbd>г</kbd>              | ҥ     |
| <kbd>⎄ Compose</kbd> <kbd>н</kbd> <kbd>ь</kbd>              | њ     |
| <kbd>⎄ Compose</kbd> <kbd>т</kbd> <kbd>ц</kbd>              | ҵ     |
| **Диграфы**                                                 |       |
| <kbd>⎄ Compose</kbd> <kbd>ь</kbd> <kbd>і</kbd>              | ы     |
| <kbd>⎄ Compose</kbd> <kbd>ъ</kbd> <kbd>і</kbd>              | ы     |
| <kbd>⎄ Compose</kbd> <kbd>ь</kbd> <kbd>\|</kbd>             | ы     |
| <kbd>⎄ Compose</kbd> <kbd>ъ</kbd> <kbd>\|</kbd>             | ы     |
| <kbd>⎄ Compose</kbd> <kbd>ь</kbd> <kbd>1</kbd>              | ы     |
| <kbd>⎄ Compose</kbd> <kbd>ъ</kbd> <kbd>1</kbd>              | ы     |
| <kbd>⎄ Compose</kbd> <kbd>¨</kbd> <kbd>ь</kbd> <kbd>і</kbd> | ӹ     |
| <kbd>⎄ Compose</kbd> <kbd>¨</kbd> <kbd>ъ</kbd> <kbd>і</kbd> | ӹ     |
| <kbd>⎄ Compose</kbd> <kbd>"</kbd> <kbd>ь</kbd> <kbd>і</kbd> | ӹ     |
| <kbd>⎄ Compose</kbd> <kbd>"</kbd> <kbd>ъ</kbd> <kbd>і</kbd> | ӹ     |
| <kbd>⎄ Compose</kbd> <kbd>а</kbd> <kbd>\|</kbd>             | аӀ    |
| <kbd>⎄ Compose</kbd> <kbd>а</kbd> <kbd>1</kbd>              | аӀ    |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>\|</kbd>             | гӀ    |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>1</kbd>              | гӀ    |
| <kbd>⎄ Compose</kbd> <kbd>к</kbd> <kbd>\|</kbd>             | кӀ    |
| <kbd>⎄ Compose</kbd> <kbd>к</kbd> <kbd>1</kbd>              | кӀ    |
| <kbd>⎄ Compose</kbd> <kbd>л</kbd> <kbd>\|</kbd>             | лІ    |
| <kbd>⎄ Compose</kbd> <kbd>л</kbd> <kbd>1</kbd>              | лІ    |
| <kbd>⎄ Compose</kbd> <kbd>о</kbd> <kbd>\|</kbd>             | оӀ    |
| <kbd>⎄ Compose</kbd> <kbd>о</kbd> <kbd>1</kbd>              | оӀ    |
| <kbd>⎄ Compose</kbd> <kbd>п</kbd> <kbd>\|</kbd>             | пӀ    |
| <kbd>⎄ Compose</kbd> <kbd>п</kbd> <kbd>1</kbd>              | пӀ    |
| <kbd>⎄ Compose</kbd> <kbd>т</kbd> <kbd>\|</kbd>             | тӀ    |
| <kbd>⎄ Compose</kbd> <kbd>т</kbd> <kbd>1</kbd>              | тӀ    |
| <kbd>⎄ Compose</kbd> <kbd>у</kbd> <kbd>\|</kbd>             | уӀ    |
| <kbd>⎄ Compose</kbd> <kbd>у</kbd> <kbd>1</kbd>              | уӀ    |
| <kbd>⎄ Compose</kbd> <kbd>ф</kbd> <kbd>\|</kbd>             | фӀ    |
| <kbd>⎄ Compose</kbd> <kbd>ф</kbd> <kbd>1</kbd>              | фӀ    |
| <kbd>⎄ Compose</kbd> <kbd>х</kbd> <kbd>\|</kbd>             | хӀ    |
| <kbd>⎄ Compose</kbd> <kbd>х</kbd> <kbd>1</kbd>              | хӀ    |
| <kbd>⎄ Compose</kbd> <kbd>ц</kbd> <kbd>\|</kbd>             | цӀ    |
| <kbd>⎄ Compose</kbd> <kbd>ц</kbd> <kbd>1</kbd>              | цӀ    |
| <kbd>⎄ Compose</kbd> <kbd>ч</kbd> <kbd>\|</kbd>             | чӀ    |
| <kbd>⎄ Compose</kbd> <kbd>ч</kbd> <kbd>1</kbd>              | чӀ    |
| <kbd>⎄ Compose</kbd> <kbd>ш</kbd> <kbd>\|</kbd>             | шІ    |
| <kbd>⎄ Compose</kbd> <kbd>ш</kbd> <kbd>1</kbd>              | шІ    |
| <kbd>⎄ Compose</kbd> <kbd>щ</kbd> <kbd>\|</kbd>             | щІ    |
| <kbd>⎄ Compose</kbd> <kbd>щ</kbd> <kbd>1</kbd>              | щІ    |
| <kbd>⎄ Compose</kbd> <kbd>ы</kbd> <kbd>\|</kbd>             | ыӀ    |
| <kbd>⎄ Compose</kbd> <kbd>ы</kbd> <kbd>1</kbd>              | ыӀ    |
| <kbd>⎄ Compose</kbd> <kbd>\|</kbd> <kbd>У</kbd>             | Іу    |
| <kbd>⎄ Compose</kbd> <kbd>1</kbd> <kbd>У</kbd>              | Іу    |
| <kbd>⎄ Compose</kbd> <kbd>\|</kbd> <kbd>у</kbd>             | Іу    |
| <kbd>⎄ Compose</kbd> <kbd>1</kbd> <kbd>у</kbd>              | Іу    |
| **Палочка**                                                 |       |
| <kbd>⎄ Compose</kbd> <kbd>˙</kbd> <kbd>і</kbd>              | Ӏ     |
| <kbd>⎄ Compose</kbd> <kbd>і</kbd> <kbd>˙</kbd>              | Ӏ     |
| <kbd>⎄ Compose</kbd> <kbd>.</kbd> <kbd>і</kbd>              | Ӏ     |
| <kbd>⎄ Compose</kbd> <kbd>і</kbd> <kbd>.</kbd>              | Ӏ     |
| <kbd>⎄ Compose</kbd> <kbd>ь</kbd> <kbd>ы</kbd>              | Ӏ     |
| <kbd>⎄ Compose</kbd> <kbd>ъ</kbd> <kbd>ы</kbd>              | Ӏ     |
| <kbd>⎄ Compose</kbd> <kbd>ы</kbd> <kbd>ь</kbd>              | Ӏ     |
| <kbd>⎄ Compose</kbd> <kbd>ы</kbd> <kbd>ъ</kbd>              | Ӏ     |
| **Кириллические і, ї, ј на основе и, й**                    |       |
| <kbd>⎄ Compose</kbd> <kbd>˙</kbd> <kbd>и</kbd>              | і     |
| <kbd>⎄ Compose</kbd> <kbd>и</kbd> <kbd>˙</kbd>              | і     |
| <kbd>⎄ Compose</kbd> <kbd>.</kbd> <kbd>и</kbd>              | і     |
| <kbd>⎄ Compose</kbd> <kbd>и</kbd> <kbd>.</kbd>              | і     |
| <kbd>⎄ Compose</kbd> <kbd>¨</kbd> <kbd>й</kbd>              | ї     |
| <kbd>⎄ Compose</kbd> <kbd>й</kbd> <kbd>¨</kbd>              | ї     |
| <kbd>⎄ Compose</kbd> <kbd>"</kbd> <kbd>й</kbd>              | ї     |
| <kbd>⎄ Compose</kbd> <kbd>й</kbd> <kbd>"</kbd>              | ї     |
| <kbd>⎄ Compose</kbd> <kbd>˙</kbd> <kbd>й</kbd>              | ј     |
| <kbd>⎄ Compose</kbd> <kbd>й</kbd> <kbd>˙</kbd>              | ј     |
| <kbd>⎄ Compose</kbd> <kbd>.</kbd> <kbd>й</kbd>              | ј     |
| <kbd>⎄ Compose</kbd> <kbd>й</kbd> <kbd>.</kbd>              | ј     |
| **Буквы с вертикальным штрихом**                            |       |
| <kbd>⎄ Compose</kbd> <kbd>\|</kbd> <kbd>к</kbd>             | ҝ     |
| <kbd>⎄ Compose</kbd> <kbd>1</kbd> <kbd>к</kbd>              | ҝ     |
| <kbd>⎄ Compose</kbd> <kbd>\|</kbd> <kbd>ч</kbd>             | ҹ     |
| <kbd>⎄ Compose</kbd> <kbd>1</kbd> <kbd>ч</kbd>              | ҹ     |
| **Буквы с горизонтальным штрихом**                          |       |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>о</kbd>              | ө     |
| <kbd>⎄ Compose</kbd> <kbd>о</kbd> <kbd>-</kbd>              | ө     |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>г</kbd>              | ғ     |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>-</kbd>              | ғ     |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>к</kbd>              | ҟ     |
| <kbd>⎄ Compose</kbd> <kbd>к</kbd> <kbd>-</kbd>              | ҟ     |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>ү</kbd>              | ұ     |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>у</kbd>              | ұ     |
| <kbd>⎄ Compose</kbd> <kbd>ү</kbd> <kbd>-</kbd>              | ұ     |
| <kbd>⎄ Compose</kbd> <kbd>у</kbd> <kbd>-</kbd>              | ұ     |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>х</kbd>              | ӿ     |
| <kbd>⎄ Compose</kbd> <kbd>х</kbd> <kbd>-</kbd>              | ӿ     |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>е</kbd>              | ҽ     |
| <kbd>⎄ Compose</kbd> <kbd>е</kbd> <kbd>-</kbd>              | ҽ     |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>һ</kbd>              | ћ     |
| <kbd>⎄ Compose</kbd> <kbd>һ</kbd> <kbd>-</kbd>              | ћ     |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>ч</kbd> <kbd>ч</kbd> | ћ     |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>ь</kbd>              | ҍ     |
| <kbd>⎄ Compose</kbd> <kbd>ь</kbd> <kbd>-</kbd>              | ҍ     |
| **Буквы с диагональным штрихом**                            |       |
| <kbd>⎄ Compose</kbd> <kbd>к</kbd> <kbd>\\</kbd>             | ԟ     |
| <kbd>⎄ Compose</kbd> <kbd>\\</kbd> <kbd>к</kbd>             | ԟ     |
| <kbd>⎄ Compose</kbd> <kbd>р</kbd> <kbd>\\</kbd>             | ҏ     |
| <kbd>⎄ Compose</kbd> <kbd>\\</kbd> <kbd>р</kbd>             | ҏ     |
| **Буквы со штрихом сверху слева**                           |       |
| <kbd>⎄ Compose</kbd> <kbd>7</kbd> <kbd>ь</kbd>              | ъ     |
| <kbd>⎄ Compose</kbd> <kbd>7</kbd> <kbd>ъ</kbd>              | ь     |
| <kbd>⎄ Compose</kbd> <kbd>7</kbd> <kbd>к</kbd>              | ҡ     |
| <kbd>⎄ Compose</kbd> <kbd>7</kbd> <kbd>ы</kbd>              | ꙑ     |
| **Буквы с седилью**                                         |       |
| <kbd>⎄ Compose</kbd> <kbd>,</kbd> <kbd>з</kbd>              | ҙ     |
| <kbd>⎄ Compose</kbd> <kbd>з</kbd> <kbd>,</kbd>              | ҙ     |
| <kbd>⎄ Compose</kbd> <kbd>¸</kbd> <kbd>з</kbd>              | ҙ     |
| <kbd>⎄ Compose</kbd> <kbd>з</kbd> <kbd>¸</kbd>              | ҙ     |
| <kbd>⎄ Compose</kbd> <kbd>,</kbd> <kbd>с</kbd>              | ҫ     |
| <kbd>⎄ Compose</kbd> <kbd>с</kbd> <kbd>,</kbd>              | ҫ     |
| <kbd>⎄ Compose</kbd> <kbd>¸</kbd> <kbd>с</kbd>              | ҫ     |
| <kbd>⎄ Compose</kbd> <kbd>с</kbd> <kbd>¸</kbd>              | ҫ     |
| **Буква с подъёмом**                                        |       |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>'</kbd>              | ґ     |
| **Буквы с нижним выносным элементом**                       |       |
| <kbd>⎄ Compose</kbd> <kbd>т</kbd> <kbd>с</kbd>              | ц     |
| <kbd>⎄ Compose</kbd> <kbd>ш</kbd> <kbd>,</kbd>              | щ     |
| <kbd>⎄ Compose</kbd> <kbd>ж</kbd> <kbd>,</kbd>              | җ     |
| <kbd>⎄ Compose</kbd> <kbd>к</kbd> <kbd>,</kbd>              | қ     |
| <kbd>⎄ Compose</kbd> <kbd>н</kbd> <kbd>,</kbd>              | ң     |
| <kbd>⎄ Compose</kbd> <kbd>х</kbd> <kbd>,</kbd>              | ҳ     |
| <kbd>⎄ Compose</kbd> <kbd>ч</kbd> <kbd>,</kbd>              | ҷ     |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>,</kbd>              | ӷ     |
| <kbd>⎄ Compose</kbd> <kbd>л</kbd> <kbd>,</kbd>              | ԯ     |
| <kbd>⎄ Compose</kbd> <kbd>п</kbd> <kbd>,</kbd>              | ԥ     |
| <kbd>⎄ Compose</kbd> <kbd>т</kbd> <kbd>,</kbd>              | ҭ     |
| <kbd>⎄ Compose</kbd> <kbd>һ</kbd> <kbd>,</kbd>              | ԧ     |
| <kbd>⎄ Compose</kbd> <kbd>'</kbd> <kbd>ч</kbd> <kbd>ч</kbd> | ԧ     |
| <kbd>⎄ Compose</kbd> <kbd>о</kbd> <kbd>,</kbd>              | ԛ     |
| **Буква с нижним выносом слева**                            |       |
| <kbd>⎄ Compose</kbd> <kbd>,</kbd> <kbd>ч</kbd>              | ӌ     |
| **Буквы с нижним выносом посередине**                       |       |
| <kbd>⎄ Compose</kbd> <kbd>,</kbd> <kbd>ц</kbd>              | џ     |
| <kbd>⎄ Compose</kbd> <kbd>ц</kbd> <kbd>,</kbd>              | џ     |
| <kbd>⎄ Compose</kbd> <kbd>е</kbd> <kbd>,</kbd>              | ҿ     |
| <kbd>⎄ Compose</kbd> <kbd>,</kbd> <kbd>е</kbd>              | ҿ     |
| **Буквы с крюком**                                          |       |
| <kbd>⎄ Compose</kbd> <kbd>і</kbd> <kbd>9</kbd>              | ј     |
| <kbd>⎄ Compose</kbd> <kbd>к</kbd> <kbd>5</kbd>              | ӄ     |
| <kbd>⎄ Compose</kbd> <kbd>к</kbd> <kbd>9</kbd>              | ӄ     |
| <kbd>⎄ Compose</kbd> <kbd>к</kbd> <kbd>ј</kbd>              | ӄ     |
| <kbd>⎄ Compose</kbd> <kbd>л</kbd> <kbd>9</kbd>              | ԓ     |
| <kbd>⎄ Compose</kbd> <kbd>л</kbd> <kbd>ј</kbd>              | ԓ     |
| <kbd>⎄ Compose</kbd> <kbd>н</kbd> <kbd>9</kbd>              | ӈ     |
| <kbd>⎄ Compose</kbd> <kbd>н</kbd> <kbd>ј</kbd>              | ӈ     |
| <kbd>⎄ Compose</kbd> <kbd>х</kbd> <kbd>9</kbd>              | ӽ     |
| <kbd>⎄ Compose</kbd> <kbd>х</kbd> <kbd>ј</kbd>              | ӽ     |
| <kbd>⎄ Compose</kbd> <kbd>ғ</kbd> <kbd>9</kbd>              | ӻ     |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>9</kbd>              | ӻ     |
| **Буквы с крюком посередине**                               |       |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>5</kbd>              | ҕ     |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>ј</kbd>              | ҕ     |
| <kbd>⎄ Compose</kbd> <kbd>п</kbd> <kbd>5</kbd>              | ҧ     |
| <kbd>⎄ Compose</kbd> <kbd>п</kbd> <kbd>ј</kbd>              | ҧ     |
| <kbd>⎄ Compose</kbd> <kbd>ћ</kbd> <kbd>5</kbd>              | ђ     |
| <kbd>⎄ Compose</kbd> <kbd>һ</kbd> <kbd>5</kbd>              | ђ     |
| <kbd>⎄ Compose</kbd> <kbd>һ</kbd> <kbd>ј</kbd>              | ђ     |
| <kbd>⎄ Compose</kbd> <kbd>т</kbd> <kbd>5</kbd>              | ђ     |
| <kbd>⎄ Compose</kbd> <kbd>т</kbd> <kbd>ј</kbd>              | ђ     |
| **Буквы с крюком слева**                                    |       |
| <kbd>⎄ Compose</kbd> <kbd>9</kbd> <kbd>н</kbd>              | ԩ     |
| <kbd>⎄ Compose</kbd> <kbd>л</kbd> <kbd>н</kbd>              | ԩ     |
| <kbd>⎄ Compose</kbd> <kbd>ј</kbd> <kbd>н</kbd>              | ԩ     |
| **Буквы с хвостиком**                                       |       |
| <kbd>⎄ Compose</kbd> <kbd>л</kbd> <kbd>;</kbd>              | ӆ     |
| <kbd>⎄ Compose</kbd> <kbd>м</kbd> <kbd>;</kbd>              | ӎ     |
| <kbd>⎄ Compose</kbd> <kbd>н</kbd> <kbd>;</kbd>              | ӊ     |
| **Буквы с несколькими диакритиками**                        |       |
| <kbd>⎄ Compose</kbd> <kbd>"</kbd> <kbd>-</kbd> <kbd>о</kbd> | ӫ     |
| <kbd>⎄ Compose</kbd> <kbd>-</kbd> <kbd>"</kbd> <kbd>о</kbd> | ӫ     |
| **Буквы, отсутствующие в сербском и македонском**           |       |
| <kbd>⎄ Compose</kbd> <kbd>ј</kbd> <kbd>и</kbd>              | й     |
| <kbd>⎄ Compose</kbd> <kbd>й</kbd> <kbd>о</kbd>              | ё     |
| <kbd>⎄ Compose</kbd> <kbd>ј</kbd> <kbd>о</kbd>              | ё     |
| <kbd>⎄ Compose</kbd> <kbd>й</kbd> <kbd>у</kbd>              | ю     |
| <kbd>⎄ Compose</kbd> <kbd>ј</kbd> <kbd>у</kbd>              | ю     |
| <kbd>⎄ Compose</kbd> <kbd>й</kbd> <kbd>а</kbd>              | я     |
| <kbd>⎄ Compose</kbd> <kbd>ј</kbd> <kbd>а</kbd>              | я     |
| **Знаки валют**                                             |       |
| <kbd>⎄ Compose</kbd> <kbd>=</kbd> <kbd>г</kbd>              | ₴     |
| <kbd>⎄ Compose</kbd> <kbd>г</kbd> <kbd>=</kbd>              | ₴     |
| <kbd>⎄ Compose</kbd> <kbd>=</kbd> <kbd>р</kbd>              | ₽     |
| <kbd>⎄ Compose</kbd> <kbd>р</kbd> <kbd>=</kbd>              | ₽     |
| <kbd>⎄ Compose</kbd> <kbd>=</kbd> <kbd>т</kbd>              | ₮     |
| <kbd>⎄ Compose</kbd> <kbd>т</kbd> <kbd>=</kbd>              | ₮     |
| <kbd>⎄ Compose</kbd> <kbd>_</kbd> <kbd>т</kbd>              | ₸     |
| <kbd>⎄ Compose</kbd> <kbd>т</kbd> <kbd>_</kbd>              | ₸     |
| <kbd>⎄ Compose</kbd> <kbd>_</kbd> <kbd>с</kbd>              | ⃀¹    |
| <kbd>⎄ Compose</kbd> <kbd>с</kbd> <kbd>_</kbd>              | ⃀¹    |

¹: Знак кыргызского сома (подчёркнутая С) лишь в 2021 году был включён в стандарт Unicode, поэтому во многих шрифтах он пока отсутствует.

</details>

Compose-последовательности для кириллических букв с "обычными" диакритиками (акутом <kbd>´</kbd>, краткой <kbd>˘</kbd>, макроном <kbd>¯</kbd>, гачеком <kbd>ˇ</kbd> и др.) уже есть в составе Xorg (Linux) и WinCompose (Windows). Обычно они вводятся по схеме <kbd>⎄ Compose</kbd> <kbd>знак</kbd> <kbd>буква</kbd>. Списки комбинаций: [раз](https://gitlab.freedesktop.org/xorg/lib/libx11/-/blob/master/nls/en_US.UTF-8/Compose.pre#L1559), [два](https://gitlab.freedesktop.org/xorg/lib/libx11/-/blob/master/nls/en_US.UTF-8/Compose.pre#L4874).

Некоторых букв там всё равно не хватает, поэтому [они есть в нашей таблице](/.XCompose#L567).

## Похожие проекты ##

TODO

## Важное ##

[Квiр Свiт](https://queersvit.taplink.ws/) — организация, которая помогает квир- и небелым людям, пострадавшим от войны в Украине, и тем, чьим жизням угрожает растущий авторитаризм в России и Беларуси. Мы — группа волонтеров, предоставляющих финансовую помощь, жилье и транспорт нуждающимся ЛГБТК+ и небелым людям, а также рекомендации и связи с дополнительными ресурсами.
Каждый донат важен, и мы всегда благодарны людям, которые распространяют информацию о нашем деле. Спасибо!

[Queer Svit](https://queersvit.taplink.ws/) is an organization that helps queer and BAME people impacted by the war in Ukraine, and those whose lives are threated by rising authoritarianism in Russia and Belarus. We are a group of volunteers, providing financial assistance, housing, and transportation to LGBTQ+ and BAME people in need, along with guidance and connections to further resources.
Any donation helps, and we are always grateful to people who spread the word about our cause. Thank you!

## Лицензия ##

[MIT](blob/main/LICENSE)
