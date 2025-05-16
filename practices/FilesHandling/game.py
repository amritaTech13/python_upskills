
def file_update(player):
    with open('./FilesHandling/Hi_score.txt', 'w') as f:
        f.write(player)

def game():
    player1 = int(input("Enter payer 1 score: "))
    player2 = int(input("Enter payer 2 score: "))

    if player1 > player2:
        file_update(str(player1))
    else:
        file_update(str(player2))    

if __name__ == '__main__':
    game()        