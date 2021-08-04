import sys
sys.path.append('.')

from sotaP import SotaP

if __name__ == '__main__':
    print("SotaP testing")

    game = SotaP(4)

    sota = game.game()

    for step in sota: # For each step of the game
        # print(step)
        pass # Do it

    print("Game results:")
    for i in range(len(game.gameStats["scoreBoard"])-1, -1, -1):
        userName = game.gameStats["scoreBoard"][i].getName()
        fastRecordIndex = game.gameStats["scoreBoard"][i].index
        print(f"  - {userName} -> {game.gameStats['iAmThefastest'][fastRecordIndex]}")
    
    print(game.gameStats["iAmThefastest"])

    print("Testing ended")