## Чек-листы команды WAO на почту https://e.mail.ru

### Гурин Влад и Можаев Дмитрий. Страница регистрации
* После ввода корректных данных, выбора в качестве домена "mail" и нажатия на кнопку регистрации должен происходить переход на страницу ввода капчи https://account.mail.ru/signup/verify
* После ввода корректных данных, выбора в качестве домена "inbox" и нажатия на кнопку регистрации должен происходить переход на страницу ввода капчи https://account.mail.ru/signup/verify
* После ввода корректных данных, выбора в качестве домена "list" и нажатия на кнопку регистрации должен происходить переход на страницу ввода капчи https://account.mail.ru/signup/verify
* После ввода корректных данных, выбора в качестве домена "bk" и нажатия на кнопку регистрации должен происходить переход на страницу ввода капчи https://account.mail.ru/signup/verify
* После ввода корректных данных, выбора в качестве даты рождения 29 Февраля 2016 (высокосный год) и нажатия на кнопку регистрации должен происходить переход на страницу ввода капчи https://account.mail.ru/signup/verify
* После ввода в качестве имяни 80 символов в поле имени получим строку обрезанную до 40 символов
* После ввода в качестве фамилии 80 символов в поле фамилии получим строку обрезанную до 40 символов
* При нажатии на кнопку регистрации при у пустых полей формы регистрации должны появляться сообщения, с просьбой заполнить поле
* При указании в дате дня из будующего и нажатии на кнопку регистрации, должно появиться сообщение об ошибке
* При попытке зарегистрироваться с уже занятым логином, всплывает сообщение с ошибкой
* При попытке зарегистрироваться с логином, содержащим недопустимые символы, всплывает сообщение о соответствующей ошибке
* При попытке зарегистрироваться с логином, содержащим кириллические символы, всплывает сообщение о соответствующей ошибке
* При попытке зарегистрироваться с паролем, длиной менеее 8 символов, должно появиться сообщение о соответствующей ошибке
* При попытке зарегистрироваться с со слабым паролем, должно появиться сообщение об ошибке
* При попытке зарегистрироваться с со слабым паролем, совпадающим с логином, должно появиться сообщение о соответствующей ошибке
* При нажатии ссылки "условия использования" открывается новая вкладка с адрессом "https://help.mail.ru/legal/terms/mail"

#### Гурин Влад. Страница настроек почты

* После редактирования поля Firstname и нажатии на кнопку Сохранить в разделе личных данных на странице настроек, происходит переход на страницу https://e.mail.ru/settings?result=ok&afterReload=1
* После редактирования нескольких полей (Firstname, Lastname и Nickname) и нажатии на кнопку Сохранить в разделе личных данных на странице настроек, происходит переход на страницу https://e.mail.ru/settings?result=ok&afterReload=1
* При попытке сохранения пустого поля в разделе личных данных вознакает два сообщения с ошибками - одно под пустым полем, другое над разделом с личными данными
* При переключении чекбокса в разделе Работа с письмами, после нажатия на кнопку сохранить происходит переход на страницу https://e.mail.ru/settings?result=ok&afterReload=1


#### Можаев Дмитрий. Входа на почту

* После ввода правильной почты и пароля пользователя пропускают на страницу почты
* После ввода верной почты и неверного пароля пользователю выдается ошибка вводы неверного пароля
* После ввода почты с доменом yandex пользователя переадресовывают на страницу почты yandex
* После ввода почты с доменом gamil пользователя переадресовывают на страницу почты gmail
* После ввода почты с доменом yahoo пользователя переадресовывают на страницу почты yahoo
* После ввода почты с доменом rambler пользователя переадресовывают на страницу подключения к кастомной почте
* После ввода кастомной почты пользователя переадресовывают на страницу подключения к кастомной почте
* После ввода верной почты и пустого пароля пользователю выдается ошибка незаполненной почты
* После ввода верной почты и пароля пользователю отображается страница почты, после нажатия на кнопку выйти пользователя переадресовывают на 'https://mail.ru'


#### Устинов Игорь. Главная страница почты

* После ввода электронной почты, темы и текста письма письмо попадает в папку "Входящие", и его содержание соответствует введенному
* После ввода электронной почты другого аккаунта, темы и текста письма письмо попадает в папку "Входящие" другого существующего аккаунта, и содержание этого письма соответствует введенному
* После получения нового письма в папку "Входящие" его статус "Не прочитано", а всплывающее сообщение при наведении курсором на него будет "Пометить прочитанным"
* После получения нового письма в папку "Входящие" и при нажатии "кружок" слева от аватарки письма его статус изменится на "Прочитан", а всплывающее сообщение при наведении курсором на него будет "Пометить непрочитанным"
* После удаления письма оно оказывается в корзине
* После перемещения письма из корзины в папку "Входящие" оно оказывается в папке "Входящие"
* После отправки письма оно окажется в папке "Отправленные".
* При нажатии на тему письма оно откроется, показав свое содержимое
* По получении письма из другого аккаунта, ответив на него, письмо придет на тот аккаунт с добавленным текстом ответа на первоначальное письмо
* После отправления письма нескольким существующим адресатам оно окажется в папке "Входящие" у каждого из этих адресатов

#### Прищеп Дмитрий. Папки с письмами

* Авторизация почтового ящика. Создание тестового письма. Перемещение письма в папку "Архив". Проверка в соответствующей папке, что письмо переместилось.
* Авторизация почтового ящика. Создание тестового письма. Перемещение письма в папку "Архив". Перемещение из папки "Архив" в папку "Входящие"
* Авторизация почтового ящика. Создание тестового письма. Выделение письма как важное. Проверка, что письмо выделено.
* Авторизация почтового ящика. Создание тестового письма. Выделение письма как важное. Отключение маркера важности письма. Проверка, что письмо не выделено.
* Авторизация почтового ящика. Создание тестового письма. Перемещение письма в папку "Социальные сети". Проверка в соответствующей папке, что письмо переместилось. Удаление тестового письма.
* Авторизация почтового ящика. Создание тестового письма. Перемещение письма в папку "Социальные сети". Перемещение из папки "Социальные сети" в папку "Входящие". Проверка в соответствующей папке, что письмо переместилось. Удаление тестового письма.
* Авторизация почтового ящика. Создание тестового письма. Перемещение письма в папку "Рассылки". Проверка в соответствующей папке, что письмо переместилось. Удаление тестового письма.
* Авторизация почтового ящика. Создание тестового письма. Перемещение письма в папку "Рассылки". Перемещение из папки "Рассылки" в папку "Входящие". Проверка в соответствующей папке, что письмо переместилось. Удаление тестового письма.