from django.shortcuts import render

posts = [
    {
        'author': 'AbhikS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 12, 2021'
    },
    {
        'author': 'JD',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 13, 2021'
    }
]

# Create your views here.
def home(request):
    context = {'posts':posts}
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

