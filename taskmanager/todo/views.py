from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_400_BAD_REQUEST
# More rest imports as needed
from django.contrib.auth import authenticate
from datetime import date, timedelta
from .decorators import define_usage
from .models import Task


#URL /
@define_usage(returns={'url_usage': 'Dict'})
@api_view(['GET'])
@permission_classes((AllowAny,))
def index(requet):
    details = {}
    for item in list(globals().items()):
        if item[0][0:4] == 'api_':
            if hasattr(item[1], 'usage'):
                details[reverse(item[1].__name__)] = item[1].usage
    return Response(details)


#URL /signin/
#Note that in a real Django project, signin and signup would most likely be
#handled by a seperate app. For signup on this example, use the admin panel.
@define_usage(params={'username': 'String', 'password': 'String'},
              returns={'authenticated': 'Bool', 'token': 'Token String'})
@api_view(['POST'])
@permission_classes((AllowAny,))
def signin(request):
    try:
        username = request.data['username']
        password = request.data['password']
    except:
        return Response({'error': 'Please provide correct username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'authenticated': True, 'token': token.key})
    else:
        return Response({'authenticated': False, 'token': None})


#URL /all/
@define_usage(returns={'tasks': 'Dict'})
@api_view(['GET'])
def all_tasks(request):
    try:
        return Response({'tasks': request.user.task_list.all()})
    except:
        return Response({'error': 'Please provide correct token'},
                        status=HTTP_400_BAD_REQUEST)


#URL /new/
@define_usage(params={'description': 'String', 'due_in': 'Int'},
              returns={'done': 'Bool'})
@api_view(['PUT'])
def new_task(request):
    try:
        task = Task(user=request.user,
                    description=request.data['description'],
                    due=date.now() + timedelta(days=int(request.data['due_in'])))
        task.save()
        return Response({'done': True})
    except:
        return Response({'error': 'Please provide correct token'},
                        status=HTTP_400_BAD_REQUEST)


#URL /update/
@define_usage(params={'task_id': 'Int', 'description': 'String', 'due_in': 'Int'},
              returns={'done': 'Bool'})
@api_view(['POST'])
def update_task(request):
    try:
        task = request.user.task_list.get(id=int(request.data['task_id']))
        try:
            task.description = request.data['description']
        except: #Description update is optional
            pass
        try:
            task.due = date.now() + timedelta(days=int(request.data['due_in']))
        except: #Due date update is optional
            pass
        task.save()
        return Response({'done': True})
    except:
        return Response({'error': 'Please provide correct token'},
                        status=HTTP_400_BAD_REQUEST)


#URL /delete/
@define_usage(params={'task_id': 'Int'},
              returns={'done': 'Bool'})
@api_view(['DELETE'])
def delete_task(request):
    try:
        task = request.user.task_list.get(id=int(request.data['task_id']))
        task.delete()
        return Response({'done': True})
    except:
        return Response({'error': 'Please provide correct token'},
                        status=HTTP_400_BAD_REQUEST)
