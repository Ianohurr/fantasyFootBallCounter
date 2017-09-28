def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

def main():
    playerList={}
    for line in reversed(list(open('action.txt'))):
        if ('drafted' in line):
            line=line.split()
            if(line[1] not in playerList):
                playerList[line[1]]={'Players Drafted':0,'Modified active roster':0,'Player(s) added':0,'Player(s) dropped':0,'Player(s) traded':0}
            playerList[line[1]]['Players Drafted']+=1
        if ('modified active roster' in line):
            line=line.split()
            playerList[line[0]]['Modified active roster']+=1
        elif ('Add/Drop' in line):
            line=line.split()
            playerList[line[1]]['Player(s) added']+=1
            playerList[line[1]]['Player(s) dropped'] += 1
        elif ('Add' in line):
            line = line.split()
            if(line[0]=='Add' and line[2]=='added'):
                playerList[line[1]]['Player(s) added'] += 1
        elif ('Drop' in line):
            line = line.split()
            if(line[0]=='Drop' and line[2]=='dropped'):
                playerList[line[1]]['Player(s) dropped'] += 1
        elif ('Accepted Trade' in line):
            line = line.split()
            playerList[line[0]]['Player(s) traded'] += 1
            playerList[line[-1]]['Player(s) traded'] += 1

                    
    pretty(playerList)


if __name__ == '__main__':
    main()