#create dialogues for npc with only 1 button
#structure of imput file
#scene tag
#name (if the name is the same as the last npc, you can skip writing it)
#text
#button name
#each thing must be seperated by a new line
import json
import copy



infile = "input.txt"
otfile=open("output.json","w")

scenes=[]
dialogue={"scenes":scenes}
buttons=[{"name":"","commands":"/dialogue open @s @initiator "}]
npc = {"scene_tag":"","name":"","text":"","buttons":buttons}


i = 0
j = 0
last_name=""

with open(infile) as f:
    for line in f:
        if i==4:
            i=0
        if i == 0:
            npc["scene_tag"] = line.strip()
        if i==1:
            if line.strip()=="":
                npc["name"] = last_name
            else:
                npc["name"] = line.strip()
                last_name=npc["name"]
        if i == 2:
            npc["text"] = line.strip()
        if i==3:
            buttons[0]["name"] = line.strip()
            scenes.append(copy.deepcopy(npc))
        i+=1

json.dump(dialogue,otfile,indent=2)
otfile.close()
            

        
        

# save the last name in another variable
# if the line is not empty pass the new variable and add save the new variable as last_name 
# if the line is empty than pass the last_name as the variable