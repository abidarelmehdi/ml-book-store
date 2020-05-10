from django.db import transaction
from django.http import HttpResponse

from core.ai_models.content_based import CosineSimilarityModel


@transaction.atomic
def load_data(request):
    model = CosineSimilarityModel(train=True)
    return HttpResponse("Good")


# def add_book(df):
#     print(f"start adding...")
#     for idx in df.index:
#         book_data = {
#             "title": str(df["title"][idx]).strip()
#             if df["title"][idx]
#             else None,
#             "subtitle": str(df["subtitle"][idx]).strip()
#             if df["subtitle"][idx]
#             else None,
#             "language": str(df["language"][idx]).strip()
#             if df["language"][idx]
#             else None,
#             "thumbnail": str(df["thumbnail"][idx]).strip()
#             if df["thumbnail"][idx]
#             else None,
#             "description": str(df["description"][idx]).strip()
#             if df["description"][idx]
#             else None,
#             "isbn": str(df["isbn"][idx]).strip() if df["isbn"][idx] else None,
#             "publisher": str(df["publisher"][idx]).strip()
#             if df["publisher"][idx]
#             else None,
#             "pages": df["pages"][idx],
#         }
#         if book_data.get("title"):
#             book = Book.objects.create(**book_data)
#             authors_names = re.split(
#                 ";|\||/ ", str(df["authors"][idx]).strip().lower()
#             )
#             for name in authors_names:
#                 author = Author.objects.filter(name=name.strip()).first()
#                 if author:
#                     book.authors.add(author)

#             categories_labels = re.split(
#                 " - | / ", str(df["categories"][idx]).strip().lower()
#             )
#             for label in categories_labels:
#                 category = Category.objects.filter(label=label.strip()).first()
#                 if category:
#                     book.categories.add(category)
#     return df


# @transaction.atomic
# def load_data(request):
#     spliter = "&"
#     books = (
#         Book.objects.annotate(num_categories=Count("categories"))
#         .filter(num_categories__gt=0)
#         .prefetch_related("categories")
#         .filter(categories__label__endswith=")")
#     )

#     # for book in books:
#     #     for categ in book.categories.all():
#     #         categs = categ.label[:-1]
#     #         categ_object = Category.objects.filter(label=categs).first()
#     #         if categ_object:
#     #             book.categories.add(categ_object)
#     #             book.categories.remove(categ)
#     #             book.save()
#     #             print(f"Book {book.isbn} updated")
#     print(books.count())
#     return HttpResponse("Good")


# @transaction.atomic
# def load_data(request):
#     spliter = "&"
#     books = (
#         Book.objects.annotate(num_categories=Count("categories"))
#         .filter(num_categories__gt=0)
#         .prefetch_related("categories")
#         .exclude(categories__label__contains="(")
#         .filter(categories__label__endswith=")")
#     )
#     for book in books:
#         for categ in book.categories.all():
#             categs = categ.label.split(spliter)
#             if len(categs) > 1:
#                 for ct in categs:
#                     new_categ, created = Category.objects.get_or_create(
#                         label=ct.strip()
#                     )
#                     book.categories.add(new_categ)
#                 book.categories.remove(categ)
#                 book.save()
#                 print(f"Book {book.isbn} updated")
#     print(books.count())
#     return HttpResponse("Good")


# @transaction.atomic
# def load_data(request):
#     User = get_user_model()
#     with open("users_in.json", encoding="utf-8") as F:
#         json_data = json.loads(F.read())

#     users = []
#     usersnames_already_in = set()
#     users_already_in = []
#     print("Start building users.")
#     for user in json_data:
#         username = user.get("username")
#         if username not in usersnames_already_in:
#             users.append(
#                 User(
#                     id=user.get("id") + 1,
#                     username=user.get("username"),
#                     email=user.get("email"),
#                     password=user.get("password"),
#                 )
#             )
#             usersnames_already_in.add(username)
#         else:
#             users_already_in.append(user)

#     print("Saving to database.")
#     User.objects.bulk_create(users)
#     with open("users_in.json", "w", encoding="utf8") as fp:
#         json.dump(users_already_in, fp)

#     return HttpResponse("Good")


# @transaction.atomic
# def load_data(request):
#     df = pd.read_excel("authors.xlsx")
#     added = set()
#     objects = []

#     for idx in df.index:
#         authors = re.split(";|\||/ ", df["authors"][idx].strip().lower())
#         for author in authors:
#             author = author.strip()
#             if author not in added:
#                 objects.append(Author(name=author))
#             added.add(author)

#     Author.objects.bulk_create(objects)

#     return HttpResponse("Good")


# @transaction.atomic
# def load_data(request):
#     df = pd.read_excel("categories.xlsx")
#     added_categories = set()
#     categories_object = []

#     for idx in df.index:
#         categories = re.split(" - | / ", df["categories"][idx].strip().lower())
#         for category in categories:
#             if category not in added_categories:
#                 categories_object.append(Category(label=category))
#             added_categories.add(category)

#     Category.objects.bulk_create(categories_object)

#     return HttpResponse("Good")
