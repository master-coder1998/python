# 🎯 Pickalator - Team Match Predictor

A fun cricket match prediction tool that calculates winning chances based on team rankings with a randomization factor.

## 📝 Description

Pickalator analyzes two cricket teams and predicts which one is more likely to win based on their current rankings. It adds suspense with delayed output and incorporates randomization to simulate the unpredictability of real matches.

## ✨ Features

- **Team Ranking System**: Uses team rankings (1-10 scale) to calculate base chances
- **Random Factor**: Adds randomness (0-10 points) to simulate match unpredictability
- **Suspenseful Output**: Uses time delays for dramatic effect
- **Clear Visualization**: Displays final chances with emojis
- **Probability Calculation**: Converts rankings into winning probabilities

## 🚀 How It Works

### Algorithm

1. **Base Chance Calculation**:
   ```
   team_chance = 10 - team_rank
   ```
   - Higher ranking = Lower number = Better chance
   - Team ranked #2 gets 8 base points
   - Team ranked #6 gets 4 base points

2. **Random Factor**:
   ```
   team_chance += random.randint(0, 10)
   ```
   - Adds 0-10 random points to each team
   - Simulates match-day variables (form, pitch, weather, etc.)

3. **Winner Determination**:
   - Team with higher final chance is predicted to win
   - Displays both teams' final chances

### Example Calculation

```
Team 1 (RCB): Rank #2
  Base chance: 10 - 2 = 8
  Random bonus: +5
  Final: 13

Team 2 (MI): Rank #6
  Base chance: 10 - 6 = 4
  Random bonus: +8
  Final: 12

Prediction: RCB likely to win (13 > 12)
```

## 💻 Usage

### Run the Script

```bash
python Pickalator.py
```

### Customize Teams

Edit the variables at the top of the script:

```python
# Team 1 Details
team1_name = 'RCB'  # Your team name
team1_rank = 2      # Ranking (1-10, lower is better)

# Team 2 Details
team2_name = 'MI'   # Opponent name
team2_rank = 6      # Their ranking
```

### Sample Output

```
calculating chances...🙈
RCB is likely to win
Final Chances are...
Team1 chance: 13 😒😎
Team2 chance: 12 😒😎
```

## 🎮 Code Breakdown

### Imports
```python
import random  # For randomization
import time    # For delays
```

### Configuration
```python
team1_name = 'RCB'
team1_rank = 2
team2_name = 'MI'
team2_rank = 6
```

### Probability Calculation
```python
# Convert rankings to chances (inverse relationship)
team1_chance = 10 - team1_rank
team2_chance = 10 - team2_rank

# Add random factor
team1_chance += random.randint(0, 10)
team2_chance += random.randint(0, 10)
```

### Output with Suspense
```python
time.sleep(2)  # 2-second delay
print('calculating chances...🙈')

# Determine winner
if team1_chance >= team2_chance:
    print(f'{team1_name} is likely to win')
else:
    print(f'{team2_name} is likely to win')

time.sleep(1)  # 1-second delay
print('Final Chances are...')
print(f'Team1 chance: {team1_chance} 😒😎')
print(f'Team2 chance: {team2_chance} 😒😎')
```

## 🎯 Learning Concepts

This project demonstrates:

- **Variables**: Storing team data
- **Arithmetic Operations**: Calculating chances
- **Random Module**: Generating random numbers
- **Time Module**: Adding delays
- **Conditionals**: Determining winner
- **f-strings**: Formatted output
- **User Experience**: Creating suspense with timing

## 🔧 Customization Ideas

1. **Multiple Teams**: Extend to tournament mode with multiple teams
2. **Historical Data**: Use actual win/loss records instead of just rankings
3. **Player Stats**: Factor in individual player performance
4. **Weather/Venue**: Add more variables (home advantage, weather conditions)
5. **GUI**: Create a graphical interface with Tkinter
6. **Save Results**: Store predictions to a file
7. **Accuracy Tracking**: Track predictions vs actual results

## 📊 Enhancement Ideas

### Add More Factors
```python
# Form factor (recent wins)
team1_form = 0.8  # 80% recent wins
team2_form = 0.5  # 50% recent wins

# Home advantage
home_team = 1  # Team 1 is home
home_advantage = 3

# Final calculation
team1_chance = (10 - team1_rank) + (team1_form * 5) + (home_advantage if home_team == 1 else 0)
```

### Add Input Validation
```python
def get_team_rank(team_name):
    while True:
        try:
            rank = int(input(f"Enter {team_name} rank (1-10): "))
            if 1 <= rank <= 10:
                return rank
            print("Rank must be between 1 and 10")
        except ValueError:
            print("Please enter a valid number")
```

### Add Historical Tracking
```python
import json

def save_prediction(team1, team2, prediction):
    with open('predictions.json', 'a') as f:
        data = {
            'team1': team1,
            'team2': team2,
            'prediction': prediction,
            'timestamp': time.time()
        }
        json.dump(data, f)
        f.write('\n')
```

## 🐛 Known Limitations

- Rankings are manually set (not fetched from live data)
- Random factor can sometimes override significant ranking differences
- Doesn't account for head-to-head records
- No tie-handling (equal chances default to team1)

## 📚 Dependencies

- `random` (built-in)
- `time` (built-in)

No external packages required!

## 🎓 Educational Value

Perfect for learning:
- Basic Python syntax
- Module imports
- Random number generation
- String formatting
- Conditional logic
- Time-based operations

## 📝 License

Part of the personal learning repository. Feel free to use and modify!

---

**Made with ❤️ for cricket fans and Python learners!** 🏏