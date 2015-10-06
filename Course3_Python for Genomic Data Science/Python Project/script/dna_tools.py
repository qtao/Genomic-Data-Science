# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:25:20 2015

@author: zhihuixie
The program includes a set of tools for dna sequence analyses. To use the tool 
sets, please assign the path and file name to the class function. For example:
dna_tools = dna_tool_sets ("../data/dna.example.fasta")
Then, call the functions in the class, e.g call function to check length of dna
sequence:
length = dna_tools.check_length()
"""



class dna_tool_sets ():
    """ 
    This class includes a set of tools for dna sequence analyses:
    a. count_records

    b. check_length
    
    c. orf_identifier
       
    d. repeats_identifier
    
    parameter: file name including path directory
    Note: the file should be in FASTA format
    
    """
    def __init__(self, file_name):
        """ this function open input file and transform each record to dictornary
            the key and value of the dict are header and dna sequence of the record,
            respectively
        """
        self.file_name = file_name # initiate loading file 
        self.dict = {} # initiate an empty dictornary
        f_reader = open (self.file_name)
        for line in f_reader:
            line = line.strip("\n") # remove "\n" in line
            if ">" in line: # check if this line is a header
                header = line # assign line to header
                self.dict[header] = "" #add header to dictornary with an initial empty string
            else:
                self.dict[header] += line # add dna sequence to the header accordingly
        f_reader.close()
    
    def count_records (self):
        """ this function count number of records in the file"""
        number_of_records = len(self.dict) # check records in dictornary
        # Q1: How many records are in the multi-FASTA file?
        print "Q1: How many records are in the multi-FASTA file: %d \n"\
               %number_of_records
        #return number_of_records
        
    def check_length(self):
        """
        this function check length of each record and the according header 
        of the record
        """
        length_dict = {} # creat a dictornary to record length of each record
        for key, value in self.dict.items():
            length_dict[key] = len(value)
            
        lengths = length_dict.values() # count length for each sequence
        
        max_length = max(lengths) # max length of sequences 
        min_length = min(lengths) # min length of sequences
        # identifier of sequences with max length
        record_max_length = [item for item in length_dict if length_dict[item] == max_length]
        # identifier of sequences with min length        
        record_min_length = [item for item in length_dict if length_dict[item] == min_length]
        
        # Q2: What is the length of the longest sequence in the file?
        print "Q2: The length of the longest sequence: %d \n"%max_length, \
              "The number of longest sequence: %d \n"%len(record_max_length)
        # Q3: What is the length of the shortest sequence in the file?
        print "Q3: The length of the shortest sequence: %d \n"%min_length, \
              "The number of shortest sequence: %d \n"%len(record_min_length)
        # uncomment the return code to return the whole length information for 
        # each record
        #return length_dict
               
    def find_pos(self, dna):
        """ 
        help function for orf_identifier: 
        find start position and length for each read frame for a given sequence
        dna: sequence, string
        """
        start_code = "ATG"
        stop_codes = ["TAA", "TAG", "TGA"]

        pos_dict = {} #record orfs of each frame to dictornary
        
        for i in range(3): # walk through 3 different frames
            # record strat position and length for each frame to a list
            pos = []
            # generate frames
            if i == 0:
                frame = [dna[j:j+3] for j in range(i, len(dna), 3)]
            else:
                frame = [dna[:i]] + [dna[j:j+3] for j in range(i, len(dna), 3)]
            # find all possible start postions and stop positions
            start_pos = []
            stop_pos = []
            try:
                index_start_pos = [m for m, y in enumerate(frame) if \
                                  y == start_code]
                start_pos += index_start_pos # find possible positions for start code "ATG"
            except ValueError:
                pos.append((-1, 0)) # return -1 as start position if no ATG
                continue
 
            for stop_code in stop_codes:
                try:
                    # find all possible positions of stop codes
                    index_stop_code = [n for n, x in enumerate(frame) if \
                                       x == stop_code and n > min(start_pos)]
                    stop_pos += index_stop_code
                except ValueError:
                    continue
            if len(stop_pos) == 0: # add -1 as start position when no stop code find
                 pos.append((-1, 0))
            else:
                #find the closest paired code
                 while len(start_pos) != 0:
                     start = min(start_pos)
                     try:
                         end = min([stop for stop in stop_pos if stop > start])
                     except ValueError:
                         break     
                 # add start position and length
                     s_pos = len("".join(frame[:start])) + 1
                     pos.append((s_pos, (end - start + 1)*3))
                     start_pos.remove(start) 
            pos_dict["frame%d"%(i+1)] = pos 
            
        return pos_dict
        
    def revs_complement(dna):
        """
        help function for orf_identifier:
        to transform a sequence to reverse complementary sequence
        """
        pairs = {"A": "T", "C": "G", "G": "C", "T": "A"} # complementary code
        c_dna = [pairs[s] for s in dna] # complementary replace
        return "".join(c_dna)[::-1] # reverse
        
    
    def orf_identifier (self):
        """
        This function return all the orf information with start posiotion and
        length of orf in read frame 1, 2 and 3
        the values for frame 1, 2, and are represented as pairs of tuple in a list
        for example: {"header1": {"frame1":[(0, 100)], "frame2":[(20, 400)], "frame3":[(-1, 0)]},...} 
        represents for header1:
        frame1- start position: 0, length of orf: 100
        frame2- start position: 20, length of orf: 400
        frame3- No ORF detected
        """
        orf = {}
        for header, dna_seq in self.dict.items(): # generate orf for the whole file
            pos = self.find_pos(dna_seq)
            orf[header] = pos
        # find header for question 7
        id_key = [key for key in orf if "gi|142022655|gb|EQ086233.1|129" in key]
        idx = id_key[0]  
        # generate list of frames for questions 4 to 7
        frame1, frame2, all_frames, id_frames = [], [], [], []
        for key, dict_value in orf.items():
            frame1 += dict_value["frame1"]
            frame2 += dict_value["frame2"]
            frames = dict_value["frame1"] + dict_value["frame2"] + dict_value["frame3"]
            all_frames += frames
            if key == idx:
                id_frames = dict_value["frame1"] + dict_value["frame2"] + dict_value["frame3"]
            
        #Q4: What is the length of the longest ORF appearing in reading
        #frame 2 of any of the sequences?
        frame2_max_length = max(frame2, key = lambda x: x[1])
        print "Q4: The length of longest ORF in frame2: %d\n"%frame2_max_length[1]
        #Q5: What is the starting position of the longest ORF in reading frame 1 
        #in any of the sequences? 
        
        frame1_max_length_pos = max(frame1, key = lambda x: x[1])
        print "Q5: The start position of longest ORF in frame1: %d\n"%frame1_max_length_pos[0]
        #Q6: What is the length of the longest ORF appearing in any sequence and 
        #in any forward reading frame?
        max_length = max(all_frames, key = lambda x: x[1])
        print "Q6: The longest ORF of all frames and sequences: %d\n"%max_length[1]
        #Q7: What is the length of the longest forward ORF that appears in the 
        #sequence with the identifier gi|142022655|gb|EQ086233.1|129?

        max_length_id = max(id_frames, key = lambda x: x[1])
        print "Q7: The length of longest ORF for ", idx, "is: %d \n" %max_length_id[1]
        
        # uncomment the return code to return the whole orf information 
        #including starting position and length of each frame for each sequence
        
        #return orf
            
    def find_repeats(self, dna, n):
        """
        This help function for repeats_identifier find and count repeats for 
        each dna sequence
        dna: sequence, string
        n: number of repeats, int
        """
        repeats = {}
        for i in range(0, len(dna)):
            repeat = dna[i:i+n] # generate possible repeats
            if len(repeat) == n:
                if repeat not in repeats:
                    repeats [repeat] = 1 # initiate record
                else:
                    # count repeated repeats
                    repeats[repeat] = repeats.get(repeat) + 1
        return repeats
    
    def repeats_identifier(self, n):
        """
        This function generates repeats with counts for each record 
        (repeats_set) and for the whole file (combined_repeats)
        n: number of repeats, int
        """
        # record the repeats with counts for each record 
        repeats_set = {}
        for header, dna_seq in self.dict.items():
            repeats = self.find_repeats(dna_seq, n)
            repeats_set[header] = repeats 
        # record the repeats with counts for the whole file
        combined_repeats = {}
        for dict_value in repeats_set.values():
            for key in dict_value:
                if key not in combined_repeats:
                    combined_repeats[key] = dict_value[key]
                else:
                    combined_repeats[key] = combined_repeats.get(key) \
                                            + dict_value[key]
        # Q8:Find the most frequently occurring repeat of length 7 in all 
        # sequences. How many times does it occur in all?
        if n == 7:
            most_freq_7 = max (combined_repeats.values())
            print "Q8: The most frequently repeats occur: %d times \n"%most_freq_7
        # Q10:Which one of the following repeats of length 7 has a maximum 
        #number of occurrences?
            most_freq_7_seq = [key for key in combined_repeats if \
                       combined_repeats[key] == max(combined_repeats.values())]
            print "Q10: The following repeats occured most frequently: \n", most_freq_7_seq
        # Q9:Find all repeats of length 10 in the input file. Let's use Max to 
        #specify the number of copies of the most frequent repeat of length 10. 
        #How many different 10-base sequences occur Max times?
        if n == 10:
            # answer question 9
            count_most_freq_10 = len([value for value in combined_repeats.values()\
                             if value == max(combined_repeats.values())])
        
        
            print "Q9: The number of different 10-base sequences occur max times: %d \n"\
                  %count_most_freq_10
        
        # uncomment the return code to return the repeats with counts for each record 
        # (repeats_set) and for the whole file (combined_repeats)
        #return repeats_set, combined_repeats
        
if __name__ == "__main__":
    
    file_name = "../data/dna3.fasta"
    dna_tools = dna_tool_sets (file_name)
    # Q1: How many records are in the multi-FASTA file?
    dna_tools.count_records()
    
    # Q2: What is the length of the longest sequence in the file?
    # Q3: What is the length of the shortest sequence in the file?
    dna_tools.check_length()
    
    #Q4: What is the length of the longest ORF appearing in reading
    #frame 2 of any of the sequences?
    #Q5: What is the starting position of the longest ORF in reading frame 1 
    #in any of the sequences? 
    #Q6: What is the length of the longest ORF appearing in any sequence and 
    #in any forward reading frame?
    #Q7: What is the length of the longest forward ORF that appears in the 
    #sequence with the identifier gi|142022655|gb|EQ086233.1|129?
    dna_tools.orf_identifier()
    
    # Q8:Find the most frequently occurring repeat of length 7 in all 
    # sequences. How many times does it occur in all?
    # Q10:Which one of the following repeats of length 7 has a maximum 
    #number of occurrences?
    dna_tools.repeats_identifier(7)
    
    # Q9:Find all repeats of length 10 in the input file. Let's use Max to 
    #specify the number of copies of the most frequent repeat of length 10. 
    #How many different 10-base sequences occur Max times?
    dna_tools.repeats_identifier(10)