# DZ_6_Django

ДЗ № 1.
Задание 1.
Для начала работы над задачей выполните первые шаги:

- Настройте виртуальное окружение.
- Создайте новый Django-проект.
  Задание 2.
  После успешного создания проекта сделайте первую настройку. Для этого:
- Создайте первое приложение с названием catalog.
- Внесите начальные настройки проекта.
- Сделайте настройку урлов (URL-файлов) для нового приложения.
  Задание 3.
  Подготовьте два шаблона для домашней страницы и страницы с контактной информацией.
- Для создания шаблонов лучше использовать UIkit Bootstrap. Это удобный набор элементов, которые уже стилизованы и
  готовы к использованию. UIkit Bootstrap помогает избежать самостоятельной верстки макетов.
- Если возникнут проблемы при создании собственного интерфейса, возьмите за основу данный
  шаблон: https://github.com/oscarbotru/.
  Задание 4.
  В приложении в контроллере реализуйте два контроллера:
- Контроллер, который отвечает за отображение домашней страницы.
- Контроллер, который отвечает за отображение контактной информации.
  *Дополнительное задание (желательно, но не обязательно выполнять)
  Реализуйте обработку сбора обратной связи от пользователя, который зашел на страницу контактов и отправил свои данные
  для обратной связи.

-----------------------------------------------------------------------------------------------------------
ДЗ № 2.
Задание 1.
Подключите СУБД PostgreSQL для работы в проекте, для этого:

- Создайте базу данных в ручном режиме.
- Внесите изменения в настройки подключения.
  Задание 2.
  В приложении каталога создайте модели:
- Product,
- Category.
  Опишите для них начальные настройки. К начальным настройкам модели относятся метод __str__ и class Meta с описанием
  свойств модели.
  Задание 3.
  Для каждой модели опишите следующие поля:
- Product:
  -- Наименование
  -- Описание
  -- Изображение (превью)
  -- Категория
  -- Цена за покупку
  -- Дата создания (записи в БД)
  -- Дата последнего изменения (записи в БД)
- Category:
  -- Наименование
  -- Описание
  Свяжите продукт и категорию, используя связь между таблицами «Один ко многим».
  У одной категории может быть много продуктов, но у одного продукта может быть только одна категория.
  Воспользуйтесь специальным полем модели — ForeignKey().
  При необходимости подробнее про то, как работает такое поле, можно почитать
  тут: https://metanit.com/python/django/5.6.php
  Поля «Дата создания» и «Дата последнего изменения» стали стандартом для моделей. Их общепринятые названия — created_at
  и updated_at соответственно.
  Примечание:Для поля с изображением необходимо добавить соответствующие настройки (MEDIA URL, MEDIA ROOT, настроить URL
  для отображения медиаданных) в проект, а также установить библиотеку для работы с изображениями
  Pillow. Не забудьте обновить файл с зависимостями для проекта после установки новой библиотеки.
  Задание 4.
  Перенесите отображение моделей в базу данных с помощью инструмента миграций, для этого:
- создайте миграции для новых моделей;
- примените миграции;
- внесите изменения в модель продукта, добавьте поле «Дата производства продукта» (manufactured_at), примените
  обновление структуры с помощью миграций;
  откатите миграцию до состояния, когда поле «Дата производства продукта» (manufactured_at) для модели продукта еще не
  существовало, и удалите лишнюю миграцию.
  Важно сохранять всю историю миграций проекта для сохранения целостности базы данных проекта.
  Не забудьте добавить все выполненные миграции в коммит, а затем отправить в удаленный репозиторий на GitHub.
  Подсказка: Чтобы сбросить миграцию до определенной (по номеру), можно воспользоваться командой
  python manage.py migrate имя_приложения номер_миграции (например, 0003)
  Номер миграции написан в названии файла.
  Задание 5.
- Для моделей категории и продукта настройте отображение в административной панели. Для категорий выведите id и
  наименование в список отображения, а для продуктов выведите в список id, название, цену и категорию.
- При этом интерфейс вывода продуктов настройте так, чтобы можно было результат отображения фильтровать по категории, а
  также осуществлять поиск по названию и полю описания.
  Подсказка: Все настройки производите в файле admin.py.
  Для управления полями, которые выводятся в списке в панели администратора, используйте настройку list_display, для
  настройки фильтров — list_filter, для управления поиском по полям — search_fields
  В общем случае настройки административной панели для модели будут выглядеть следующим образом:
  @admin.register(Имя_модели)
  class Имя_МоделиAdmin(admin.ModelAdmin):
  list_display = (список_полей_модели_для_отображения)
  list_filter = (список_полей_для_фильтрации)
  search_fields = (список_полей_для_поиска)
  Используйте различные настройки для управления функционалом административной панели. Использовать все три настройки
  одновременно необязательно.
  Задание 6.
- Через инструмент shell заполните список категорий, а также выберите список категорий, применив произвольные
  рассмотренные фильтры. В качестве решения приложите скриншот.
- Установите библиотеку ipython для комфортной работы с инструментом shell. Не забудьте зафиксировать изменения в файле
  зависимостей проекта.
  Подсказка: В рамках задания реализуйте ORM-запросы на создание объектов, получение всех объектов, получение одного
  объекта по
  id, фильтрацию объектов по определенному полю и исключение объектов из выборки.
  Для доступа к объектам используйте команду
  Model.objects… и дополняйте ее различными методами.
  Документацию для методов взаимодействия с базой данных через Django ORM можно найти
  тут: https://docs.djangoproject.com/en/5.0/topics/db/queries/  .
  Чтобы создать объект, необходимо использовать метод create() и перечислить все обязательные поля.
  Чтобы получить список всех объектов, необходимо использовать метод all().
  Чтобы получить один объект, используйте метод get().
  Чтобы отфильтровать объекты по определенному значению поля, необходимо использовать метод filter() и указать в скобках
  имя_поля=”значение_поля”.
  Чтобы исключить объекты из выборки по определенному значению поля, необходимо использовать метод exclude() и указать в
  скобках имя_поля=”значение_поля”.
- Сформируйте фикстуры для заполнения базы данных.
  Фикстуры создайте командой. Для управления кодировкой используйте опцию -Xutf8 для команды. Такой параметр уместно
  будет использовать на операционной системе Windows.
  В общем случае команда для создания фикстур будет выглядеть следующим образом:
  python -Xutf8 manage.py dumpdata имя_приложения > имя_папки_с_фикстурами/имя_приложения_data.json
- Напишите кастомную команду, которая умеет заполнять данные в базу данных, при этом предварительно ее зачищать от
  старых данных.
  Подсказка:
  Удалите все объекты с помощью ORM-запроса
  Модель.objects.all().delete(). Удалить необходимо продукты и категории.
  Сначала создайте категории, а затем создайте продукты, так как модели связаны между собой.
  Считайте данные из JSON-файла, который сформировали командой в шаге ранее.
  В методе handle() циклично пройдите данные из JSON и положите в список объект, который вы создадите на основе этих
  данных.
  Для связывания объектов используйте ORM-запрос на получение данных из БД.
  В общем случае команда будет выглядеть так:
  class Command(BaseCommand):
  @staticmethod
  def json_read_categories(): # Здесь мы получаем данные из фикстурв с категориями
  @staticmethod
  def json_read_catalog(): # Здесь мы получаем данные из фикстурв с продуктами
  def handle(self, *args, **options):
  Удалите все продукты
  Удалите все категории
  Создайте списки для хранения объектов
  product_for_create = []
  Обходим все значения категорий из фиктсуры для получения информации об одном объекте
  for category in Command.json_read_categories():
  category_for_create.append(
  Category(название_поля=значение_из_словаря, ..., название_поля=значение_из_словаря)
  )
  Создаем объекты в базе с помощью метода bulk_create()
  Category.objects.bulk_create(category_for_create)
  Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
  for product in Command.json_read_catalog():
  product_for_create.append(
  Product(название_поля=значение_из_словаря, ...,
  получаем категорию из базы данных для корректной связки объектов
  поле_категории=Category.objects.get(pk=значение_из_словаря), ...,
  название_поля=значение_из_словаря)
  )
  Создаем объекты в базе с помощью метода bulk_create()
  Product.objects.bulk_create(product_for_create)
  Примечание: Последний пункт можно реализовать в связке с инструментом работы с фикстурами, можно описать вставку
  данных отдельными
  запросами.

*Дополнительное задание (желательно, но не обязательно выполнять)
В контроллер отображения главной страницы добавить выборку последних пяти товаров и вывод их в консоль.
Создать модель для хранения контактных данных и попробовать вывести данные, заполненные через админку, на страницу с
контактами.

-----------------------------------------------------------------------------------------------------------
ДЗ № 3.
Задание 1.
Создайте новый контроллер и шаблон, которые будут отвечать за отображение отдельной страницы с товаром, на которой
необходимо вывести всю информацию о самом товаре.
Подсказка:
Контроллер для отдельной страницы с товаром — это отображение одного товара.
Товар хранится в базе данных с определенным id (в Django принято использовать pk (PrimaryKey)).
Чтобы получить данные о товаре, необходимо забрать данные о нем из базы данных. Сделать это с помощью ORM-запроса,
например:
Model.objects.get(pk=pk)
Для выполнения такого ORM-запроса наш контроллер должен получать аргумент pk (или id) на вход. Контроллеры получают
параметры из URL.
URL для контроллера отображения одного товара будет примерно таким:
path('/путь_к_продукту/<int:pk>', имя_контроллера, name='имя_url'),
Чтобы контроллер обработал переданный ему аргумент pk, нам нужно передать его в контроллер:
def имя_контроллера(request, pk):
Соберите контекст для шаблона. В контекст мы передаем данные, которые необходимо отобразить в шаблоне. Контекст
формируется в виде словаря и передается в функцию render:
context = {'object': Model.objects.get(pk=pk)}
Обратите внимание на название ключа в словаре контекста. Через него мы будем получать данные об объекте в шаблоне.
Контекст необходимо передать в шаблон для обработки:
return render(request, 'путь_к_шаблону', context)
В самом шаблоне мы получаем данные через обращение к переданному в контексте объекту (по ключу) и обращаемся к его полям
через точку, например:
<p>{{ object.name }}</p>
Примечание: Для создания шаблонов лучше использовать UI kit Bootstrap, при возникновении проблем можно брать за основу данный шаблон.

Задание 2.
В созданный ранее шаблон для главной страницы выведите список товаров в цикле. Для единообразия выводимых карточек
отображаемое описание необходимо обрезать после первых выведенных 100 символов.
Подсказка:
Все товары хранятся в базе данных.
Чтобы получить данные о товарах, необходимо забрать данные о них из базы данных. Сделать это с помощью ORM-запроса,
например:
Model.objects.all()
Соберите контекст для шаблона. В контекст мы передаем данные, которые необходимо отобразить в шаблоне. Контекст
формируется в виде словаря и передается в функцию render:
context = {'object_list': Model.objects.all()}
Обратите внимание на название ключа в словаре контекста. Через него мы будем получать данные об объекте в шаблоне.
Контекст необходимо передать в шаблон для обработки: return render(request, 'путь_к_шаблону', context)
В самом шаблоне нам нужно получать данные о каждом объекте из списка — в шаблоне необходимо запустить цикл
{% for object in object_list %}
Теперь мы циклично будем обходить каждый объект в списке и обращаться к его полям через точку, например:
{{ object.name }}
Не забудьте закрыть цикл {% endfor %}

Задание 3.
Из-за расширения количества шаблонов появляется слишком много повторяющегося кода, поэтому выделите общий (базовый)
шаблон, а также подшаблон с главным меню.
В подшаблон вынесите общие для всех кодовые части (HTML-код). Не забудьте разместить блок с контентом, куда будут
вставляться шаблоны, которые используют подшаблон:
{% block content %}
{% endblock %}
И подключите их к другим шаблонам с помощью
{% extends 'путь к базовому шаблону' %}
Код расширенного шаблона разместите внутри блока с контентом.
Примечание: При необходимости можно выделить больше общих шаблонов.

Задание 4.
Для выводимого изображения на странице реализуйте шаблонный фильтр или шаблонный тег, который преобразует переданный
путь в полный путь для доступа к медиафайлу.
Подсказка:
Создайте файл, например: your_app/templatetags/имя_файла.py
Создайте переменную для работы с библиотекой шаблонов Django: register = template.Library()
Внутри файла используйте декоратор register.simple_tag() для регистрации тега или register.filter() для фильтра.
Создайте функцию тега/фильтра, которая будет принимать данные и добавлять к ним media/ перед переданной строкой:
def mymedia(data):
if data:
return f'/media/{data}'
return '#'
В вашем шаблоне загрузите ваш тег/фильтр
{% load имя_файла %}
Используйте его для вывода пути к медиафайлу
<img class="card-img-top" src="{{ object.поле_изображения| название фильтра }}" ... >
или
<img class="card-img-top" src="{{ название тега object.поле_изображения }}" ... >

*Дополнительное задание (желательно, но не обязательно выполнять).
Добавьте функционал создания продукта через внешний интерфейс, созданный вручную.
Реализуйте постраничный вывод списка продуктов.

-----------------------------------------------------------------------------------------------------------
ДЗ № 4.
Задание 1.
Переведите имеющиеся контроллеры с FBV на CBV.
Не забудьте про контроллер контактов. Для его замены можно воспользоваться View или TemplateView. Документацию можно
найти https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.TemplateView.

Задание 2.
Создайте новую модель блоговой записи со следующими полями:

- заголовок;
- slug (реализовать через CharField);
- содержимое;
- превью (изображение);
- дата создания;
- признак публикации;
- количество просмотров.
  Для работы с блогом реализуйте CRUD для новой модели.
  CRUD реализуйте на основе CBV (ListView, DetailView, CreateView, UpdateView, DeleteView)
  Соблюдайте нейминг шаблонов для CBV контроллеров - …_list.html, …_detail.html, …_form.html.
  Примечание:
  Slug — человекопонятный URL, представляет собой набор символов, которые можно прочитать как связные слова или
  предложения в адресной строке. И служит уникальным идентификатором записи в рамках одной модели.
  Состоит из безопасных для обработки запроса символов: 0–9, a–z (обычно в нижнем регистре), символ -

Задание 3.
Модифицируйте вывод и обработку запросов, добавив следующую логику на уровне контроллеров:
При открытии отдельной статьи увеличивать счетчик просмотров.
Для решения этой задачи можно воспользоваться переопределением метода
get_object() в DetailView.
Подсказка:
Метод get_object() должен получать данные из вызова метода get_object() родителя (с помощью функции super()), вносить
необходимые изменения и сохранять объект в базе данных. Не забудьте вернуть измененный объект из метода.
Примерный код метода в DetailView:
def get_object(self, queryset=None):
self.object = super().get_object(queryset)
self.object.счетчик_просмотров += 1
self.object.сохранить()
return текущий_объект
Не забудьте определить верный queryset для View.

Выводить в список статей только те, которые имеют положительный признак публикации.
Признак публикации — булево поле. Статья может быть опубликована или нет (True/False).
Отфильтруйте статьи блога с помощью ORM-запроса.

При создании динамически формировать slug name для заголовка.
Для решения этой задачи можно воспользоваться переопределением метода form_valid() в CreateView.
Подсказка:
Метод form_valid() должен получать данные из формы, вносить необходимые изменения и сохранять объект в базе данных. Не
забудьте вызвать метод
super().form_valid() для корректного завершения работы метода.
Примерный код метода в CreateView:
def form_valid(self, форма):
if form.is_valid():
new_blog = форма.save()
new_blog.slug = преобразование заголовка в slug с помощью функции slugify()
new_blog.save()
return super().form_valid(форма)
После успешного редактирования записи необходимо перенаправлять пользователя на просмотр этой статьи.
Для решения этой задачи можно воспользоваться переопределением метода get_success_url() в UpdateView.
Метод должен возвращать объект reverse с параметрами args.

*Дополнительное задание (желательно, но не обязательно выполнять).
Когда статья достигает 100 просмотров, отправлять себе на почту поздравление с достижением.
Примечание: для отправки писем рекомендуем использовать почтовый сервис Яндекса

-----------------------------------------------------------------------------------------------------------
ДЗ № 5.
Задание 1.
Продолжаем работать с проектом из предыдущего домашнего задания. Для модели продуктов реализуйте механизм CRUD,
задействовав модуль django.forms.
Условия для пользователей:

- могут создавать новые продукты,
- не могут создавать продукты с запрещенными словами в названии и описании.
  Для исключения загрузки запрещенных продуктов реализуйте валидацию названия и описания продукта таким образом, чтобы
  нельзя было в них добавлять слова: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.
  Для настройки валидации внутри формы определите методы clean для полей (например,clean_name()).
  При наличии запрещенных слов — выбрасывайте ошибку forms.ValidationError() с соответствующим сообщением.
  Если валидация проходит успешно, возвращайте cleaned_data.

Задание 2.
Добавьте новую модель «Версия», которая должна содержать следующие поля:

- продукт,
- номер версии,
- название версии,
- признак текущей версии.
  При наличии активной версии реализуйте вывод в список продуктов информации об активной версии.
  Признак текущей версии — булево поле, является ли версия для продукта текущей для отображения на сайте или нет.
  Для отображения активной версии расширьте метод get_context_data() контроллера списка продуктов, получите данные о
  версиях продукта и выберите текущую (активную) версию для продукта.

Задание 3.
Добавьте реализацию работы с формами для версий продукта.
Примечание:
Все созданные формы нужно стилизовать так, чтобы они были в единой стилистике оформления всей платформы.
Для этого можно воспользоваться методом __init__ либо самостоятельно изучить пакет crispy-forms.
При стилизации формы методом __init__ можно создать класс-миксин для сокращения дублирования кода.
Для стилизации булевого поля используйте специальный стиль — form-check-input.

*Дополнительное задание (желательно, но не обязательно выполнять).
В один момент может быть только одна активная версия продукта, поэтому при изменении версий необходимо проверять, что
пользователь в качестве активной версии указал только одну. В случае возникновения ошибки вернуть сообщение пользователю
и попросить выбрать только одну активную версию.

-----------------------------------------------------------------------------------------------------------
ДЗ № 6.
Задание 1.
Создайте новое приложения для работы с пользователем. Определите собственную модель для пользователя, при этом задайте
электронную почту как поле для авторизации.
Также добавьте поля:

- аватар,
- номер телефона,
- страна.
  Не забудьте откатить миграции приложения auth до внесения изменений в настройки проекта и переопределения модели для
  авторизации.
  Если этого не сделать, вы не сможете взаимодействовать с базой данных.
  Чтобы откатить миграции приложения auth можно воспользоваться командой python manage.py migrate auth zero

Задание 2.
В сервисе реализуйте функционал аутентификации, а именно:

- Регистрация пользователя по почте и паролю.
  Создайте контроллер для регистрации, который будет взаимодействовать с формой регистрации — пользователю достаточно
  ввести почту и пароль.
- Верификация почты пользователя через отправленное письмо.
  В контроллере регистрации переопределите метод form_valid() и встройте автоматическую отправку электронного сообщения
  пользователю на указанный в форме регистрации адрес.
  Для отправки электронной почты воспользуйтесь встроенной в Django функцией send_mail().
  Не забудьте настроить почтовый сервер, через который будет происходить отправка электронной почты.
  Документацию можно найти тут https://docs.djangoproject.com/en/5.0/topics/email/.
- Авторизация пользователя.
  Создайте отдельный контроллер для авторизации (LoginView) и зарегистрируйте его в приложении.
- Восстановление пароля зарегистрированного пользователя на автоматически сгенерированный пароль.
  Создайте новый контроллер для восстановления пароля.
  В интерфейсе кнопка «Восстановить пароль» должна отображаться на странице входа.
  Пользователь вводит адрес электронной почты, в контроллере происходит генерация пароля, перезапись пароля для
  пользователя с соответствующим адресом электронной почты и отправка сообщения с новым паролем на адрес почты.
  Пароль можно сгенерировать с помощью библиотеки random.
  Помните, что пароль в базе данных хранится в захешированном виде. Для установки пароля пользователю можно
  воспользоваться функцией
  make_password() (посмотреть в документации про эту
  функцию https://docs.djangoproject.com/en/5.0/topics/auth/passwords/#django.contrib.auth.hashers.make_password).

Задание 3.
Все контроллеры, которые отвечают за работу с продуктами, закройте для анонимных пользователей, при этом создаваемые
продукты должны автоматически привязываться к авторизованному пользователю.
Чтобы закрыть контроллеры от анонимных пользователей, добавьте в CBV-контроллеры дополнительное наследование от
LoginRequiredMixin (документация
здесь https://docs.djangoproject.com/en/5.0/topics/auth/default/#the-loginrequiredmixin-mixin).
Не забудьте добавить поле для продуктов, которое будет указывать на владельца. Оно должно быть ссылкой на модель
пользователя.
Для автоматической привязки пользователя к продукту переопределите в контроллере создания продукта метод form_valid().
Текущий авторизованный пользователь доступен через self.request.user
— запишите его в только что созданный продукт и не забудьте сохранить объект в базу данных.

*Дополнительное задание (желательно, но не обязательно выполнять).
Добавьте интерфейс редактирования профиля пользователя.