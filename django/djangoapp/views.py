from django.shortcuts import render,redirect
from rest_framework.views import APIView, Response
from rest_framework import viewsets, status

from djangoapp import forms, models, serializers
# Create your views here.

def index(req):
	return render(req, 'index.html')


def stud(req):
	form = forms.StudForm
	if req.method == 'POST':
		form = forms.StudForm(req.POST)
		if form.is_valid():
			form.save()
			return redirect('stud')
	context = {
		'form': form
	}
	return render(req, 'stud.html', context)


class StudApi(APIView):
	serializer_class = serializers.StudSerializer
	def get(self, request,  format = None):
		obj = models.StudModel.objects.all()
		serializer = serializers.StudSerializer(obj, many=True)
		return Response(serializer.data)
	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			message = f'Create Successfull'
			return Response({'message':message})
		else:
			return Response(
				serializer.errors,
				status = status.HTTP_400_BAD_REQUEST
				)	