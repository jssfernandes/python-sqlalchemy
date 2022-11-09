import os
import random
# from datetime import datetime
from src.models import db, Manufacturer, Car, Color
from src.database import db_session, datetime

if not os.path.exists(os.path.join(os.path.abspath(os.curdir), 'instance')):
    os.mkdir(os.path.join(os.path.abspath(os.curdir), 'instance'))

manufacturers = Manufacturer.query.all()
colors = Color.query.all()
cars = Car.query.all()

if manufacturers is None or not manufacturers:
    create_manufacturer = [
        Manufacturer(id=1, name="Chevrolet", founded=datetime(1911, 11, 3)),
        Manufacturer(id=2, name="Ford", founded=datetime(1903, 6, 15)),
        Manufacturer(id=3, name="Volkswagen", founded=datetime(1937, 5, 28)),
    ]
    for create in create_manufacturer:
        db_session.add(create)

if colors is None or not colors:
    create_color = [
        Color(id=1, color="Black"),
        Color(id=2, color="Blue"),
        Color(id=3, color="Green"),
        Color(id=4, color="Red"),
        Color(id=5, color="Yellow"),
        Color(id=6, color="White"),
    ]
    for create in create_color:
        db_session.add(create)


def colors_cars():
    colors_of_cars = []
    quantity = random.randint(1, 5)
    list_colors = random.sample(range(0, 5), quantity)
    print(f'quantity: {quantity}')
    print(f'list of colors: {list_colors}')
    for color in list_colors:
        colors_of_cars.append(create_color[color])
    return colors_of_cars


if cars is None or not cars:
    cor_carro1 = [create_color[3],create_color[2],create_color[0]]
    cor_carro2 = [create_color[2],create_color[5],create_color[1]]
    cor_carro3 = [create_color[0],create_color[2],create_color[4]]
    cor_carro4 = create_color
    cor_carro5 = [create_color[3],create_color[2]]
    create_car = [
        Car(colors=colors_cars(),id=1,model="Chevelle", year_manufacture=1970, country_origin="USA", engine_power=450, manufacturer_id=create_manufacturer[0].id),
        Car(colors=colors_cars(),id=2,model="Mustang GT 500", year_manufacture=11969, country_origin="USA", engine_power=430, manufacturer_id=create_manufacturer[1].id),
        Car(colors=colors_cars(),id=3,model="Gol GTi", year_manufacture=11989, country_origin="BR", engine_power=120, manufacturer_id=create_manufacturer[2].id),
        Car(colors=create_color,id=4,model="Opala SS", year_manufacture=11974, country_origin="BR", engine_power=250, manufacturer_id=create_manufacturer[0].id),
        Car(colors=colors_cars(),id=5,model="Maverick GT", year_manufacture=11974, country_origin="BR", engine_power=199, manufacturer_id=create_manufacturer[1].id),
    ]
    for create in create_car:
        db_session.add(create)


db_session.commit()
