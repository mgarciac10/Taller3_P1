from dotenv import load_dotenv, find_dotenv
import json
import os
from openai import OpenAI
import numpy as np
from movie.models import Movie

class OpenAIManager:
    load_dotenv(find_dotenv('api_keys.env'))
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('openai_api_key'))
    
    def get_embedding(self, text, model="text-embedding-3-small"):
        text = text.replace("\n", " ")
        return self.client.embeddings.create(input = [text], model=model).data[0].embedding
    
    def cosine_similarity(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    def get_recommendation(self, req):
        emb = self.get_embedding(req)
        sim = []
        movies = Movie.objects.all()
        for movie in movies:
            movie_emb = list(np.frombuffer(movie.emb))
            sim.append(self.cosine_similarity(emb,movie_emb))
        sim = np.array(sim)
        idx = np.argmax(sim)
        idx = int(idx)
        return movies[idx]