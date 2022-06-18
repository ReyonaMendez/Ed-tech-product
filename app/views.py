from PIL import Image,ImageColor 
from django.shortcuts import render

# Create your views here.
def white(request):
  if request.method == 'GET':
    return render(request,"index.html")
  else:
    color = request.POST['dropdown-bg']
    size =  request.POST['img_size']
    img2 = ImageColor.getrgb(color)
    
    if size == 'large':
      width = 7680
      height = 4320
    elif size == 'medium':
      width = 1920
      height = 1080
    elif size == 'small':
      width = 640
      height = 480 
    img  = Image.new( mode = "RGB",size = (width, height), color =img2)
    img.save('app/static/images/color-output.png')
    return render(request,'result.html')













# def result(request,id=None):
#   if id:
#     with open ("color-output.png",'rb') as f:
#       fv = f.read()
#       # img_value = img.show()
#       return render(request,"result.html",{'key_img':fv})


  
  
  
  
  
  
  


# def results(request):
#   if request.method=="POST":
#     bgcolor=request.POST["bgcolor"]
#     imgsize=request.POST["img_size"]
#     context = { 'bgcolor_key' : bgcolor, 'img_key': imgsize}
#     return render(request, "result.html", context)
   



  