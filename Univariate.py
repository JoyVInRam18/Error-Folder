#class Univariate(object):
#    def __init__(self):
#        pass
class Univariate:
    @staticmethod
    def QuanQual(dataset):
        # your logic here
        return quan, qual


def QuanQual(dataset):
    quan=[]
    qual=[]
    for columnName in dataset.columns:
        print(columnName)
        if(dataset[columnName].dtype=='O'):
           print("qual")
           qual.append(columnName)
        else:
           print("quan")
           quan.append(columnName)
        return quan,qual