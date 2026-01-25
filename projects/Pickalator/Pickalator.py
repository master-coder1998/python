import random
import time
# print(random.randint(1,100))

team1_name = 'RCB'
team1_rank= 2

team2_name = 'MI'
team2_rank =6

team1_chance=10 - team1_rank
team2_chance=10 - team2_rank

team1_chance+= random.randint(0,10)
team2_chance+= random.randint(0,10)

time.sleep(2)

print('calculating chances...🙈')

if team1_chance >= team2_chance:
    print(f'{team1_name} is likely to win')
else    :
    print(f'{team2_name} is likely to win') 

time.sleep(1)
print(' Final Chances are...')


print(f'Team1 chance: {team1_chance} 😒😎')    
print(f'Team2 chance: {team2_chance} 😒😎')