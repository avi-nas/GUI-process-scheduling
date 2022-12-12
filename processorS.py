from tkinter import *




# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def findWaitingTime(processes, n, wt):
	rt = [0] * n

	# Copy the burst time into rt[]
	for i in range(n):
		rt[i] = processes[i][1]
	complete = 0
	t = 0
	minm = 999999999
	short = 0
	check = False

	# Process until all processes gets
	# completed
	while (complete != n):
        
		# Find process with minimum remaining
		# time among the processes that
		# arrives till the current time`
		for j in range(n):
			if ((processes[j][2] <= t) and
				(rt[j] < minm) and rt[j] > 0):
				minm = rt[j]
				short = j
				check = True
		if (check == False):
			t += 1
			continue
            
		# Reduce remaining time by one
		rt[short] -= 1

		# Update minimum
		minm = rt[short]
		if (minm == 0):
			minm = 999999999

		# If a process gets completely
		# executed
		if (rt[short] == 0):

			# Increment complete
			complete += 1
			check = False

			# Find finish time of current
			# process
			fint = t + 1

			# Calculate waiting time
			wt[short] = (fint - proc[short][1] -	
								proc[short][2])

			if (wt[short] < 0):
				wt[short] = 0
        
		# Increment time
		t += 1

# Function to calculate turn around time
def findTurnAroundTime(processes, n, wt, tat):
    
	# Calculating turnaround time
	for i in range(n):
		tat[i] = processes[i][1] + wt[i]

# Function to calculate average waiting
# and turn-around times.
def findavgTime(processes, n):
	wt = [0] * n
	tat = [0] * n

	# Function to find waiting time
	# of all processes
	findWaitingTime(processes, n, wt)

	# Function to find turn around time
	# for all processes
	findTurnAroundTime(processes, n, wt, tat)

	# Display processes along with all details
	print("Processes Burst Time	 Waiting",
					"Time	 Turn-Around Time")
	total_wt = 0
	total_tat = 0
	for i in range(n):

		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", processes[i][0], "\t\t",
				processes[i][1], "\t\t",
				wt[i], "\t\t", tat[i])

	print("\nAverage waiting time = %.5f "%(total_wt /n) )
	print("Average turn around time = ", total_tat / n)
    
# Driver code
if __name__ =="__main__":
    
	# Process id's
	proc = [[1, 6, 1], [2, 8, 1],
			[3, 7, 2], [4, 3, 3]]
	n = 4
	findavgTime(proc, n)
    
# ----------------------------------------------------------------------------------------------------


# of FCFS scheduling
def findWaitingTimeFCFS(processes, n,
                    bt, wt):

    # waiting time for
    # first process is 0
    wt[0] = 0

    # calculating waiting time
    for i in range(1, n ):
        wt[i] = bt[i - 1] + wt[i - 1]

# Function to calculate turn
# around time
def findTurnAroundTimeFCFS(processes, n,
                    bt, wt, tat):

    # calculating turnaround
    # time by adding bt[i] + wt[i]
    for i in range(n):
        tat[i] = bt[i] + wt[i]

# Function to calculate
# average time
def findavgTimeFCFS( processes, n, bt):

    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0

    # Function to find waiting
    # time of all processes
    findWaitingTimeFCFS(processes, n, bt, wt)

    # Function to find turn around
    # time for all processes
    findTurnAroundTimeFCFS(processes, n,
                    bt, wt, tat)

    # Display processes along
    # with all details
    print( "Processes Burst time " +
                " Waiting time " +
                " Turn around time")

    # Calculate total waiting time
    # and total turn around time
    Label(root, text="Burst Time").grid(row=n+5,column=0)
    Label(root,text="Waiting Time").grid(row=n+5,column=1)
    Label(root, text="Turn-Around Time").grid(row=n+5,column=2)
    
    for i in range(n):
    
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" " + str(i + 1) + "\t\t" +str(bt[i]) + "\t " +str(wt[i]) + "\t\t " +str(tat[i]))
        
        Label(root, text=bt[i]).grid(row=n+6+i,column=0)
        Label(root,text=wt[i]).grid(row=n+6+i,column=1)
        Label(root, text=tat[i]).grid(row=n+6+i,column=2)

    Label(root, text="\nAverage WT %.5f "%(total_wt /n)).grid(row=2*n+6,column=0)
    Label(root, text="Average TAT %.5f "% (total_tat / n)).grid(row=2*n+7,column=0)

    print( "Average waiting time = "+
                str(total_wt / n))
    print("Average turn around time = "+
                    str(total_tat / n))

    
#-----------------------------------------------------------------------------------------------------
    

# Python3 implementation for Priority Scheduling with
# Different Arrival Time priority scheduling
"""1. sort the processes according to arrival time
2. if arrival time is same the acc to priority
3. apply fcfs """




# Using FCFS Algorithm to find Waiting time
def get_wt_time( num,wt,proc):

    # declaring service array that stores
    # cumulative burst time
    service = [0] * num

    # Initialising initial elements
    # of the arrays
    service[0] = 0
    wt[0] = 0

    for i in range(1,num):
        service[i] = proc[i - 1][1] + service[i - 1]
        wt[i] = service[i] - proc[i][0] + 1

        # If waiting time is negative,
        # change it o zero
        if(wt[i] < 0) :	
            wt[i] = 0
        
def get_tat_time(num,tat, wt,proc):

    # Filling turnaroundtime array
    for i in range(num):
        tat[i] = proc[i][1] + wt[i]

def findgc(num , proc):
    
    # Declare waiting time and
    # turnaround time array
    wt = [0] * 5
    tat = [0] * 5

    wavg = 0
    tavg = 0

    # Function call to find waiting time array
    get_wt_time(num,wt,proc)
    
    # Function call to find turnaround time
    get_tat_time(num,tat, wt,proc)

    stime = [0] * 5
    ctime = [0] * 5
    stime[0] = 1
    ctime[0] = stime[0] + tat[0]
    
    # calculating starting and ending time
    for i in range(1,num ):
        stime[i] = ctime[i - 1]
        ctime[i] = stime[i] + tat[i] - wt[i]

    print("Process_no\tStart_time\tComplete_time",
            "\tTurn_Around_Time\tWaiting_Time")
    Label(root, text="Process_no").grid(row=num+5,column=0)
    Label(root,text="Start_time").grid(row=num+5,column=1)
    Label(root, text="Complete_time").grid(row=num+5,column=2)

    Label(root, text="Turn_Around_Time").grid(row=num+5,column=3)
    Label(root,text="Waiting_Time").grid(row=num+5,column=4)
    
    # display the process details
    for i in range(num):
        wavg += wt[i]
        tavg += tat[i]
        
        print(proc[i][3], "\t\t", stime[i],
                        "\t\t", end = " ")
        print(ctime[i], "\t\t", tat[i], "\t\t\t", wt[i])
        Label(root, text=proc[i][3]).grid(row=num+6+i,column=0)
        Label(root,text=stime[i]).grid(row=num+6+i,column=1)
        Label(root, text=ctime[i]).grid(row=num+6+i,column=2)
        Label(root,text=tat[i]).grid(row=num+6+i,column=3)
        Label(root, text=wt[i]).grid(row=num+6+i,column=4)
    # display the average waiting time
    # and average turn around time
    print("Average waiting time is : ", end = " ")
    print(wavg / num)
    print("average turnaround time : " , end = " ")
    print(tavg /num)
    Label(root, text="\nAverage WT %.5f "%(wavg/num)).grid(row=2*num+6,column=0)
    Label(root, text="Average TAT %.5f "% (tavg / num)).grid(row=2*num+7,column=0)

    
    





    
#------------------------------------------------------------------------------------------------------

def findWaitingTimeRR(processes, n, bt,
                        wt, quantum):
    rem_bt = [0] * n

    # Copy the burst time into rt[]
    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0 # Current time

    # Keep traversing processes in round
    # robin manner until all of them are
    # not done.
    while(1):
        done = True

        # Traverse all processes one by
        # one repeatedly
        for i in range(n):
        
            # If burst time of a process is greater
            # than 0 then only need to process further
            if (rem_bt[i] > 0) :
                done = False # There is a pending process

                if (rem_bt[i] > quantum) :
                
                    # Increase the value of t i.e. shows
                    # how much time a process has been processed
                    t += quantum

                    # Decrease the burst_time of current
                    # process by quantum
                    rem_bt[i] -= quantum

                # If burst time is smaller than or equal
                # to quantum. Last cycle for this process
                else:
                
                    # Increase the value of t i.e. shows
                    # how much time a process has been processed
                    t = t + rem_bt[i]

                    # Waiting time is current time minus
                    # time used by this process
                    wt[i] = t - bt[i]

                    # As the process gets fully executed
                    # make its remaining burst time = 0
                    rem_bt[i] = 0

        # If all processes are done
        if (done == True):
            break
        
# Function to calculate turn around time
def findTurnAroundTimeRR(processes, n, bt, wt, tat):

    # Calculating turnaround time
    for i in range(n):
        tat[i] = bt[i] + wt[i]


# Function to calculate average waiting
# and turn-around times.
def findavgTimeRR(processes, n, bt, quantum):
    wt = [0] * n
    tat = [0] * n

    # Function to find waiting time
    # of all processes
    findWaitingTimeRR(processes, n, bt,
                        wt, quantum)

    # Function to find turn around time
    # for all processes
    findTurnAroundTimeRR(processes, n, bt,
                                wt, tat)

    # Display processes along with all details
    print("Processes Burst Time	 Waiting",
                    "Time Turn-Around Time")
    total_wt = 0
    total_tat = 0

    Label(root, text="Burst Time").grid(row=n+5,column=0)
    Label(root,text="Waiting Time").grid(row=n+5,column=1)
    Label(root, text="Turn-Around Time").grid(row=n+5,column=2)
    
    
    for i in range(n):
    
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" ", i + 1, "\t\t", bt[i],"\t\t", wt[i], "\t\t", tat[i])
        Label(root, text=bt[i]).grid(row=n+6+i,column=0)
        Label(root,text=wt[i]).grid(row=n+6+i,column=1)
        Label(root, text=tat[i]).grid(row=n+6+i,column=2)

    Label(root, text="\nAverage WT %.5f "%(total_wt /n)).grid(row=2*n+6,column=0)
    Label(root, text="Average TAT %.5f "% (total_tat / n)).grid(row=2*n+7,column=0)
       


#--------------------------------------------------------------------------------------------------------------



















def solve(num,algof,bTime,aTime,priorityList,quantum):
   
    process = list()
    for i in range(1,num+1):
        process.append(i)

    burstList = list()
    arivalList = list()
    prList = list()
    for i in range(num):
        burstList.append(bTime[i].get())
        arivalList.append(aTime[i].get())

    
    if(algof == 1):
        pass
    elif(algof == 2):
    
        findavgTimeFCFS(process,num,burstList)





    elif(algof == 3):
        proc = []
        for i in range(num):
            l = []
            for j in range(4):
                l.append(0)
            proc.append(l)
        
        for i in range(num):
            prList.append(priorityList[i].get())
        
            
        for i in range(num):

            proc[i][0] = arivalList[i]
            proc[i][1] = burstList[i]
            proc[i][2] = prList[i]
            proc[i][3] = i + 1
    
        # Using inbuilt sort function
        proc = sorted (proc, key = lambda x:x[2])
        proc = sorted (proc)
    
        # Calling function findgc for
        # finding Gantt Chart
        findgc(num ,proc)

            


    elif(algof == 4):
        
        findavgTimeRR(process,num, burstList,quantum.get())

    

def createInputTable(num,algof):
    quantum = IntVar()
    
    bTime = [0]*num
    aTime = [0]*num
    priorityList = [0]*num 
    for i in range(num):
        bTime[i] = IntVar()
        aTime[i] = IntVar()
        priorityList[i] = IntVar()

    Label(root, text='Process').grid(row=2,column=0)
    Label(root, text='Burst Time').grid(row=2,column=1)
    
    for i in range(num):
        Label(root, text="P"+str(i+1)).grid(row=i+3,column=0)
        Entry(root,textvariable=bTime[i]).grid(row=i+3,column=1)
        
    
        
    if( algof == 3):
        Label(root, text='Arrival Time').grid(row=2,column=2)
        Label(root, text='Priority').grid(row=2,column=3)
        for i in range(num):
            Entry(root,textvariable=aTime[i]).grid(row=i+3,column=2)
            Entry(root,textvariable=priorityList[i]).grid(row=i+3,column=3)
    if(algof==4):
        Label(root,text="Time quantum").grid(row=num+3,column=0)
        Entry(root,textvariable=quantum).grid(row=num+3,column=1)
        
   
    Button(root,text="Compute",fg = 'blue',command=lambda:solve(num,algof,bTime,aTime,priorityList,quantum)).grid(row=num+4,column=0) 


root = Tk()
root.geometry("800x600")

radioValue = IntVar()

current_value = IntVar()

root.title('Process schudling')
Radiobutton(root, text='SJF', variable=radioValue, value=1).grid(row=0,column=0)

Radiobutton(root, text='FCFS', variable=radioValue, value=2).grid(row=0,column=1)
Radiobutton(root, text='Priority non premtive', variable=radioValue, value=3).grid(row=0,column=2)

Radiobutton(root, text='Round Robin', variable=radioValue, value=4).grid(row=0,column=3)
Label(root, text='Number of process').grid(row=1,column=0)
sbox = Spinbox(root,textvariable=current_value, from_ = 0, to = 10).grid(row=1,column=1)
Button(root, text ='submit',command=lambda:createInputTable(current_value.get(),radioValue.get()), fg ='blue').grid(row=1,column=3)





mainloop()








