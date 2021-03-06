from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect


def post_list(request):
    """
    first/
        first_file.txt
        second/
            second_file.txt
            third/
                module.py
                fourth/
                    fourth_file.txt
    modoule.py에서
    0. 현재 경로
        os.path.abspath(__file__)
    1. third/ 폴더에 대한 경로
        os.path.dirname(<현재경로>)
    2. second/second_file.txt 의 경로
        os.path.join(<second 폴더의 경로>, 'second_file.txt')
    3. fourth/ 폴더의 경로
        os.path.join(<현재경로>, 'fourth')
    4. fourth/fourth_file.txt의 경로
        os.path.join(<현재경로>, 'fourth', 'fourth_file.txt')

        third에 있는 views.py에서
        third에 있는 post_list.html을 불러온다.


    :param request:
    :return:
    """
    # cur_file_path = os.path.abspath(__file__)
    # print(f'cur_file_path:{cur_file_path}')
    # blog_dir_path = os.path.dirname(cur_file_path)
    # print(f'blog_dir_path:{blog_dir_path}')
    # app_path = os.path.dirname(blog_dir_path)
    #
    # templates_path = os.path.join(app_path, 'templates')
    #
    # post_list_path = os.path.join(templates_path, 'blog', 'post_list.html')

    # result = open(post_list_path, 'rt').read()

    # html = render_to_string('blog/post_list.html')
    #
    # return HttpResponse(html)

    posts = Post.objects.all().order_by('-id')

    context = {
        'posts': posts,
    }

    result = '글 목록<br>'
    for post in posts:
        result += f'- {post.title}<br>' \

    return render(request, 'blog/post_list.html', context)


def post_detail(request, post_id):

    post = Post.objects.get(id=post_id)

    context ={
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)


def post_create(request):

    if request.method == 'POST':

        print(request.POST.get('title'))
        print(request.POST.get('text'))
        print(request.user.username)
        print(type(request.user))

        new_post = Post.objects.create(title=request.POST.get('title'),
                                       text=request.POST.get('text'),
                                       author=request.user,
                                       )
        # HTTP Redirection 을 보낼 URL
        # root URL 로 리다이렉트

        return redirect('post-list')
        # return HttpResponseRedirect('/')

    else:
        return render(request, 'blog/post_create.html')


def post_delete(request, post_id):

    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.delete()
        return redirect('post-list')
