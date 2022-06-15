import pytest
from tastypie import LinkedList

def test_create():
  pies = LinkedList(("blueberry", "marionberry", "peach"))

  all_pies = []

  for pie in pies:
    all_pies.append(pie)


  assert all_pies == ["blueberry", "marionberry", "peach"]

def test_dunder_iter():
  pies = LinkedList(["blueberry", "marionberry","peach"])
  
  dunditer = iter(pies)

  assert next(dunditer) == "blueberry"
  assert next(dunditer) == "marionberry"
  assert next(dunditer) == "peach"

def test_stop_iter():
  pies = LinkedList(["blueberry", "marionberry","peach"])
  
  dunditer = iter(pies)
  with pytest.raises(StopIteration):
        while True:
            pies = next(dunditer)
 




def test_dunder_eq():

  every_pie = ["blueberry", "marionberry", "peach"]
  pies = LinkedList(every_pie)

  assert list(pies) == every_pie

def test_pie_len():
  pie_range = range(1, 3+1)

  pies = LinkedList(pie_range)

  assert len(pies) == 3


