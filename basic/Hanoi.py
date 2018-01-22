step=1
def hanoi(num,src,tmp,dst):
    global step
    if num==1:
        print("step",step,": move from "+src+" to "+dst+" ;")
        step=step+1
    else:
        hanoi(num-1,src,dst,tmp)
        print("step",step,": move from "+src+" to "+dst+" ;")
        step=step+1
        hanoi(num-1,tmp,src,dst)
hanoi(4,'A','B','C')
