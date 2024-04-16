import re

def markdown_to_blocks(markdown):
    # Split the markdown into blocks using double newline as delimiter
    blocks = re.split(r'\n{2,}', markdown)
    
    # Remove leading and trailing whitespace from each block
    blocks = [block.strip() for block in blocks]
    
    # Remove any empty blocks
    blocks = [block for block in blocks if block]
    
    return blocks