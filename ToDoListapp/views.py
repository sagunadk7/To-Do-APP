from django.shortcuts import render, redirect, get_object_or_404
from service.models import Services
from django.contrib import messages
def ToDoApp(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        date = request.POST.get('date')
        
        Services.objects.create(
            task = task,
            date = date
        )
        messages.success(request,'Task added successfully')
        
    
        
        return redirect('home')
    
    
    return render(request,'index.html')

def yourtask(request):
    queryset = Services.objects.all()
    context = {'tasks':queryset}
        
    
    
    return render(request,'yourtask.html',context)


def deletetask(request, taskid):  
    task = get_object_or_404(Services, id=taskid)  
    if request.method == 'POST':
        task.delete()
        return redirect('yourtask')  
