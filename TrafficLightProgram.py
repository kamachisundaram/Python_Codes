def TrafficProgram(exp_time=1,waitTime=3):
    for i in range(exp_time):
        
        TrafficArea=["S","W","N","E"]
        
        def setRed(*args):
            '''Use this function to create RED'''

            for i in args:
                print("Setting RED to "+str(i))

        def setGreen(x):
            '''Use this function to create Green signal'''
            print("Setting Green to "+str(x))

        def setYellow(x):
            '''Use this function to create Green signal'''
            print("Setting Yellow to "+str(x))

        for i in range(len(TrafficArea)):
            d=TrafficArea[i]
            TrafficArea.pop(i)
            setGreen(d)
            setYellow(TrafficArea[(i+1)-4])
            setRed(TrafficArea)
            TrafficArea.insert(i,d)
            import time; time.sleep(waitTime)

TrafficProgram()
