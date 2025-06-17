# 🧪 Python Project with Pydantic, Requests and Pytest

Небольшой Python-проект в рамках прохождения летней практики в ВУЗе, использующий:
- [Pydantic](https://docs.pydantic.dev/latest) — для валидации данных.
- [Requests](https://docs.python-requests.org/en/latest/) — для HTTP-запросов.
- [Pytest](https://docs.pytest.org/en/latest/) — для тестирования.
- [Logging](https://docs.python.org/3.10/library/logging.html) — для логирования тестов.
- И сам Python v3.10

---

## 🧩 Содержание
В работе тестируется [API коллекции Метрополитен-музея](https://metmuseum.github.io). Для каждого endpoint определена соответсвующая модель в файле models.py.
В файле pytests.py написаны 10 тестов, проверяющие различные аспекты ответов API.
Также, в этом файле описан класс LoggedSession, который является обёрткой над requests.get для удобного логирования всех входящие и исходящие данные. В данном варианте реализовано логирование метода get.

---

## 🧪 Тесты
Запустите тесты с помощью cmd: 
```bash
  pytest pytests.py
```
А также используйте флаги, для отображения логов в консоле:
```bash
  pytest pytests.py -v --capture=no
```
А ещё, можно запустить тест отдельно, например: 
```bash
  pytest pytests.py::test_search_objects_by_keyword -v --capture=no
```
