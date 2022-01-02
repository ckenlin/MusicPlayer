
def cases(case,position,xo,list):
    if case[position]!='X' and case[position]!='Y':
        case[position]=xo.upper()
        list.append(str(position+1))
        return True
    else :
        print('Space ',position+1,'is not empty')
        #print_board(list)
        return False


def cases_full(case):
    ck=0
    for c in case:
        if c=='X'or c=='Y':
            ck=1
        else:
            ck=0 
            break
    if ck==1:
        print("It's a draw!!")
        return True
    else: return False


def chek_winner(list):
    result = ['123', '159', '456', '357', '963', '789', '741','852']
    for i in result:
        cc = 0
        for j in list:
            if j in i:
                cc = cc+1
            if cc == 3:
                cc = 0
                return True
            if j == list[-1] and cc != 3:
                cc = 0
                break              
    return False


def print_board(case):
    num=['1','2','3','4','5','6','7','8','9']
  
    print(f'\n {case[6]} | {case[7]} | {case[8]}')
    print('-----------')
    print(f' {case[3]} | {case[4]} | {case[5]}')
    print('-----------')
    print(f' {case[0]} | {case[1]} | {case[2]}\n')


def play():
    done=False 
    player1_score=0
    player2_score=0
    name={'player1':'','player2':''}
    while True:
        name['player1']=input('Hey player1 Enter your first name:').title()
        if name['player1']!='':
            break
        else :
            print("Please reenter your name!")
    while True:
        name['player2']=input('Hey player2 Enter your first name:').title()
        if name['player2']!='':
            break
        else :
            print("Please reenter your name!")
   
    while done!=True:
        k = []
        case=['1','2','3','4','5','6','7','8','9']
        print('Picking up a random player to start...')
        from random import randint
        n=randint(1, 2)
  
        if n==1:
            print('{} is going to start'.format(name['player1']),'first')
            while True:
                XO1 = input('Chose between X or Y:')  
                if XO1.upper()=='X' or XO1.upper()=='Y':
                    break
                else :
                    print( name['player1']+" Please chose between X and Y!")
 
            if XO1.upper()=='X':
                XO2='Y'
            else:
                XO2 = 'X'
            k.append(1)
            k.append(2)
        else : 
            print('{} is going to start'.format(name['player2']),'first')
           
            while True:
                XO2 = input('Chose between X or Y:')   
                if  XO2.upper()=='X' or  XO2.upper()=='Y':
                    break
                else :
                    print(name['player2']+" Please chose between X and Y!")

            if XO2.upper() == 'X':
                XO1 = 'Y'
            else:
                XO1 = 'X'
            k.append(2)
            k.append(1)
        end= False
        l1=[]
        l2=[]
        c=0
        print('\n||---',name['player2'],'Score:',player2_score,'---||---',name['player1'],'Score:',player1_score,'---||')

        while end !=True:
            for i in k:
                if end== True:
                    break
                print_board(case)
                if i==1:
                    while True:
                        while True:
                            c = input('{} Where do you want to put your {}:'.format(name['player1'],XO1))
                            if c!='' and not c.isalpha():
                                break
                            else:
                                print('please chose a number between 1 & 9!')
                        print('\033[H\033[J')
                        if cases(case,int(c)-1,XO1,l1)==True:
                            break
                        else:
                            print('please chose !!')
                            print_board(case)
                       
                else :
                    while True:
                        while True:
                            c = input('{} Where do you want to put your {}:'.format(name['player2'],XO2))
                            
                            if c!='' and not c.isalpha():
                                break
                            else:
                                print('please chose a number between 1 & 9!')
                        print('\033[H\033[J')
                        if cases(case, int(c)-1, XO2,l2)==True:
                            break
                        else:
                            print('please chose one of the free spaces available!!')
                            print_board(case)
                        
                           
                if len(l1)>=3 :
                 if chek_winner(l1):
                     print(name['player1'],'you are the winner!!')
                     player1_score+=1
                     print_board(case)
                     end=True
                     break
                        
                if len(l2) >= 3:
                    if chek_winner(l2):
                         print(name['player2'],'You are the WINNER!!')
                         player2_score+=1
                         print_board(case)
                         end=True
                         break
                if cases_full(case) == True:
                    end=True
                    print_board(case)
                    break
        while True:
            answer =input('If you want to continue playing type YES/Y else type NO/N ')
            if answer.upper()=='YES' or answer.upper()=='Y' :
                print("Lets go again...")
                break
            elif answer.upper()=='NO' or answer.upper()=='N' : 
                done=True  
                player1_score=0
                player2_score=0
                print ('Thanks for playing. See you next time ;)')
                break
            else :
                print('Please chose from one of the options you have!!')
            
               
play()

