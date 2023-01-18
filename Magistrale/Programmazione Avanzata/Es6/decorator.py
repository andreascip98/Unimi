def memoization(func): 
    def wrapper(*args):
        if args in wrapper.mem:
            print('result fetched from cache: ',wrapper.mem[args])
            return wrapper.mem[args]
        else:
            val = func(*args)
            wrapper.mem[args] = val
            print('new result, now caching: ',(args[1:],val))
            return val
    wrapper.mem = dict()    
    return wrapper


def logging(func): 
    def wrapper(*args):
        print('### called: {}{}'.format(func.__name__,args[1:]))
        return func(*args)
    return wrapper
   
def stack_trace(func):
    stack_trace.stk = []
    def wrapper(*args):
        stack_trace.stk = [(func.__name__, args[1])]+ stack_trace.stk
        print([s for s in stack_trace.stk], sep ="\n")
        res = func(*args)
        stack_trace.stk = stack_trace.stk[1:]
        return res
    return wrapper

class MyMath:

    @memoization
    def fib(self,n): return n if n<=1 else self.fib(n-1) + self.fib(n-2)

    @logging
    def fact(self,n): return n if n<2 else self.fact(n-1) * n

    @stack_trace
    def taylor(self,f,n): return 1 if n<1 else f**n/self.fact(n) + self.taylor(f,n-1)


if __name__ == "__main__":

    m = MyMath()
    print(m.fib(15),m.fib(20),m.fib(15))
    print(m.fact(5))
    print(m.taylor(5,5))
