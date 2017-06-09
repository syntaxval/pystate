#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
StateMachine.

"""

from random import random

__all__ = [

]

__author__ = "syntaxval"
__copyright__ = "copyright (c) 2017, syntaxval"
__version__ = "0.0.1"
__license__ = "BSD 2-Clause license"

transitions = {
    'A' : {
        'push_left' : 'A',
        'push_right' : 'B',
        'push_up': 'A',
        'push_down' : 'D'
    },
    'B' : {
        'push_left' : 'A',
        'push_right' : 'C',
        'push_up' : 'B',
        'push_down' : 'E'
    },
    'C' : {
        'push_left' : 'B',
        'push_right' : 'C',
        'push_up' : 'C',
        'push_down' : 'F'
    },
    'D' : {
        'push_left' : 'D',
        'push_right' : 'E',
        'push_up' : 'A',
        'push_down' : 'G'
    },
    'E' : {
        'push_left' : 'D',
        'push_right' : 'F',
        'push_up' : 'B',
        'push_down' : 'H'
    },
    'F' : {
        'push_left' : 'E',
        'push_right' : 'F',
        'push_up' : 'C',
        'push_down' : 'I'
    },
    'G' : {
        'push_left' : 'G',
        'push_right' : 'H',
        'push_up' : 'D',
        'push_down' : 'G'
    },
    'H' : {
        'push_left' : 'G',
        'push_right' : 'I',
        'push_up' : 'E',
        'push_down' : 'H'
    },
    'I' : {
        'push_left' : 'H',
        'push_right' : 'I',
        'push_up' : 'F',
        'push_down' : 'I'
    }
}

def move_left():
    print("moving left...")

def move_right():
    print("moving right...")

def move_up():
    print("moving up...")

def move_down():
    print("moving down...")

actions = {
    'push_left': move_left,
    'push_right': move_right,
    'push_up': move_up,
    'push_down': move_down
}

def do_action(state):
    return actions[state]()

def transition (state, event):
    return transitions[state][event]

def get_events():
    return sorted(actions.keys(), key=lambda _: random())


# ...
if __name__ == "__main__":

    """ Example run. """

    initial_state = 'E'
    current_state = initial_state
    events = get_events()

    print("Starting at: " + current_state)

    for event in events:
        current_state = transition(current_state, event)
        do_action(event)
        print("Now at: " + current_state)

    print("Finished.")
