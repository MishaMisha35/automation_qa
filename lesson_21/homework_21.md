Завдання на створення моделі з допомогою Pony ORM:

1. Створіть базу даних, яка має три таблиці:

    - Таблиця `Items`:
        - Поле `id` - первинний ключ (Primary Key), автоінкрементне ціле число.
        - Поля `title_ua`, `title_or`, `type_src`, `year`, `director`, `description`, `poster`, `json`, `imdb` - строкові поля.

    - Таблиця `Seasons`:
        - Поле `id` - первинний ключ (Primary Key), автоінкрементне ціле число.
        - Поля `source_id`, `name`, `season`, `title` - строкові поля.

    - Таблиця `Links`:
        - Поле `id` - первинний ключ (Primary Key), автоінкрементне ціле число.
        - Поля `source_id`, `series_id`, `quality`, `its_work`, `type_src`, `m3u_links`, `subs` - строковий тип полів.

2. Зв'яжіть моделі між собою:

    - В `Items` існує зв'язок один-до-багатьох з `Links` через поле `id`.
    - В `Seasons` існує зв'язок один-до-багатьох з `Links` через поле `source_id`.

3. Задайте параметри бази данихякі можна передавати до функції `db.bind()`:

    - Для MySQL:
        - Постачальник: 'mysql'
        - Хост: 'localhost'
        - Користувач: 'root'
        - Пароль: 'root'
        - Назва бази даних: 'uakino'

    - Для SQLite:
        - Постачальник: 'sqlite'
        - Назва файлу: 'uakino.db'
        - Створити базу даних, якщо її не існує.
4. Використовуйте декоратори `@db_session` для функцій `check_in_base`, `add_to_db`, `add_m3u`, та `save`, щоб забезпечити їхню роботу в межах транзакцій.
