#! /usr/bin/env python

# author   : Mattis List
# email    : mattis.list@lingpy.org
# created  : 2015-01-20 15:26
# modified : 2015-01-20 15:50

"""! @package utils.ipa2sampa
"""

from __future__ import print_function,unicode_literals
import unicodedata
import codecs, os

# load sampa and ipa csv file
try:
    data = codecs.open('./pylmflib/utils/ipa2sampa/sampa.csv', 'r', 'utf-8')
except:
    data = codecs.open(os.path.split(os.path.abspath(__file__))[0] + '/sampa.csv', 'r', 'utf-8')

# load source and target items
sota = []

for line in data:
    if not line.strip() or line.startswith('#'):
        pass
    else:
        so,ta = unicodedata.normalize("NFD",line.strip()).split('\t')
        try:
            ta = eval('"""'+ta+'"""')
        except:
            pass
        sota += [(so,ta)]
sota = dict([(b,a) for a,b in sota])

def uni2sampa(sequence):
    """
    Convert sequence in unicode-ipa to ascii-sampa.
    
    Notes
    -----
    Forked from LingPy's version for ipa2sampa, which is based on code
    taken from Peter Kleiweg
    (http://www.let.rug.nl/~kleiweg/L04/devel/python/xsampa.html).
    """
    result = ''
    if type(sequence) == str:
        sequence = unicode(sequence, 'utf-8')

    seq = [k for k in unicodedata.normalize('NFD', sequence)]

    while seq:
        seg = seq.pop(0)
        try:
            out = sota[seg]
        except KeyError:
            out = seg
        result += out
    return result

if __name__ == '__main__':

    with codecs.open('./pylmflib/utils/ipa2sampa/tokens.test','r','utf-8') as f:
        for line in f:
            seq = line.strip()
            print(seq,'\t',uni2sampa(seq))
