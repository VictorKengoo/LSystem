import re 

class Gramatica(object):

     def alfabeto(self,arrayString):
        for string in arrayString:
            i = string.find('£ :')
            if i != -1:
                alphabetString = string.replace('£ :','').strip()
                alphabetArray =  alphabetString.split(',')
                alphabetArray = list(map(str.strip, alphabetArray))
                alphabetArray.remove('+')
                alphabetArray.remove('-')
                return alphabetArray

        return None

     def passos(self,arrayString):
        for string in arrayString:
            i = string.find('n :')
            if i != -1:
                return string.replace('n :','').strip()
            
        return None

     def axioma(self,arrayString):
        for string in arrayString:
            i = string.find('@ :')
            if i != -1:
                return string.replace('@ :','').strip()
            
        return None

     def angulo(self,arrayString):
        for string in arrayString:
            i = string.find('§ :')
            if i != -1:
                return string.replace('§ :','').strip().replace('º','')
            
        return None

     def regra(self,arrayString):
          reg = []
          for string in arrayString:
               if(re.match('(p\d* :)',string)):
                   stringfix = string.replace('\n','').replace('→','->')
                   rules.append(re.sub('(p\d* :)','',stringfix))

          return reg

     def __init__(self, ArrayStringsOfTxt):
         self.alfabet = self.findAlphabet(ArrayStringsOfTxt)
         self.steps = self.findSteps(ArrayStringsOfTxt)
         self.axiom = self.findAxion(ArrayStringsOfTxt)
         self.angle = self.findAngle(ArrayStringsOfTxt)
         self.rules = self.findRules(ArrayStringsOfTxt)


