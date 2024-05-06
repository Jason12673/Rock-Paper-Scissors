import random

options = ['rock', 'paper', 'scissors']

def make_ai_decisions():
  return random.choice(options)

def print_player_decisions(player_list, decision_list):
  print("-------------------")
  for i in range(len(player_list)):
    print("{}: {}".format(player_list[i], decision_list[i]))
  print("-------------------")

def get_who_made_decision(decision, player_list, decision_list):
  players = []
  for i in range(len(player_list)):
    if decision_list[i] == decision:
      players.append(player_list[i])
  return players
  
def get_human_decision():
  while True:
    decision = str(input("Rock, Paper, or Scissors? ")).lower()
    if decision == "rock" or decision == "paper" or decision == "scissors":
      return decision
    else:
      print("BAD INPUT")

def calculate_losing_players(player_list, decision_list):
  rock_players = get_who_made_decision('rock', player_list, decision_list)
  paper_players = get_who_made_decision('paper', player_list, decision_list)
  scissors_players = get_who_made_decision('scissors', player_list, decision_list)

  # If there exists rock, paper, and scissors players, no one wins.
  if rock_players and paper_players and scissors_players:
    return []

  # If there are only rock and paper players, paper beats rock
  if rock_players and paper_players:
    return rock_players

  # If there are only paper and scissors players, scissors beats paper
  if paper_players and scissors_players:
    return paper_players

  # If there are only scissors and rock players, rock beats scissors
  if scissors_players and rock_players:
    return scissors_players

  # If there's just one group of players with a decision, or no decisions.
  return []

def eliminate_any_losing_players(player_list, decision_list):
  losing_players = calculate_losing_players(player_list, decision_list)
  if not losing_players:
    print("No clear winner, so go again!\n")
    return

  linking_verb = "are"
  if len(losing_players) == 1:
    linking_verb = "is"
  print('{} {} eliminated.'.format(', '.join(losing_players), linking_verb))

  for losing_player in losing_players:
    player_index = player_list.index(losing_player)
    decision_list.pop(player_index)
    player_list.remove(losing_player)
  print('{} player(s) remain.\n'.format(len(player_list)))

def rock_paper_scissors():
  number_of_ai = int(input("How many computer players? "))
  print("WELCOME TO ROCK, PAPER, SCISSORS. THERE ARE {} PARTICIPANTS PLAYING.".format(number_of_ai+1))

  player_list = ['Human']
  decision_list = ['']

  for i in range(number_of_ai):
    player_list.append("AI_" + str(i))
    decision_list.append('')

  game_is_over = False
  while not game_is_over:
    for i in range(len(player_list)):
      if "Human" == player_list[i]:
        decision_list[i] = get_human_decision()
      else:
        decision_list[i] = make_ai_decisions()
    print_player_decisions(player_list, decision_list)
    eliminate_any_losing_players(player_list, decision_list)
    if len(player_list) == 1:
      print("{} WINS!!!".format(player_list[0]))
      game_is_over = True
      
rock_paper_scissors()
