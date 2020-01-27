## Чек-листы команды WAO на почту https://e.mail.ru

### Гурин Влад и Можаев Дмитрий. Страница регистрации

1. Успешная регистрация
    * После ввода корректных имен, фамилии и логина
    * Выбора пола (мужского/женского)
    * Существующей прошедшей даты
    * Нажатия на кнопку регистрации 
        - Выбор домена mail, пол: мужской
        - Выбор домена inbox, пол: женский
        - Выбор домена list, пол: мужской
        - Выбор домена bk, пол: женский, дата из високосного года (29.02.16)
    * Происходит переход на страницу https://account.mail.ru/signup/verify

2. Капча
    * Появляется при слишком быстром заполнении поля "Номер телефона"
    * В случае успешного ввода происходит регистрация 
    * При нажатии на "Не вижу код" должна обновиться капча
    * При нажатии на "Назад" должен произойти переход на страницу регистрации
            - Введенные ранее данные должны сохраниться
            - Должна быть возможность отредактировать введенные ранее данные и продолжить регистрацию

3. Попытка регистрации (всплывает сообщение об ошибке)
    * С уже занятым логином
    * С логином, содержащим хотя бы один недопустимый символ (любой, кроме букв и цифр)
    * С логином, содержащим кириллические символы
    * С паролем, длиной менее 8-ми символов
    * Со слабым паролем
    * С паролем, совпадающим с логином
    * С незаполненной капчей
    * С неверной капчей
    * Невозможно зарегистрироваться при указании даты рождения из будущего
    * Имя больше 40 символов
    * Фамилия больше 40 символов

4. Выбор дат
    * после выбора месяца нельзя выбрать день, которого в этом месяце нет (30.02.2016)
    * после выбора года нельзя выбрать день, которого в этом году нет (29.02.2016)
    * при смене месяца день меняется на максимально возможный для этого месяца (31 декабря на 30 ноября)


### Можаев Дмитрий. Вход на почту, Редактирование в форме письма

1. Проверка пароля
    * Введен правильный пароль => пользователь попадает на страницу почты с письмами
    * Введен неправильный пароль => пользователю выдается ошибка ввода неверного пароля

2. После ввода почты пользователя переадресовывают на страницу почты соответствующего домена
    * Yandex
    * Gmail
    * Yahoo
    * Rambler
    * Нестандартный домен пользователя

3. Выход из почты (сессия очищается, редирект на главную)
    * через кнопку "выйти"
    * через /logout
        - повторная авторизация работает


### Устинов Игорь. Операции с письмами

* При нажатии на письмо оно откроется, показав свое содержимое

1. Статус письма
    * Письмо приходит непрочитанным
    * После прочтения его статус меняется на "Прочитан"
    * Прочитанное письмо можно сделать непрочитанным
        - через меню
        - через "кружок"

2. Ответ на письмо
    * Отправляем письмо на другой аккаунт
    * Затем отвечаем на него с этого аккаунта обратно
    * Письмо придет цитата первоначального письма

3. Проверка форматирования
    * Жирное форматирование
    * Курсив
    * Подчеркнутое
    * Зачеркнутое
    * Изменение цвета:
        - Текста
        - Фона текста
    * При отмене действия/форматирования письмо должно принять исходное форматирование
        - Жирный формат текста
        - Курсив
            + потом изменить на жирный
            + потом на подчеркнутый
            + потом на зачеркнутый
    * Редактирование форматирования
            - Поменять шрифт на Заголовок1
            - Выставить выравнивание на "по центру"
            - Увеличить отступ
            - 2 раза увеличить отступ и 1 раз уменьшить
    * в письмо можно добавлять ссылки
    
4. Отправка письма
    * Письмо окажется в папке "Отправленные".
    * Письмо придет в папку "Входящие" каждому указанному адресату при отправке письма
        - даже если отправляем письмо самому себе
    * При попытке отправления следующих писем должна появиться ошибка отправки письма
        - Пустое письмо
        - Без получателя
        - Без темы


### Прищеп Дмитрий. Папки с письмами

* Письмо должно оказаться в той папке, куда его переместили

1. Черновики
    * Неотправленное письмо попадает в черновики
    * Черновик можно дозаполнить и отправить

2. Важность письма
    * Письмо можно сделать важным
    * Важное письмо можно сделать неважным


