from sqlalchemy import create_engine, Column, Integer, VARCHAR, ForeignKey
from decouple import config
from sqlalchemy.orm import declarative_base, relationship,sessionmaker

engine = create_engine(f'postgresql://{config("USER")}:{config("PASSWORD")}'
                       f'@{config("HOST")}:{config("PORT")}/{config("DB")}')
print("connect")

Base = declarative_base()


class Vuz(Base):
    __tablename__ = "vuz"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100), nullable=False)



class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    full_name = Column(VARCHAR(100), nullable=False)
    age = Column(Integer)
    vuz_id = Column(Integer, ForeignKey("vuz.id"))
    vuz = relationship("Vuz", backref="vuzy")

    def __repr__(self):
        return self.full_name

Base.metadata.create_all(engine)




Session = sessionmaker(bind=engine)
session = Session()

# vuz1 = Vuz(name="KSTU")
# vuz2 = Vuz(name="KRSU")
# vuz3 = Vuz(name="MUK")
# session.add(vuz1)
# session.add(vuz2)
# session.add(vuz3)
# session.commit()
#=====================================================================
# with Session() as session:
#     st1 = Student(full_name='Tabyldieva Nazgul',age=25,vuz_id=1)
#     st2 = Student(full_name='Suranchiev Mirbek',age=28,vuz_id=2)
#     st3 = Student(full_name='Largin Andrei',age=22,vuz_id=3)
#     session.add(st1)
#     session.add(st2)
#     session.add(st3)
#     session.commit()
#=====================================================================
# users = session.query(Student).all()
# for i in users:
    # print(i.full_name)
    
    
# users = session.query(Student).filter(Student.vuz_id==2).all()
# users = session.query(Student).filter(Student.vuz_id==2).first()
# print(users)


# user = session.query(Student).filter(Student.vuz_id==2).first()

# user.full_name='SUranchiev Mirba'
# session.commit()
# print(user.full_name)


# users = session.query(Student).get(1)
# session.delete(users)
# session.commit()
# print(users)



# all_query = session.query(Vuz,Student).join(Student, Vuz.id==Student.vuz_id).all()

# for i,j in all_query:
#     print(i.name,j.full_name)
#===============================================================================================

'''


5записей для студ
'''
#=====================================================================
