# -*- coding: utf-8 -*-

def index():
    form = FORM(
        INPUT(_type='submit', _value='CSV', _class='btn btn-secondary float-right'),
        _action='default/output.csv'
    )
    if request.extension == 'csv':
        return csv()
    links = [
        lambda r: A('پذیرش', _href=URL("default", "reception_section", args=[r.id_code])),
        lambda r: A('بیمار', _href=URL("default", "patient_section", args=[r.id_code])),
        lambda r: A('پزشک', _href=URL("default", "physician_section", args=[r.id_code])),
        lambda r: A('آزمایشگاه', _href=URL("default", "lab_section", args=[r.id_code])),
        lambda r: A('ژنها 1 تا 10', _href=URL("default", "genes_1_10", args=[r.id_code])),
        lambda r: A('ژنها 11 تا 20', _href=URL("default", "genes_11_20", args=[r.id_code])),
        lambda r: A('ژنها 21 تا 30', _href=URL("default", "genes_21_30", args=[r.id_code])),
        lambda r: A('ژنها 31 تا 40', _href=URL("default", "genes_31_40", args=[r.id_code])),
        lambda r: A('ژنها 41 تا 50', _href=URL("default", "genes_41_50", args=[r.id_code])),
        lambda r: A('ژنها 51 تا 60', _href=URL("default", "genes_51_60", args=[r.id_code])),
        lambda r: A('ژنها 61 تا 70', _href=URL("default", "genes_61_70", args=[r.id_code])),
        lambda r: A('ژنها 71 تا 80', _href=URL("default", "genes_71_80", args=[r.id_code])),
        lambda r: A('ژنها 81 تا 90', _href=URL("default", "genes_81_90", args=[r.id_code])),
        lambda r: A('ژنها 91 تا 100', _href=URL("default", "genes_91_100", args=[r.id_code])),
        ]
    grid = SQLFORM.grid(
        db.principal_info,
        advanced_search = False,
        #deletable=False,
        csv=False,
        user_signature = False,
        links = links,
        )

    return locals()

def reception_section():
    tbl = db.reception_section
    #record = tbl(request.args(0))
    record = db(tbl.id_code==request.args(0)).select().first()
    form = SQLFORM(tbl,record)
    form.vars.id_code = request.args(0)
    if form.process().accepted:
        #response.flash("Success") 
        msg = 'success'
        redirect(URL("default", "index"))
    elif form.errors: 
        msg = form.errors 
        #response.flash("Error")
    return locals()


def patient_section():
    tbl = db.patient_section
    record = db(tbl.id_code==request.args(0)).select().first()
    tbl.id.readable = False
    form = SQLFORM(tbl,record)
    form.vars.id_code = request.args(0)
    if form.process().accepted:
        #response.flash("Success") 
        msg = 'success'
        redirect(URL("default", "index"))
    elif form.errors: 
        msg = form.errors 
        #response.flash("Error")       
    return locals()    


def physician_section():
    tbl = db.physician_section
    record = db(tbl.id_code==request.args(0)).select().first()
    tbl.id.readable = False
    form = SQLFORM(tbl,record)
    form.vars.id_code = request.args(0)
    if form.process().accepted:
        #response.flash("Success") 
        msg = 'success'
        redirect(URL("default", "index"))
    elif form.errors: 
        msg = form.errors 
        #response.flash("Error")     
    return locals()        


def lab_section():
    tbl = db.lab_section
    record = db(tbl.id_code==request.args(0)).select().first()
    tbl.id.readable = False
    form = SQLFORM(tbl,record)
    form.vars.id_code = request.args(0)
    if form.process().accepted:
        #response.flash("Success") 
        msg = 'success'
        redirect(URL("default", "index"))
    elif form.errors: 
        msg = form.errors 
        #response.flash("Error")    
    return locals() 


def genes_1_10():
    tbl = db.genes_1_10
    record = db(tbl.id_code==request.args(0)).select().first()
    tbl.id.readable = False
    form = SQLFORM(tbl,record)
    form.vars.id_code = request.args(0)
    if form.process().accepted:
        #response.flash("Success") 
        msg = 'success'
        redirect(URL("default", "index"))
    elif form.errors: 
        msg = form.errors 
        #response.flash("Error")    
    return locals() 


def genes_11_20():
    tbl = db.genes_11_20
    record = db(tbl.id_code==request.args(0)).select().first()
    tbl.id.readable = False
    form = SQLFORM(tbl,record)
    form.vars.id_code = request.args(0)
    if form.process().accepted:
        #response.flash("Success") 
        msg = 'success'
        redirect(URL("default", "index"))
    elif form.errors: 
        msg = form.errors 
        #response.flash("Error")    
    return locals() 


def genes_21_30():
    tbl = db.genes_21_30
    record = db(tbl.id_code==request.args(0)).select().first()
    tbl.id.readable = False
    form = SQLFORM(tbl,record)
    form.vars.id_code = request.args(0)
    if form.process().accepted:
        #response.flash("Success") 
        msg = 'success'
        redirect(URL("default", "index"))
    elif form.errors: 
        msg = form.errors 
        #response.flash("Error")    
    return locals() 


def genes_31_40():
    tbl = db.genes_31_40
    record = db(tbl.id_code==request.args(0)).select().first()
    tbl.id.readable = False
    form = SQLFORM(tbl,record)
    form.vars.id_code = request.args(0)
    if form.process().accepted:
        #response.flash("Success") 
        msg = 'success'
        redirect(URL("default", "index"))
    elif form.errors: 
        msg = form.errors 
        #response.flash("Error")    
    return locals() 


def genes_41_50():
    tbl = db.genes_41_50
    record = db(tbl.id_code==request.args(0)).select().first()
    tbl.id.readable = False
    form = SQLFORM(tbl,record)
    form.vars.id_code = request.args(0)
    if form.process().accepted:
        #response.flash("Success") 
        msg = 'success'
        redirect(URL("default", "index"))
    elif form.errors: 
        msg = form.errors 
        #response.flash("Error")    
    return locals() 


def genes_51_60():
    tbl = db.genes_51_60
    record = db(tbl.id_code==request.args(0)).select().first()
    tbl.id.readable = False
    form = SQLFORM(tbl,record)
    form.vars.id_code = request.args(0)
    if form.process().accepted:
        #response.flash("Success") 
        msg = 'success'
        redirect(URL("default", "index"))
    elif form.errors: 
        msg = form.errors 
        #response.flash("Error")    
    return locals() 


def genes_61_70():
    tbl = db.genes_61_70
    record = db(tbl.id_code==request.args(0)).select().first()
    tbl.id.readable = False
    form = SQLFORM(tbl,record)
    form.vars.id_code = request.args(0)
    if form.process().accepted:
        #response.flash("Success") 
        msg = 'success'
        redirect(URL("default", "index"))
    elif form.errors: 
        msg = form.errors 
        #response.flash("Error")    
    return locals() 


def genes_71_80():
    tbl = db.genes_71_80
    record = db(tbl.id_code==request.args(0)).select().first()
    tbl.id.readable = False
    form = SQLFORM(tbl,record)
    form.vars.id_code = request.args(0)
    if form.process().accepted:
        #response.flash("Success") 
        msg = 'success'
        redirect(URL("default", "index"))
    elif form.errors: 
        msg = form.errors 
        #response.flash("Error")    
    return locals() 


def genes_81_90():
    tbl = db.genes_81_90
    record = db(tbl.id_code==request.args(0)).select().first()
    tbl.id.readable = False
    form = SQLFORM(tbl,record)
    form.vars.id_code = request.args(0)
    if form.process().accepted:
        #response.flash("Success") 
        msg = 'success'
        redirect(URL("default", "index"))
    elif form.errors: 
        msg = form.errors 
        #response.flash("Error")    
    return locals() 

def genes_91_100():
    tbl = db.genes_91_100
    record = db(tbl.id_code==request.args(0)).select().first()
    tbl.id.readable = False
    form = SQLFORM(tbl,record)
    form.vars.id_code = request.args(0)
    if form.process().accepted:
        #response.flash("Success") 
        msg = 'success'
        redirect(URL("default", "index"))
    elif form.errors: 
        msg = form.errors 
        #response.flash("Error")    
    return locals() 


def output():
    from os import path
    data = ''

    tables = [
        (db.principal_info,1),
        (db.reception_section,2),
        (db.patient_section,2),
        (db.physician_section,2),
        (db.lab_section,2),
        (db.genes_1_10,2),
        (db.genes_11_20,2),
        (db.genes_21_30,2),
        (db.genes_31_40,2),
        (db.genes_41_50,2),
        (db.genes_51_60,2),
        (db.genes_61_70,2),
        (db.genes_71_80,2),
        (db.genes_81_90,2),
        (db.genes_91_100,2),
        ]

    field_name = [t[0].fields[t[1]:] for t in tables]
    labels = [[f.label for f in t[0]][t[1]:] for t in tables]
    header = ','.join([','.join(l) for l in labels])
    data += header

    for p in db(tables[0][0]).select():
        rec = []
        id_code = p.get('id_code')
        for t in range(len(tables)):
            r = db(tables[t][0].id_code == id_code).select().first()
            for f in field_name[t]:
                if r:
                    v = r.get(f, '')
                    rec.append('' if v == None else str(v))
                else:
                    rec.append('')
        data += ('\n' + ','.join(rec))
    return data