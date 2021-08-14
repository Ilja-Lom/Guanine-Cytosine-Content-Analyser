"""NOTE: I do not believe this to be a viable solution using dictionaries. This is due to their inability to index making it hard to retrieve the correct values"""

new_sequence = True
title_sequence = {} #This is a dictionary for the title and corresponding sequence
list_of_sequences = []
sorting_by_GC = [] #this is a list in which the sequences are sorted by GC content
new_list = [] #test list

while new_sequence:
    title = input("If you are done with entering sequences, enter 'd'\nEnter the title of the sequence:\n")
    if title == "d":
        new_sequence = False
    else:
        sequence = input("Enter the sequence:\n")
        how_many_GC = sequence.count('G') + sequence.count('C')
        title_sequence[title] = sequence, how_many_GC
        list_of_sequences.append(title_sequence)
        title_sequence = {}

for sequence in list_of_sequences:
    new_list.append(*sequence.values()) #the * apparently 'unpacks' the list
    print(f"Printing list:\n{new_list}")
    print(new_list[1])


#for gc in set(title_sequence.values()):

#print(list_of_sequences)

#print(title_sequence)

#print(list_of_sequences[1])

##An idea I have is why not calculate the GC in right after entering the sequence? This is to evade accessing it later

















