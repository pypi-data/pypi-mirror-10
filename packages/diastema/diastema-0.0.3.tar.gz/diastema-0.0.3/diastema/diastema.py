import numpy
import matplotlib.pyplot as plt
from scipy.stats.kde import gaussian_kde
from scipy.stats.mstats import mode
from math import log10

import glob, os.path, time, os

from essentia import *  # Importer toutes les fonctions de la bibliotheque Essentia
from essentia.standard import * # Importer toutes les fonctions du module **standard** de Essentia
#from pandas import *

numpy.set_printoptions(precision=4)

class Melodie(object):
	"""Une classe definissant une melodie et ses caracteristiques, a partir de la liste de ses frequences"""
		
	def __init__(self, file, xmin=0, xmax=500):
		self.file_path = file
		self.file_name = os.path.split(self.file_path)[1]
		self.file_label = self.file_name.split(".")[0]
		self.file_exten = self.file_name.split(".")[1]
		self.freqref = 500
		
		self.xmin = xmin
		self.xmax = xmax
		self.x = numpy.linspace(self.xmin,self.xmax,self.xmax-self.xmin)

		if self.file_exten == 'txt':
			self.frequences = numpy.loadtxt(file)
			self.freq = self.frequences[~numpy.isnan(self.frequences)]
			#self.freqtransmode = self.transmode(self.freqref)

			self.fmin = min(self.freq)
			self.fmax = max(self.freq)
			self.fmean = numpy.mean(self.freq)
			self.fstd = numpy.std(self.freq)

			#self.pdf = gaussian_kde(self.freqtransmode[~numpy.isnan(self.freqtransmode)],bw_method=.1)
			self.pdf = gaussian_kde(self.freq[~numpy.isnan(self.freq)],bw_method=.1)
			self.pdf = self.pdf(self.x)

			self.peaks()

		if self.file_exten == 'wav':
			self.file_pitch_extract(self.file_path)

	def __str__(self):
		return "File : %s" % (self.file_name)

	def file_pitch_extract(self,file):
		"""Extraction des frequences avec PredominantMelody()
		Le resultat est un fichier .txt"""

		start = time.time()
		print start,' : Extraction des f0 de ',self.file_name

		audio = MonoLoader(filename = file)() # creation de l'instance
		melodie = PredominantMelody() # creation de l'instance
		pitch, confidence = melodie(audio) 
		pitch[pitch==0]=numpy.nan
		nom_fichier = self.file_name.replace("wav", "txt");
		numpy.savetxt(os.path.split(self.file_path)[0]+'/txt/'+nom_fichier,pitch,fmt='%1.3f')

		end = time.time()
		print 'Fichier',self.file_label,'analyse (',end - start,') secondes'

		return
	
	def pdf(self):
		"""
		Estime la densite de probabilite

		Parameters
		----------
		x : array_like

		Returns
		-------
		y : array_like
	    	Returns a ....

	    """

		return self.pdf.evaluate(self.x)

	def pdf_show(self):
	 	"""Affichage de la fonction de la densite de probabilite"""

		plt.plot(self.x,self.pdf,linewidth=3,alpha=.6,label=self.file_label)
		plt.plot(self.peaks, self.peakspdf, "ro")
		for i in range(0,len(self.peaks)):
			plt.annotate(
					"%.2f" % self.peaks[i],
					xy=(self.peaks[i], self.peakspdf[i]),
					xytext=(self.peaks[i], (self.peakspdf[i]+0.0001)))
		plt.legend()

	def peaks(self):
		"""Obtenir les Peaks du PDF

		"""

		c = (numpy.diff(numpy.sign(numpy.diff(self.pdf))) < 0).nonzero()[0] + 1 # local max

		self.peaks = self.x[c]
		self.peakspdf = self.pdf[c]
		c1 = numpy.array(self.peaks, float)
		c2 = numpy.array(self.peakspdf, float)
		c = numpy.array([c1,c2])
		c = c.transpose()
		c = c[c[:,1].argsort()]
		self.ordredpeaks = c[::-1]

		return self.ordredpeaks

	# def transmode(self,freqref):
	# 	"""Transpose all the frequencies by setting the mode on a given reference frequency

	# 	"""
	# 	interv_transpo = mode(self.freq)[0]/freqref
	# 	self.freqtransposed = self.freq / interv_transpo
	# 	return self.freqtransposed

	def tonique(self,percent=0.5,method="mode"):
		"""
		Get the tonic frequency defined as the mode of the last frequencies array.
		These as selected by the percent argument. Two methods are possible : pdf or mode.
		
		Input :
		-----------
			percent (optional) : a percentage of the number of frames from the total size
			of the frequencies array to give the last frequencies. Default percent= 8
		
		Output :
		-----------

			M : the mode
			N : the mode converted inside an octave
			Final_Freqs : the last frequencies according to the percentage
		"""
		L = len(self.freq)
		Nb_Frames = L*percent/100
		Final_Freqs = self.freq[(L-Nb_Frames):L]

		if method=="pdf":
			# Down to the same octave centered on the mode
			Final_Freqs[Final_Freqs>mode(self.freq)[0]*2] = Final_Freqs[Final_Freqs>mode(self.freq)[0]*2]/2.
			Final_Freqs[Final_Freqs<(mode(self.freq)[0]/2.)] = Final_Freqs[Final_Freqs<mode(self.freq)[0]/2.]*2

			self.final_pdf = gaussian_kde(Final_Freqs)
			lmax= numpy.argmax(self.final_pdf(self.x))+self.xmin
			#plt.plot(x,self.final_pdf(x))
			return self.final_pdf,lmax,Final_Freqs

		if method=="mode":
			M = mode(Final_Freqs)
			if M[0] > mode(self.freq)[0]*2:
				N = M[0]/2
			if M[0] < mode(self.freq)[0]/2:
				N = M[0]*2
			else:
				N = M[0]
			return M[0],N.tolist()[0],Final_Freqs

	def get_intervals(self,percent=0.5,method="mode",unit="savart"):
		"""
		Converts the frequencies into a linear space

		Input :
		-----------
			percent (optional) : percent from the last frequencies to take in consideration. Default = 0.5%
			method (optional) : Two available methods : _pdf_ and _mode_. Default = mode
			unit (optional) : the Unit to use : savart of cent. Default = savart.
		
		Output :
		-----------
			self.intervals : the intervals in the choosen unit.
		"""
		self.intervals = []
		if unit == "savart":
			self.intervals = (numpy.log10(self.ordredpeaks[:,0]/self.tonique(percent,method)[1]))*1000
		if unit == "cent":
			self.intervals = (numpy.log2(self.ordredpeaks[:,0]/self.tonique(percent,method)[1]))*1200
		return self.intervals

class Melodies(object):
	"""Une classe definissant un ensemble de melodies, leur degre d'homogeneite et de proximite

	Attributs:
		- path : un dossier contenant les fichiers .wav ou .txt
	"""

	def __init__(self, path,xmin=0,xmax=500):
		self.path = path  # L'adresse obtenu = un dossier
#		self.exten = exten
		try:
		    os.makedirs(self.path+'txt/')
		except OSError:
		    pass

		self.folder_txt = glob.glob(path+'txt/'+'*.txt')  # Tous les fichiers .txt du dossier
		self.folder_wav = glob.glob(path+'*.wav')  # Tous les fichiers .wav du dossier

		self.melodies = []

		if len(self.folder_txt) == len(self.folder_wav):
			print 'Lecture et analyse de ',len(self.folder_wav),' fichiers (.txt) dans le dossier :',self.path
			for melodie in self.folder_txt:
				self.melodies.append(Melodie(melodie,xmin,xmax))
			#self.Simatrix()
		else:
			print 'Analyse de ',len(self.folder_wav),' fichiers Audio (.wav) dans le dossier :'
			for melodie in self.folder_wav:
				self.melodies.append(Melodie(melodie,xmin,xmax))
			for melodie in self.folder_txt:
				self.melodies.append(Melodie(melodie,xmin,xmax))
		
		self.PdfCorr()
		
	def pitch_extract(self):
		"""Extrait les frequences f0 des tous les fichiers .wav du dossier"""

		files = glob.glob(self.path+'*.wav')
		#fichiers = []
		for fichier_audio in self.melodies:
			self.file_pitch_extract(fichier_audio)
		return

	def PdfCorr(self):
		"""Cree la matrice des coefficients de correlation a partir des pdfs, classe sur la premiere colonne

		"""
		PDFS = []
		for i in range(0,len(self.melodies)):
		    PDFS.append(self.melodies[i].pdf)
		self.PdfCorr = numpy.corrcoef(PDFS)
		return self.PdfCorr

	def PdfsPlot(self,allplots="Yes",gpdf="No"):
		"""Dessine les PDFs de tous les fichiers

		"""
		if allplots == "Yes":
			for melodie_pdf in self.melodies:
				melodie_pdf.pdf_show()
		if gpdf == "Yes":
			self.GlobalPdf()
			self.GPDF_show()
			#plt.plot(self.melodies[0].x,self.GPDF,label="GPDF")
		return plt.show()

	def Simatrix(self):
		"""Cree la matrice des coefficients de correlation a partir des pdfs

		"""
		R = self.PdfCorr
		l = len(self.PdfCorr)
		plt.pcolor(R)
		plt.colorbar()
		plt.yticks(numpy.arange(0.5,l+0.5),range(1,l+1))
		plt.xticks(numpy.arange(0.5,l+0.5),range(1,l+1))
		return plt.show()

	def SimPdf(self,i):
		"""PDF des similarites, basee sur la melodie i

		"""
		#self.PdfCorr = self.PdfCorr[:, self.PdfCorr[i].argsort()]
		PdfCorrI = self.PdfCorr[i]
		b = gaussian_kde(PdfCorrI)
		x = numpy.arange(0,1,0.001)
		Y = b(x)
		plt.plot(x,Y)

	def SimPdfs(self):
		"""PDFs des similarites, basee sur toutes les SimPdf

		"""
		for i in range(0,len(self.PdfCorr)):
			self.SimPdf(i)

	def Intervals(self):
		"""Get intervals of all Melodies

		"""
		self.Intervals = []
		for i in range(0,len(self.melodies)):
			self.Intervals.append(self.melodies[i].get_intervals())
		return self.Intervals

	def AllTonics(self,percentages,method="pdf"):
		"""Get all tonics with different percentages

		"""
		for i in range(0,len(self.melodies)):
			phrase = []
			for j in percentages:
				phrase.append(self.melodies[i].tonique(j, method)[1])
			print 'Toniques possibles de la Phrase', i, ' : ', phrase	
		return

	def GlobalPdf(self):
		"""Get a global PDF as a sum of all pdf-s

		"""
		a = [self.melodies[0].pdf]
		for i in range(1,len(self.melodies)):
		    a = numpy.append(a,[self.melodies[i].pdf],axis=0)
		self.GPDF = numpy.sum(a,axis=0)
		return self.GPDF

	def GPDF_show(self):
	 	"""Plot the Global PDF and shows its peaks"""

		self.GlobalPdf()
		self.GlobalPeaks()
		plt.plot(self.melodies[0].x,self.GPDF,linewidth=3,alpha=.6,label="GPDF")
		plt.plot(self.Gpeaks, self.Gpeakspdf, "ro")
		for i in range(0,len(self.Gpeaks)):
			plt.annotate(
					"%.2f" % self.Gpeaks[i],
					xy=(self.Gpeaks[i], self.Gpeakspdf[i]),
					xytext=(self.Gpeaks[i], (self.Gpeakspdf[i]+0.0001)))
		plt.legend()

	def GlobalPeaks(self):
		"""Get global peaks from Global PDF 

		"""
		c = ((numpy.diff(numpy.sign(numpy.diff(self.GPDF))) < 0).nonzero()[0] + 1)#+self.melodies[0].xmin # local max

		self.Gpeaks = self.melodies[0].x[c]
		self.Gpeakspdf = self.GPDF[c]
		c1 = numpy.array(self.Gpeaks, float)
		c2 = numpy.array(self.Gpeakspdf, float)
		c = numpy.array([c1,c2])
		c = c.transpose()
		c = c[c[:,1].argsort()]
		self.Gordredpeaks = c[::-1]

		self.GP = self.Gordredpeaks
		return self.GP

	def GlobalScale(self):
		"""Get a global scale from GlobalPeaks 

		"""
		P = self.GlobalPeaks()[:,0]
		self.Echelle = []
		for i in range(0,len(self.GP)):
			nb_ext = len(self.melodies)
			#tonique = self.melodies[nb_ext-1].tonique()[1]
			tonique = self.GetTheTonic()
			self.Echelle.append(log10(P[i]/tonique)*1000)
		return self.Echelle

	def GetTheTonic(self):
		lastonic = self.melodies[len(self.melodies)-1].tonique()[1]
		def find_nearest(array,value):
		    idx = (numpy.abs(array-value)).argmin()
		    return array[idx]
		P = self.GlobalPeaks()[:,0]
		self.TheTonic = find_nearest(P,lastonic)
		return self.TheTonic

def epi(list="No"):
	global inter
	inter = {'2/1*4/3':2/1.*4/3.,'2/1*5/4':2/1.*5/4.,'2/1*6/5':2/1.*6/5.,
	         '2/1*9/8':2/1.*9/8.,'2/1*10/9':2/1.*10/9.,'2/1*12/11':2/1.*12/11.,
	         '2/1':2/1.,'3/2*5/4':3/2.*5/4.,'3/2*6/5':3/2.*6/5.,'3/2*9/8':3/2.*9/8.,
	         '3/2*10/9':3/2.*10/9.,'3/2':3/2.,'4/3':4/3.,'5/4':5/4.,'9/8*12/11':9/8.*12/11.,
	          '6/5':6/5.,'9/8':9/8.,'10/9':10/9.,'12/11':12/11.,'1/1':1/1.,'16/15':16/15.}
	if list=="Yes":
		for i in range(0,len(inter)):
			I = numpy.float32(log10(inter.values()[i])*1000)
			print inter.keys()[i],' :: ',I, 's.'
	return inter

def Inters(Echelle):
	"""Compares scale information with defined ratios

	Input :
	-----------
		Echelle : a scale data in savarts
	"""
	
	inter = epi()
	I = inter.values()
	Int = []
	for i in range(0,len(I)):
	     Int.append(log10(I[i])*1000)
	        
	        
	Intervalles = []
	for i in range(0,len(Echelle)):
	    dist = []
	    for j in range(0,len(Int)):
	        dist.append(abs(abs(Echelle[i])-abs(Int[j])))
	    Index_Intervalle_Proche = dist.index(min(dist))
	    Nom_Intervalle_Proche = inter.keys()[dist.index(min(dist))]
	    Difference = "{:.2f}".format(min(dist))
	    #print Echelle[i],inter.values()[dist.index(min(dist))]
	    if Echelle[i]>=log10(inter.values()[dist.index(min(dist))])*1000:
	        signe = '+'
	    else: signe  = '-'
	    Intervalles.append(["{:.2f}".format(Echelle[i]),Nom_Intervalle_Proche,signe, Difference])
	return Intervalles