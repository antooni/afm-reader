import sys
sys.path.append('../src')

for p in sys.path:
    print(p)

import decoder


def testA():
    assert decoder.add(1,1) == 2
