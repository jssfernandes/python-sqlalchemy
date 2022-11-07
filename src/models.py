import src.database as db
import json


# association_table = db.Table(
#     "association_table",
#     db.Model.metadata,
#     db.Column("left_id", db.ForeignKey("left_table.id"), primary_key=True),
#     db.Column("right_id", db.ForeignKey("right_table.id"), primary_key=True),
# )

class Manufacturer(db.Model):
    __tablename__ = 'manufacturer'

    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    name = db.Column(db.String(99))
    founded = db.Column(db.Date)

    def __init__(self, name, founded):
        self.name = name
        self.founded = founded

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

    @property
    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)


class Color(db.Model):
    __tablename__ = 'color'

    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    color = db.Column(db.String(99))

    def __init__(self, color):
        self.color = color

    def to_json(self):
        return json.dumps(
            dict(
                id=self.id,
                name=self.color,
            )
            , sort_keys=True, default=str,
            # indent=4,
        )

    @property
    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)


class Car(db.Model):
    __tablename__ = 'car'
    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    model = db.Column(db.String(140))
    year_manufacture = db.Column(db.Integer)
    country_origin = db.Column(db.String(140))
    engine_power = db.Column(db.Integer)

    # manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey(Manufacturer.id))
    # usando o Relation para relacionamento de tabelas
    manufacturer = db.relation(Manufacturer, backref=db.backref('car', lazy='dynamic'))

    def __init__(self, model, year_manufacture, country_origin, engine_power, manufacturer):
        self.model = model
        self.year_manufacture = year_manufacture
        self.country_origin = country_origin
        self.engine_power = engine_power
        self.manufacturer = manufacturer

    def to_json(self):
        return json.dumps(
            dict(
                id=self.id,
                model=self.model,
                year_manufacture=self.year_manufacture,
                country_origin=self.country_origin,
                engine_power=self.engine_power,
                manufacturer=json.loads(self.manufacturer.to_json()),
            )
            , sort_keys=True, default=str,
            # indent=4,
        )

    @property
    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)


class CarColor(db.Model):
    __tablename__ = "car_color"
    car_id = db.Column(db.ForeignKey(Car.id), primary_key=True)
    color_id = db.Column(db.ForeignKey(Color.id), primary_key=True)

    # usando o Relation para relacionamento de tabelas, no caso esse relacionamento se trata do Many to Many
    car = db.relation(Car, backref=db.backref('car_color', lazy=True))
    color = db.relation(Color, backref=db.backref('car_color', lazy='dynamic'))

    def __init__(self, car, color):
        self.car = car
        self.color = color

    def to_json(self):
        return json.dumps(
            dict(
                car=json.loads(self.car.to_json()),
                color=json.loads(self.color.to_json()),
            )
            , sort_keys=True, default=str,
            # indent=4,
        )

    @property
    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)


db.init_db()
