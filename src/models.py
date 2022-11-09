import src.database as db
import json


# usando para o relacionamento relacionamento de tabelas muitos para muitos entre as tabelas car e color
car_color = db.Table(
    'car_color',
    db.Model.metadata,
    # db.declarative_base().metadata,
    db.Column(
        'car_id',
        db.Integer,
        db.ForeignKey('car.id'),
        primary_key=True
    ),
    db.Column(
        'color_id',
        db.Integer,
        db.ForeignKey('color.id'),
        primary_key=True
    )
)


class Manufacturer(db.Model):
    __tablename__ = 'manufacturer'

    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    name = db.Column(db.String(99))
    founded = db.Column(db.Date)

    # def __init__(self, name, founded):
    #     self.name = name
    #     self.founded = founded

    def to_json(self):
        return json.dumps(
            dict(
                id=self.id,
                name=self.name,
                founded=self.founded,
            )
            , sort_keys=True, default=str,
            # indent=4,
        )

    # @property
    # def __eq__(self, other):
    #     return type(self) is type(other) and self.id == other.id
    #
    # def __ne__(self, other):
    #     return not self.__eq__(other)


class Color(db.Model):
    __tablename__ = 'color'

    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    color = db.Column(db.String(99))

    # usando o Relationships para relacionamento de tabelas muitos para muitos com a tabela car
    cars = db.relationship(
        "Car",
        secondary=car_color,
        back_populates="colors"
    )
    # OUTRA FORMA DE RELACIONAMENTOS
    # cars = db.relationship(
    #     "Car",
    #     secondary=car_color,
    #     # back_populates="colors",
    #     backref='colors',
    #     lazy='dynamic',
    # )

    # def __init__(self, color):
    #     self.color = color

    def to_json(self):
        return json.dumps(
            dict(
                id=self.id,
                name=self.color,
                # cars=self.cars
            )
            , sort_keys=True, default=str,
            # indent=4,
        )

    # @property
    # def __eq__(self, other):
    #     return type(self) is type(other) and self.id == other.id
    #
    # def __ne__(self, other):
    #     return not self.__eq__(other)


class Car(db.Model):
    __tablename__ = 'car'
    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    model = db.Column(db.String(140))
    year_manufacture = db.Column(db.Integer)
    country_origin = db.Column(db.String(140))
    engine_power = db.Column(db.Integer)

    manufacturer_id = db.Column(db.Integer, db.ForeignKey(Manufacturer.id))
    # usando o Relationships para relacionamento de tabelas
    manufacturers = db.relationship(Manufacturer)
    # usando o Relationships para relacionamento de tabelas muitos para muitos com a tabela color
    colors = db.relationship(
        "Color",
        secondary=car_color,
        back_populates="cars"
    )
    # OUTRA FORMA DE RELACIONAMENTOS
    # _colors = db.relationship(
    #     "Color",
    #     secondary=car_color,
    #     # back_populates="cars",
    #     backref=db.backref('car_color_backref', lazy='dynamic')
    # )

    # def __init__(self, model, year_manufacture, country_origin, engine_power, manufacturer):
    #     self.model = model
    #     self.year_manufacture = year_manufacture
    #     self.country_origin = country_origin
    #     self.engine_power = engine_power
    #     self.manufacturer = manufacturer

    def to_json(self):
        return json.dumps(
            dict(
                id=self.id,
                model=self.model,
                year_manufacture=self.year_manufacture,
                country_origin=self.country_origin,
                engine_power=self.engine_power,
                manufacturer=json.loads(self.manufacturers.to_json()),
                color=[json.loads(color.to_json()) for color in self.colors]
            )
            , sort_keys=True, default=str,
            # indent=4,
        )

    # @property
    # def __eq__(self, other):
    #     return type(self) is type(other) and self.id == other.id
    #
    # def __ne__(self, other):
    #     return not self.__eq__(other)


# class CarColor(db.Model):
#     __tablename__ = "car_color"
#     car_id = db.Column(db.ForeignKey(Car.id), primary_key=True)
#     color_id = db.Column(db.ForeignKey(Color.id), primary_key=True)
#
#     # usando o Relationships para relacionamento de tabelas, no caso esse relacionamento se trata do Many to Many
#     car = db.relationship(Car)
#     color = db.relationship(Color)
#
#     # def __init__(self, car, color):
#     #     self.car = car
#     #     self.color = color
#
#     def to_json(self):
#         return json.dumps(
#             dict(
#                 car=json.loads(self.car.to_json()),
#                 color=json.loads(self.color.to_json()),
#             )
#             , sort_keys=True, default=str,
#             # indent=4,
#         )
#
#     @property
#     def __eq__(self, other):
#         return type(self) is type(other) and self.id == other.id
#
#     def __ne__(self, other):
#         return not self.__eq__(other)


db.init_db()
