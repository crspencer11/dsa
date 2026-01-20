import json
from typing import List

filename = "/home/coderpad/data/sample_blocks.json"
f = open(filename, "r")
blocks = json.loads(f.read())
f.close()

def main(input: List[dict]):
    """
    [
        ['Client', 'Policy Number'],
        ['Frami Group', 'ABC-123']
    ]
    """
    max_rows, max_cols = find_dimensions(blocks)
    output_array = [[None for _ in range(max_cols)] for _ in range(max_rows)]

    for block in input:
        if block["BlockType"].lower() == "cell":
            row, col = block['RowIndex'] - 1, block['ColumnIndex'] - 1
            relationships = block['Relationships'][0]
            children = relationships['Ids']
            output_str = find_words(children, input)
            output_array[row][col] = output_str
            
    return output_array

def find_words(children: List[str], json_input: List[dict]) -> str:
    final_words = []
    for child in children:
        for line_item in json_input:
            if line_item['Id'] == child:
                final_words.append(line_item['Text'])
    return " ".join(final_words)

def find_dimensions(json_input):
    row_size, col_size = 0, 0
    for block in json_input:
        if block["BlockType"].lower() != 'word':
            if block['RowIndex'] > row_size:
                row_size = block['RowIndex']
            
            if block['ColumnIndex'] > col_size:
                col_size = block['ColumnIndex']
    return row_size, col_size

output = main(blocks)