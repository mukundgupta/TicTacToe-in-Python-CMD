import sys
plays = [' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ']
run = 1
def main():
    global plays
    
    global run
    while True:
        plays = [' ',' ',' ',
                ' ',' ',' ',
                ' ',' ',' ']
        p1 = input("Name of player 1(X): ")
        p2 = input("Name of player 2(O): ")
        input("\nPress ENTER to start")
        play_grid()
        run = 1
        print("Enter the number of the block you want to place in")
        
        while run <= 9:
            while True:
                try:
                    t1 = input("X: ")
                    if t1 == 'e':
                        sys.exit("Bye")
                    t1 = int(t1)
                    if t1 > 0 and t1 <= 9 and plays[t1-1] == " ":
                        break
                except:
                    if t1 == 'e':
                        sys.exit()
                    print("Must be an integer between 1 and 9, and grid must be empty at that position")
            print(run)
            run += 1
            
            plays[t1-1] = 'X'
            play_grid()
            if check_wins() == 1:
                print(f"{p1} won!!")
                break
            elif check_wins() == 2:
                print(f"{p2} won!!")
                break
            elif run >= 9:
                break
            while True:
                print("RUN: ",run)
                if run >= 9:
                    print("RUN IS 9")
                    break
                try:
                    
                    t2 = input("O: ")
                    if t2 == 'e':
                        sys.exit("Bye")
                    t2 = int(t2)
                    if t2 > 0 and t2 <= 9 and plays[t2-1] == " ":
                        break
                except:
                    if t2 == 'e':
                        sys.exit("Bye")
                    print("Must be an integer between 1 and 9, and grid must be empty at that position")

            print(run)
            run += 1
            plays[t2-1] = "O"
            play_grid()
            print(plays)
            if check_wins() == 1:
                print(f"{p1}(X) won!!")
                break
            elif check_wins() == 2:
                print(f"{p1}(O) won!!")
                break
   
            
            
        
        print("Game Over!")
        if check_wins() == 0:
            print("It was a Tie!\n")
        print("""
Press enter to restart
or press 'e' and enter to exit\n""")
        r = input(">>>")
        if r == 'e':
            sys.exit()
        

def check_wins():
    global plays
    win_plays = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    x_plays = []
    y_plays = []
    for i in range(len(plays)):
        if plays[i] == "X":
            x_plays.append(i)
        elif plays[i] == "O":
            y_plays.append(i)
    x_won = False
    y_won = False
    x_c = 0
    y_c = 0
    
    for i in win_plays:
        x_c=  0
        y_c = 0
        for k in i:
            if len(x_plays) >= 3: 
                if k in x_plays:
                    x_c += 1
                    if x_c == 3:
                        x_won = True
                        break
        for k in i:
            if len(y_plays) >= 3:
                if k in y_plays:
                    y_c += 1
                    if y_c == 3:
                        y_won = True
                        break

    if x_won == True:
        return 1
    elif y_won == True:
        return 2
    else:
        return 0
        
  

def play_grid():
    pr = False
    gr = 0
    global plays
    block = 1
    for m in range(0,3):
        gr += 1
        print(gr,end='')
        for i in range(0,5):
            for k in range(0,11):
                if k == 3 or k == 7:
                    if i != 2 and i != 0:
                        print("|",end='')
                    else:
                        if gr == 2 or gr == 5 or gr == 8:
                            print(" |",end='')
                        else:
                            print("\b|",end='')

                        
                    
                    if gr % 3 != 0:
                        gr += 1
                        print(f"{gr}",end='')
                        pr = True
                else:
                    if pr == True:
                        print(" ",end='')
                        pr = False
                    else:
                        print("   ",end='')

                    if i == 2:
                        if k == 0 or k == 4 or k == 8:
                            print(plays[block-1],end='')
                            block += 1
            print()
        if m != 2:
            for i in range(0,30):
                print("_",end='')
            print()
    print()

    
main()
