# 🎮 Rock Paper Scissors - Game Against Computer

A fun interactive command-line game where you play Rock, Paper, Scissors against the computer over multiple rounds.

## 📋 Description

This project implements the classic Rock, Paper, Scissors game against a computer opponent. The player specifies the number of games to play, and after each round, the running score is displayed. The winner is determined at the end based on who won more rounds.

## ✨ Features

- **Multi-Round Gameplay** - Play as many games as you want in one session
- **Smart Input Handling** - Enter full words (rock, Rock, R, ro) or single letters
- **Real-Time Scoring** - Score updates after each round
- **Input Validation** - Rejects invalid inputs and prompts again
- **Clear Output** - Shows computer's choice, scores, and final results
- **Random AI** - Computer makes random choices using the random module

## 🛠 Prerequisites

- Python 3.x (uses only standard library)

## 📦 Installation

No external dependencies required! Clone or download the file and run:

```bash
python "Rock Paper Scissors.py"
```

## 🚀 Usage

```bash
python "Rock Paper Scissors.py"
```

When prompted:
```
Enter the number of games you want to play: 3
```

Then for each round:
```
User's Input: rock
Computer's Input: Paper
```

The game will display:
- Computer's choice for each round
- Running score
- Final results with the winner

## 📁 Files

- `Rock Paper Scissors.py` - Main game application

## 🎮 Game Rules

- **Rock beats Scissors** 🪨 > ✂️
- **Scissors beats Paper** ✂️ > 📄
- **Paper beats Rock** 📄 > 🪨
- **Same choice = Tie** 🤝

## 🔧 How It Works

### Input Processing
```python
user_input = input("\nUser's Input: ")[0]
user_input = user_input.upper()
```
- Takes first character of input
- Converts to uppercase
- Allows flexible input (rock, R, ro all work)

### Computer Choice
```python
comp_input = random.choice(list(my_dict.keys()))
```
- Randomly selects from ['R', 'P', 'S']

### Win Conditions
```python
if (user_input=='R' and comp_input=='P') or ...
    comp_count += 1
elif (user_input=='P' and comp_input=='R') or ...
    user_count += 1
else:
    print("TIE")
```

## 💡 Learning Concepts

- **Random Module** - Computer AI using random.choice()
- **Conditional Logic** - Multiple if/elif conditions
- **String Operations** - Input processing and comparison
- **Loops** - While loop for game rounds
- **Input Validation** - Checking valid inputs
- **Variable Management** - Tracking scores and game state
- **Dictionaries** - Mapping input codes to display names

## 📊 Sample Game Session

```
Enter the number of games you want to play: 5

User's Input: rock
Computer's Input: Scissors

SCORE:
User Score: 1     Computer Score: 0

User's Input: paper
Computer's Input: Paper

TIE

SCORE:
User Score: 1     Computer Score: 0

...

FINAL SCORE:
User Score: 3               Computer Score: 2

CONGRATULATIONS! YOU WON!
```

## 📝 Possible Outcomes

1. **User Wins** - More rounds won than computer
2. **Computer Wins** - Computer wins more rounds
3. **Tie** - Both win the same number of rounds

## 💡 Tips for Playing

- Input is flexible: "Rock", "rock", "ro", or "R" all work
- Press Ctrl+C to quit early (before all rounds finish)
- Invalid inputs will be rejected and you'll get another chance
- The scoring system clearly shows who's winning

## 🌟 Potential Enhancements

- [ ] Implement Rock-Paper-Scissors-Lizard-Spock variant
- [ ] Add difficulty levels (AI strategy)
- [ ] Track statistics and winrate
- [ ] Add animation and visual effects
- [ ] Implement scoreboard/leaderboard
- [ ] Add sound effects
- [ ] Create GUI version with tkinter
- [ ] Implement weighted random (computer mimics user patterns)
- [ ] Add best-of-N series logic
- [ ] Player vs Player mode (two humans)

## 📚 Related Topics

- Game Development Fundamentals
- Random Number Generation
- Conditional Logic and Decision Trees
- Input Validation and Error Handling
- Interactive Console Applications
- Scoring Systems

## 🎯 Game Theory

This is a classic example of:
- **Zero-sum game** - One player's gain is another's loss
- **Rock-paper-scissors paradox** - No winning strategy
- **Nash Equilibrium** - Random play is optimal
- Equal probability (1/3) for each choice beats any strategy

## 📖 Interesting Facts

- Rock-Paper-Scissors originated in ancient China
- Professional RPS tournaments exist!
- The game is used to study game theory and strategy
- Computer randomness is crucial for fairness
- Players often use patterns (psychology involved)

## 🎮 Extensions You Could Try

1. **Keep tournament records** - Save results to a file
2. **Study user patterns** - AI that learns weak patterns
3. **Multiplayer** - Two players at same keyboard
4. **Statistics** - Track win percentage, most used choice
5. **Difficulty modes** - Easy (random), Medium (counter), Hard (pattern-based)
