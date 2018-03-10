class Light_Tester(object):
    lights=None;
    def __init__(self, n):
        self.lights = [[False]*n for _ in range(n)]
        
    def apply(self, cmd):
        pass
    def count(self):
        return 0;
    
     
# class FileParser(object):
#     '''
#     classdocs
#     '''
# 
# 
#     def __init__(self, filename):
#         pass; 
#     
#     def parse_file(self):
#         instructions=[];
#         instructions.Add(Instruct("turn on",0,0,5,5))
#         instructions.Add(Instruct("turn off",1,1,4,4))
#         instructions.Add(Instruct("Switch",1,0,2,0))
#         return instructions;
#         '''
#         Constructor
#         '''
# class Instruct(object):
#     '''
#     classdocs
#     '''
#     Code="";
#     X1=0;
#     Y1=0;
#     X2=0;
#     Y2=0;
# 
#     def __init__(self, code,x1,y1,x2,y2):
#         '''
#         Constructor
#         '''
#         self.Code=code;
#         self.X1=x1;
#         self.Y1=y1;
#         self.X2=x2;
#         self.Y2=y2;
