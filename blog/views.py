from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Notice, Board

# Create your views here.

def registerPage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_login')
    context = {'form': form}
    return render(request, 'registration/register.html', context)

@login_required
def notice_list(request):
    notices = Notice.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/notice_list.html', {'notices': notices})

@login_required
def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'blog/notice_detail.html', {'notice': notice})

def blog_index(request):
    return render(request, 'blog/index.html')

@login_required
def blog_home(request):
    return render(request, 'blog/home.html')

@login_required
def board_list(request):
    boards = Board.objects.all()

    return render(request, 'blog/board_list.html', {'boards': boards})

@login_required
def board_write(request):
    if request.method == 'POST':
        if request.POST['title']:
            board = Board.objects.create(title=request.POST['title'], contents=request.POST['contents'])
        else:
            board = Board.objects.create(title=request.POST['title'], contents=request.POST['contents'])
        return redirect('board_list')
    return render(request, 'blog/board_write.html')

@login_required
def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'blog/board_detail.html', {'board': board})