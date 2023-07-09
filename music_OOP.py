import random

class Musics:
    def __init__(self, performer, title, score):
        self.performer = performer
        self.title = title
        self.score = int(score)

    def __str__(self):
        return f'{self.performer:60}: {self.title:30} | Score: {self.score}'

    def get_score(self):
        return self.score

    def set_score(self, value):
        value += random.randint(0,50+1)
        self.score = value


with open('lista.csv', 'r', encoding='utf8') as file:
   whole_data = [Musics(*row.strip().split(';')) for row in file]

print(f'{"Performer":60}| {"Title":30} | Score\n{"-"*110}')
for data in whole_data:
    data.set_score(data.get_score())

whole_data.sort(key=lambda x: x.score, reverse=True)
highest_score = max(whole_data, key=lambda x: x.score)

for i in whole_data:
    print(i)

print('\n')
print('The highest score:')
print(f'{"Performer":60}| {"Title":30} | Score\n{"-"*110}')
print(highest_score)
