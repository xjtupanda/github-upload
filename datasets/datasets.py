import os
import torch

datasets = {}

def register_dataset(name):
    def decorator(cls):
        datasets[name] = cls
        return cls
    return decorator

def make_dataset(name):
    '''
        A simple dataset builder
    '''
    dataset = datasets[name]()
    return dataset
