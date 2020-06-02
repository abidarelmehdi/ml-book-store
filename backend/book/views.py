from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count, Avg, OuterRef, Subquery
from django.views.generic import View
from django.db.models.functions import Coalesce, Floor
from core.ai_models.cosine_similarity import CosineSimilarityModel
from core.ai_models.user_preferences import UserPreferencesModel
from book.models import Book


@transaction.atomic
def load_data(request):
    return HttpResponse("Good")


class CosineSimilarityContentBasedModel(View):
    """
        Simple view to trigger training of content-based model
    """

    def get(self, request):
        CosineSimilarityModel(train=True)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


class UserPreferencesContentBasedModel(View):
    """
        Simple view to train user preference content based model
    """

    def get(self, request):
        UserPreferencesModel(train=True)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


class RefreshBooks(View):
    """
        Simple view to refresh book stats (raters, average ratings) 
    """

    def get(self, request):
        Book.objects.update(
            raters=Coalesce(
                Subquery(
                    Book.objects.filter(id=OuterRef("id"))
                    .annotate(c=Count("user_ratings__id"))
                    .values("c")[:1]
                ),
                0,
            ),
            avg_ratings=Coalesce(
                Subquery(
                    Book.objects.filter(id=OuterRef("id"))
                    .annotate(avg=Floor(Avg("user_ratings__rate")))
                    .values("avg")[:1]
                ),
                0,
            ),
        )
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
