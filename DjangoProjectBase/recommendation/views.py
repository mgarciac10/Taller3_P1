from django.shortcuts import render
from movie.models import Movie
from moviereviews.openAIManager import OpenAIManager

# Create your views here.
def recommendation(request):
    recommendationRequest = request.GET.get('recommendation')
    if recommendationRequest:
        openAIManager = OpenAIManager()
        movie = openAIManager.get_recommendation(recommendationRequest)
        movies = [movie]
    else:
        movies = Movie.objects.all()
    return render(request, 'recommendation.html', {'recommendationRequest':recommendationRequest, 'movies':movies})