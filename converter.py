from nltk.parse.corenlp import CoreNLPParser
from nltk.stem import WordNetLemmatizer
from nltk.tree import *

import json
from six.moves import urllib
from words import *


#################################################################################################################


def englishToISLConverter(input_string):
    input_string = input_string.capitalize()

    isl_parsed_token_list = convert_eng_to_isl(input_string)
    print("\n\nISL Token list:")
    print(isl_parsed_token_list)

    lemmatized_isl_token_list = lemmatize_tokens(isl_parsed_token_list)
    print("\n\nLemmatized Token List:")
    print(lemmatized_isl_token_list)

    filtered_isl_token_list = filter_stop_words(lemmatized_isl_token_list)
    print("\n\nFiltered Stop Words:")
    print(filtered_isl_token_list)

    isl_text_string = ""
    for token in filtered_isl_token_list:
        isl_text_string += token
        isl_text_string += " "
    print("\n\nISL Sentence:")
    print(isl_text_string)
    isl_text_string = isl_text_string.lower()

    print("\n\nProcessed ISL Sentence:")
    print(pre_process(isl_text_string))

    data = {
        'isl_text_string': isl_text_string,
        'pre_process_string': pre_process(isl_text_string)
    }
    # delete this line
    return data


#################################################################################################################


def convert_eng_to_isl(input_string):

    if len(list(input_string.split(' '))) is 1:
        return list(input_string.split(' '))

    # Initializing stanford parser
    parser = CoreNLPParser()

    # Generates all possible parse trees sort by probability for the sentence
    possible_parse_tree_list = [tree for tree in parser.parse(input_string.split())]

    # Get most probable parse tree
    parse_tree = possible_parse_tree_list[0]
    # print(parse_tree)
    # output = '(ROOT
    #               (S
    #                   (PP (IN As) (NP (DT an) (NN accountant)))
    #                   (NP (PRP I))
    #                   (VP (VBP want) (S (VP (TO to) (VP (VB make) (NP (DT a) (NN payment))))))
    #                )
    #             )'

    # Convert into tree data structure
    parent_tree = ParentedTree.convert(parse_tree)    
    print("\n\nParse Tree:\n")
    print(parent_tree)   

    modified_parse_tree = modify_tree_structure(parent_tree)
    print("\n\nModified Parse Tree:\n")
    print(modified_parse_tree)

    isl_sentence = modified_parse_tree.leaves()
    return isl_sentence


#################################################################################################################


def modify_tree_structure(parent_tree):
    # Mark all subtrees position as 0
    tree_traversal_flag = label_parse_subtrees(parent_tree)
    # Initialize new parse tree
    modified_parse_tree = Tree('ROOT', [])
    i = 0
    for sub_tree in parent_tree.subtrees():
        if sub_tree.label() == "NP":
            i, modified_parse_tree = handle_noun_clause(i, tree_traversal_flag, modified_parse_tree, sub_tree)
        if sub_tree.label() == "VP" or sub_tree.label() == "PRP":
            i, modified_parse_tree = handle_verb_prop_clause(i, tree_traversal_flag, modified_parse_tree, sub_tree)

    # recursively check for omitted clauses to be inserted in tree
    for sub_tree in parent_tree.subtrees():
        for child_sub_tree in sub_tree.subtrees():
            if len(child_sub_tree.leaves()) == 1:  #check if subtree leads to some word
                if tree_traversal_flag[child_sub_tree.treeposition()] == 0 and tree_traversal_flag[child_sub_tree.parent().treeposition()] == 0:
                    tree_traversal_flag[child_sub_tree.treeposition()] = 1
                    modified_parse_tree.insert(i, child_sub_tree)
                    i = i + 1

    return modified_parse_tree


#################################################################################################################


def label_parse_subtrees(parent_tree):
    tree_traversal_flag = {}

    for sub_tree in parent_tree.subtrees():
        tree_traversal_flag[sub_tree.treeposition()] = 0
    return tree_traversal_flag


#################################################################################################################


def handle_noun_clause(i, tree_traversal_flag, modified_parse_tree, sub_tree):
    # if clause is Noun clause and not traversed then insert them in new tree first
    if tree_traversal_flag[sub_tree.treeposition()] == 0 and tree_traversal_flag[sub_tree.parent().treeposition()] == 0:
        tree_traversal_flag[sub_tree.treeposition()] = 1
        modified_parse_tree.insert(i, sub_tree)
        i = i + 1
    return i, modified_parse_tree


#################################################################################################################


def handle_verb_prop_clause(i, tree_traversal_flag, modified_parse_tree, sub_tree):
    # if clause is Verb clause or Proportion clause recursively check for Noun clause
    for child_sub_tree in sub_tree.subtrees():
        if child_sub_tree.label() == "NP" or child_sub_tree.label() == 'PRP':
            if tree_traversal_flag[child_sub_tree.treeposition()] == 0 and tree_traversal_flag[child_sub_tree.parent().treeposition()] == 0:
                tree_traversal_flag[child_sub_tree.treeposition()] = 1
                modified_parse_tree.insert(i, child_sub_tree)
                i = i + 1
    return i, modified_parse_tree


#################################################################################################################


def lemmatize_tokens(token_list):
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []
    for token in token_list:
        lemmatized_words.append(lemmatizer.lemmatize(token))

    return lemmatized_words


#################################################################################################################


def filter_stop_words(words):
    stopwords_set = set(['a', 'an', 'the', 'is'])
    words = list(filter(lambda x: x not in stopwords_set, words))
    return words


#################################################################################################################


def pre_process(sentence):
    words = list(sentence.split())
    final_string = ""

    for word in words:
        if word not in eligible_words:
            for letter in word:
                final_string += " " + letter
        else:
            final_string += " " + word

    return final_string

