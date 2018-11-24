from django.shortcuts import render
from django.utils import timezone
from .models import Rescatado
from django.shortcuts import render, get_object_or_404
from .forms import ResForm
from django.shortcuts import redirect

# Create your views here.
def res_list(request):
    posts = Rescatado.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/res_list.html', {'posts': posts})

def res_detail(request, pk):
    post = get_object_or_404(Rescatado, pk=pk)
    return render(request, 'blog/res_detail.html', {'post': post})

def res_new(request):
    if request.method == "POST":
        form = ResForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('res_detail', pk=post.pk)
    else:
        form = ResForm()
    return render(request, 'blog/res_edit.html', {'form': form})

def res_edit(request, pk):
    post = get_object_or_404(Rescatado, pk=pk)
    if request.method == "POST":
        form = ResForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('res_detail', pk=post.pk)
    else:
        form = ResForm(instance=post)
    return render(request, 'blog/res_edit.html', {'form': form})

def res_delete(request, pk):
    post = get_object_or_404(Rescatado, pk=pk)
    if request.method == 'POST':
        Rescatado.delete(post)
        return render(request, 'blog/res_list.html', {'post':post})
    else:
        form = ResForm(instance=post)
    return render(request, 'blog/res_delete.html', {'form':form})
