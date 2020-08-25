class RecursionDemo:

    def countDown(self,num):
        print(num)
        if(num == 0): return
        self.countDown(num-1)

    def countUp(self, num, i = 0):
        print(i)
        i+= 1
        if(num == i): return
        self.countUp(num,i)

    def tri_recursion(self,k):
        if(k>0):
            result = k+tri_recursion(k-1)
            print(result)
        else:
            result = 0
            return result
