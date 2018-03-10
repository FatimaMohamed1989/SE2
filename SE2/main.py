'''
Created on 10 Mar 2018

@author: user
'''
import urllib3
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
    N=0;


    def __init__(self, filename):
        self.FileName=filename;
        pass; 
    
    def parse_file(self):
        instructions=[];
        http = urllib3.PoolManager()
        response = http.request('GET', self.FileName)
        theData = response.data.decode('utf-8');
        thelist = theData.split('\n');
        numOfLines=0;
        for line in thelist:
            if numOfLines == 0:
                self.N = int(line.strip());
            else:
                if line[:7]=="turn on":
                    instructions.append(self.parse_line(line[7:],"turn on"));
                elif line[:8]=="turn off":
                    instructions.append(self.parse_line(line[8:],"turn off"));
                elif line[:6]=="switch":
                    instructions.append(self.parse_line(line[6:],"switch"));
                else:
                    pass;
            numOfLines=numOfLines+1;
        return instructions;
    def parse_line(self, line,code):
        n = line.find("through");
        theInstruct=Instruct("",0,0,0,0);
        theInstruct.Code=code;
        start="";
        finish = "";
        if (n != -1):
            start = line[:n];
            finish = line[n+7:];
            startArray =start.strip().split(",");
            finishArray =finish.strip().split(",");
            theInstruct.X1=startArray[0].strip();
            theInstruct.Y1=startArray[1].strip();
            theInstruct.X2=finishArray[0].strip();
            theInstruct.Y2=finishArray[1].strip();
        #print(theInstruct.Code + " " +  theInstruct.X1 + "/" +  theInstruct.Y1 + " ooooo "  + " " +  theInstruct.X2 + "/" + theInstruct.Y2);
        return theInstruct;
        
class Light_Tester(object):
    lights=None;
    def __init__(self, n):
        self.GridSize=n;
        self.lights = [[False]*self.GridSize for _ in range(self.GridSize)]
        
    def apply(self, cmd):
        if cmd.Code=="turn on":
            for i in range(int(cmd.X1), int(cmd.X2)+1):
                for j in range(int(cmd.Y1), int(cmd.Y2)+1):
                    self.lights[i][j] = True
        elif cmd.Code=="turn off":
            for i in range(int(cmd.X1), int(cmd.X2)+1):
                for j in range(int(cmd.Y1), int(cmd.Y2)+1):
                    self.lights[i][j] = False
        elif cmd.Code=="switch":
            #print(cmd.X1 + " " + cmd.X2 + " " + cmd.Y1 + " " + cmd.Y2)
            for i in range(int(cmd.X1), int(cmd.X2)+1):
                for j in range(int(cmd.Y1), int(cmd.Y2)+1):
                    self.lights[i][j] = not self.lights[i][j]
            
             
    def count(self):
        num=0;
        for i in range(self.GridSize):
            for j in range(self.GridSize):
                if self.lights[i][j] == True:
                    num=num+1;      
        return num;

 
def main(filename):
    theParser= FileParser(filename);
    
    instructions = theParser.parse_file();

    theLights=Light_Tester(theParser.N);
 
    for cmd in instructions:
        theLights.apply(cmd);
    print(theLights.count())
if __name__ == '__main__':
    main();