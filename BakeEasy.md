# Bake Easy Requirements

# Option to select which image to project

# TODO
#Creates UV Panel
#-1. Creates SmartUV (Selected when Bake is pressed)
#-2. Creates ProjectionUV (Keep selected only before the  baking process)


# TODO
#Create Material 
#--Name material  (Material_Name: Baked_Em_<ObjectName>)
#--An open image selection ("../Textures/<Selected Image>")
#--Create ShaderEmissionNode (strength: 1.00) 
#--Connect ShaderEmissionNode.output["Emission"] to MaterialOutput.input["surface"]

# TODO
#Check Image(ID) class
#--Creates blank image node (ID: <Material_Name>, height: 1024, width: 1024, alpha_mode: 'NONE', selected: false:) 
#--Creates blank image node (filepath: "../<Selected Image>", selected: true) -> connect This.image.input["color"] to ShaderEmissionNode.input["surface"]
#Let user know they are ready to make changes to projectionUV

# TODO
#Only bake after you project everything correctly
#Bake
#Saves image and connects new baked image  
#--Selects SmartUV 
#--Selects Blank Image Node (ID: <Material_Name)
#--Saves Image 
#Connect new Blank Image (ID:<Material_Name) -> ShaderEmissionNode.input["Color"]

