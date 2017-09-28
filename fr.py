
    
def main():
    playerList={}
    with open('action.txt') as f:
        for line in f:
            if ('modified active roster' in line):
                line=line.split()
                if(line[0] not in playerList):
                    playerList[line[0]]={'modified active roster':1}
                else:
                    if('modified active roster' not in playerList[line[0]]):
                        playerList[line[0]]['modified active roster']=1
                    else:
                        playerList[line[0]]['modified active roster']+=1
            elif ('added' in line):
                line=line.split()
                if(line[1] not in playerList):
                    playerList[line[1]]={'Player(s) added':1}
                else:
                    if('Player(s) added' not in playerList[line[1]]):
                        playerList[line[1]]['Player(s) added']=1
                    else:
                        playerList[line[1]]['Player(s) added']+=1
                    
    print(playerList)
        

if __name__ == '__main__':
    main()