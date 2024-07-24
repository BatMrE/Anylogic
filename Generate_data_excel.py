# Main file

excelOutputFile.writeDataSet(datasetXSamples, 1, 2, 1);
excelOutputFile.writeDataSet(datasetYSamples, 1, 2, 3);


# Multiple cols

excelOutputFile.setCellValue("X", 1, 1, 2);
excelOutputFile.writeDataSet(datasetXSamples, 1, 2, 1);
excelOutputFile.setCellValue("Y", 1, 1, 4);
excelOutputFile.writeDataSet(datasetYSamples, 1, 2, 3);
excelOutputFile.setCellValue("fcPrevTime", 1, 1, 6);
excelOutputFile.writeDataSet(dataset_fcPrevTime, 1, 2, 5);
