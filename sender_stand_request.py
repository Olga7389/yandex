# Ольга Андрюхина, 7-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data

#Cоздание заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body)
#Сохранение трека заказа
def get_new_track():
    response = post_new_order(data.order_body)
    track = response.json()["track"]
    return track
#Получения заказа по треку
def get_order_body(track):
    params_with_track= {"t": track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                        params=params_with_track)