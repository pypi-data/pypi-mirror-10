=================================================
Diastema: Musical intervals and modality analysis
=================================================

Overview
========

**Diastema**, is a project to analyse musical modality. It uses Python2.

For now, it's main features are :

* Fondamental frequencies extraction (using *PredominentMelody()* from **Essentia**);
* Getting the main frequencies as peaks of the probability density function from frequencies;
* Comparing PDFs using a correlation coefficient;
* Getting a similarity matrix between melodies.

Installation
============

First, you need to install manually **Essentia** (http://essentia.upf.edu/).

Then, install Diastema with the following :

.. code:: python

	git clone https://github.com/AnasGhrab/diastema
	python setup.py install


Usage
=====

To use Diastema :

.. code:: python

	from diastema import *
	path = "path/to/a/folder/with/audios/wav/files/"
	Music = Melodies(path)
	
Then you can

.. code:: python

	Music.PdfsPlot()
	Music.Simatrix()
		
Contact
=======

Homepage: http://anas.ghrab.tn

Email:

 * Anas Ghrab <anas.ghrab@gmail.com>

License
=======

The MIT License (MIT)

Copyright (c) 2015 Anas Ghrab

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

