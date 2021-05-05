###Modeling and Simulation of protein structure as a 2D lattice model
###Input data:PHPHPHPHPPHPHPPPPHHPPPHPHPPHPPPHPPHPHHPPPHHHHPHPHPPHPHHPHHHHPPHPHPPHPHHPHHPHPHPPHPHHHH
###part A: Given the input data generate a configurations and report coordinate and orientation for the given input data.

####importing necessary tool
import random

###test string and converting string to list
protein_sequence ="PHPHPHPHPPHPHPPPPHHPPPHPHPPHPPPHPPHPHHPPPHHHHPHPHPPHPHHPHHHHPPHPHPPHPHHPHHPHPHPPHPHHHH"
protein_sequence_list=list(protein_sequence)

####create a walk variable for path and walking dictionary
walk= ["up", "down", "right", "left"]
orientation_dictionary={"up":"01","right":"00","left":"10","down":"11"}
walk_dict= {"up": {"x": 0, "y": 1}, "down": {"x": 0, "y": -1},"left": {"x": -1, "y": 0},"right": {"x": 1, "y": 0}}

###initializing dictionary for 1st aminoacid
dict={"0,0":{"AA":protein_sequence_list[0], "Next":None, "Prev":None, "Move":None,"orientation":None}}
count=0
current_position=[0,0]
char_currentpos="0,0"
input2=protein_sequence_list[1:]
for i in range(len(input2)):
    count+=1
    random_walk=random.choice(walk) ###path walked randomly
    random_dict=walk_dict[random_walk]
    update_position=[current_position[0]+random_dict["x"],current_position[1]+random_dict["y"]] ####adding x and y value to the move ,it gives the interim positions to current position
    move_position = str(update_position[0])+"," + str(update_position[1]) ###changing walk position to string
    if move_position not in dict:
        dict[char_currentpos]["Next"]=move_position
        dict[char_currentpos]["orientation"]=orientation_dictionary[random_walk]
        prev=char_currentpos
        char_currentpos=move_position
        current_position=update_position ###replace previous position by updated position of walk
        dict[char_currentpos]={"AA":input2[i],"Prev":prev,"Next":None,"Move":random_walk,"orientation":None}
    else:
        walk.remove(random_walk) ###remove walk if it is already occupied
        random_walk=random.choice(walk) ###random walk
        random_dict=walk_dict[random_walk]
        update_position=[current_position[0]+random_dict["x"],current_position[1]+random_dict["y"]]
        move_position = str(update_position[0])+"," + str(update_position[1])
        dict[char_currentpos]["Next"]=move_position
        prev=char_currentpos
        dict[char_currentpos]["orientation"]=orientation_dictionary[random_walk]
        char_currentpos=move_position
        current_position=update_position
        dict[char_currentpos]={"AA":input2[i],"Prev":prev,"Next":None,"Move":random_walk,"orientation":None}
print(dict)

print("AA"," ","Move"," ","Orientation")
element="0,0"
while element:
    print(dict[element]["AA"],dict[element]["Move"],dict[element]["orientation"])
    element=dict[element]["Next"]
    if element==None:
        break
        

###Part B: Validating given configuration (an orientation or coordinate string) from part A.

coordinates='- 01 00 00 00 11 10 10 11 00 11 11 11 11 00 00 11 00 00 11 00 00 00 01 00 00 01 10 01 00 01 10 10 10 01 10 01 10 10 01 10 01 01 01 01 01 00 01 00 00 11 10 11 11 11 11 11 00 01 00 11 11 00 01 01 01 00 00 11 10 11 11 00 01 00 00 00 00 01 10 10 01 01 01 10'
coordinates=coordinates.split(' ')
# print(coordinates)
initial_coordinate=[(0,0)] ###start coordinate at 00
for i in range(1,len(coordinates)):
    x=coordinates[i]
    # print(x)
    set_cord=initial_coordinate[len(initial_coordinate)-1]
    # print(set_cord)
    if x=="00":
        changed_coordinate=(set_cord[0]+1,set_cord[1])
    elif x=="01":
        changed_coordinate=(set_cord[0],set_cord[1]+1)
    elif x=="10":
        changed_coordinate=(set_cord[0]-1,set_cord[1])
    elif x=="11":
        changed_coordinate=(set_cord[0],set_cord[1]-1)
    initial_coordinate.append(changed_coordinate) ###joining list of coordinates by using .append
print(initial_coordinate)
set_initial=set(initial_coordinate) ###making set of coordinates to compare similarity of coordinates
# print(set_initial)
if len(set_initial)==len(coordinates): ###comparing length of coordinate and initial coordinates
    print("It is valid")
else:
    print("It is not valid")