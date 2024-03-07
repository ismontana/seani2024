from django.shortcuts import render

from .forms import CandidateForm
def add_candidate(request):
    form = CandidateForm()
    return render(request,
                  'exam/add_candidate.html',
                  {'form': form})