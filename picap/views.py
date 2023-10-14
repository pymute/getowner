from rest_framework import generics
from .models import Car, Owner
from .serializers import CarSerializer

class CarDestroyView(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
class CarList(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

class CarListCreate(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarListByOwner(generics.ListAPIView):
    serializer_class = CarSerializer
    def get_queryset(self):
        owner_id = self.kwargs['owner_id']
        return Car.objects.filter(owner__id=owner_id)









# def post(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         postseria = Posts(posts,many=True)
#         return JsonResponse(postseria, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser.parse(request)
#         dateseria = Posts(data=data)
#         if dateseria.is_valid:
#             return JsonResponse(dateseria.data,status=201)
        
#     return JsonResponse({},status=400)