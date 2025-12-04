from rest_framework.generics import ListAPIView

from .views import (UserProfileViewSet, CountryListAPIView,
                    CountryDetailAPIView, DirectorListAPIView, DirectorDetailSerializer,
                    ActorListAPIView,ActorDetailAPiView, GenreListAPIView,GenreDetailAPIView, MovieListAPIView, MovieDetailAPIView,
                    MovieLanguagesViewSet,
                    MomentViewSet, RatingViewSet, FavoriteViewSet, FavoriteMovieViewSet, HistoryViewSet,
                    DirectorDetailAPIView,RegisterView,LoginView,LogoutView)
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'users/',UserProfileViewSet)
router.register(r'movie_languages/',MovieLanguagesViewSet)
router.register(r'moment/',MomentViewSet)
router.register(r'rating/',RatingViewSet)
router.register(r'favorite/',FavoriteViewSet)
router.register(r'favorite_movie/',FavoriteMovieViewSet)
router.register(r'history/',HistoryViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('movie/',MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/',MovieDetailAPIView.as_view(), name='movie_detail'),
    path('country/',CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/',CountryDetailAPIView.as_view(), name='country_detail'),
    path('director/',DirectorListAPIView.as_view(), name='director_list'),
    path('director/<int:pk>',DirectorDetailAPIView.as_view(), name='director_detail'),
    path('genre/',GenreListAPIView.as_view(), name='genre_list'),
    path('genre/<int:pk>/',GenreDetailAPIView.as_view(),name='genre_detail'),
    path('actor/',ActorListAPIView.as_view(), name='actor_list'),
    path('actor/<int:pk>/',ActorDetailAPiView.as_view(), name='actor_detail'),
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout')

]
