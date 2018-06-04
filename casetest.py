import os
import subprocess

class CaseTest():
    def __init__(self):
        path = os.getcwd() 
        path2 =  ['/inputs/','/outputs/']
        self.cases = {}
        print( path+path2[0] , len(path+path2[0]) )
        for i in range( len(os.listdir(path+path2[0])) ):
            self.cases[i] = {}
            file = open( path + path2[0] + str(i) + '.in' )
            self.cases[i]['size'] = int(file.readline())
            self.cases[i]['matrix'] = []
            for j in range( self.cases[i]['size'] ):
                self.cases[i]['matrix'].append( list( map(int,file.readline().split() ) ) )
            
            file.close()
            file = open( path + path2[1] + str(i) + '.out' )
            self.cases[i]['answer'] = int(file.readline())

    def run( self, code ):
        path = os.getcwd() 
        path2 =  ['/inputs/','/outputs/']
        total = 0
        for case in self.cases:
            call = "python " + code + " < " + path + path2[0] + str(case) + ".in"
            print(call)
            output = subprocess.check_output([call])
            print(output)
            file = open( path + path2[0] + str(case) + ".out" )
            answer = int(file.readline())
            sumDist = 0
            output = list( map(int,output.split() ) )
            for i in range( len(output)-1 ):
                sumDist += self.cases[case]['matrix'][ output[i] ][ output[i+1] ]
            if self.cases[case]['answer'] <= sumDist <= 2*self.cases[case]['answer']:
                total += 1

        return total

