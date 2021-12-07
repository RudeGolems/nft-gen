# NFT Generator
This script generates NFT art based on its desired traits with their specific rarities. It has been used to generate the full collection of Rude Golems.
The intention behind this is simply the authentication of this project but also a way for new projects to easily create their own NFT collection without any coding experience.

**Features**
* NFT generation with unlimited amount of traits
* Quantity and rarity of each trait taken into account
* Removal of duplicates while generating
* Metadata creation for instant Candy Machine use

## Getting Started
Ensure you have [Python](https://www.python.org/downloads/) installed
Install PIP if you haven't yet
```
python get-pip.py
```
Install Pillow
```
pip install pillow
```
## Setup
1. Clone the repository or download the .zip. Example:
```
git clone git@github.com:RudeGolems/nft-generator.git
```
2. Paste all your traits in the `/images` directory
3. Open main.py
  * Insert your trait file names in the lists or create/remove lists (make sure to edit code after that)
  * Fill out the rarities json object with quantity and rarity (1 is 100%, 0.5 is 50%...)
  * Go to the bottom and edit the metadata to your liking
4. Run the script. Example:
```
cd nft-generator
python main.py
```
More information regarding all this you find in the code. You should understand it better there.
