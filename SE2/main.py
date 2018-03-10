'''
Created on 10 Mar 2018

@author: user
'''
class Instruct(object):
    '''
    classdocs
    '''
    Code="";
    X1=0;
    Y1=0;
    X2=0;
    Y2=0;

    def __init__(self, code,x1,y1,x2,y2):
        '''
        Constructor
        '''
        self.Code=code;
        self.X1=x1;
        self.Y1=y1;
        self.X2=x2;
        self.Y2=y2;
        
class FileParser(object):
    '''
    classdocs
    '''
    FileName="";

    def __init__(self, filename):
        FileName=filename;
        pass; 
    
    def parse_file(self):
        instructions=[];
        instructions.append(Instruct("turn on",0,0,5,5));# the count should be 36
        instructions.append(Instruct("turn off",1,1,4,4));# the count should be 36-4=32
        instructions.append(Instruct("switch",1,0,2,0));# the count should be 32 - 2 = 30
        return instructions;
        
class Light_Tester(object):
    lights=None;
    GridSize=0;
    def __init__(self, n):
        self.GridSize=n;
        self.lights = [[False]*self.GridSize for _ in range(self.GridSize)]
        
    def apply(self, cmd):
        if cmd.Code=="turn on":
            for i in range(cmd.X1, cmd.X2+1):
                for j in range(cmd.Y1, cmd.Y2+1):
                    self.lights[i][j] = True
        elif cmd.Code=="turn off":
            for i in range(cmd.X1, cmd.X2+1):
                for j in range(cmd.Y1, cmd.Y2+1):
                    self.lights[i][j] = False
        elif cmd.Code=="switch":
            for i in range(cmd.X1, cmd.X2+1):
                for j in range(cmd.Y1, cmd.Y2+1):
                    self.lights[i][j] = not self.lights[i][j]
            
             
    def count(self):
        num=0;
        for i in range(self.GridSize):
            for j in range(self.GridSize):
                if self.lights[i][j] == True:
                    num=num+1;      
        return num;

 
def main(filename, N):
    
    theLights=Light_Tester(N);
 
    theParser= FileParser("");
    instructions = theParser.parse_file();
    
    for cmd in instructions:
        theLights.apply(cmd);
        print(theLights.count())
if __name__ == '__main__':
    main("The filename",6);