import timeit

def timer(number, repeat):
  def wrapper(func):
    runs = timer.repeat(func, number=number, repeat=repeat)
    print(sum(runs) / len(runs))
    
  return wrapper
