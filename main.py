from PIL import Image
import json
import random
import threading
from itertools import repeat

"""
Watch out on the syntax and make sure to add a new trait all over the script if you add one. Same goes for removing a trait.
"""
rarities = {
    "Backgrounds": [{'Trait': 'Example1', 'Quantity': 4444, 'Rarity': 0.5}, {'Trait': 'Example2', 'Quantity': 4444, 'Rarity': 0.5}], # 0.5 means 50% of and quantity just the amount of usage in the collection
    "Skins": [{'Trait': 'Example1', 'Quantity': 4444, 'Rarity': 0.5}, {'Trait': 'Example2', 'Quantity': 4444, 'Rarity': 0.5}],
    "Armors": [{'Trait': 'Example1', 'Quantity': 4444, 'Rarity': 0.5}, {'Trait': 'Example2', 'Quantity': 4444, 'Rarity': 0.5}],
    "Chains": [{'Trait': 'Example1', 'Quantity': 4444, 'Rarity': 0.5}, {'Trait': 'Example2', 'Quantity': 4444, 'Rarity': 0.5}],
    "Mouths": [{'Trait': 'Example1', 'Quantity': 4444, 'Rarity': 0.5}, {'Trait': 'Example2', 'Quantity': 4444, 'Rarity': 0.5}],
    "Eyes": [{'Trait': 'Example1', 'Quantity': 4444, 'Rarity': 0.5}, {'Trait': 'Example2', 'Quantity': 4444, 'Rarity': 0.5}],
    "Over Heads": [{'Trait': 'Example1', 'Quantity': 4444, 'Rarity': 0.5}, {'Trait': 'Example2', 'Quantity': 4444, 'Rarity': 0.5}] # don't put a comma here because it is the end of the json object
}

whole = [] # for duplicate check

"""
Creates random shuffled lists of each trait category with all its traits and their desired quantity.
"""
backgroundsList = []
for x in rarities['Backgrounds']:
    backgroundsList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(backgroundsList)
skinsList = []
for x in rarities['Skins']:
    skinsList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(skinsList)
armorsList = []
for x in rarities['Armors']:
    armorsList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(armorsList)
chainsList = []
for x in rarities['Chains']:
    chainsList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(chainsList)
mouthsList = []
for x in rarities['Mouths']:
    mouthsList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(mouthsList)
eyesList = []
for x in rarities['Eyes']:
    eyesList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(eyesList)
overheadsList = []
for x in rarities['Over Heads']:
    overheadsList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(overheadsList)

path = 'images/' # standard path to the images directory

"""
Please keep the same format which is having Eyes_ for example at least before the actual trait name. Don't forget .png or .jpg or whatever at the end.
"""
bgs = ['01_BG_Blue.png', '02_BG_Red.png']
skins = ['01_Skins_Base.png', '02_Skins_Special.png']
armors = ['00_Armor_Example1.png', '01_Armor_Example_2.png']
chains = ['00_Chains_Example1.png', '01_Chains_Example 2.png']
mouths = ['01_Mouth_Example 1.png', '02_Mouth_Example2.png']
eyez = ['00_Eyes_Example 1.png', '01_Eyes_Example_2.png']
overheads = ['00_Overhead_Example_1.png', '01_Overhead_Example2.png']

count = 0

def gen():
    while count != 8888: # size of collection, so script stops
        traits = []
        traits_names = []

        """
        Just some checks to avoid issues coming up in the big lists of traits.
        """
        for x in backgroundsList:
            if len(x) < 2:
                backgroundsList.remove(x)
        for x in skinsList:
            if len(x) < 2:
                skinsList.remove(x)
        for x in armorsList:
            if len(x) < 2:
                armorsList.remove(x)
        for x in chainsList:
            if len(x) < 2:
                chainsList.remove(x)
        for x in mouthsList:
            if len(x) < 2:
                mouthsList.remove(x)
        for x in eyesList:
            if len(x) < 2:
                eyesList.remove(x)
        for x in overheadsList:
            if len(x) < 2:
                overheadsList.remove(x)
                
        """
        Collecting of the randomly chosen traits.
        """
        bgcheck = random.choice(backgroundsList)
        backgroundsList.remove(bgcheck)
        for x in bgs:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == bgcheck:
                bg = x
                break

        skincheck = random.choice(skinsList)
        skinsList.remove(skincheck)
        for x in skins:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == skincheck:
                skin = x
                break

        armorcheck = random.choice(armorsList)
        armorsList.remove(armorcheck)
        for x in armors:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == armorcheck:
                armor = x
                break

        chaincheck = random.choice(chainsList)
        chainsList.remove(chaincheck)
        for x in chains:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == chaincheck:
                chain = x
                break

        mouthcheck = random.choice(mouthsList)
        mouthsList.remove(mouthcheck)
        for x in mouths:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == mouthcheck:
                mouth = x
                break

        eyescheck = random.choice(eyesList)
        eyesList.remove(eyescheck)
        for x in eyez:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == eyescheck:
                eyes = x
                break

        overheadcheck = random.choice(overheadsList)
        overheadsList.remove(overheadcheck)
        for x in overheads:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == overheadcheck:
                overhead = x
                break
                
        """
        Exceptions for traits that don't fit with everything.
        """       
        if armor == '01_Armor_Example1.png':
            eyes = '00_Eyes_None.png'
        if overhead == '07_Overhead_Example_2.png':
            eyes = '00_Eyes_None.png'
            mouth = '00_Mouth_None.png'

        traits.extend((bg, skin, armor, chain, mouth, eyes, overhead)) # putting all traits for this NFT in a list (make sure to choose your order of layering by this list from left to right)

        for trait in traits:
            trait = trait.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] # getting the exact trait names from the file name
            traits_names.append(trait)
            
        if traits not in whole: # duplicate check

            whole.append(traits)

            for trait in traits:
                if 'BG' in trait:
                    nft = Image.open(path+trait).convert('RGBA') # important for background
                else:
                    trait = Image.open(path+trait)
                    nft = Image.alpha_composite(nft, trait) # layer process of each trait
            
            """
            This is the most dangerous part. Please triple check your metadata because 95% of all errors when uploading to a Candy Machine are caused by wrong metadata.
            Please remove the comments from it if you are done with setup xd.
            """
            metadata = {
                "name":f"Example #{count+1}","symbol":"", # +1 because metadata files need to start with 0 but your NFT obviously has the number 1
                "description":"This is my awesome description.", # description of your project
                "seller_fee_basis_points":500,"image":f"{count}.png","external_url":"https://example.com/", # 500 stands for 5% royalties on marketplaces and external_url is your project's website
                "attributes":[
                    {"trait_type":"Background","value":traits_names[0]}, # number in the brackets is the index number of the trait in the list where you decided the layer order
                    {"trait_type":"Skin","value":traits_names[1]},
                    {"trait_type":"Armor","value":traits_names[2]},
                    {"trait_type":"Chain","value":traits_names[3]},
                    {"trait_type":"Mouth","value":traits_names[4]},
                    {"trait_type":"Eyes","value":traits_names[5]},
                    {"trait_type":"Over Head","value":traits_names[6]}],
                    "collection":{"name":"Project","family":"Project"},
                    "properties":{"files":[{"uri":f"{count}.png","type":"image/png"}],
                    "category":"image","maxSupply":1,"creators":[{"address":"JvdfHOfbu9bhfgbDF123456789","share":100}]} # 100 means 100% of the royalties' proceeds and you can add more to split it
            }

            nft.save(f'results/{count}.png',"PNG") # saving of the generated NFT

            metadata = json.dumps(metadata)
            metadataFile = open(f"results/{count}.json", "w")
            metadataFile.write(metadata) # saving of the metadata of this generated NFT
            metadataFile.close()

            count += 1

        else: # add traits to the list when a duplicate is found
            backgroundsList.append(traits_names[0])
            skinsList.append(traits_names[1])
            armorsList.append(traits_names[2])
            chainsList.append(traits_names[3])
            mouthsList.append(traits_names[4])
            eyesList.append(traits_names[5])
            overheadsList.append(traits_names[6])
            invisibleList.append(virtue)

    else:
        print('Successfully Generated All NFTs!')

threading.Thread(target=gen, args=()).start() # thread to start the gen, feel free to add more function and threads to speed up the generation process
