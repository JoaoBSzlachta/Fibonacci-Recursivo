import time


class Fibonacci:

  def __init__(self):
    self.first = 0
    self.second = 1

  def Func(self, value):
    if (value == 1):
      return self.first
    elif (value == 2):
      return self.second
    else:
      return self.Func(value - 1) + self.Func(value - 2)


start = time.time()
fib = Fibonacci()
print(fib.Func(30))
end = time.time()
print(f"{end - start}")
