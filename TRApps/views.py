# HttpResponse is used to
# pass the information
# back to view
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms.AssessmentForm import *
from .model.tabelAssessment import Assessment
from .forms.addStudentForm import mahasiswaForm
from .model.tabelMahasiswa import Mahasiswa
from .forms.dosenForm import DosenForm
from .model.tabelDosen import Dosen
from .model.tabelMataKuliah import MataKuliah
from .forms.matakuliahForm import mkForm
from .model.tabelDosenPengampu import DosenPengampu
from .forms.dosenpengampuForm import DosenPengampuForm
from .forms.testForm import testForm
from .model.tabelTest import Test
from .forms.kunciJawabanForm import kunciJawabanForm
from .model.tabelKunciJawaban import KunciJawaban
from .model.tabelScoring import Scoring
from .forms.studentScoreForm import ScoreStudentForm
from .SimpleTR.main import main

# Defining a function which
# will receive request and
# perform task depending
# upon function definition

def homeview(request):
	# logic of view will be implemented here
	context = {
		"data ": "Gfg"
	}
	return render(request, "home.html", context)

def createMahasiswa(request):
	context={}
	form = mahasiswaForm(request.POST or None)
	if form.is_valid():
		form.save()

	context['form'] = form
	context['dataset'] = Mahasiswa.objects.all()
	return render(request, "addStudent.html", context)

def createDosen(request):
	context = {}
	form = DosenForm(request.POST or None)
	if form.is_valid():
		form.save()

	context['form'] = form
	context['dataset'] = Dosen.objects.all()
	return render(request, "tabelDosen.html", context)

def createMK(request):
	context = {}
	form = mkForm(request.POST or None)
	if form.is_valid():
		form.save()

	context['form'] = form
	context['dataset'] = MataKuliah.objects.all()
	return render(request, "tabelMK.html", context)

def createdosenPengampu(request):
	context = {}
	form = DosenPengampuForm(request.POST or None)
	if form.is_valid():
		form.save()

	context['form'] = form
	context['dataset'] = DosenPengampu.objects.all()
	return render(request, "tabelDosenPengampu.html", context)

def createTest(request):
	context = {}
	form = testForm(request.POST or None)
	if form.is_valid():
		form.save()

	context['form'] = form
	context['dataset'] = Test.objects.all()
	return render(request, "tabelTest.html", context)

def createKunciJawaban(request, id):
	test_instance = None
	if id:
		test_instance = Test.objects.get(pk=id)

	context = {}
	if request.method == 'POST':
		form = kunciJawabanForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = kunciJawabanForm(initial={'tanggalUjian': test_instance.id, 'mata_kuliah': test_instance.mata_kuliah })

	context['form'] = form
	context['dataset'] = KunciJawaban.objects.all()
	context['test_instance'] = test_instance
	return render(request, "tabelKunciJawaban.html", context)


def createStudentScore(request, id):
	test_instance = None
	if id:
		test_instance = Test.objects.get(pk=id)

	context = {}
	if request.method == 'POST':
		form = ScoreStudentForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = ScoreStudentForm()

	context['form'] = form
	context['dataset'] = Scoring.objects.all()
	context['test_instance'] = test_instance
	return render(request, "viewStudentScore.html", context)

def viewJadwal(request):
	context = {}
	context['dataset'] = Test.objects.all()
	return render(request, "viewJadwal.html", context)

def viewStudent(request):
	context = {}
	context['dataset'] = Mahasiswa.objects.all()
	return render(request, "viewStudent.html", context)

def assessmentStudent(request, id):
	test_instance = None
	if id:
		test_instance = Test.objects.get(pk=id)

	context = {}
	kunci_jawaban = KunciJawaban.objects.filter(tanggalUjian=test_instance)
	if request.method == 'POST':
		context['mahasiswa'] = Mahasiswa.objects.get(pk=request.POST['mahasiswa'])
		total_score = 0
		for kunci in kunci_jawaban:
			score = 0
			try:
				file_jawaban_mhs = request.FILES['jawaban-'+str(kunci.id)]

				assesment = Assessment()
				assesment.file = file_jawaban_mhs
				jawaban = main(assesment.file)['recognized']
				if jawaban == kunci.jawaban:
					score = int(kunci.point)
				assesment.score = score
				assesment.save()

				kunci.score = score
				total_score += score
			except:
				kunci.score = 0
		context['total_score'] = total_score
		form = ScoreStudentForm(request.POST)
	if form.is_valid():
		scoring = form.save(commit=False)
		scoring.hasilScore = total_score
		scoring.save()
	else:
		form = ScoreStudentForm(initial={'tanggalUjian': test_instance, 'dosen_pengampu': test_instance.mata_kuliah})
	context['kunci_jawaban'] = kunci_jawaban
	context['form'] = form
	context['test_instance'] = test_instance
	return render(request, "startAssessmentStudent.html", context)


def startAssessment(request):
	if request.method == 'POST':
		form = AssessmentForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('success')
	else:
		form = AssessmentForm()
	return render(request, 'imageupload.html', {'form': form})


def success(request):
	return HttpResponse('successfully uploaded')


def displayAssessment(request):
	if request.method == 'GET':
		# getting all the objects of hotel.
		assesment = Assessment.objects.all()
		return render((request, 'displayimage.html',
					   {'images': Assessment}))

def StudentList(request):
	context = {
		"data ": "Gfg"
	}
	return render(request, 'addStudent.html', context)