# -*- coding: utf-8 -*-

import arcpy
arcpy.env.overwriteOutput = True


shape = "C:\\DadosGis\\ESTUDOS\\1_PARACEL\\ANALISES\\9_SGF\\Shape\\VW_Paracel.shp"
out = "C:\\DadosGis\\ESTUDOS\\1_PARACEL\\ANALISES\\9_SGF\\Shape\\VW_Paracel_utm.shp"
projecao = arcpy.SpatialReference(31981)

#realizar a conversão para sirgas utm 21S
arcpy.management.Project(shape, out, projecao)

#adiciona campo
arcpy.management.AddField(out,'PROJTAL', 'TEXT')

arcpy.management.CalculateField(out,'PROJTAL','!ID_PROJETO!+!CD_TALHAO!')
