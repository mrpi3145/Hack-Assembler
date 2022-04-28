

class HashMap:

    def __init__(self) -> None:
        self.size=70
        self.map=map=[[] for sub in range(self.size)]

        pass


    def get(self,key):
        index=hash(key)%self.size

        for entry in self.map[index]:
            if key in entry:
                return entry[key]
        
        return -1
            
        
    def remove(self,key):
        index=hash(key)%self.size
        pop_i=0

        for entry in self.map[index]:
            if key in entry:
                self.map[index].pop(pop_i)
            pop_i=pop_i+1

                
            
    def put(self,key,value):
        index=hash(key)%self.size

        for entry in self.map[index]:
            if key in entry:
                entry[key]=value
                return
        self.map[index].append({key:value})
            
        

    def has(self,key):
        index=hash(key)%self.size

        for entry in self.map[index]:
            if key in entry:
                return True
        
        return False


