# CS114 Spring 2018 Homework 4
# Part-of-speech Tagging with Hidden Markov Models

import os
from collections import defaultdict

class POSTagger():

    def __init__(self):
        # you can choose which data structures you want to use
        self.transition = None
        self.emission = None

    '''
    Trains a supervised hidden Markov model on a training set.
    Transition probabilities P(s|p)
    Emission probabilities P(w|s)
    '''
    def train(self, train_set):
        # iterate over training documents
        for root, dirs, files in os.walk(train_set):
            for name in files:
                with open(os.path.join(root, name)) as f:
                    # be sure to split documents into sentences here
                    pass

    '''
    Implements the Viterbi algorithm.
    Use v and backpointer to find the best_path.
    '''
    def viterbi(self, sentence):
        # you can choose which data structures you want to use
        v = None
        backpointer = None
        # initialization step
        # recursion step
        # termination steps
        best_path = []
        return best_path

    '''
    Tests the tagger on a development or test set.
    Returns a dictionary of sentence_ids mapped to their correct and predicted
    sequences of POS tags such that:
    results[sentence_id]['correct'] = correct sequence of POS tags
    results[sentence_id]['predicted'] = predicted sequence of POS tags
    '''
    def test(self, dev_set):
        results = defaultdict(dict)
        # iterate over testing documents
        for root, dirs, files in os.walk(dev_set):
            for name in files:
                with open(os.path.join(root, name)) as f:
                    pass
        return results

    '''
    Given results, calculates overall accuracy
    '''
    def evaluate(self, results):
        accuracy = 0.0
        return accuracy

if __name__ == '__main__':
    pos = POSTagger()
    # make sure these point to the right directories
    pos.train('brown/train')
    results = pos.test('brown/dev')
    print(pos.evaluate(results))
