# Iris (Jihan) Zhang
# ID: jxz971
import sys

try:
    with open(sys.argv[1], 'r') as schema:
        # read the schema file line by line
        schema_contents = schema.readlines()
        LINE_WIDTH = 0
        for schema_line in schema_contents:
            # ignore the commented lines
            if schema_line[0] != '#':
                # find 'width'
                index_of_keyword = schema_line.find('width')
                # find the index of next token and record that token
                while index_of_keyword != -1:
                    index_of_next_token = index_of_keyword + 5
                    next_token = ''
                    # ignore whitespaces
                    while schema_line[index_of_next_token] == ' ':
                        index_of_next_token = index_of_next_token+1
                    # record tokens until next whitespace
                    while index_of_next_token < len(schema_line) and schema_line[index_of_next_token] != ' ':
                        next_token = next_token + schema_line[index_of_next_token]
                        index_of_next_token = index_of_next_token + 1
                    # check whether the token is an integer
                    try:
                        WIDTH_INTEGER = int(next_token)
                    except ValueError:
                        WIDTH_INTEGER = 0
                    index_of_keyword = schema_line.find('width', index_of_keyword+1)
                    # add each line together
                    LINE_WIDTH = LINE_WIDTH + WIDTH_INTEGER

    with open(sys.argv[2], 'r') as data:
        # read data file line by line
        data_content = data.readlines()
        valid_line = 0
        total_line = 0
        for data_line in data_content:
            # calculate the total lines in data file
            total_line = total_line +1
            # find the number of valid lines in data file
            if len(data_line) - data_line.count('\n') == LINE_WIDTH:
                valid_line = valid_line+1
    # calculate the number of invalid lines in data file
    invalid_line = total_line-valid_line
    # print formatted output
    print(str(valid_line) + ' ' + str(invalid_line))
# deal with missing file
except IOError:
    print('0 0')