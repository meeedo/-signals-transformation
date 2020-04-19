# importing the required module 
import matplotlib.pyplot as plt 


def Reverse (x_coordinates , y_coordinates ) :
       for m in range(0,number):
           x_coordinates[m]*=-1

       for b in range (0,number):
           print ("reversed ("+str(x_coordinates[b])+","+str(y_coordinates[b])+")")





def scale (x_coordinates , y_coordinates ,z) :
       x_array = x_coordinates 
       y_array = y_coordinates
       tmp=0
       
       for a in range(0,number):
               y_array[a]=y_coordinates[a]
                           
       if (z%1==0):
              
              for s in range(0,number):
                      #if(x_coordinates[s]%z ==0 ):
                             x_coordinates[s] *=z
                             tmp = int (x_coordinates[s])
                             if (tmp<=number):
                                    
                                    print(tmp)
                                    y_coordinates[s]=y_array[tmp-1]
                             else:
                                    x_coordinates[s]=0
                                    y_coordinates[s]=0
                      #else:
                       #      x_coordinates[s]=0
                        #     y_coordinates[s]=0
                     

       else:
              for s in range(0,number):
                      x_coordinates[s] *=z
                      tmp = int (x_coordinates[s])
                      if(x_coordinates[s]%1 ==0 ):
                             
                             if (tmp<=number):
                                    
                                    print(tmp)
                                    y_coordinates[s]=y_array[tmp]
                             else:
                                    x_coordinates[s]=0
                                    y_coordinates[s]=0
                      else:
                             x_coordinates[s]=0
                             y_coordinates[s]=0
       
       for d in range (0,number):
           print ("scaled ("+str(x_coordinates[d])+","+str(y_coordinates[d])+")")





def shift (x_coordinates , y_coordinates , r) :          
        for w in range(0,number):
           x_coordinates[w]+=r

        for q in range (0,number):
           print ("scaled ("+str(x_coordinates[q])+","+str(y_coordinates[q])+")")





number =int( input ("How many points?"))
#coordinates = robjects.vector()
x_coordinates = []
y_coordinates = []
for x in range(0,number):
    x_temp =int( input("enter x-coordinate: "))
    x_coordinates.append(x_temp)
    y_temp =int( input("enter y-coordinate: "))
    y_coordinates.append(y_temp)

choice = int( input("what do you want to do \n 1-Reverse \n 2-Shifting \n 3-Scaling"))
if choice == 1:
    Reverse(x_coordinates , y_coordinates )
    
elif choice == 2:
    z = int( input("Enter the value you want to shift with :"))
    shift (x_coordinates , y_coordinates , z)
    
elif choice == 3:
    r = float( input("Enter the value you want to scale with :"))
    scale (x_coordinates , y_coordinates , r)



#plt.bar for draw discrete
#plt.plote for draw a continous


for i in range (0,number):
       plt.bar(x_coordinates[i], y_coordinates[i]) 
  
# naming the x axis 
plt.xlabel('time - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('the graph after transformation :') 
    

# function to show the plot 
plt.show() 
