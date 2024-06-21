# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

tracker = {}

def player(prev_play, opponent_history=[]):

    if prev_play:
        opponent_history.append(prev_play)

    val = 6

    if len(opponent_history) <= val:
        guess = "R"
    
    else:
        patt = "".join(opponent_history[-val:])
        extend_patt = "".join(opponent_history[-(val + 1):])
        tracker[extend_patt] = tracker.get(extend_patt, 0) + 1

        odds = [patt + "R", patt + "P", patt + "S"]
        for move in odds:
            tracker.setdefault(move, 0)

        predict = max(odds, key = tracker.get)
        guess = {"P": "S", "R": "P", "S": "R"}[predict[-1]]
    
    return guess
