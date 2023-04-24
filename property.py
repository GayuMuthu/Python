import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table
from reportlab.lib.pagesizes import letter
import os
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm

inputFile = pd.read_csv("C:\\Users\\Gayathiri\\Desktop\\Work\\April\\24_4_23\\ManageProperty.csv");

groupLocation = inputFile.groupby(['Location']);
Avg_SqFt = groupLocation.agg({"Price": "mean", "SquareFt": "mean"}).reset_index();
groupProperty = inputFile.groupby(['PropertyType']);
Avg_BedroomBathroom = groupProperty.agg({"Bedrooms": "mean", "Bathrooms": "mean"}).reset_index();

print(Avg_SqFt);
print(Avg_BedroomBathroom);

output = inputFile.groupby(['Location', 'PropertyType']);

propertyData = output.agg({"Price": "mean", "SquareFt": "mean", "Bedrooms": "mean", 
                  "Bathrooms": "mean"}).reset_index();

data = [];

data.append(list(Avg_SqFt.columns))
for index, row in Avg_SqFt.iterrows():
    data.append(row);
data.append(" ");

data.append(list(Avg_BedroomBathroom.columns))
for index, row in Avg_BedroomBathroom.iterrows():
    data.append(row);
data.append(" ");

data.append(list(propertyData.columns))
for index, row in propertyData.iterrows():
    data.append(row);
data.append(" ");

data.append(" ");
def onFirstPage(canvas, document):
    canvas.drawCentredString(270, 750, 'Manage Property')
data.append(" ");

pdf = SimpleDocTemplate("C:\\Users\\Gayathiri\\Desktop\\Work\\April\\24_4_23\\ManageProperty.pdf",
    pagesize = letter);

propertyDataTable= Table(data);
propertyDataList =[];
propertyDataList.append(propertyDataTable);

pdf.build(propertyDataList, onFirstPage=onFirstPage,onLaterPages=onFirstPage);