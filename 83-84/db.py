from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()

class Questions(Base):
    __tablename__ = 'questions'

    id = Column(Integer, autoincrement=True, primary_key=True)
    text = Column(String)
    number = Column(Integer)

    answers = relationship('Answers', back_populates='question')

    def __repr__(self):
        return f'{self.id}-{self.text}'


class Answers(Base):
    __tablename__ = 'answers'

    id = Column(Integer, autoincrement=True, primary_key=True)
    text = Column(String)
    question_id = Column(Integer, ForeignKey('questions.id'))

    question = relationship('Questions', back_populates='answers')

    def __repr__(self):
        return f'{self.id}-{self.text}'

class DB():
    def __init__(self):
        self.engine = create_engine("sqlite:///quiz.db")
        self.Session = sessionmaker(bind=self.engine)

    def get_next_question(self, prev_number=0):
        next_number = prev_number + 1

        with self.Session() as session:
            question = session.query(Questions).filter_by(number=next_number).first()
        return question

    def get_answers(self, question_id):
        with self.Session() as session:
            question = session.query(Answers).filter_by(question_id=question_id).all()
        return question

db = DB()
# поулчил вопрос
res = db.get_next_question()
# получил ответы, передав id вопроса
print(db.get_answers(res.id))
