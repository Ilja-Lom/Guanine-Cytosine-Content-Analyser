import matplotlib.pyplot as plt

#initialising the required lists, and dictionaries
new_sequence = True #regulates the while loop function
titles = [] #stores the titles for the sequences
sequences = [] #stores the sequences
GC_content = [] #stores the integer value of the GC quantity per sequence
graph_data = {} #this stores the data for the graphs which includes the sequence title and the corresponding GC content

#loop to receive title and sequence
while new_sequence:
    title = input("If you are done with entering sequences, enter 'done'\nEnter the title of the sequence:\n")
    titles.append(title)
    if title == "done":
        new_sequence = False
    else:
        sequence = input("Enter the sequence:\n")
        sequences.append(sequence)
        GC_content.append(sequence.count('G') + sequence.count('C'))

#loop to calculate the GC content of each sequence
for content in GC_content:

    max_value = max(GC_content) #highest GC content value in the GC_content list
    max_index = GC_content.index(max_value) #index of sequence of highest GC content value
    graph_data[titles[max_index]] = max_value #appends the title and sequence of the highest GC sequence
    print(f"Sequence of {titles[max_index]} has the largest GC content of {max_value}") #this was used for testing
    GC_content[max_index] = 0 #this erases the sequence just processed so that the next largest could be found

#plotting data
plt.bar(graph_data.keys(), graph_data.values(), color='r')

#formating plot
plt.title("The Guanine-Cytosine Content of Sequences in Descending Order", fontsize=24)
plt.xlabel("The Title of the Sequence", fontsize=16)
plt.ylabel("Number of Guanine and Cytosine Nucleotides in the Sequence", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.style.use(['dark_background'])

plt.show()



