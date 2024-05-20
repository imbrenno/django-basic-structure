import json
from rest_framework import viewsets
from rest_framework.response import Response
from main.database.models.person_model import Person
from main.services.serializers.person_serializer import PersonSerializer


class PersonCtrl(viewsets.ViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def list(self, request):
        serializer = self.serializer_class(
            self.queryset,
            many=True,
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        person = self.queryset.filter(pk=pk).first()
        if person:
            serializer = self.serializer_class(person)
            return Response(serializer.data)
        return Response({"message": "Person not found"}, status=404)

    def create(self, request):
        data = json.dumps(request.data)
        print(f" data, request: {data}")
        serializer = self.serializer_class(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        person = self.queryset.filter(pk=pk).first()
        if person:
            serializer = self.serializer_class(person, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        return Response({"message": "Person not found"}, status=404)

    def destroy(self, request, pk=None):
        person = self.queryset.filter(pk=pk).first()
        if person:
            person.delete()
            return Response({"message": "Person deleted"}, status=204)
        return Response({"message": "Person not found"}, status=404)
