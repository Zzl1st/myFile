#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 19:32:52 2017

@author: xu
"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import tensorflow as tf

v1 = tf.Variable(tf.constant(1.0,shape=[1],name='v1'))
v2 = tf.Variable(tf.constant(2.0,shape=[1],name='v2'))
result = v1 + v2

init_op = tf.global_variables_initializer()

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init_op)
    saver.save(sess,"/home/xu/桌面/xu/5.4.1/ModelText.ckpt")