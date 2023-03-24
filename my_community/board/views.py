from django.shortcuts import render
from .models import Board

# Create your views here.
def board_list(request):
    # 모든 게시글 가져오기
    boards = Board.objects.all().order_by('-id')
    
    return render(request, 'board_list.html', {'boards': boards})