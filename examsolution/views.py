from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *




# Create your views here.

# Home page view with empty url

def home(request):
    

    
    all_exam_boards = ExamBoard.objects.all()
    
    context = {
        
        'all_exam_boards' : all_exam_boards,
        
        
    }
    
    return render(request, 'examsolution/home.html', context)

# Syllabus page view

def syllabi(request):
   
    context = {

    }
    
    return render(request,'examsolution/syllabi.html',context)

# Notes page view

def notes(request):
    
    context = {
        
    }
    
    return render(request, 'examsolution/notes.html', context)

# Topical Past Paper views starts here

def index_topical_past_paper(request):
    
    exam_board_list = ExamBoard.objects.all()
           
    context = {

        'exam_board_list' : exam_board_list,

    }

    return render(request, 'examsolution/topical_past_paper.html', context)

def subject_topical_past_paper(request,exam_board):
    
    exam_board_selected = get_object_or_404(ExamBoard,exam_board=exam_board)
    
    context = {
        'exam_board_selected' : exam_board_selected,
    }
    
    return render(request,"examsolution/subject_topical_past_paper.html",context)

def topics_topical_past_paper(request,exam_board,subject_selected):
    topic_paper_list = BoardSubTopic.objects.filter(subject_key__subject=subject_selected)
    context = {
        'subject_selected':subject_selected,
        'topic_paper_list':topic_paper_list,
        'exam_board' : exam_board,
    }
    
    return render(request,"examsolution/topics_topical_past_paper.html",context)

def view_topical_past_paper(request,exam_board,subject_selected,topic_id):
    year_set = Year.objects.all()
    session_set = Session.objects.all()
    topic_paper_object = get_object_or_404(BoardSubTopic, pk=topic_id)
    selected_topic_paper_set = topic_paper_object.questionanswer_set.all()
    new_selected_topic_paper_set = topic_paper_object.questionanswer_set.filter(year_key=request.POST.get("year",False), session_key=request.POST.get("session",False))
    

    

    context = {
        'exam_board' : exam_board,
        'subject_selected' :subject_selected,
        'topic_paper_object' : topic_paper_object,
        'selected_topic_paper_set' : selected_topic_paper_set,
        'new_selected_topic_paper_set':new_selected_topic_paper_set,
        'year_set' : year_set,
        'session_set' : session_set,
        
    }

    return render(request,"examsolution/view_topical_past_paper.html",context)
# Topical Past Paper views ends here

# Past Paper view starts here

def index_past_papers(request):
    
    exam_board_list = ExamBoard.objects.all()
    
    context = {
        'exam_board_list': exam_board_list
    }
    
    return render(request, 'examsolution/past_papers.html', context)

def subject_past_papers(request,exam_board):
    
    exam_board_selected = get_object_or_404(ExamBoard,exam_board=exam_board)
    
    context = {
        'exam_board_selected' : exam_board_selected,
    }
    
    return render(request,'examsolution/subject_past_papers.html',context)

def year_past_papers(request,exam_board,subject_selected):
    
    years_available_list = Year.objects.all()
    
    context = {
        'years_available_list':years_available_list,
        'exam_board' : exam_board,
        'subject_selected':subject_selected,
        
    }
    
    return render(request,'examsolution/year_past_papers.html',context)

def view_past_paper(request,exam_board,subject_selected,year):
    
    march_past_papers_selected_list = FullQuestionAnswer.objects.filter(session_key__session='March',year_key__year=year,subject_key__subject=subject_selected).order_by('full_question_name')
    june_past_papers_selected_list = FullQuestionAnswer.objects.filter(session_key__session='June',year_key__year=year,subject_key__subject=subject_selected).order_by('full_question_name')
    november_past_papers_selected_list = FullQuestionAnswer.objects.filter(session_key__session='November',year_key__year=year,subject_key__subject=subject_selected).order_by('full_question_name')
    
    march_extras = ReportThreshPrep.objects.filter(session_key__session='March',year_key__year = year,subject_key__subject=subject_selected).order_by('extra_name')
    june_extras = ReportThreshPrep.objects.filter(session_key__session='June',year_key__year = year,subject_key__subject=subject_selected).order_by('extra_name')
    november_extras = ReportThreshPrep.objects.filter(session_key__session='November',year_key__year = year,subject_key__subject=subject_selected).order_by('extra_name')
    
    context = {
        
        'exam_board' : exam_board,
        'subject_selected' : subject_selected,
        'year':year,
        'march_past_papers_selected_list' : march_past_papers_selected_list,
        'june_past_papers_selected_list':june_past_papers_selected_list,
        'november_past_papers_selected_list':november_past_papers_selected_list,
        'march_extras' : march_extras,
        'june_extras':june_extras,
        'november_extras':november_extras,
       
    }
    
    return render(request,'examsolution/view_past_paper.html',context)

# Past Paper view ends here

# Test Yourself starts here

def index_test_yourself(request):
    
    multiple_choice_available_list = FullQuestionAnswer.objects.filter(paper_number__paper_num='1')
    
    context = {
        'multiple_choice_available_list' : multiple_choice_available_list,
    }
    
    return render(request, 'examsolution/test_yourself.html', context)

def taking_test(request,question_id):
    
    mcq_paper_selected = FullQuestionAnswer.objects.get(id=question_id).paperoneanswers_set.all()
    
    context = {
        'mcq_paper_selected' : mcq_paper_selected,
    }
    
    return render(request,'examsolution/taking_test.html',context)

# Test Yourself ends here

# College view

def college(request):

    
    context = {
        
    }
    
    return render(request, 'examsolution/college.html', context)

# Contact PiiLearn view

def contactpiilearn(request):
    
    context = {
       
    }
    
    return render(request, 'examsolution/contact_piilearn.html', context)

def exam_board(request):
    
    context = {

    }
    
    return render(request,'examsolution/exam_board.html',context)