Twid includes simple functions about Taiwan Identification Card system.
See also: http://en.wikipedia.org/wiki/National_Identification_Card_%28Republic_of_China%29

Quick Start
^^^^^^^^^^^
::

 >>> from twid import female, male, kaohsiung
 >>> female()
 'X249592708'
 >>> kaohsiung()
 'E168646609'
 >>> kaohsiung(male())
 'E167853593'
