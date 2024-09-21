from django.shortcuts import render
from movie.models import Movie

# Create your views here.
def recommendation(request):
    recommendationRequest = request.GET.get('recommendation')
    if recommendationRequest:
        
        pass
    else:
        movies = Movie.objects.all()
    return render(request, 'recommendation.html', {'recommendationRequest':recommendationRequest, 'movies':movies})