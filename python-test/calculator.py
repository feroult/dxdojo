class Calculator(object):
 
    def add(self, x, y):
        return x+y

    def subtract(self, x, y):
        return x-y

    def list(self,size):
    	arr = [];
    	for counter in range(1, size):
    		arr.append('tst'+str(counter))
        return arr

    def map(self):
    	arr = {};
    	arr['tst1'] = 1
    	arr['tst2'] = 2
        return arr