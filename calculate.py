# -*- coding: utf-8 -*-

import arcpy

Linhas = "Linhas"
exp = "grau1 = u'0º - 16º'\\n  classe1 = grau1.encode('iso-8859-1').decode('utf-8')\\n  if x == '1':\\n    return classe1\\n  else:\\n    return 'Zero'"
arcpy.CalculateField_management(Linhas,"Classif", "cal(!teste!)", "PYTHON_9.3", "def cal(x):\\n  "+exp)



