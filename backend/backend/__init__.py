from .celery import app as celery_app

"""This ensures that celery app is imported 
everytime django is started.
"""
__all__ = ['celery_app']