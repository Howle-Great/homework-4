## Чек-листы команды WAO на почту https://e.mail.ru

### Пояснение терминов

**Недопустимые символы** - все кроме латинских букв, цифр,
знаков подчеркивания («_»), точек («.»), минусов («-»)

### Гурин Влад и Можаев Дмитрий. Страница регистрации

* После ввода корректных данных (домен mail) и нажатия на кнопку регистрации должен происходить переход на страницу ввода капчи https://account.mail.ru/signup/verify
* После ввода корректных данных (домен inbox) и нажатия на кнопку регистрации должен происходить переход на страницу ввода капчи https://account.mail.ru/signup/verify
* После ввода корректных данных (домен list) и нажатия на кнопку регистрации должен происходить переход на страницу ввода капчи https://account.mail.ru/signup/verify
* После ввода корректных данных (домен bk) и нажатия на кнопку регистрации должен происходить переход на страницу ввода капчи https://account.mail.ru/signup/verify
* После ввода корректных данных (пол male) и нажатия на кнопку регистрации должен происходить переход на страницу ввода капчи https://account.mail.ru/signup/verify
* После ввода корректных данных (пол  female) и нажатия на кнопку регистрации должен происходить переход на страницу ввода капчи https://account.mail.ru/signup/verify
* После ввода корректных данных (високосный год и дата 29.02.16) и нажатия на кнопку регистрации должен происходить переход на страницу ввода капчи https://account.mail.ru/signup/verify
* Ввести в форму имени 80 символов и проверить, что их стало 40
* Ввести в форму фамилию 80 символов и проверить, что их стало 40
* При нажатии на кнопку регистрации при у пустых полей формы регистрации должны появляться сообщения, с просьбой заполнить поле
* При указании в дате дня из будующего и нажатии на кнопку регистрации, должно появиться сообщение об ошибке
* При попытке зарегистрироваться с уже занятым логином, всплывает сообщение с ошибкой
* При попытке зарегистрироваться с логином, содержащим недопустимые символы, всплывает сообщение о ошибке использования недопустимых символов
* При попытке зарегистрироваться с логином, содержащим кириллические символы, всплывает сообщение о ошибке использования кирилических символов
* При попытке зарегистрироваться с паролем, длиной менеее 8 символов, должно появиться сообщение о ошибке регистрации с слишком коротким паролем
* При попытке зарегистрироваться с со слабым паролем, должно появиться сообщение об ошибке
* При попытке зарегистрироваться с со слабым паролем, совпадающим с логином, должно появиться сообщение о ошибке регистрации с слишком слабым паролем
* При нажатии ссылки "условия использования" открывается новая вкладка с адрессом "https://help.mail.ru/legal/terms/mail"
* При нажатии на Невижу код, должна обновиться капча
* При попытке зарегистрироваться с пустой капчей, возникнет соответствующая ошибка
* При попытке зарегистрироваться с неверной капчей, возникнет соответствующая ошибка
* При нажатии на кнопку Назад в окне ввода капчи, должен произойти переход на страницу регистрации
* При нажатии на кнопку Назад в окне ввода капчи, должен произойти переход на страницу регистрации с сохраненными ранее введенными данными
* При нажатии на кнопку Назад в окне ввода капчи, должен произойти переход на страницу, после чего должна быть возможность отредактировать данные и продолжить регистрацию



#### Можаев Дмитрий. Входа на почту, Редактирование в форме письма

* После ввода правильной почты и пароля пользователя пропускают на страницу почты
* После ввода верной почты и неверного пароля пользователю выдается ошибка вводы неверного пароля
* После ввода почты с доменом yandex пользователя переадресовывают на страницу почты yandex
* После ввода почты с доменом gamil пользователя переадресовывают на страницу почты gmail
* После ввода почты с доменом yahoo пользователя переадресовывают на страницу почты yahoo
* После ввода почты с доменом rambler пользователя переадресовывают на страницу подключения к кастомной почте
* После ввода кастомной почты пользователя переадресовывают на страницу подключения к кастомной почте
* После ввода верной почты и пустого пароля пользователю выдается ошибка незаполненной почты
* После ввода верной почты и пароля пользователю отображается страница почты, после нажатия на кнопку выйти пользователя переадресовывают на 'https://mail.ru'
* При написании письма выделить текст и сменить его шрифт на Заголовок1, отправить письмо и проверить, что изменения применились
* При написании письма выделить текст и сменить его выравнивание на "по центру", отправить письмо и проверить, что изменения применились
* При написании письма выделить текст и сменить его отступ увеличив, отправить письмо и проверить, что изменения применились
* При написании письма выделить текст и сменить его отступ 2 раза увеличив и 1 раз уменьшив, отправить письмо и проверить, что изменения применились

#### Устинов Игорь. Главная страница почты

* После ввода электронной почты, темы и текста письма письмо попадает в папку "Входящие", и его содержание соответствует введенному
* После ввода электронной почты другого аккаунта, темы и текста письма письмо попадает в папку "Входящие" другого существующего аккаунта, и содержание этого письма соответствует введенному
* После получения нового письма в папку "Входящие" и при нажатии "кружок" слева от аватарки письма его статус изменится на "Прочитан", а всплывающее сообщение при наведении курсором на него будет "Пометить непрочитанным"
* После удаления письма оно оказывается в корзине
* После перемещения письма из корзины в папку "Входящие" оно оказывается в папке "Входящие"
* После отправки письма оно окажется в папке "Отправленные".
* При нажатии на тему письма оно откроется, показав свое содержимое
* По получении письма из другого аккаунта, ответив на него, письмо придет на тот аккаунт с добавленным текстом ответа на первоначальное письмо
* После отправления письма нескольким существующим адресатам оно окажется в папке "Входящие" у каждого из этих адресатов
* Если сделать текст жирным при написании письма, то после получения письма адресатом текст в письме окажется жирным
* Если сделать текст курсивом при написании письма, то после получения письма адресатом текст в письме окажется оформленным курсивом
* Если сделать текст подчеркнутым при написании письма, то после получения письма адресатом текст в письме окажется подчеркнутым
* Если сделать текст зачеркнутым при написании письма, то после получения письма адресатом текст в письме окажется зачеркнутым
* Если изменить цвет текста при написании письма, то после получения письма адресатом текст в письме окажется того цвета, который был выбран отправителем
* Если изменить цвет фона текста при написании письма, то после получения письма адресатом цвет фона текста в нем окажется таким, каким его выбрал отправитель

#### Прищеп Дмитрий. Папки с письмами

* Авторизация почтового ящика. Создание тестового письма. Перемещение письма в папку "Архив". Проверка в соответствующей папке, что письмо переместилось.
* Авторизация почтового ящика. Создание тестового письма. Перемещение письма в папку "Архив". Перемещение из папки "Архив" в папку "Входящие"
* Авторизация почтового ящика. Создание тестового письма. Выделение письма как важное. Проверка, что письмо выделено.
* Авторизация почтового ящика. Создание тестового письма. Выделение письма как важное. Отключение маркера важности письма. Проверка, что письмо не выделено.
* Авторизация почтового ящика. Создание тестового письма. Перемещение письма в папку "Социальные сети". Проверка в соответствующей папке, что письмо переместилось. Удаление тестового письма.
* Авторизация почтового ящика. Создание тестового письма. Перемещение письма в папку "Социальные сети". Перемещение из папки "Социальные сети" в папку "Входящие". Проверка в соответствующей папке, что письмо переместилось. Удаление тестового письма.
* Авторизация почтового ящика. Создание тестового письма. Перемещение письма в папку "Рассылки". Проверка в соответствующей папке, что письмо переместилось. Удаление тестового письма.
* Авторизация почтового ящика. Создание тестового письма. Перемещение письма в папку "Рассылки". Перемещение из папки "Рассылки" в папку "Входящие". Проверка в соответствующей папке, что письмо 
переместилось. Удаление тестового письма.
* Авторизация почтового ящика. Создание и отправка нового пустого письма. Проверка появления ошибки.
* Авторизация почтового ящика. Создание и отправка нового письма без получателя. Проверка появления ошибки.
* Авторизация почтового ящика. Создание и отправка нового письма без темы. Проверка, что письмо отправилось.
* Авторизация почтового ящика. Создание нового письма. Сохранение письма как черновик. Проверка в соответствующей папке, что письмо переместилось. Удаление тестового письма.
* Авторизация почтового ящика. Создание нового письма. Сохранение письма в черновики. Проверка в соответствующей папке, что письмо переместилось. Открытие черновика. Дозаполнение темы и отправителя. Отправка письма. Проверка, что письмо отправлено.
* Авторизация почтового ящика. Создание нового письма. Изменить формат текста на жирный. Отменить действие. Проверка текста на исходное форматирование.
* Авторизация почтового ящика. Создание нового письма. Изменить формат текста на курсив, потом на жирный, потом на подчеркнутый, потом на зачеркнутый. Отменить все форматирование. Проверка текста на исходное форматирование.
* Авторизация почтового ящика. Создание нового письма. Заполение полей. Добавление ссылки в письмо. Заполнение свойств ссылки. Проверка наличия ссылки в теле письма.
