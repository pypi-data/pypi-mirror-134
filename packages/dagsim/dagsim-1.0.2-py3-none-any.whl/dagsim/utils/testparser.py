from dagsim.utils.parser import Parser

testValue = 2
parser = Parser(file_name="testyml.yml")
data = parser.parse(draw=False)
print(data)
