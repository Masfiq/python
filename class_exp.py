class DataType:
    mullo = 100
    def __init__(self,name,num):
        self.name = name
        self.value = num 
        



data_type1 = DataType("Integer", 1234)
print(data_type1.name)
print(data_type1.value)
print('=====================')
print(DataType.mullo)
# data_type2 = DataType(‘String’, ‘Hello’)
# print(data_type2.name)
# print(data_type2.value)
# print('=====================')
# data_type3 = DataType(‘Float’, 4.0)
# print(data_type3.name)
# print(data_type3.value)