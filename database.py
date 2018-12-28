from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///rta.db', echo=True)
Base = declarative_base()

class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True, autoincrement = True)
    name = Column(String(100))
    company = Column(String(100))
    post = Column(String(50))
    persons = Column(Integer)
    edu = Column(String(20))
    degree = Column(String(20))
    majors = Column(String(500))
    target = Column(String(20))
    status = Column(String(10))

    def show(self):
        return {
                'id': self.id,
                'name': self.name,
                'company': self.company,
                'post': self.post,
                'persons': self.persons,
                'edu': self.edu,
                'degree': self.degree,
                'majors': self.majors,
                'target': self.target,
                'status': self.status
            }

def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)

DBSession = sessionmaker(bind=engine)

session = DBSession()
# project = Project(name='Bob1', company='sdfs')
# session.add(project)
ret = session.query(Project).all()
for project in ret:
    print(project.show())

session.commit()
session.close()

