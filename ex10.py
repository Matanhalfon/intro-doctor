###################################
# ex10.py
# matan halfon,matan.halfon,205680648
# intro2cs ex7 2017-2018
# Describe : building a decision  tree of illness which every leaf is
# a illness which suite to the symptoms yes or no had in diagnose
# to get to this path in the tree.
# also building a tree accordingly to the some symptomes and records of former
# petiante
###################################

import itertools as iter

class Node:
    '''A class that every node holds data and childes a positive and negative'''
    def __init__(self, data="", pos=None, neg=None):
        self.data = data
        self.positive_child = pos
        self.negative_child = neg

    def get_data(self):
        ''':return the data'''
        return self.data

    def get_positive(self):
        ''':return the positive childe'''
        return self.positive_child

    def get_negative(self):
        ''':return negative'''
        return self.negative_child

    def is_leaf(self):
        ''':return true if the node childes are None'''
        if self.positive_child == None and self.negative_child == None:
            return True

    def set_pos_childes(self, positive):
        '''set the node positive childe'''
        self.positive_child = positive

    def set_neg_childes(self, negative):
        '''set the node negative childe'''
        self.negative_child = negative


class Record:
    '''class thet holds a petint record holds the patiant illnes and his symptoms'''
    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.split()
            records.append(Record(words[0], words[1:]))
        return records




class Diagnoser:
    '''A class that holds a root(the first node of the tree) and can preform all kind of diagnosik methods on it'''
    def __init__(self, root):
        self.__root = root
        self.__list_of_illness = []
        self.list_of_paths_to_illness = []

    def diagnose(self, symptoms):
        '''A method that diagnose which illness you have acoordingly to the symptoms and the root the class holds'''
        return self.diagnose_helper(symptoms, self.__root)

    def diagnose_helper(self, symptoms, node):
        '''A helping function that preform the recursive the diagnose '''
        if (node.positive_child == None) and (node.negative_child == None):
            return node.data
        elif node.data in symptoms:
            node = node.positive_child
            return self.diagnose_helper(symptoms, node)
        elif node.data not in symptoms:
            node = node.negative_child
            return self.diagnose_helper(symptoms, node)

    def calculate_error_rate(self, records):
        '''A method that cheks if the diagnose was right for each record and return an error rate
        which cumpute by divding the error num by all the records '''
        error_count = 0
        for record in records:
            symptoms = record.symptoms
            if self.diagnose(symptoms) != record.illness:
                error_count += 1
        error_rate = error_count / len(records)
        return error_rate

    def all_illnesses(self):
        '''a method that return all the illnessses of the tree'''
        self.all_illnesses_helper(self.__root)
        return sorted(self.__list_of_illness)

    def all_illnesses_helper(self, node):
        '''A helping function for "all illnesses" that run along the tree and retun the leaf'''
        if node.positive_child == None:
            self.__list_of_illness.append(node.data)
            return
        left = node.negative_child
        right = node.positive_child
        self.all_illnesses_helper(left)
        self.all_illnesses_helper(right)

    def most_common_illness(self, records):
        '''a method that return the most common illness in the tree '''
        illness_dic = {}
        most_commen_illnes = None
        max_reptitive = 0
        for record in records:
            illness = self.diagnose(record.symptoms)
            if illness not in illness_dic:
                illness_dic[illness] = 1
            else:
                illness_dic[illness] += 1
            if illness_dic[illness] > max_reptitive:
                max_reptitive = illness_dic[illness]
                most_commen_illnes = illness
        return most_commen_illnes

    def paths_to_illness(self, illness):
        '''A method that return the path to each illness of the by true false for each "turn " in the tree'''
        path = []
        self.path_to_illness_helper(illness, self.__root, path)
        return self.list_of_paths_to_illness

    def path_to_illness_helper(self, illness, node, path, ):
        '''An helping function for path to illnesss the method run along the tree recursivly and "collcting the
        oath data" and when getting to a leaf the function add it to the self path for illness'''
        if node.positive_child == None and node.negative_child == None:
            if node.data == illness:
                the_path = path[:]
                return the_path
            return None
        else:
            path = path + [True]
            pos_path = self.path_to_illness_helper(illness, node.positive_child, path)
            if pos_path != None:
                self.list_of_paths_to_illness.append(pos_path)
            path.pop()
            path = path + [False]
            neg_path = self.path_to_illness_helper(illness, node.negative_child, path)
            if neg_path != None:
                self.list_of_paths_to_illness.append(neg_path)
            path.pop()
        return None


def build_tree(records, symptoms):
    ''''A function that gets a bunch of symptoms and records and return the root of a tree of which every of the
    symptoms are in the same deapth of the tree,  and than place the most commen illness for this symptoms
     from the records to the leaf using the helping function "build_symptoms_tree" to do it recursively'''
    path={}
    tree = build_symptom_tree(symptoms,records,path)
    return tree

def not_on_list(list1,list2):
    '''A function that cheaks if any of one lists items are in the anther list '''
    for i in list1:
        if i in list2:
            return False
    else:
        return True

def find_most_commen_illnes(records, path):
    '''A function that gets a records and a path and returns the most commen illness acoordingly to the path
    and the records'''
    dict_for_path = {}
    most_recent_illness = None
    most_repitive = 0
    no_path = [i for i in path if path[i] == False]
    yes_path = [i for i in path if path[i] == True]
    for record in records:
        if not_on_list(record.symptoms,no_path):
            if set(yes_path) <= set(record.symptoms):
                if record.illness not in dict_for_path:
                    dict_for_path[record.illness] = 1
                else:
                    dict_for_path[record.illness] += 1
                if dict_for_path[record.illness] > most_repitive:
                    most_recent_illness = record.illness
                    most_repitive = dict_for_path[record.illness]
    if most_recent_illness == None:
        most_recent_illness = records[0].illness
    return most_recent_illness



def build_symptom_tree(symptoms,records,path,start=0):
    '''A function that builds a tree which every deaph of holds a symptoms and then recursivly
    holds the path which contains each symptoms that passed with true and false in a dictanry and than
    using the function "find_most_common_illness" to put the right leaf '''
    if start ==len(symptoms) :
        illnes_to_set=Node(find_most_commen_illnes(records,path))
        return illnes_to_set
    tree=Node(symptoms[start])
    path[symptoms[start]]=True
    tree.set_pos_childes(build_symptom_tree(symptoms,records,path,start+1))
    path[symptoms[start]]=False
    tree.set_neg_childes(build_symptom_tree(symptoms,records,path,start+1))
    return tree


def optimal_tree(records, symptoms, depth):
    '''a function that creates all the potintial trees for each combinations of symptoms in a given depth
    and return the one with the lowest error rate'''
    all_symptoms_combs=iter.combinations(symptoms,depth)
    lowest_error_rate=1
    best_tree=None
    for i in all_symptoms_combs:
        new_tree=build_tree(records,i)
        dia_tree=Diagnoser(new_tree)
        error_rate=dia_tree.calculate_error_rate(records)
        if error_rate<lowest_error_rate:
            best_tree=new_tree
            lowest_error_rate=error_rate
    return best_tree




