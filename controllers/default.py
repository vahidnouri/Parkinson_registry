# -*- coding: utf-8 -*-



import sys
reload(sys)
sys.setdefaultencoding('utf-8') 
from cStringIO import StringIO
import csv


#import pandas as pd
ui = dict(widget='',
          header='',
          content='',
          default='',
          cornerall='',
          cornertop='',
          cornerbottom='',
          button='button btn btn-default',
          buttontext='buttontext button',
          #buttonadd='icon plus icon-plus glyphicon glyphicon-plus',
          #buttonback='icon leftarrow icon-arrow-left glyphicon glyphicon-arrow-left',
          #buttonexport='icon downarrow icon-download glyphicon glyphicon-download',
          #buttondelete='icon trash icon-trash glyphicon glyphicon-trash',
          #buttonedit='icon pen icon-pencil glyphicon glyphicon-arrow-pencil',
          #buttontable='icon rightarrow icon-arrow-right glyphicon glyphicon-arrow-right',
          #buttonview='icon magnifier icon-zoom-in glyphicon glyphicon-arrow-zoom-in',
          )

  


class CSVExporter(object):

    file_ext = "csv"
    content_type = "text/csv"

    def __init__(self, rows):
        self.rows = rows
 

    def export(self):
        if self.rows:
            s = StringIO()
            
            csv_writer = csv.writer(s)
            #form = SQLFORM(db.people)
            #col = []
            #for f in form.fields:
            #    col.append(form.custom.label[f])
            col = self.rows.colnames    
            
            
                
            heading = [c.split('.')[-1].upper() for c in col]
            csv_writer.writerow(heading)
            self.rows.export_to_csv_file(s, represent=True, write_colnames=False)
            return s.getvalue()
        else:
            return ''

def index():
    grid = SQLFORM.grid(db.people,
        #fields=[db.people.f_name,db.people.id_code,],
        advanced_search = False,
        user_signature = False,
        csv = True,
        #showbuttontext = False,
        exportclasses=dict(csv=(CSVExporter, 'CSV')),
        #ui = ui,
    )
    return locals()
"""
def download():
    form = FORM(INPUT(_type='submit', _value='download'), _action='download.csv')
    if request.extension == 'csv':
        return get_csv()
    return locals()


def get_csv():
    import xlwt 
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Python Sheet 1") 
    #sheet1.write(0, 0, "This is the First Cell of the First Sheet") 
    #book.save("spreadsheet.csv")
    form = SQLFORM(db.people)
    record = 2
    for num in range(record):
        row = sheet1.row(num)
        for field in form.fields:
            value = form.custom.label[field]
        #for index,col in form:
        #    value = txt[index]
            row.write(field, value)
    #s = 'سلام'
    #sheet1.write(0,0,s)
    book.save("spreadsheet.csv")
    #for c in s :
    #s = s.replace(c, replacements[c])


    return s.encode('utf8')


"""
