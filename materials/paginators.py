from rest_framework.pagination import PageNumberPagination


class TrainingCoursePaginator(PageNumberPagination):
    page_size = 4
    page_query_param = 'page_size'
    max_page_size = 30


class LessonPaginator(PageNumberPagination):
    page_size = 4
    page_query_param = 'page_size'
    max_page_size = 30
