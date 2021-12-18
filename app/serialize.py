from rest_framework import serializers



class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=20)
    email=serializers.EmailField(max_length=30)
    designation=serializers.CharField(max_length=50)



    # def to_representation(self, value):
          
          
    #       data=super().to_representation(value)
    #       lis=[]
         
       
          
    #       lis.append(list(data.values()))
          
          
          
    #       #getting values and converting dict(consisting values) to list of lists
    #       return lis