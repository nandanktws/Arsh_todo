from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from .models import TodoListItem
from .form import TaskForm
from django.shortcuts import render
def todoappView(request):
    return render(request, 'todolist.html')

def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items}) 
    
def addTodoView(request):
    print("comnes here")
    if request.method == 'POST':
        tes = request.POST['content']
        print(tes,"--------------")
        new_item = TodoListItem(content=tes)
        print("bvbvcbvzcjhvdc")
        new_item.save()
        return HttpResponseRedirect('/todoapp/') 
    
    
def update_task(request, pk):
    task = TodoListItem.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/todoapp/')
    return render(request, "update.html", {"task_edit_form": form})

def deleteTodoView(request,i):
    print(i,"-------------------")
    y = TodoListItem.objects.get(id=i)
    
    print(y,"________+++")
    y.delete()
    return HttpResponseRedirect('/todoapp/') 


def viewSingleTodoitem(request,id):
    print(request.method)    
    print("hello")
    if request.method == 'GET': 
        try:
            new = TodoListItem.objects.get(id=id)
            # Member.objects.get(phone=123)
            
            print(new,"_____________________++")
            context = {'new': new}

            print("hihihihi")
            
            return render (request,'single_todo.html',context=context)
        except Exception as e:
            print(e)
            new=None
            return HttpResponse('Todo not found')
    else:
        return HttpResponse('Got post request')
    
    

        



