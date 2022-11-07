from src.models import Manufacturer, Car, Color, CarColor
from src.database import db_session as session

if __name__ == '__main__':
    manufactuers = Manufacturer.query.all()
    cars = Car.query.all()
    colors = Color.query.filter_by(color='Yellow').first()
    cars_colors_by_color = CarColor.query.filter_by(color_id='1').all()
    cars_colors_by_car = CarColor.query.filter_by(car_id='2').all()

    manufactuer_by_name = Manufacturer.query.filter_by(name='Ford').first()
    cars_by_manufacturer = (
        Car.query
        .join(Manufacturer, Car.manufacturer_id == Manufacturer.id)
        .filter_by(name='Ford')
        .all()
    )

    cars_by_color = (
        Car.query
        .join(CarColor, Car.id == CarColor.car_id)
        .join(Color, Color.id == CarColor.color_id)
        .filter_by(color='Yellow')
        .all()
    )
    cars_by_color2 = (
        session.query(Car)
        .join(CarColor, Car.id == CarColor.car_id)
        .join(Color, Color.id == CarColor.color_id)
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

    print('filtro de carro por cor Amarelo')
    for car in cars_by_color:
        print(car.to_json())
    print('filtro de carro por cor Amarelo 2')
    for car in cars_by_color2:
        print(car.to_json())

    for car in cars_colors_by_color:
        print(car.to_json())

    for car in cars_colors_by_car:
        print(car.to_json())

