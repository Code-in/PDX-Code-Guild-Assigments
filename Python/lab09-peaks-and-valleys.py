

def peaks(data):
    index_back2 = 0
    index_back1 = 0
    output = []
    for index in range(len(data)):
        #print(f"index:{index} value:{data[index]}")
        if (data[index_back1] > data[index] and data[index_back1] > data[index_back2]) and index_back1 not in output: #going up
            #print(f"higher: index:{index} value:{data[index]}")
            output.append(index_back1)
        index_back2 = index_back1
        index_back1 = index
    return output

def valleys(data):
    index_back2 = 0
    index_back1 = 0

    output = []
    for index in range(len(data)):
        if (data[index_back1] < data[index] and data[index_back2] > data[index_back1]) and index_back1 not in output: #going up
            #print(f"higher: index:{index} value:{data[index]}")
            output.append(index_back1)
        index_back2 = index_back1
        index_back1 = index

    return output

def peaks_and_valleys(data):
    output = []
    output = peaks(data)
    output += valleys(data)
    return output

def dams(data, peaks, valleys):
    current_peak = 0
    output = []
    for i in range(len(peaks)):
        current_peak = peaks[i]
        for j in range(peaks[i] + 1, len(data)):
            if data[j] == data[current_peak]:
                output.append([peaks[i],j])
                break
    return output


def max_height_of_data(data):
    maxval = 0
    for val in data:
        if val > maxval:
            maxval = val
    return maxval



def print_xo(data, peaks, valleys, dams):
    output = []
    maxheight = max_height_of_data(data)
    print(f"max: {maxheight}")
    
    graph = ""
    
    for v in range(maxheight, 1, -1): # loop vertically to max height for each horizontal 9 element
        horzontal = ""
        for h in range(len(data)): # looping horizontally through all the 20 elements
            if data[h] > v:
                horzontal += "X"
            else:
                in_dam = False
                for dam in dams:
                    if (dam[0] < h < dam[1]) and ((v >= data[h]) and (v < data[dam[0]])): # need to determine if vertical value is >= than base value and < than dam vertical value.
                        in_dam = True
                        break
                if in_dam:
                    horzontal += "0"
                else:
                    horzontal += " "


                
        print(horzontal)
    # check to make sure we are not equal to a peak or a valley or in the dam ranges.
    






def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    print(f"peaks: {peaks(data)}") # [6, 14]
    print(f"valleys: {valleys(data)}") # [9, 17]
    print(f"peaks and valleys: {peaks_and_valleys(data)}") # # [6, 9, 14, 17]
    print(f"dams: {dams(data, peaks(data), valleys(data))}")
    
    peaks_list = peaks(data)
    valleys_list = valleys(data)
    dam_list = dams(data, peaks(data), valleys(data))
    print(f"print out: {print_xo(data, peaks_list, valleys_list, dam_list)}")
    print_xo(data, peaks_list, valleys_list, dam_list)
main()