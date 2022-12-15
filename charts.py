#!/usr/bin/env python

import matplotlib.pyplot as plt

First_test     = [37, 15]
Second_test    = [24, 9]
First_control  = [36, 0]
Second_control = [28, 4]

categories = ['Dark', 'Fluorescent']
explodes = [0, 0.05]

plt.figure(figsize=(6,6))
patches, texts, pcts = plt.pie(First_test, labels=categories, explode = explodes, startangle=90, autopct='%1.1f%%',
        textprops={'size': 'x-large'})
plt.setp(pcts, color='white', fontweight='bold')
plt.title('First Test', fontsize=30)
#plt.legend(fontsize='xx-large')
plt.savefig('First_Test')
plt.close()

plt.figure(figsize=(6,6))
patches, texts, pcts = plt.pie(Second_test, labels=categories, explode = explodes, startangle=90, autopct='%1.1f%%',
        textprops={'size': 'x-large'})
plt.setp(pcts, color='white', fontweight='bold')
plt.title('Second Test', fontsize=30)
#plt.legend(fontsize='xx-large')
plt.savefig('Second_Test')
plt.close()

plt.figure(figsize=(6,6))
patches, texts, pcts = plt.pie(First_control, labels=categories, explode = explodes, startangle=90, autopct='%1.1f%%',
        textprops={'size': 'x-large'})
plt.setp(pcts, color='white', fontweight='bold')
plt.title('First control', fontsize=30)
#plt.legend(fontsize='xx-large')
plt.savefig('First_control')
plt.close()

plt.figure(figsize=(6,6))
patches, texts, pcts = plt.pie(Second_control, labels=categories, explode = explodes, startangle=90, autopct='%1.1f%%',
        textprops={'size': 'x-large'})
plt.setp(pcts, color='white', fontweight='bold')
plt.title('Second control', fontsize=30)
#plt.legend(fontsize='xx-large')
plt.savefig('Second_control')
plt.close()