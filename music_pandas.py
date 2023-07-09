import pandas
import random

my_music_df = pandas.read_csv('lista.csv', sep=';', header=None)
my_music_df.rename(columns={0: 'Performer', 1: 'Title', 2: 'Score'}, inplace=True)


my_music_df.sort_values('Score', inplace=True, ascending=False)  # sort from highest to lowest used ascending=False
print(my_music_df)
print('-'*90)

my_music_df['Score'] = [(row + random.randint(0,50+1)) for row in my_music_df['Score']]
my_music_df.sort_values('Score', inplace=True, ascending=False)
print(my_music_df.reset_index(drop=True))  # with drop it won't put the old index into the DF
print('-'*90)

best_score = my_music_df.loc[lambda x: x['Score'] == max(x['Score'])] # found the highest score and return with his loc
print(best_score)
print('-'*90)

my_music_df.reset_index(inplace=True)
my_music_df.rename(columns={'index':'old_index'}, inplace=True)
print(my_music_df)
my_music_df.to_excel('into_excel.xlsx')
