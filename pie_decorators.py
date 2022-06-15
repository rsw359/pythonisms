from functools import wraps
from time import sleep

def has_cream(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    type_of_sweets = func(*args, **kwargs)

    creamed = type_of_sweets.upper() + "has butter cream"

    return creamed

def wait_for_cream(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    sleep(3)
    return func(*args, **kwargs)
  return wrapper


@has_cream
def say(txt):
    return txt

if __name__ == "__main__":
  print(say("French Vanilla Cake"))