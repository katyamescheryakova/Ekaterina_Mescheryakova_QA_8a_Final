import configuration
import requests
import data

#Оъявляется функция на создание заказа
def post_new_order(body):
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body,
        headers=data.headers
    )
#Проверяется ответ об успешном создании зсказа
    assert response.status_code == 201

    return response

#Объявляется функция на получение трек-номера
def get_track_number():
    response = post_new_order(data.order_body)
    track_number = str(response.json()["track"])  # Преобразование номер трека в тип данных Строка
    new_headers = data.headers.copy()
    new_headers["track"] = track_number

    # Выполняется запрос для получения информации по треку
    response = requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_PATH + "?t=" + track_number)

    return response
