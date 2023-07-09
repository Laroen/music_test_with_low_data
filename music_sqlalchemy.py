from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import desc
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
import pandas
import random


My_Base = declarative_base()

class Musics(My_Base):
    __tablename__ = "musics"

    row_index = Column(Integer, primary_key=True)
    performer = Column(String(60))
    title = Column(String(40))
    score = Column(Integer)

    def __repr__(self):
        return f'{self.performer:60}: {self.title:40} | Score: {self.score}'


music_dataframe = pandas.read_csv('lista.csv', sep=';', header=None)
music_dataframe.rename(columns={0: 'Performer', 1: 'Title', 2: 'Score'}, inplace=True)
music_dataframe['Performer'].astype(dtype=str)
music_dataframe['Title'].astype(dtype=str)
print(music_dataframe)

engine = create_engine("mysql+pymysql://root@localhost/music_test")
My_Base.metadata.create_all(engine)

print(music_dataframe.dtypes)
with Session(engine) as session:
    for row in music_dataframe.iterrows():
        print(row[1].values[0])
        music_db = Musics(
            performer = row[1].values[0],
            title = row[1].values[1],
            score = row[1].values[2]
            )
        session.add(music_db)
        session.commit()

session = Session(engine)

for row in session.query(Musics).all():
    row.score += random.randint(0,50+1)
session.commit()

max_points = session.query(func.max(Musics.score)).scalar()
query_1 = session.query(Musics).where(Musics.score == max_points)
update(Musics).values(score=Musics.score + random.randint(0,50+1))

score_sort = session.query(Musics).order_by(Musics.score.desc()).all()
print('Sorted list after score rises in each row with 0-50 points:')
for row in score_sort:
    print(row)

print('\n\nHighest score reached:')
for i in query_1:
    print(f'{i.performer:60}: {i.title:40} | Score: {i.score}')