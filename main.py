from sqlalchemy.ext.serializer import loads, dumps
from src.models import Manufacturer, Car, Color
from src.database import db_session as session

if __name__ == '__main__':
    manufactuers = Manufacturer.query.all()
    cars = Car.query.all()
    colors = Color.query.filter_by(color='Yellow').first()
    cars_colors_by_color = Color.query.join(Color.cars).filter_by(id=1).all()
    cars_colors_by_car = Color.query.join(Color.cars).filter_by(id=2).all()

    manufactuer_by_name = Manufacturer.query.filter_by(name='Ford').first()
    cars_by_manufacturer = (
        Car.query
        .join(Manufacturer)
        .filter_by(name='Ford')
        .all()
    )

    cars_by_color = (
        Car.query
        .join(Car.colors)
        .filter_by(color='White')
        .all()
    )
    cars_by_color2 = (
        session.query(Car)
        .join(Car.colors)
        .filter_by(color='Yellow')
        .all()
    )

    for manufactuer in manufactuers:
        print(manufactuer.to_json())

    for car in cars:
        print(car.to_json())

    print(manufactuer_by_name.to_json())

    for car in cars_by_manufacturer:
        print(car.to_json())

    print('filtro de carro por cor Branco')
    for car in cars_by_color:
        print(car.to_json())
    print('filtro de carro por cor Amarelo')
    for car in cars_by_color2:
        print(car.to_json())

    for car in cars_colors_by_color:
        print(car.to_json())

    for car in cars_colors_by_car:
        print(car.to_json())

