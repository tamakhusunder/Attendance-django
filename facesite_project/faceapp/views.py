from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Teacherdb

# Create your views here.
# def index(request):
#     return HttpResponse('Hello world 2')




# def database_collection():
# 	teacherdbs=Teacherdb.objects
# 	cursor = connection.cursor()
# 	cursor.execute("SELECT COUNT(*) FROM faceapp_teacherdb")
#     sql_totstaff = fetchone()
#     print(connection.queries)
# 	print('sunder')
# 	print(sql_totstaff)
# 	print('sunder')
# 	return teacherdbs,sql_totstaff

################

def database_collection():
	teacherdbs=Teacherdb.objects.all()
	# sql_totstaff=Teacherdb.objects.raw("SELECT  COUNT(*) FROM faceapp_teacherdb")
	#sql-->*:all()			WHERE:filter()
	sql_totstaff = Teacherdb.objects.all().count()
	sql_present = Teacherdb.objects.filter(attendance="Present").count()
	sql_absent = Teacherdb.objects.filter(attendance="Absent").count()
	print('sunder')
	print(sql_present)
	return teacherdbs,sql_totstaff,sql_present,sql_absent

def index(request):
	teacherdbs,sql_totstaff,sql_present,sql_absent=database_collection()
	return render(request,'faceapp/index.html',{'teacherdbs':teacherdbs,'sql_totstaff':sql_totstaff,'sql_present':sql_present,'sql_absent':sql_absent})

def register(request):
	return render(request,'faceapp/register.html',{})

def addstaff(request):
	return render(request,'faceapp/add_new_staff.html',{})

def face_exe(request):
	return render(request,'faceapp/face_exe.html',{})

def chart(request):
	return render(request,'faceapp/charts.html',{})

def table(request):
	teacherdbs,sql_totstaff,sql_present,sql_absent=database_collection()
	return render(request,'faceapp/tables.html',{'teacherdbs':teacherdbs})


# <<<<<<<<<----application code--->>>>>>>>>>>>>>>>>>>

# <<<<<<<<<<<< 1.Capture the face>>>>>>>>>>>>>>>>
def captureface(request):
	from os import listdir
	from os.path import isfile, join
	import os
	import cv2
	import dlib
	import numpy as np

	from facesite.settings import BASE_DIR
	
	# POST input_name of user input collected
	val_name=str(request.POST["ipname"])
	print(val_name)
	# path for making folder for input name
	path_name=BASE_DIR+r'\\media\\faceapp\\images\\capture\\'+val_name
	
	if not os.path.exists(path_name):
		print(path_name)
		print('<<<<<<<<<<<<<<<<<sunder>>>>>>>>>>>>>>>>>>>>>>>>>>')
		os.makedirs(path_name)
	
		# <<<<<<<<<<<<< code of capturing picture>>>>>>>>>>
		detector = dlib.get_frontal_face_detector()

		# Initialize Webcam
		cap = cv2.VideoCapture(0)
		# img_size = 64
		margin = 0.2
		frame_count = 0

		while True:
		    ret, frame = cap.read()
		    frame_count += 1
		    print(frame_count)   
		    input_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		    img_h, img_w, _ = np.shape(input_img)
		    detected = detector(frame, 1)
		    faces = []
		    
		    if len(detected) > 0:
		        for i, d in enumerate(detected):
		            x1, y1, x2, y2, w, h = d.left(), d.top(), d.right() + 1, d.bottom() + 1, d.width(), d.height()
		            xw1 = max(int(x1 - margin * w), 0)
		            yw1 = max(int(y1 - margin * h), 0)
		            xw2 = min(int(x2 + margin * w), img_w - 1)
		            yw2 = min(int(y2 + margin * h), img_h - 1)
		            face =  frame[yw1:yw2 + 1, xw1:xw2 + 1, :]
		            file_path = path_name
		            file_name = file_path+r"\\"+val_name+str(frame_count)+"_"+str(i)+".jpg"
		            print(file_name)
		            dim = (224,224)
		            face = cv2.resize(face,dim)
		            cv2.imwrite(file_name, face)
		            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
		    cv2.imshow("Face Capturing..", frame)
		    if cv2.waitKey(1) == 13 or frame_count == 5 : #13 is the Enter Key and plz put value of frame_count as per photo to be clicked
		        break

		cap.release()
		cv2.destroyAllWindows()      

	return redirect('/')


# <<<<<<<<<<<<<<3.Recognize the face>>>>>>>>>>>>>>>>>
def recognization(request):
	# Load our model
	from tensorflow.keras.models import load_model
	from datetime import datetime

	from os import listdir
	from os.path import isfile, join
	import os
	import cv2
	import numpy as np
	from tensorflow.keras.preprocessing.image import ImageDataGenerator
	from tensorflow.keras.preprocessing.image import img_to_array
	import dlib


	from facesite.settings import BASE_DIR

	# file_name = os.path.dirname(__file__) +'\\datasets\\test_catvnoncat.h5'
	# test_dataset = h5py.File(file_name, "r")

	model_path=BASE_DIR+r'\\static\\faceapp\\train_model\\face_new_model3.h5'
	Project7Sem = load_model(model_path)

	face_classes = {0: 'Amar Naga', 1: 'Anirudh Basukala', 2: 'Manish Kharbuja', 3: 'Manish Nhuchhe', 4: 'SKSir',5: 'Sunder'}


	def draw_label(image, point, label, font=cv2.FONT_HERSHEY_SIMPLEX,
	               font_scale=0.8, thickness=1):
	    size = cv2.getTextSize(label, font, font_scale, thickness)[0]
	    x, y = point
	    cv2.rectangle(image, (x, y - size[1]), (x + size[0], y), (255, 0, 0), cv2.FILLED)
	    cv2.putText(image, label, point, font, font_scale, (255, 255, 255), thickness, lineType=cv2.LINE_AA)
	    
	margin = 0.2
	t= 1
	# load model and weights
	img_rows, img_cols = 100, 100

	detector = dlib.get_frontal_face_detector()

	cap = cv2.VideoCapture(0)
	cap.set(cv2.CAP_PROP_FRAME_WIDTH,1000)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1000)
	temp= []
	temp_face=[]
	while True:
	    ret, frame = cap.read()
	    frame = cv2.resize(frame, None, fx=0.8, fy=0.8, interpolation = cv2.INTER_LINEAR)
	    preprocessed_faces = []           
	 
	    input_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	  
	    #cv2.imshow('Test image',input_img )

	    img_h, img_w, _ = np.shape(input_img)
	    detected = detector(frame, 1)
	    faces = np.empty((len(detected), img_h, img_w, 3))
	    
	    preprocessed_faces_emo = []
	    if len(detected) > 0:
	        for i, d in enumerate(detected):
	            x1, y1, x2, y2, w, h = d.left(), d.top(), d.right() + 1, d.bottom() + 1, d.width(), d.height()
	            xw1 = max(int(x1 - margin * w), 0)
	            yw1 = max(int(y1 - margin * h), 0)
	            xw2 = min(int(x2 + margin * w), img_w - 1)
	            yw2 = min(int(y2 + margin * h), img_h - 1)
	            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
	            # cv2.rectangle(img, (xw1, yw1), (xw2, yw2), (255, 0, 0), 2)
	            #faces[i, :, :, :] = cv2.resize(frame[yw1:yw2 + 1, xw1:xw2 + 1, :], (img_size, img_size))
	            face =  frame[yw1:yw2 + 1, xw1:xw2 + 1, :]
	            temp_face=face
	            face = cv2.resize(face, (224,224), interpolation = cv2.INTER_AREA)
	            face = face.astype("float") / 255.0
	            face = img_to_array(face)
	            face = np.expand_dims(face, axis=0)
	            preprocessed_faces.append(face)
	           # print(preprocessed_faces)
	       
	        
	        face_labels = []
	        
	        for i, d in enumerate(detected):
	            preds = Project7Sem.predict(preprocessed_faces[i])[0]
	            #print(type(preds))
	           # count = len([i for i in preds if i > 0.3]) 
	        #0.3 is good
	        
	            if (max(preds))>0.60:
	                #print(preds.argmax())
	                #print(face_classes[preds.argmax()])
	                face_labels.append(face_classes[preds.argmax()])
	                
	                if face_classes[preds.argmax()]  not in temp:
	                                temp.append(face_classes[preds.argmax()])
	            else:
	                #print(count)
	#                 date_time = datetime.now()
	#                 d = date_time.strftime("%Y%m%d%H%M%S")
	#                 outpath='D:/unknown_pics/'+d+'.jpg'
	                #t=t+1
	#                 cv2.imwrite(outpath,temp_face)
	                face_labels.append('unknown')
	        # draw results
	        for i, d in enumerate(detected):
	            label = "{}".format(face_labels[i])
	            draw_label(frame, (d.left(), d.top()), label)
	   
	        
	    cv2.imshow("face recognition", frame)
	    if cv2.waitKey(1) == 13: #13 is the Enter Key
	        break

	cap.release()
	cv2.destroyAllWindows()  

	return redirect('/')   









###########work to be done 
def offline(request):
	from tkinter import Tk
	from tkinter import filedialog
	import os
	#dialog box for opening the video file
	my_filetypes = [('mp4  files', '*.mp4'), ('png files', '.png'),('jpg files', '.jpg'), ('all files', '.*')]
	file_path = filedialog.askopenfilename(parent=window,
                                    initialdir=os.getcwd(),
                                    title="Please select a file:",
                                    filetypes=my_filetypes)
	#    capture_value='C:/Users/Hukka/Desktop/test videos/videorec.mp4'
	if len(file_path) >0:	 #check for empty string and to remove error 
		file_path=file_path.replace('/','\\')
		myVars = {'capture_value':file_path}
		exec(open('webcam_recognizer_unknown.py').read(), myVars)

	
	return('/')


#######

# def home(request):
# 	return render(request,'faceapp/index.html',{})

