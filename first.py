global u
global v

def search_multiple_strings_in_file(file_name, list_of_strings):
    """Get line from the file along with line numbers, which contains any string from the list"""
    line_number = 0
    list_of_results = []
    # Open the file in read only modegh
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            line_number += 1
            # For each line, check if line contains any string from the list of strings
            for string_to_search in list_of_strings:
                if string_to_search in line:
                    # If any string is found in line, then append that line along with line number in list
                    list_of_results.append((string_to_search, line_number, line.rstrip()))
    # Return list of tuples containing matched string, line numbers and lines where string is found
    return list_of_results

matched_lines = search_multiple_strings_in_file('Audio_record.txt', ['Stream Open', 'Stop audio Recording'])
#print('Total Matched lines : ', len(matched_lines))
for elem in matched_lines:
    if elem[0] == 'Stream Open':
        z = elem[2]
        time1=z[18:20]
        global u
        u=int(time1)
        #print(int(time1))
    if elem[0] == 'Stop audio Recording':
        z = elem[2]
        time2 = z[18:20]
        #print(int(time2))
        global v
        v=int(time2)
        #time3=time2-time1

#    print('Word = ', elem[0], ' :: Line Number = ', elem[1], ' :: Line = ', elem[2])
w=v-u
if w==30:
    print("pass")
else:
    print("fail")

