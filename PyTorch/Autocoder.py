#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 18:30:28 2017

@author: xu
"""
#it's a simple AutoEncoder
class autoencoder(nn.Module):
    def__init__(self):
        super(autoencoder,self).__init__()
        self.encoder = nn.Sequential(
                nn.Linear(28*28,128),
                nn.ReLU(True),
                nn.Linear(128,64),
                nn.ReLU(True),
                nn.Linear(64,12),
                nn.ReLU(True),
                nn.Linear(12,3)
                )
        self.decoder = nn.Sequential(
                nn.Linear(3,12),
                nn.ReLU(True),
                nn.Linear(12,64),
                nn.ReLU(True),
                nn.Linear(64,128),
                nn.ReLU(True),
                nn.Linear(128,28*28),
                nn.Tanh()
                )
    def forward(self,x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x