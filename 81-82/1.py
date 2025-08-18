from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine

Base = declarative_base()

class Notes(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    text = Column(String)

    def __repr__(self):
        return f"{self.id}-{self.title}"

# engine = create_engine('sqlite:///notes.db', echo=True)
#
# # фабрика для создания сессий, подключаем базу
# Session = sessionmaker(bind=engine)
#
# # получаем первую заметку
# with Session() as session:
#     note = session.query(Notes).all()[0]
#     print(note.title, note.text)
#
#
# # добавление заметки
# with Session() as session:
#     note = Notes(title='еще одна заметка', text='текст заметки')
#     session.add(note)
#     session.commit()
#
class DB:
    def __init__(self):
        engine = create_engine('sqlite:///notes.db')
        self.Session = sessionmaker(bind=engine)

    def add_note(self, title, text):
        """Метод для добавления заметки"""
        with self.Session() as session:
            note = Notes(title=title, text=text)
            session.add(note)
            session.commit()

    def get_notes(self):
        """Получение всех заметок"""
        with self.Session() as session:
            notes = session.query(Notes).all()
        return notes

    def del_note(self, note_id):
        """Удаление заметок"""
        with self.Session() as session:
            note = session.query(Notes).filter_by(id=note_id).first()
            if note:
                session.delete(note)
                session.commit()


db = DB()

while True:
    user = input('Выбери действие: \n'
                 '1 - добавить заметку, \n  '
                 '2 - посмотреть список \n '
                  '3 - удалить по id ')
    if user == '1':
        title = input('Введи название: ')
        text = input('Введи текст: ')
        db.add_note(title, text)
        print('Замтека добавлена')
    elif user == '2':
        notes = db.get_notes()
        for note in notes:
            print(note.title, note.text, f'({note.id})')
    elif user == '3':
        note_id = int(input('Введи id заметки'))
        db.del_note(note_id)


