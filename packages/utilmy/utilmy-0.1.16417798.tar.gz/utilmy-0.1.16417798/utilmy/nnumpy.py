# -*- coding: utf-8 -*-
HELP= """



"""
import os, sys, time, datetime,inspect, json, yaml, gc

from collections import OrderedDict

###################################################################################################
verbose = 0

def log(*s):
    print(*s, flush=True)

def log2(*s):
    if verbose >1 : print(*s, flush=True)

def help():
    from utilmy import help_create
    ss  = help_create("utilmy.nnumpy", prefixs= [ 'test'])  #### Merge test code
    ss += HELP
    print(ss)



###################################################################################################
def test_all():
    """#### python test.py   test_nnumpy
    """
    def test():
        log("Testing nnumpy ...")
        from utilmy.nnumpy import to_dict,to_timeunix,to_datetime,np_list_intersection,np_add_remove
        to_dict(kw=[1,2,3])
        to_timeunix(datex="2020-10-06")
        to_datetime("10/05/2021")
        l1 = [1,2,3]
        l2 = [3,4,1]
        result = np_list_intersection(l1,l2)
        set_ = {1,2,3,4,5}
        result = np_add_remove(set_,[1,2],6)
        log("np_add_remove",result)
    test()
    
    
def test0():
    log("Testing nnumpy ...")
    to_dict(kw=[1,2,3])
    to_timeunix(datex="2020-10-06")
    to_datetime("10/05/2021")


def test1():
    l1 = [1,2,3]
    l2 = [3,4,1]
    result = np_list_intersection(l1,l2)
    set_ = {1,2,3,4,5}
    result = np_add_remove(set_,[1,2],6)
    log("np_add_remove",result)




##############################################################################################################
####### Numpy, Dict, List compute related  ###################################################################
from collections import OrderedDict


class LRUCache(object):
    def __init__(self, max_size=4):
        if max_size <= 0:
            raise ValueError

        self.max_size = max_size
        self._items = OrderedDict()

    def _move_latest(self, key):
        # Order is in descending priority, i.e. first element
        # is latest.
        self._items.move_to_end(key, last=False)

    def __getitem__(self, key, default=None):
        if key not in self._items:
            return default

        value = self._items[key]
        self._move_latest(key)
        return value

    def __setitem__(self, key, value):
        if len(self._items) >= self.max_size:
            keys = list(self._items.keys())
            key_to_evict = keys[-1]
            self._items.pop(key_to_evict)

        self._items[key] = value
        self._move_latest(key)
        
        
        
class fixedDict(OrderedDict):
    """  fixed size dict
          ddict = fixedDict(limit=10**6)

    """
    def __init__(self, *args, **kwds):
        self.size_limit = kwds.pop("limit", None)
        Dict.__init__(self, *args, **kwds)
        self._check_size_limit()

    def __setitem__(self, key, value):
        OrderedDict.__setitem__(self, key, value)
        self._check_size_limit()

    def _check_size_limit(self):
        if self.size_limit is not None:
            while len(self) > self.size_limit:
                self.popitem(last=False)


class dict_to_namespace(object):
    #### Dict to namespace
    def __init__(self, d):
        self.__dict__ = d


def to_dict(**kw):
  ## return dict version of the params
  return kw


def to_timeunix(datex="2018-01-16"):
  if isinstance(datex, str)  :
     return int(time.mktime(datetime.datetime.strptime(datex, "%Y-%m-%d").timetuple()) * 1000)

  if isinstance(datex, datetime.date)  :
     return int(time.mktime( datex.timetuple()) * 1000)


def to_datetime(x) :
  import pandas as pd
  return pd.to_datetime( str(x) )


def np_list_intersection(l1, l2) :
  return [x for x in l1 if x in l2]


def np_add_remove(set_, to_remove, to_add):
    # a function that removes list of elements and adds an element from a set
    result_temp = set_.copy()
    for element in to_remove:
        result_temp.remove(element)
    result_temp.add(to_add)
    return result_temp


def to_float(x, valdef=-1):
    try :
        return float(x)
    except :
        return valdef

def to_int(x, valdef=-1):
    try :
        return int(x)
    except :
        return -1


def is_int(x):
    try :
        int(x)
        return True
    except:
        return False


def is_float(x):
    try :
        float(x)
        return True
    except:
        return False





###################################################################################################
if __name__ == "__main__":
    import fire
    fire.Fire()




