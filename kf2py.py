import sys


def transpile(ptr,mem):

    args=sys.argv
    path=args[1]

    with open(path,encoding='utf-8') as f:
        code=f.read()

        code_list=list(code)

    head=0
    buf=''
    
    while head<len(code_list):

        if code_list[head]=='！':

            if buf=='たのしー':
                
                ptr+=1
        
            elif buf=='たーのしー':
                mem[ptr]=(mem[ptr]+1)&0xff

            elif buf=='すごーい':
                ptr-=1

            elif buf=='すっごーい':
                
                mem[ptr]=(mem[ptr]-1)&0xff

            elif buf=='うわー':
                
                if mem[ptr]==0:
                    count=1
                    
                    while count!=0:
                        head+=1

                        if head==len(code_list):
                            print("'わーい' is missing")
                            sys.exit(1)

                        if code_list[head]=='！':
                            
                            if buf=='うわー':
                                count+=1

                            elif buf=='わーい':
                                count-=1

                            
                            buf=''
                            
                        buf+=code_list[head]

            elif buf=='わーい':
                
                if mem[ptr]!=0:
                    count=1

                    while count!=0:
                        head-=1

                        if head < 0:
                            print("'うわー' is missing")
                            sys.exit(1)

                        if code_list[head]=='！' or head==0:
                            
                            if buf=='いーわ':
                                count+=1
                            
                            elif buf=='ーわう':
                                count-=1

                            buf=''
                        
                        else:
                            buf+=code_list[head]

            elif buf=='なにこれなにこれ':
                
                sys.stdout.write(chr(mem[ptr]))

            elif buf=='おもしろーい':
                
                mem[ptr]=ord(sys.stdin.read(1))
            
            else:
                pass

            buf=''

        else:
            buf+=code_list[head]

        head+=1


def main():
    ptr=0
    mem_size=int(input("Input memory size: "))
    mem=[0 for i in range(mem_size)]

    transpile(ptr,mem)

if __name__=='__main__':
    main()














"""

⣿⣿⣿⣿⣿⣿⣿⡿⠉⠙⣿⣿⣿⣿⠏⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠁⣀⠀⠘⣿⣿⠋⠀⣄⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⠀⣼⣿⣠⣄⢹⡇⣴⣾⣿⣧⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠃⣼⣿⣿⡇⣿⡆⢱⣿⣿⣿⣿⣧⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡟⢸⣿⣿⠻⠙⣿⣷⢸⣿⠋⠟⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠇⣿⣿⠍⣹⣷⣿⣿⣿⣿⣿⣕⢹⣿⣧⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡀⣿⢟⣵⣾⣿⠟⠻⣿⡿⠻⣷⣮⡿⡟⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡟⣴⢹⣿⣿⣿⠁⣠⣦⣜⣡⣦⣈⢻⣿⣶⣂⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⢱⣏⣿⣯⣿⡟⣾⣿⣿⣿⢿⣿⠻⣿⢻⣿⣷⡁⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡇⣼⣹⣿⣿⡼⣋⣬⢽⡻⣷⣿⣿⠄⠉⠈⣿⣿⣇⡆⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⢁⣿⣧⢻⣿⡷⠆⠀⢀⣦⣬⣻⠟⠁⢠⡼⣿⢇⣼⣿⠘⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡎⣿⣿⣶⡌⠓⢷⠣⢸⣿⣿⣿⣷⣆⣚⡇⡅⡝⣿⡧⠃⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡇⠋⢿⡗⢝⠺⣿⣿⣿⣿⢿⡷⢿⣿⣿⠇⠜⡇⠘⠁⣀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣄⣠⡙⠈⠘⠴⢙⠝⠛⠝⢫⠞⣉⠉⡀⠀⢀⣤⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡇⠠⢆⡰⢐⣤⣜⣲⣇⢛⠸⣿⡆⢿⡦⢬⠚⢫⢀⣿⣿⣿⣿⣿⣿⣿⣿
⡏⣴⡖⣦⠁⠀⠀⠀⡘⠿⣬⢽⣾⣷⢸⣿⣿⠆⠰⢱⣿⡇⣼⣿⣿⣿⣿⣿⣿⣿⣿
⣇⠛⣉⡈⢾⣷⣄⢺⡟⢡⠈⠈⠙⠛⠒⠉⣁⣀⠲⣬⣙⠰⠿⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡆⠙⢛⣋⣄⣡⡼⢯⡽⠀⣩⠀⢉⣿⠧⣤⣶⣤⣶⠆⣽⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⢃⣤⠸⢿⣅⢀⡷⠚⣷⡀⢰⣄⠘⢳⣤⠿⢿⣤⡼⢀⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣆⠁⢠⣼⠋⠉⣷⠖⢻⣿⠋⠙⢟⠙⢻⡄⢠⡝⢀⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡙⠋⣢⠴⠿⡦⡼⠻⣂⣠⣺⣻⢿⣾⠀⣄⠛⠻⠿⠿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠃⣴⣈⡛⣿⠗⡀⢈⡛⠿⠟⠣⣿⣯⣶⡿⠀⣾⡇⠀⢠⣉⠻⣿⣿
⣿⣿⣿⣿⣿⠏⣸⠤⣉⠷⣠⣾⣷⢀⣴⡈⠇⣴⣌⠻⣟⣧⣾⣧⠀⢀⣼⡿⠀⠈⣿
⣿⣿⣿⣿⢃⣼⣼⡓⢡⣾⣿⣿⣿⠈⣖⢳⢸⣿⣿⣿⣮⣉⠋⠡⣴⣿⠟⠁⠀⠀⣽
⣿⣿⣿⡇⢸⣿⠏⣴⣿⣿⣿⣿⡟⢰⣿⠇⣸⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣿
⣿⣿⣿⢰⣌⡋⢸⣿⣿⣿⣿⡿⠹⠘⠍⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⡀⡀⢸⣿⣿⣿⣿⠇⣤⡀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣇⠛⠿⢈⣿⣿⣿⣿⣧⣭⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

"""