# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# AppConfig configuration made easy. Look inside private/appconfig.ini
# Auth is for authenticaiton and access control
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires web2py 2.15.5 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
configuration = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(configuration.get('db.uri'),
             pool_size=configuration.get('db.pool_size'),
             migrate_enabled=configuration.get('db.migrate'),
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = [] 
if request.is_local and not configuration.get('app.production'):
    response.generic_patterns.append('*')

# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = 'bootstrap4_inline'
response.form_label_separator = ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=configuration.get('host.names'))

# -------------------------------------------------------------------------
# create all tables needed by auth, maybe add a list of extra fields
# -------------------------------------------------------------------------
auth.settings.expiration = 3600 * 8  # seconds

auth.settings.extra_fields['auth_user'] = [
    Field("reception", type="boolean"),
    Field("patient", type="boolean"),
    Field("physician", type="boolean"),
    Field("lab", type="boolean"),
    Field("genes", type="boolean"),
    Field("admin_", type="boolean"),
]
auth.define_tables( migrate=False )
auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else configuration.get('smtp.server')
mail.settings.sender = configuration.get('smtp.sender')
mail.settings.login = configuration.get('smtp.login')
mail.settings.tls = configuration.get('smtp.tls') or False
mail.settings.ssl = configuration.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = True
auth.settings.registration_requires_approval = True
auth.settings.reset_password_requires_verification = False

# -------------------------------------------------------------------------  
# read more at http://dev.w3.org/html5/markup/meta.name.html               
# -------------------------------------------------------------------------
response.meta.author = configuration.get('app.author')
response.meta.description = configuration.get('app.description')
response.meta.keywords = configuration.get('app.keywords')
response.meta.generator = configuration.get('app.generator')
response.show_toolbar = configuration.get('app.toolbar')

# -------------------------------------------------------------------------
# your http://google.com/analytics id                                      
# -------------------------------------------------------------------------
response.google_analytics_id = configuration.get('google.analytics_id')

# -------------------------------------------------------------------------
# maybe use the scheduler
# -------------------------------------------------------------------------
if configuration.get('scheduler.enabled'):
    from gluon.scheduler import Scheduler
    scheduler = Scheduler(db, heartbeat=configuration.get('scheduler.heartbeat'))

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)

genders = ["","مرد","زن"]
yes_no = ["","بلی","خیر"]
off_on = ["","Off","On"]
after_before = ["","قبل از 6 عصر","بعد از 6 عصر"]
yes_no_none = ["","بلی","خیر","چیزی تعریف نمی کند"]
yes_no_no_one = ["","بلی","خیر","همبستر ندارد"]
life_conditions = ["","1.تنها","2.با خانواده","3. پرستار در منزل","4. مرکز نگهداری"]
job_conditions = ["","آفت کش و سموم مورد استفاده کشاورزی","حلالهای شیمیایی","ترومای سر","سایر"]
fab_score = ["","0","1","2","3"]
sleep_times = ["","1-10","11-20","بیشتر از 20"]
blood_type = ["","EDTA","Heparin","سایر"]
treat_scores = ["","1.فیزیوتراپی","2.کار درمانی","3.گفتار درمانی"]
counsiousness = [""] + [i for i in range(11)]
info_score = ["","Patient","Caregiver","Patient+Caregiver"]
#str(list(range(0,11)))
#counsiousness = ["0","1","2","3","4","5","6","7","8","9","10"]
gait = [""] +[i for i in range(5)]
hoehn = [""] +[i for i in range(6)]
moca1 = ["","0","1","2","3","4","5"]
moca3 = ["","0","1","2"]
moca4 = ["","0","1"]
moca10 = ["","0","1","2","3","4","5","6"]
bai = ["","0","1","2","3"]
mschwab = ["","0","10","20","30","40","50","60","70","80","90","100"]
edu_list = ["","بی سواد","ابتدایی","سیکل","دیپلم","فوق دیپلم","لیسانس","فوق لیسانس و بالاتر"]

genes = []
for i in range(1,101):
    genes.append(Field("gene_{}".format(i),"string",label="ژن {}".format(i)))
    for j in range(1,11):
        genes.append(Field("variant_{}_gene{}".format(j,i),"string",label="ژن {} واریانت {}".format(i,j)))

#f = [


########## Lab Table

#    ]

# f += genes


db.define_table("principal_info",
    Field("f_name", "string",label="نام و نام خانوادگی"),
    Field("id_code", "string",label="کدملی", required=True),
    migrate = False,
    fake_migrate=False,
    )
db.principal_info.id_code.requires=IS_NOT_IN_DB(db,'principal_info.id_code')    
# -----------------------Reception Section ------------------------------

db.define_table("reception_section", 
#    Field("f_name", "string",label="نام و نام خانوادگی"),
    Field("id_code", "string",label="کدملی", writable=False, readable = False),
    Field("address", "text",label="محل سکونت"),
    Field("tel", "string",label="تلفن"),
    Field("e_mail", "string",label="ایمیل"),
    Field("insurance_type", "string",label="نوع بیمه"),
    Field("visit_data_day", "string",label="روز ویزیت"),
    Field("visit_data_month", "string",label="ماه ویزیت"),
    Field("visit_data_year", "string",label="سال ویزیت"),
    Field("doctor_name", "string",label="نام پزشک"),
    Field("birth_date_day", "string",label="روز تولد"),
    Field("birth_date_month", "string",label="ماه تولد"),
    Field("birth_date_year", "string",label="سال تولد"),
    Field("gender", requires=IS_IN_SET(genders, zero=None),label="جنسیت"),
    Field("education", requires=IS_IN_SET(edu_list, zero=None),label="تعداد سالهای تحصیل رسمی"),
    Field("career", "string",label="شغل"),
    Field("income", "string",label="درآمد ماهیانه"),
    #Field("sickness_start_day", "string",label="روز شروع بیماری"),
    #Field("sickness_start_month", "string",label="ماه شروع بیماری"),
    Field("sickness_start_year", "string",label="سال شروع بیماری"),
    Field("visit_number", "string",label="تعداد ویزیت در سال بعلت بیماری پارکینسون"),
    Field("family_records", requires=IS_IN_SET(yes_no, zero=None),label="1.سابقه فامیلی پدر و مادر"),
    Field("sibiling_numbers", "string",label="2.تعداد خواهر و برادر"),
    Field("children_numbers", "string",label="3.تعداد فرزندان"),
    Field("fr_4_1", requires=IS_IN_SET(yes_no, zero=None),label="4.فامیل درجه اول مبتلا به بیماری پارکینسون "),
    Field("fr_4_2", "string",label="4.سن شروع"),
    Field("fr_5_1", requires=IS_IN_SET(yes_no, zero=None),label="5.فامیل درجه دوم  مبتلا به بیماری پارکینسون "),
    Field("fr_5_2", "string",label="5.سن شروع"),
    Field("fr_6_1", requires=IS_IN_SET(yes_no, zero=None),label="6.فامیل درجه سوم مبتلا به بیماری پارکینسون  "),
    Field("fr_6_2", "string",label="6.سن شروع"),
    Field("fr_7_1", requires=IS_IN_SET(yes_no, zero=None),label="7.فامیل درجه اول مبتلا به بیماری حرکتی "),
    Field("fr_7_2", "string",label="7.سن شروع"),
    Field("fr_8_1", requires=IS_IN_SET(yes_no, zero=None),label="8.فامیل درجه دوم  مبتلا به بیماری حرکتی "),
    Field("fr_8_2", "string",label="8.سن شروع"),
    Field("fr_9_1", requires=IS_IN_SET(yes_no, zero=None),label="9.فامیل درجه سوم مبتلا به بیماری حرکتی "),
    Field("fr_9_2", "string",label="9.سن شروع"),
    Field("fr_10_1", requires=IS_IN_SET(yes_no, zero=None),label="10.فامیل درجه اول مبتلا به بیماری ذهنی "),
    Field("fr_10_2", "string",label="10.سن شروع"),
    Field("fr_11_1", requires=IS_IN_SET(yes_no, zero=None),label="11.فامیل درجه دوم مبتلا به بیماری ذهنی"),
    Field("fr_11_2", "string",label="11.سن شروع"),
    Field("fr_12_1", requires=IS_IN_SET(yes_no, zero=None),label="12.فامیل درجه سوم مبتلا به بیماری ذهنی"),
    Field("fr_12_2", "string",label="12.سن شروع"),
    Field("fr_13_1", requires=IS_IN_SET(yes_no, zero=None),label="13.بیماری پارکینسون در سایر بستگان "),
    Field("fr_13_2", "string",label="13.سن شروع"),
    Field("fr_13_3", "string",label="13.نسبت فرد مبتلا"),
    Field("fr_14_1", requires=IS_IN_SET(yes_no, zero=None),label="14.سایر بیماریهای نوروژنتیک در بستگان درجه اول  "),
    Field("fr_14_2", "string",label="14.سن شروع"),
    Field("fr_14_3", "string",label="14.نسبت فرد مبتلا"),
    Field("fr_15_1", requires=IS_IN_SET(yes_no, zero=None),label="15.سایر بیماریهای نوروژنتیک در بستگان درجه دوم "),
    Field("fr_15_2", "string",label="15.سن شروع"),
    Field("fr_15_3", "string",label="15.نسبت فرد مبتلا"),
    Field("fr_16_1", requires=IS_IN_SET(yes_no, zero=None),label="16.سایر بیماریهای نوروژنتیک در بستگان درجه سوم "),
    Field("fr_16_2", "string",label="16.سن شروع"),
    Field("fr_16_3", "string",label="16.نسبت فرد مبتلا"),
    Field("fr_17", requires=IS_IN_SET(yes_no, zero=None),label="سابقه ثبت یکی از بستگان در این رجیستری"),
    Field("check_id_code", "string",label="کد ملی"),
    Field("check_name", "string",label="نام و نام خانوادگی"),
    Field("ped_draw_path", "string",label="مسیر عکس شجره"),
    
    Field("sr_cigar", requires=IS_IN_SET(yes_no, zero=None),label="سیگار"),
    Field("sr_cof", requires=IS_IN_SET(yes_no, zero=None),label="کافئین"),
    Field("sr_alc", requires=IS_IN_SET(yes_no, zero=None),label="الکل"),
    Field("sr_op", requires=IS_IN_SET(yes_no, zero=None),label="اپیوم"),
    Field("sr_others", "string",label="سایر مواد اعتیاد آور"),
    Field("sr_conditions", requires=IS_IN_SET(life_conditions, zero=None),label="شرایط زندگی"),
    Field("sr_jobc",requires=IS_IN_SET(job_conditions, zero=None) ,label="مواجهه شغلی"),
    Field("other_fields", "string",label="سایر موارد"),


    Field("phy_others", "text",label="سابقه بیماری های دیگر"),
    Field("phy_hospital", "text",label="سابقه بستری"),
    Field("phy_surgery", "text",label="اعمال جراحی"),
    migrate = False,
)

#-------------------- Patient Section -------------------------------

db.define_table("patient_section",
    Field("id_code", "string",label="کدملی", writable=False, readable = False),
    #Field("updr", "string",label="UPDRS"),
    Field("mse", requires=IS_IN_SET(mschwab, zero=None),label= "Schwab معیار فعالیت های روزانه "),
    Field("eq", "string",label= "EQ-5D5L کیفیت زندگی"),
    Field("epworth", "string",label="Epworth معیار خواب"),

    #Field("partner_sleep","string",label=" خواب شریک زندگی"),   
    Field("partner_sleep_1", requires=IS_IN_SET(yes_no, zero=None),label="1.آیا فرد بیمار در خواب با صدای بلند خر و پف میکند؟"),
    Field("partner_sleep_2", requires=IS_IN_SET(yes_no, zero=None),label="2.آیا میزان خر و پف فرد بیمار به میزانی می باشد که شما را از خواب بیدار کند؟"),
    Field("partner_sleep_3", requires=IS_IN_SET(yes_no, zero=None),label="3.آیا میزان صدا به حدی بوده است که شما مجبور باشید برای خواب به اتاق دیگری بروید؟"),
    Field("partner_sleep_4", requires=IS_IN_SET(yes_no, zero=None),label="4.آیا خر و پف فرد بیمار در صورت انسداد بینی ( به عنوان مثال سرماخوردگی) بد تر می شود؟"),
    Field("partner_sleep_5", requires=IS_IN_SET(yes_no, zero=None),label="5.آیا فرد بیمار در هنگام خواب دچار توقف تنفس می شود؟"),
    Field("partner_sleep_5_1", requires=IS_IN_SET(sleep_times, zero=None),label="چند بار در شب اتفاق می افتد؟ "),
    Field("partner_sleep_6", requires=IS_IN_SET(yes_no, zero=None),label="6.آیا تا کنون فرد بیمار را برای اطمینان از سلامت او، از خواب بیدار کرده اید؟"),
    Field("partner_sleep_7", requires=IS_IN_SET(yes_no, zero=None),label="7.آیا فرد بیمار در هنگام خواب بسیار بی قرار می باشد؟"),
    Field("partner_sleep_8", requires=IS_IN_SET(yes_no, zero=None),label="8.آیا شخصیت فرد بیمار اخیرا دچار تغییر شده است؟"),
    Field("partner_sleep_8_1","text",label="8.1.توضیح"),
    Field("partner_sleep_9", requires=IS_IN_SET(yes_no, zero=None),label="9.آیا فرد بیمار در طول روز به راحتی به خواب میرود؟"),
    Field("partner_sleep_9_1", requires=IS_IN_SET(yes_no, zero=None),label="9.1.آیا در هنگام رانندگی این اتفاق رخ داده است؟"),
    Field("msq_1_1", requires=IS_IN_SET(yes_no, zero=None),label="آیا شما همراه بیمار زندگی می کنید؟"),
    Field("msq_1_2", requires=IS_IN_SET(yes_no, zero=None),label="آیا شما در اتاق مشترک با بیمار می خوابید؟"),
    Field("msq_1_3", requires=IS_IN_SET(yes_no, zero=None),label="آیا بعلت رفتارهای نامناسب وی حین خواب است؟"),
    
    Field("rbd_1", requires=IS_IN_SET(yes_no, zero=None),label="RBD 1."),
    Field("rbd_1_a","string",label="RBD 1. تعداد ماه .الف"),
    Field("rbd_1_b", requires=IS_IN_SET(yes_no, zero=None),label="RBD 1.ب"),
    Field("rbd_1_c", requires=IS_IN_SET(yes_no_no_one, zero=None),label="RBD 1.ج"),
    Field("rbd_1_d", requires=IS_IN_SET(yes_no_none, zero=None),label="RBD 1.د"),
    Field("rbd_1_e", requires=IS_IN_SET(yes_no_none, zero=None),label="RBD 1.ه"),
    Field("plms_2", requires=IS_IN_SET(yes_no, zero=None),label="PLMS 2."),
    Field("rls_3", requires=IS_IN_SET(yes_no, zero=None),label="RLS 3."),
    Field("rls_3_a", requires=IS_IN_SET(yes_no, zero=None),label="RLS 3.الف"),
    Field("rls_3_b", requires=IS_IN_SET(after_before, zero=None),label="RLS 3.ب"),
    Field("sw_4", requires=IS_IN_SET(yes_no, zero=None),label="SW 4."),
    Field("osa_5", requires=IS_IN_SET(yes_no, zero=None),label="OSA 5."),
    Field("osa_6", requires=IS_IN_SET(yes_no, zero=None),label="OSA 6."),
    Field("osa_6_a", requires=IS_IN_SET(yes_no, zero=None),label="OSA 6.الف"),
    Field("srlc_7", requires=IS_IN_SET(yes_no, zero=None),label="SRLC 7."),
    Field("insomnia_8", requires=IS_IN_SET(counsiousness, zero=None),label=" Alertness 8."),
    
    Field("b_1_1", requires=IS_IN_SET(gait, zero=None),label="B.1.1"),
    Field("b_1_2", requires=IS_IN_SET(gait, zero=None),label="B.1.2"),
    Field("b_1_3", requires=IS_IN_SET(gait, zero=None),label="B.1.3"),
    Field("b_1_4", requires=IS_IN_SET(gait, zero=None),label="B.1.4"),
    Field("b_1_5", requires=IS_IN_SET(gait, zero=None),label="B.1.5"),
    Field("b_1_6", requires=IS_IN_SET(gait, zero=None),label="B.1.6"),

    Field("freezing_total", 'integer', label="Freezing of gait total"),
    #Field("nms_part","string",label=" NMS پرسشنامه"), 
    Field("nms_1", requires=IS_IN_SET(yes_no, zero=None),label="NMS 1."),
    Field("nms_2", requires=IS_IN_SET(yes_no, zero=None),label="NMS 2."),
    Field("nms_3", requires=IS_IN_SET(yes_no, zero=None),label="NMS 3."),
    Field("nms_4", requires=IS_IN_SET(yes_no, zero=None),label="NMS 4."),
    Field("nms_5", requires=IS_IN_SET(yes_no, zero=None),label="NMS 5."),
    Field("nms_6", requires=IS_IN_SET(yes_no, zero=None),label="NMS 6."),
    Field("nms_7", requires=IS_IN_SET(yes_no, zero=None),label="NMS 7."),
    Field("nms_8", requires=IS_IN_SET(yes_no, zero=None),label="NMS 8."),
    Field("nms_9", requires=IS_IN_SET(yes_no, zero=None),label="NMS 9."),
    Field("nms_10", requires=IS_IN_SET(yes_no, zero=None),label="NMS 10."),
    Field("nms_11", requires=IS_IN_SET(yes_no, zero=None),label="NMS 11."),
    Field("nms_12", requires=IS_IN_SET(yes_no, zero=None),label="NMS 12."),
    Field("nms_13", requires=IS_IN_SET(yes_no, zero=None),label="NMS 13."),
    Field("nms_14", requires=IS_IN_SET(yes_no, zero=None),label="NMS 14."),
    Field("nms_15", requires=IS_IN_SET(yes_no, zero=None),label="NMS 15."),
    Field("nms_16", requires=IS_IN_SET(yes_no, zero=None),label="NMS 16."),
    Field("nms_17", requires=IS_IN_SET(yes_no, zero=None),label="NMS 17."),
    Field("nms_18", requires=IS_IN_SET(yes_no, zero=None),label="NMS 18."),
    Field("nms_19", requires=IS_IN_SET(yes_no, zero=None),label="NMS 19."),
    Field("nms_20", requires=IS_IN_SET(yes_no, zero=None),label="NMS 20."),
    Field("nms_21", requires=IS_IN_SET(yes_no, zero=None),label="NMS 21."),
    Field("nms_22", requires=IS_IN_SET(yes_no, zero=None),label="NMS 22."),
    Field("nms_23", requires=IS_IN_SET(yes_no, zero=None),label="NMS 23."),
    Field("nms_24", requires=IS_IN_SET(yes_no, zero=None),label="NMS 24."),
    Field("nms_25", requires=IS_IN_SET(yes_no, zero=None),label="NMS 25."),
    Field("nms_26", requires=IS_IN_SET(yes_no, zero=None),label="NMS 26."),
    Field("nms_27", requires=IS_IN_SET(yes_no, zero=None),label="NMS 27."),
    Field("nms_28", requires=IS_IN_SET(yes_no, zero=None),label="NMS 28."),
    Field("nms_29", requires=IS_IN_SET(yes_no, zero=None),label="NMS 29."),
    Field("nms_30", requires=IS_IN_SET(yes_no, zero=None),label="NMS 30."),

    #Field("quip_label","string",label=" Quip-any time During PD-Full"),    
    Field("qdpd_full_a_1_1", requires=IS_IN_SET(yes_no, zero=None),label="A 1.1 "),
    Field("qdpd_full_a_1_2", requires=IS_IN_SET(yes_no, zero=None),label="A 1.2 "),
    Field("qdpd_full_a_1_3", requires=IS_IN_SET(yes_no, zero=None),label="A 1.3 "),
    Field("qdpd_full_a_1_4", requires=IS_IN_SET(yes_no, zero=None),label="A 1.4 "),
    Field("qdpd_full_a_2_1", requires=IS_IN_SET(yes_no, zero=None),label="A 2.1 "),
    Field("qdpd_full_a_2_2", requires=IS_IN_SET(yes_no, zero=None),label="A 2.2 "),    
    Field("qdpd_full_a_2_3", requires=IS_IN_SET(yes_no, zero=None),label="A 2.3 "),    
    Field("qdpd_full_a_2_4", requires=IS_IN_SET(yes_no, zero=None),label="A 2.4 "),    
    Field("qdpd_full_a_3_1", requires=IS_IN_SET(yes_no, zero=None),label="A 3.1 "),    
    Field("qdpd_full_a_3_2", requires=IS_IN_SET(yes_no, zero=None),label="A 3.2 "),    
    Field("qdpd_full_a_3_3", requires=IS_IN_SET(yes_no, zero=None),label="A 3.3 "),    
    Field("qdpd_full_a_3_4", requires=IS_IN_SET(yes_no, zero=None),label="A 3.4 "),    
    Field("qdpd_full_a_4_1", requires=IS_IN_SET(yes_no, zero=None),label="A 4.1 "),    
    Field("qdpd_full_a_4_2", requires=IS_IN_SET(yes_no, zero=None),label="A 4.2 "),    
    Field("qdpd_full_a_4_3", requires=IS_IN_SET(yes_no, zero=None),label="A 4.3 "),    
    Field("qdpd_full_a_4_4", requires=IS_IN_SET(yes_no, zero=None),label="A 4.4 "),    
    Field("qdpd_full_a_5_1", requires=IS_IN_SET(yes_no, zero=None),label="A 5.1 "),    
    Field("qdpd_full_a_5_2", requires=IS_IN_SET(yes_no, zero=None),label="A 5.2 "),    
    Field("qdpd_full_a_5_3", requires=IS_IN_SET(yes_no, zero=None),label="A 5.3 "),    
    Field("qdpd_full_a_5_4", requires=IS_IN_SET(yes_no, zero=None),label="A 5.4 "),    
    Field("qdpd_full_b_1_1", requires=IS_IN_SET(yes_no, zero=None),label="B 1.1 "),
    Field("qdpd_full_b_1_2", requires=IS_IN_SET(yes_no, zero=None),label="B 1.2 "),
    Field("qdpd_full_b_1_3", requires=IS_IN_SET(yes_no, zero=None),label="B 1.3 "),
    Field("qdpd_full_b_2", requires=IS_IN_SET(yes_no, zero=None),label="B 2. "),
    Field("qdpd_full_b_3", requires=IS_IN_SET(yes_no, zero=None),label="B 3. "),
    Field("qdpd_full_c_1", requires=IS_IN_SET(yes_no, zero=None),label="C 1. "),
    Field("qdpd_full_c_2", requires=IS_IN_SET(yes_no, zero=None),label="C 2. "),
    Field("qdpd_full_c_3", requires=IS_IN_SET(yes_no, zero=None),label="C 3. "),
    Field("qdpd_full_c_4", requires=IS_IN_SET(yes_no, zero=None),label=" C 4. "),
    Field("qdpd_full_c_5", requires=IS_IN_SET(yes_no, zero=None),label="C 5. "),

    Field("bai_1", requires=IS_IN_SET(bai, zero=None),label="BAI 1."),
    Field("bai_2", requires=IS_IN_SET(bai, zero=None),label="BAI 2."),
    Field("bai_3", requires=IS_IN_SET(bai, zero=None),label="BAI 3."),
    Field("bai_4", requires=IS_IN_SET(bai, zero=None),label="BAI 4."),
    Field("bai_5", requires=IS_IN_SET(bai, zero=None),label="BAI 5."),
    Field("bai_6", requires=IS_IN_SET(bai, zero=None),label="BAI 6."),
    Field("bai_7", requires=IS_IN_SET(bai, zero=None),label="BAI 7."),
    Field("bai_8", requires=IS_IN_SET(bai, zero=None),label="BAI 8."),
    Field("bai_9", requires=IS_IN_SET(bai, zero=None),label="BAI 9."),
    Field("bai_10", requires=IS_IN_SET(bai, zero=None),label="BAI 10."),
    Field("bai_11", requires=IS_IN_SET(bai, zero=None),label="BAI 11."),
    Field("bai_12", requires=IS_IN_SET(bai, zero=None),label="BAI 12."),
    Field("bai_13", requires=IS_IN_SET(bai, zero=None),label="BAI 13."),
    Field("bai_14", requires=IS_IN_SET(bai, zero=None),label="BAI 14."),
    Field("bai_15", requires=IS_IN_SET(bai, zero=None),label="BAI 15."),
    Field("bai_16", requires=IS_IN_SET(bai, zero=None),label="BAI 16."),
    Field("bai_17", requires=IS_IN_SET(bai, zero=None),label="BAI 17."),
    Field("bai_18", requires=IS_IN_SET(bai, zero=None),label="BAI 18."),
    Field("bai_19", requires=IS_IN_SET(bai, zero=None),label="BAI 19."),
    Field("bai_20", requires=IS_IN_SET(bai, zero=None),label="BAI 20."),
    Field("bai_21", requires=IS_IN_SET(bai, zero=None),label="BAI 21."),

    Field("bai_total", 'integer',label="BAI امتیاز نهایی."),
    Field("beck_total", "string",label=" Total Score of Beck Depression Inventory Short form"),    
    Field("mri_path", "string",label=" مسیر عکس های ام آر آی"),
    migrate = False,
    
    #fake_migrate = True,
    )


#------------------ Physician Section ----------------------------

db.define_table("physician_section",
    Field("id_code", "string",label="کدملی", writable=False, readable = False),
    #Field("physician_part","string",label=" بخش پزشک"),         
    Field("ped_people", "string",label="تعداد افرادی که در شجره مبتلا هستند "),
    Field("ped_generation", "string",label="نسل چندم در شجره"),
    Field("ped_number", "string",label="نفر چندم در نسل"),
    Field("ped_age", "string",label="سن شخص مبتلا در نسل "),
    
    Field("medicine_bkg_p", "string",label="داروهای قبلی پارکینسون"),
    Field("medicine_time_1", "string",label="مدت مصرف هر دارو"),
    Field("medicine_current_p", "string",label="داروهای فعلی برای پارکینسون"),
    Field("medicine_time_2", "string",label="مدت مصرف هر دارو"),
    Field("medicine_tradition", "string",label="درمانهای سنتی و مکمل"),
    Field("other_treats", requires=IS_IN_SET(treat_scores, zero=None),label="درمانهای بازتوانی"),
    Field("prodermal", "string",label="علایم پرودرمال پارکینسون"),
    Field("smell_reduc", requires=IS_IN_SET(yes_no, zero=None),label="کاهش بویایی"),
    Field("ysb", requires=IS_IN_SET(yes_no, zero=None),label="سابقه یبوست"),
    Field("excess_sleep", requires=IS_IN_SET(yes_no, zero=None),label="خواب آلودگی شدید روزانه"),
    Field("low_blood_p", requires=IS_IN_SET(yes_no, zero=None),label="فشار خون پایین"),
    Field("erectile", requires=IS_IN_SET(yes_no, zero=None),label="اختلال erectile شدید"),
    Field("piss", requires=IS_IN_SET(yes_no, zero=None),label="اختلال ادراری"),
    #Field("stress", requires=IS_IN_SET(yes_no, zero=None),label="افسردگی و اضطراب"),
    

    Field("generation_1", "string",label="تعداد افراد بیمار در نسل اول"),
    Field("age_1_1", "string",label="سن شروع بیماری"),
    Field("age_1_2", "string",label="سن شروع بیماری"),
    Field("age_1_3", "string",label="سن شروع بیماری"),
    Field("age_1_4", "string",label="سن شروع بیماری"),
    Field("age_1_5", "string",label="سن شروع بیماری"),

    Field("generation_2", "string",label="تعداد افراد بیمار در نسل دوم"),
    Field("age_2_1", "string",label="سن شروع بیماری"),
    Field("age_2_2", "string",label="سن شروع بیماری"),
    Field("age_2_3", "string",label="سن شروع بیماری"),
    Field("age_2_4", "string",label="سن شروع بیماری"),
    Field("age_2_5", "string",label="سن شروع بیماری"),

    Field("generation_3", "string",label="تعداد افراد بیمار در نسل سوم"),
    Field("age_3_1", "string",label="سن شروع بیماری"),
    Field("age_3_2", "string",label="سن شروع بیماری"),
    Field("age_3_3", "string",label="سن شروع بیماری"),
    Field("age_3_4", "string",label="سن شروع بیماری"),
    Field("age_3_5", "string",label="سن شروع بیماری"),

    Field("generation_4", "string",label="تعداد افراد بیمار در نسل چهارم"),
    Field("age_4_1", "string",label="سن شروع بیماری"),
    Field("age_4_2", "string",label="سن شروع بیماری"),
    Field("age_4_3", "string",label="سن شروع بیماری"),
    Field("age_4_4", "string",label="سن شروع بیماری"),
    Field("age_4_5", "string",label="سن شروع بیماری"),

    Field("generation_5", "string",label="تعداد افراد بیمار در نسل پنجم"),
    Field("age_5_1", "string",label="سن شروع بیماری"),
    Field("age_5_2", "string",label="سن شروع بیماری"),
    Field("age_5_3", "string",label="سن شروع بیماری"),
    Field("age_5_4", "string",label="سن شروع بیماری"),
    Field("age_5_5", "string",label="سن شروع بیماری"),

    Field("generation_6", "string",label="تعداد افراد بیمار در نسل ششم"),
    Field("age_6_1", "string",label="سن شروع بیماری"),
    Field("age_6_2", "string",label="سن شروع بیماری"),
    Field("age_6_3", "string",label="سن شروع بیماری"),
    Field("age_6_4", "string",label="سن شروع بیماری"),
    Field("age_6_5", "string",label="سن شروع بیماری"),


    Field("hight", "string",label="قد"),
    Field("weight", "string",label="وزن"),
    Field("blood_p_s", "string",label="فشار خون خوابیده"),
    Field("blood_p_st1", "string",label="فشار خون یک دقیقه بعد از ایستادن"),
    Field("blood_p_st3", "string",label="فشار خون سه دقیقه بعد از ایستادن"),
    Field("heart_beat_sl", "string",label="ضربان قلب خوابیده"),
    Field("heart_beat_st1", "string",label="ضربان قلب یک دقیقه بعد از ایستادن"),
    Field("heart_beat_st3", "string",label="ضربان قلب سه دقیقه بعد از ایستادن"),


    #Field("updrs_title", "string",label="MDS UPDRS Score Sheet"),
    Field("updrs_1_a", requires=IS_IN_SET(info_score, zero=None),label="1.A.Source of information"),
    Field("updrs_1_1", requires=IS_IN_SET(gait, zero=None),label="1.1.Cognitive impairment "),
    Field("updrs_1_2", requires=IS_IN_SET(gait, zero=None),label="1.2.Hallucinations and psychosis "),
    Field("updrs_1_3", requires=IS_IN_SET(gait, zero=None),label="1.3.Depressed mood "),
    Field("updrs_1_4", requires=IS_IN_SET(gait, zero=None),label="1.4.Anxious mood "),
    Field("updrs_1_5", requires=IS_IN_SET(gait, zero=None),label="1.5.Apathy "),
    Field("updrs_1_6", requires=IS_IN_SET(gait, zero=None),label= "1.6.Features of DDS "),
    Field("updrs_1_6_a", requires=IS_IN_SET(info_score, zero=None),label="1.6a.Who is filling out questionnaire؟"),

    Field("updrs_1_7", requires=IS_IN_SET(gait, zero=None),label="1.7.Sleep problems"),
    Field("updrs_1_8", requires=IS_IN_SET(gait, zero=None),label="1.8.Daytime sleepiness "),
    Field("updrs_1_9", requires=IS_IN_SET(gait, zero=None),label="1.9.Pain and other sensations "),
    Field("updrs_1_10", requires=IS_IN_SET(gait, zero=None),label="1.10.Urinary problems "),
    Field("updrs_1_11", requires=IS_IN_SET(gait, zero=None),label="1.11.Constipation problems "),
    Field("updrs_1_12", requires=IS_IN_SET(gait, zero=None),label="1.12.Light headedness on standing "),
    Field("updrs_1_13", requires=IS_IN_SET(gait, zero=None),label="1.13.Fatigue "),
    Field("updrs_total_1", 'integer',label="Total score UPDRS Part I"),

    Field("updrs_2_1", requires=IS_IN_SET(gait, zero=None),label="2.1.Speech "),
    Field("updrs_2_2", requires=IS_IN_SET(gait, zero=None),label="2.2.Saliva and drooling "),
    Field("updrs_2_3", requires=IS_IN_SET(gait, zero=None),label="2.3.Chewing and swallowing "),
    Field("updrs_2_4", requires=IS_IN_SET(gait, zero=None),label="2.4.Eating tasks "),
    Field("updrs_2_5", requires=IS_IN_SET(gait, zero=None),label="2.5.Dressing "),
    Field("updrs_2_6", requires=IS_IN_SET(gait, zero=None),label="2.6.Hygiene "),
    Field("updrs_2_7", requires=IS_IN_SET(gait, zero=None),label="2.7.Handwriting"),
    Field("updrs_2_8", requires=IS_IN_SET(gait, zero=None),label="2.8.Doing hobbies and other activities "),
    Field("updrs_2_9", requires=IS_IN_SET(gait, zero=None),label="2.9. Turning in bed "),
    Field("updrs_2_10", requires=IS_IN_SET(gait, zero=None),label="2.10.Tremor "),
    Field("updrs_2_11", requires=IS_IN_SET(gait, zero=None),label="2.11.Getting out of bed "),
    Field("updrs_2_12", requires=IS_IN_SET(gait, zero=None),label="2.12.Walking and balance "),
    Field("updrs_2_13", requires=IS_IN_SET(gait, zero=None),label="2.13.Freezing "),
    Field("updrs_total_2", 'integer',label="Total score UPDRS Part II"),

    Field("updrs_3_a", requires=IS_IN_SET(yes_no, zero=None),label="3a.Is the patient on medication؟ "),
    Field("updrs_3_b", requires=IS_IN_SET(off_on, zero=None),label="3b.Patient’s clinical state "),
    Field("updrs_3_c", requires=IS_IN_SET(yes_no, zero=None),label="3c. Is the patient on medication?"),
    Field("updrs_3_c1", "string",label="3c1. Minutes since last dose: "),

    Field("updrs_3_1", requires=IS_IN_SET(gait, zero=None),label="3.1.Speech"),
    Field("updrs_3_2", requires=IS_IN_SET(gait, zero=None),label="3.2.Facial expression"),
    Field("updrs_3_3a", requires=IS_IN_SET(gait, zero=None),label="3.3a.Rigidity– Neck"),
    Field("updrs_3_3b", requires=IS_IN_SET(gait, zero=None),label="3.3b.Rigidity– RUE"),
    Field("updrs_3_3c", requires=IS_IN_SET(gait, zero=None),label="3.3c.Rigidity– LUE"),
    Field("updrs_3_3d", requires=IS_IN_SET(gait, zero=None),label="3.3d.Rigidity– RLE"),
    Field("updrs_3_3e", requires=IS_IN_SET(gait, zero=None),label="3.3e.Rigidity– LLE"),
    Field("updrs_3_4a", requires=IS_IN_SET(gait, zero=None),label="3.4a.Finger tapping– Right hand"),
    Field("updrs_3_4b", requires=IS_IN_SET(gait, zero=None),label="3.4b.Finger tapping– Left hand"),
    Field("updrs_3_5a", requires=IS_IN_SET(gait, zero=None),label="3.5a.Hand movements– Right hand"),
    Field("updrs_3_5b", requires=IS_IN_SET(gait, zero=None),label="3.5b.Hand movements– Left hand"),
    Field("updrs_3_6a", requires=IS_IN_SET(gait, zero=None),label="3.6a.Pronation- supination movements– Right hand"),
    Field("updrs_3_6b", requires=IS_IN_SET(gait, zero=None),label="3.6b.Pronation- supination movements– Left hand"),
    Field("updrs_3_7a", requires=IS_IN_SET(gait, zero=None),label="3.7a.Toe tapping– Right foot"),
    Field("updrs_3_7b", requires=IS_IN_SET(gait, zero=None),label="3.7b.Toe tapping– Left foot"),
    Field("updrs_3_8a", requires=IS_IN_SET(gait, zero=None),label="3.8a.Leg agility– Right leg"),
    Field("updrs_3_8b", requires=IS_IN_SET(gait, zero=None),label="3.8b.Leg agility– Left leg"),
    Field("updrs_3_9", requires=IS_IN_SET(gait, zero=None),label="3.9.Arising from chair"),
    Field("updrs_3_10", requires=IS_IN_SET(gait, zero=None),label="3.10.Gait"),
    Field("updrs_3_11", requires=IS_IN_SET(gait, zero=None),label="3.11.Freezing of gait"),
    Field("updrs_3_12", requires=IS_IN_SET(gait, zero=None),label="3.12.Postural stability"),
    Field("updrs_3_13", requires=IS_IN_SET(gait, zero=None),label="3.13.Posture"),
    Field("updrs_3_14", requires=IS_IN_SET(gait, zero=None),label="3.14.Global spontaneity of movement"),
    Field("updrs_3_15a", requires=IS_IN_SET(gait, zero=None),label="3.15a.Postural tremor– Right hand"),
    Field("updrs_3_15b", requires=IS_IN_SET(gait, zero=None),label="3.15b.Postural tremor– Left hand"),
    Field("updrs_3_16a", requires=IS_IN_SET(gait, zero=None),label="3.16a.Kinetic tremor– Right hand"),
    Field("updrs_3_16b", requires=IS_IN_SET(gait, zero=None),label="3.16b.Kinetic tremor– Left hand"),
    Field("updrs_3_17a", requires=IS_IN_SET(gait, zero=None),label="3.17a.Rest tremor amplitude– RUE"),
    Field("updrs_3_17b", requires=IS_IN_SET(gait, zero=None),label="3.17b.Rest tremor amplitude– LUE"),
    Field("updrs_3_17c", requires=IS_IN_SET(gait, zero=None),label="3.17c.Rest tremor amplitude– RLE"),
    Field("updrs_3_17d", requires=IS_IN_SET(gait, zero=None),label="3.17d.Rest tremor amplitude– LLE"),
    Field("updrs_3_17e", requires=IS_IN_SET(gait, zero=None),label="3.17e.Rest tremor amplitude– Lip/jaw"),
    Field("updrs_3_18a", requires=IS_IN_SET(gait, zero=None),label="3.18a.Constancy of rest"),
    Field("updrs_total_3", 'integer',label="Total score UPDRS Part III"),


    
    Field("updrs_3_18b", requires=IS_IN_SET(yes_no, zero=None),label="Were dyskinesias present؟"),
    Field("updrs_3_18c", requires=IS_IN_SET(yes_no, zero=None),label="Did these movements interfere with ratings؟"),
    Field("updrs_3_18d", requires=IS_IN_SET(hoehn, zero=None),label="Hoehn and Yahr Stage"),
    Field("updrs_4_1", requires=IS_IN_SET(gait, zero=None),label="4.1.Time spent with dyskinesias"),
    Field("updrs_4_2", requires=IS_IN_SET(gait, zero=None),label="4.2.Functional impact of dyskinesias"),
    Field("updrs_4_3", requires=IS_IN_SET(gait, zero=None),label="4.3.Time spent in the OFF state"),
    Field("updrs_4_4", requires=IS_IN_SET(gait, zero=None),label="4.4.Functional impact of fluctuations"),
    Field("updrs_4_5", requires=IS_IN_SET(gait, zero=None),label="4.5.Complexity of motor fluctuations"),
    Field("updrs_4_6", requires=IS_IN_SET(gait, zero=None),label="4.6.Painful OFF-state dystonia"),

    #Field("fab_title", "string",label="The FAB "),
    Field("fab_1", requires=IS_IN_SET(fab_score, zero=None),label="FAB 1."),
    Field("fab_2", requires=IS_IN_SET(fab_score, zero=None),label="FAB 2."),
    Field("fab_3", requires=IS_IN_SET(fab_score, zero=None),label="FAB 3."),
    Field("fab_4", requires=IS_IN_SET(fab_score, zero=None),label="FAB 4."),
    Field("fab_5", requires=IS_IN_SET(fab_score, zero=None),label="FAB 5."),
    Field("fab_6", requires=IS_IN_SET(fab_score, zero=None),label="FAB 6."),
    Field("moca_1", requires=IS_IN_SET(moca1, zero=None),label="مونترال 1."),
    Field("moca_2", requires=IS_IN_SET(bai, zero=None),label="مونترال 2."),
    Field("moca_3", requires=IS_IN_SET(moca3, zero=None),label="مونترال 3."),
    Field("moca_4", requires=IS_IN_SET(moca4, zero=None),label="مونترال 4."),
    Field("moca_5", requires=IS_IN_SET(bai, zero=None),label="مونترال 5."),
    Field("moca_6", requires=IS_IN_SET(moca3, zero=None),label="مونترال 6."),
    Field("moca_7", requires=IS_IN_SET(moca4, zero=None),label="مونترال 7."),
    Field("moca_8", requires=IS_IN_SET(moca3, zero=None),label="مونترال 8."),
    Field("moca_9", requires=IS_IN_SET(moca1, zero=None),label="مونترال 9."),
    Field("moca_10", requires=IS_IN_SET(moca10, zero=None),label="مونترال 10."),

    Field("moca_total", 'integer',label="مونترال جمع امتیاز."),    
    Field("starkstein_total", "string",label=" Starkstein امتیاز نهایی آپاتی"),
    migrate = False,
    redefine = False,
)


    #migrate = True, fake_migrate = True
    #)

#------------------Lab Section ----------------------------
db.define_table("lab_section", 
    Field("id_code", "string",label="کدملی", writable=False, readable = False),
    Field("lab_2", requires=IS_IN_SET(blood_type, zero=None),label="خون"),
    Field("lab_part", "string",label=" سایر"),
    Field("lab_1", requires=IS_IN_SET(yes_no, zero=None),label=" DNA استخراج"),    
    Field("lab_3", "string",label="حجم خون باقیمانده"),
    Field("lab_4", "string",label="روش"),
    Field("lab_5", "string",label="DNA غلظت"),    
    Field("lab_6", "string",label="DNA حجم میکرولیتر"),
    migrate = False,
    )
    # 
db.define_table("genes_1_10",Field("id_code", "string",label="کدملی", writable=False, readable = False),Field("project", "string",label="Project"),*genes[0:110],migrate = False)
db.define_table("genes_11_20",Field("id_code", "string",label="کدملی", writable=False, readable = False),*genes[110:220],migrate = False)
db.define_table("genes_21_30",Field("id_code", "string",label="کدملی", writable=False, readable = False),*genes[220:330],migrate = False)
db.define_table("genes_31_40",Field("id_code", "string",label="کدملی", writable=False, readable = False),*genes[330:440],migrate = False)
db.define_table("genes_41_50",Field("id_code", "string",label="کدملی", writable=False, readable = False),*genes[440:550],migrate = False)
db.define_table("genes_51_60",Field("id_code", "string",label="کدملی", writable=False, readable = False),*genes[550:660],migrate = False)
db.define_table("genes_61_70",Field("id_code", "string",label="کدملی", writable=False, readable = False),*genes[660:770],migrate = False)
db.define_table("genes_71_80",Field("id_code", "string",label="کدملی", writable=False, readable = False),*genes[770:880],migrate = False)
db.define_table("genes_81_90",Field("id_code", "string",label="کدملی", writable=False, readable = False),*genes[880:990],migrate = False)
db.define_table("genes_91_100",Field("id_code", "string",label="کدملی", writable=False, readable = False),*genes[990:1100],migrate = False)
