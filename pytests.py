import logging
import time
import requests
from models import Objects, Object, Departments

# Настройка логгера
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
    force=True
)
logger = logging.getLogger(__name__)
BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1"
# инструкция к API: https://metmuseum.github.io

class LoggedSession:                    # логирование из единой точки
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def request(self, method, url, **kwargs):
        # Формируем полный URL
        full_url = url if "://" in url else f"{self.base_url}{url}"

        # Логируем запрос
        print()
        logger.info(f"Запрос: {method} {full_url}")
        logger.debug(f"Параметры: {kwargs.get('params')}")
        logger.debug(f"Заголовки: {kwargs.get('headers')}")
        logger.debug(f"Тело запроса: {kwargs.get('json') or kwargs.get('data')}")

        # Выполняем запрос
        start_time = time.time()
        response = self.session.request(method, full_url, **kwargs)
        elapsed = time.time() - start_time

        # Логируем ответ
        logger.info(f"Ответ: {response.status_code} за {elapsed:.3f} сек.")
        try:
            logger.debug(f"Тело ответа: {response.json()}")
        except ValueError:
            logger.debug(f"Текст ответа: {response.text}")

        return response

    def get(self, url, **kwargs):
        return self.request("GET", url, **kwargs)
    # можно добавить и др, например post, put, delete

client = LoggedSession(base_url=BASE_URL)



'''  ------------------  T E S T S  -----------------  '''

def test_get_availability_website():
    r = requests.get('https://collectionapi.metmuseum.org')
    assert r.ok
    assert r.text == "Hello World"


def test_get_objects():
    response = client.get(f"{BASE_URL}/objects")
    assert response.ok
    assert Objects.model_validate(response.json())


def test_get_object_by_id():
    object_id = 1  # Пример существующего objectID
    response = client.get(f"{BASE_URL}/objects/{object_id}")
    assert response.ok
    assert Object.model_validate(response.json())

def test_get_object_invalid():
    object_id = -1  # Предполагается, что такого objectID не существует
    response = client.get(f"{BASE_URL}/objects/{object_id}")
    assert response.status_code == 404
    assert response.reason == "Not Found"


def test_get_departments():
    response = client.get(f"{BASE_URL}/departments")
    assert response.ok
    assert Departments.model_validate(response.json())


def test_search_objects_by_keyword():
    keyword = "sunflowers"
    response = client.get(f"{BASE_URL}/search", params={"q": keyword})
    assert response.ok
    assert Objects.model_validate(response.json())

def test_search_with_invalid_keyword():
    keyword = ""
    response = client.get(f"{BASE_URL}/search", params={"q": keyword})
    assert response.ok
    assert Objects.model_validate(response.json())


def test_search_with_filters1():
    keyword = "sunflowers"
    ishighlight = True
    response = client.get(f"{BASE_URL}/search", params={"q": keyword, "isHighlight": ishighlight})
    assert response.ok
    assert Objects.model_validate(response.json())

def test_search_with_filters2():
    keyword = "cat"
    department_id = 6  # Asian Art
    response = client.get(f"{BASE_URL}/search", params={"q": keyword, "departmentId": department_id})
    assert response.ok
    assert Objects.model_validate(response.json())


def test_search_with_pagination():
    keyword = "flowers"
    per_page = 10
    response = client.get(f"{BASE_URL}/search", params={"q": keyword, "perPage": per_page})
    assert response.ok
    assert Objects.model_validate(response.json())

