import sender_stand_request
import data

def test_get_track_number():
    #Выполнение запроса на создание нового заказа
    response = sender_stand_request.post_new_order(data.order_body)

    # Проверка успешного создания заказа
    assert response.status_code == 201

    # Получение номера трека созданного заказа
    track_number = response.json()["track"]
    assert track_number is not None

    # Получение заказа по номеру трека
    response = sender_stand_request.get_track_number()

    # Проверка, что заказ получен (код ответа 200)
    assert response.status_code == 200












