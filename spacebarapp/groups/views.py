from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.contrib import messages
from django.db import IntegrityError
from django.urls import reverse
from django.views import generic
from .models import Group, GroupMember
# Create your views here.


class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = Group


class SingleGroup(generic.DetailView):
    model = Group


class ListGroups(generic.ListView):
    model = Group
