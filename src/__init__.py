import os
# from datetime import datetime
from src.models import Manufacturer, Car, Color, CarColor, db
from src.database import db_session, datetime

if not os.path.exists(os.path.join(os.path.abspath(os.curdir), 'instance')):
    os.mkdir(os.path.join(os.path.abspath(os.curdir), 'instance'))

manufacturers = Manufacturer.query.all()
colors = Color.query.all()
cars = Car.query.all()
cars_colors = CarColor.query.all()

if manufacturers is None or not manufacturers:
    create_manufacturer = [
        Manufacturer("Chevrolet", datetime(1911, 11, 3)),
        Manufacturer("Ford", datetime(1903, 6, 15)),
        Manufacturer("Volkswagen", datetime(1937, 5, 28)),
    ]
    for create in create_manufacturer:
        db_session.add(create)
    # db_session.add(create_manufacturer[0])
    # db_session.add(create_manufacturer[1])
    # db_session.add(create_manufacturer[2])

if colors is None or not colors:
    create_color = [
        Color("Black"),
        Color("Blue"),
        Color("Green"),
        Color("Red"),
        Color("Yellow"),
        Color("White"),
    ]
    for create in create_color:
        db_session.add(create)
    # db_session.add(create_color[0])
    # db_session.add(create_color[1])
    # db_session.add(create_color[2])
    # db_session.add(create_color[3])
    # db_session.add(create_color[4])
    # db_session.add(create_color[5])

if cars is None or not cars:
    create_car = [
        Car("Chevelle", 1970, "USA", 450, create_manufacturer[0]),
        Car("Mustang GT 500", 1969, "USA", 430, create_manufacturer[1]),
        Car("Gol GTi", 1989, "BR", 120, create_manufacturer[2]),
        Car("Opala SS", 1974, "BR", 250, create_manufacturer[0]),
        Car("Maverick GT", 1974, "BR", 199, create_manufacturer[1]),
    ]
    for create in create_car:
        db_session.add(create)
    # db_session.add(create_car[0])
    # db_session.add(create_car[1])
    # db_session.add(create_car[2])
    # db_session.add(create_car[3])
    # db_session.add(create_car[4])


if cars_colors is None or not cars_colors:
    create_car_color = [
        CarColor(create_car[0], create_color[1]),
        CarColor(create_car[0], create_color[0]),
        CarColor(create_car[0], create_color[2]),
        CarColor(create_car[1], create_color[3]),
        CarColor(create_car[1], create_color[4]),
        CarColor(create_car[1], create_color[1]),
        CarColor(create_car[1], create_color[5]),
        CarColor(create_car[2], create_color[1]),
        CarColor(create_car[2], create_color[0]),
        CarColor(create_car[2], create_color[2]),
        CarColor(create_car[2], create_color[4]),
        CarColor(create_car[3], create_color[5]),
        CarColor(create_car[3], create_color[1]),
        CarColor(create_car[3], create_color[2]),
        CarColor(create_car[4], create_color[0]),
        CarColor(create_car[4], create_color[1]),
    ]
    for create in create_car_color:
        db_session.add(create)


db_session.commit()
