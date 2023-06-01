from sqlalchemy import create_engine, Column, Integer,VARCHAR, Text, ForeignKey
from decouple import config
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine(f'postgresql://{config("USER")}:{config("PASSWORD")}'
                       f'@{config("HOST")}:{config("PORT")}/{config("NAME")}')

print("connect")

Base = declarative_base()


class Laptop(Base):
    __tablename__ = "laptop"
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    description = Column(Text)
    image = Column(Text)
    price = Column(VARCHAR(100))

    def __repr__(self):
        return self.title


Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()

# vuz1 = Vuz(name="KSTU")
# vuz2 = Vuz(name="KRSU")
# vuz3 = Vuz(name="MUK")
# session.add(vuz1)
# session.add(vuz2)
# session.add(vuz3)
# session.commit()
# with Session() as session:
#     st = Student(full_name="Tabyldieva Nazgul", age=25, vuz_id=1)
#     st2 = Student(full_name="Suranchiev Mirbek", age=28, vuz_id=2)
#     st3 = Student(full_name="Largin Andrei", age=22, vuz_id=3)
#     session.add(st)
#     session.add(st2)
#     session.add(st3)
#     session.commit()

# users = session.query(Student).all()
# for i in users:
#     print(i.vuz_id)

# user = session.query(Student).filter(Student.vuz_id==2).first()
# print(user.full_name)
# user.full_name = "Suranchiev Mirba"
# session.commit()

# user = session.query(Student).get(1)
# session.delete(user)
# session.commit()