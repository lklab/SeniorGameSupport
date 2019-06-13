from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import os
from pathlib import Path

@csrf_exempt
def receive_data(request) :
	if request.method == "POST" :
		directory_path = str(Path.home()) + "/senior_log"
		
		if not os.path.isdir(directory_path) :
			os.mkdir(directory_path)

		file_path = directory_path + "/" + request.POST["filename"]

		log_file = open(file_path, 'w')
		log_file.write(request.POST["data"])
		log_file.close()

		print("log data is saved to " + file_path)
		return HttpResponse("")
	else :
		return render(request, 'html/default.html', {})

#return render(request, 'html/default.html', {})

# Create your views here.
