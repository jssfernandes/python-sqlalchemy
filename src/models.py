import json
import src.database as db


class Manufacturer(db.Model):
    __tablename__ = 'manufacturer'

    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    name = db.Column(db.String(99))
    founded = db.Column(db.Date)

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


class Color(db.Model):
    __tablename__ = 'color'

    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    color = db.Column(db.String(99))

    # usando o Relationships para relacionamento de tabelas muitos para muitos com a tabela car
    cars = db.relationship(
        "Car",
        secondary='car_color',
        back_populates="colors"
    )

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
        secondary='car_color',
        back_populates="cars"
    )

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

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


# objeto criado para os relacionamentos entre as tabelas do tipo Many to Many
# usando para o relacionamento relacionamento de tabelas muitos para muitos entre as tabelas car e color
class CarColor(db.Model):
    __tablename__ = "car_color"
    car_id = db.Column(db.Integer, db.ForeignKey(Car.id), primary_key=True)
    color_id = db.Column(db.Integer, db.ForeignKey(Color.id), primary_key=True)


db.init_db()
