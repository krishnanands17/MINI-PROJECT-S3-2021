from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import MySQLdb
import csv
#from django.shortcuts import render_to_response
from django.core.files.storage import FileSystemStorage
import simplejson as json
from django.http import Http404
from datetime import date
from datetime import datetime
import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import re
# Create your views here.
con=MySQLdb.connect("localhost","root","","amazon_db")
c=con.cursor()
analyser = SentimentIntensityAnalyzer()


def print_sentiment_scores(name):
    lst=[]
    dataset = pd.read_csv('1429_1.csv', delimiter = ',')
    corpus = []
    corpusn = []
    dataset1 = pd.read_csv('items.csv', delimiter = ',')
    iteam=[]
    # for j in range(0, 20):
    #         pname = re.sub('[^a-zA-Z]', ' ', dataset['name'][j])
    #         iteam.append(pname)
    # for j in range(0, 20):
    #         k=0
    cnt=0
    cntn=0
    print("kkkkkkkkkkkkkkkkkkkkkkkkkkkk")
    print(name)
    for i in range(0,100):  
            review = re.sub('[^a-zA-Z0-1]', ' ', dataset['userreviews'][i])
            pname = re.sub('[^a-zA-Z0-1]', ' ', dataset['name'][i])
            name= re.sub('[^a-zA-Z0-1]', ' ', name)
            print(name.replace(",", ""))
            if(name.replace(",", "")==pname):
                print("ppppppppppppppppppppppppppppp")
                print(name)
                vadersenti = analyser.polarity_scores(review)
                cnt=cnt+vadersenti['pos']
                cntn=cntn+vadersenti['neg']
                corpus.append(cnt)
                corpusn.append(cntn)
            
                
    corpus.append(cnt)
    corpusn.append(cntn)
    lst.append(name)
    lst.append(corpus)
    lst.append(corpusn)
    return lst

    # cntp=0
    # cntn=0
    # dataset = pd.read_csv('C:\\Users\\Aagneya\\Desktop\\sngce\\lastcopy\\1429_1.csv', delimiter = ',')
    # dataset1 = pd.read_csv('C:\\Users\\Aagneya\\Desktop\\sngce\\lastcopy\\item.csv', delimiter = ',')
    # iteam=[]
    # for i in range(0, 20):
    #     pname = re.sub('[^a-zA-Z]', ' ', dataset['name'][i])
    #     iteam.append(pname)

    # corpus = []  
    # s=[]
    # for i in range(0, 400):  
    #     review = re.sub('[^a-zA-Z]', ' ', dataset['userreviews'][i])
    #     pname = re.sub('[^a-zA-Z]', ' ', dataset['name'][i])
    #     s=pname.split()
    #     # for s1 in s:
    #     #     if(s1==items):

    #     vadersenti = analyser.polarity_scores(review)
    #     cntp=cntp+vadersenti['pos']
    #     cntn=cntn+vadersenti['neg']
    #             # break
    # corpus.append(cntp) 
    # corpus.append(cntn)
    # corpus.append(pname)      
    # # dataset = pd.read_csv('C:\\Users\\ARUN C G\\Desktop\\1429_1.csv', delimiter = ',')
    # # corpus = []  
    
    # # for i in range(0, 1000):  
    # #     review = re.sub('[^a-zA-Z]', ' ', dataset['userreviews'][i])  
       
        
    # #     vadersenti = analyser.polarity_scores(tweets)
    # #     corpus.append(pd.Series([vadersenti['pos'], vadersenti['neg'], vadersenti['neu'], vadersenti['compound']]))

    # return corpus
def sujection(name):
    lst=[]
    dataset = pd.read_csv('1429_1.csv', delimiter = ',')
    corpus = []
    corpusn = []
    cnt=0
    cntn=0
   # dataset1 = pd.read_csv('C:\\Users\\Aagneya\\Desktop\\sngce\\lastcopy\\items.csv', delimiter = ',')
    iteam=[]
    

    for i in range(0, 100):  
            review = re.sub('[^a-zA-Z]', ' ', dataset['userreviews'][i])
            pname = re.sub('[^a-zA-Z]', ' ', dataset['name'][i])
            name= re.sub('[^a-zA-Z]', ' ', name)
            #print(pname)
            if(name==pname):

                #k=k+1
                vadersenti = analyser.polarity_scores(review)
                cnt=cnt+vadersenti['pos']
                cntn=cntn+vadersenti['neg']
    corpus.append(cnt)
    corpusn.append(cntn)
    lst.append(name)
    lst.append(corpus)
    lst.append(corpusn)
    msg="No suggestion"
    if(cnt<cntn):
        msg="pls improve the mentioned area"+ review
        lst.append(msg)
    lst.append(msg)
    return lst
def AdminPage(request):
    return render(request,'AdminPage.html') 
def adminviewcustomer(Request):
    
    s="select * from cusreg"
    c.execute(s)
    data=c.fetchall()
    return render(Request,'adminviewcustomer.html',{"data":data})
def adminviewMURCHENT(Request):
    
    s="select * from merchantreg"
    c.execute(s)
    data=c.fetchall()
    return render(Request,'adminviewMURCHENT.html',{"data":data})
def adminremove(Request):
    id=Request.GET.get("id")
    if "sub1" in Request.POST :
        war=Request.POST.get("t2")
        s="insert into warning (mid,warning) values('"+str(id)+"','"+str(war)+"')"
        c.execute(s)
        con.commit()
    if "sub2" in Request.POST :
        war=Request.POST.get("t1")
        
        s="delete from login  where uname in (select username from merchantreg where mrid='"+str(id)+"')"
        c.execute(s)
        
        s="delete from merchantreg where mrid='"+str(id)+"'"
        c.execute(s)
        con.commit()
    return render(Request,'adminremove.html',{"id":id})
def CustomerHome(request):
    return render(request,'CustomerHome.html') 

def MerchantHome(request):
    return render(request,'MerchantHome.html') 

def Index(request):
    return render(request,'index.html') 

def login(Request):
    msg=""

    if(Request.POST):
        username=Request.POST.get("t1")
        password=Request.POST.get("t2")
        qry="select type from login where uname='"+str(username)+"' and password='"+str(password)+"'"
        c.execute(qry)
        data=c.fetchone()
        print("-------------------------------------------")
        print(data)
        if(data):
            if(data[0]=="marchant"):
                c.execute("select mrid from merchantreg where username='" + username + "' and status='1'")
                ui=c.fetchone()
                
                if(ui):
                    Request.session["mid"]=ui[0]
                    return HttpResponseRedirect("/MerchantHome")
                else:
                    
                    msg="wait for approval"
                    print("**************************************************************")
                    print(msg)
            elif(data[0]=="customer"):
                c.execute("select * from cusreg where username='" + username + "'")
                ci=c.fetchall()
                Request.session["cid"]=ci[0][0]
                Request.session["NAME"]=ci[0][1]
                return HttpResponseRedirect("/CustomerHome")
            elif(data[0]=="admin"):
                
                return HttpResponseRedirect("/adminviewcustomer")
            else:
                msg="invalid username or password"
        else:
            msg="invalid username or password"
        con.commit()
    # except:
    #     print("in")
    #     msg="wait for approval"
    #     # msg="Invalid username or password"
    return render(Request,'login.html',{"msg":msg})
def approve(request):
    id=request.GET.get("id")
    st="1"
    ss="update merchantreg set status='"+str(st)+"' where mrid='"+str(id)+"'"
    c.execute(ss)
    con.commit()

    return HttpResponseRedirect("/adminviewmurchent")
def marchantreg(Request):
    msg=""
    if(Request.POST):
        name=Request.POST.get("t1")
        owner=Request.POST.get("t2")
        address=Request.POST.get("address")
        district=Request.POST.get("district")
        state=Request.POST.get("state")
        pin=Request.POST.get("pincode")
        phone=Request.POST.get("phone")
        email=Request.POST.get("email")
        username=Request.POST.get("username")
        password=Request.POST.get("password")
        cpassword=Request.POST.get("cpassword")
        types="marchant"
        qry1="select count(*) from login where uname='"+str(username)+"'"
        c.execute(qry1)
        data=c.fetchone()
        if(int(data[0])==0):

            qry="insert into merchantreg(name,owner,address,district,state,pin,phone,email,username,password,cpassword) values('"+str(name)+"','"+str(owner)+"','"+str(address)+"','"+str(district)+"','"+str(state)+"','"+str(pin)+"','"+str(phone)+"','"+str(email)+"','"+str(username)+"','"+str(password)+"','"+str(cpassword)+"')"
            
            q2="insert into login(uname,password,type) values('"+str(username)+"','"+str(password)+"','"+str(types)+"')"
            c.execute(q2)
            c.execute(qry)
            print(qry)
            con.commit()
        else:
            msg="plz try another username"
    return render(Request,'marchantreg.html',{"msg":msg}) 

def customerreg(Request):
    msg=""
    if(Request.POST):
        fname=Request.POST.get("fname")
        lname=Request.POST.get("lname")
        address=Request.POST.get("address")
        district=Request.POST.get("district")
        state=Request.POST.get("state")
        pincode=Request.POST.get("pincode")
        phono=Request.POST.get("phone")
        dob=Request.POST.get("date")
        gender=Request.POST.get("gender")
        email=Request.POST.get("email")
        username=Request.POST.get("username")
        password=Request.POST.get("password")
        cpassword=Request.POST.get("cpassword")
        types="customer"
        qry1="select count(*) from login where uname='"+str(username)+"'"
        c.execute(qry1)
        data=c.fetchone()
        if(int(data[0])==0):

            qry="insert into cusreg(fname,lname,address,email,pincode,gender,phono,username,password,cpassword,district,state) values('"+str(fname)+"','"+str(lname)+"','"+str(address)+"','"+str(email)+"','"+str(pincode)+"','"+str(gender)+"','"+str(phono)+"','"+str(username)+"','"+str(password)+"','"+str(cpassword)+"','"+str(district)+"','"+str(state)+"')"
            q2="insert into login(uname,password,type) values('"+str(username)+"','"+str(password)+"','"+types+"')"
            c.execute(q2)
            c.execute(qry)
            print(qry)
            con.commit()

        else:
            msg="plz try another username"
    return render(Request,'customerreg.html',{"msg":msg})

def brand(Request):
    c.execute("select * from catogory")
    data=c.fetchall()
    if(Request.POST):
        cid=Request.POST.get("catname")
        scid=Request.POST.get("scname")
        bname=Request.POST.get("bname")
        spec=Request.POST.get("specification")
        qry="insert into brand(cid,scid,bname,spec) values(%s,%s,%s,%s)"
        c.execute(qry,(cid,scid,bname,spec))
        con.commit()
    return render(Request,'brand.html',{"data":data})

def catogory(Request):
    if(Request.POST):
        cname=Request.POST.get("ctname")
        #spec=Request.POST.get("specification")
        qry="insert into catogory(cname) values('"+str(cname)+"')"
        c.execute(qry)
        con.commit()
    return render(Request,'catogory.html')

def subcatogory(Request):
    c.execute("select * from catogory")
    data = c.fetchall()
    if(Request.POST):
        cid=Request.POST.get("catname")
        scname=Request.POST.get("scname")
        
        qry="insert into subcatogory(cid,scname) values('"+str(cid)+"','"+str(scname)+"')"
        print(qry)
        c.execute(qry)
        con.commit()
    return render(Request,'subcategory.html',{"data":data})

def model(Request):
    data=""
    try:
            c.execute("select * from catogory")
    except:
        raise Http404
        
    data=c.fetchall()   
    if(Request.POST):
        cid=Request.POST.get("catname")
        scid=Request.POST.get("scname")
        bid=Request.POST.get("bname")
        mname=Request.POST.get("mname")
        spec=Request.POST.get("specification")
        price=Request.POST.get("price")
        qt=Request.POST.get("q")
        mi = Request.session["mid"]
        c.execute("select scid from subcatogory where scname='" + scid + "'")
        ui=c.fetchone()
        scat_id=ui[0]
        c.execute("select bid from brand where bname='" + bid + "'")
        print("select bid from brand where bname='" + bid + "'")
        Sbi=c.fetchone()
        bi_id=Sbi[0]
        if Request.FILES.get("p1"):
              myfile=Request.FILES.get("p1")
              fs=FileSystemStorage()
              filename=fs.save(myfile.name , myfile)
              uploaded_file_url = fs.url(filename)
        qry="insert into model(cid,scid,bid,mname,spec,price,pic,qty,merchid) values('"+str(cid)+"','"+str(scat_id)+"','"+str(bi_id)+"','"+mname+"','"+spec+"','"+price+"','"+uploaded_file_url+"','"+str(qt)+"','"+str(mi)+"')"
        c.execute(qry)
        con.commit()
    return render(Request,'model.html',{"cat":data})

def subcat(request):
  sublist=[]
  catid=request.GET.get("dataid")
  c.execute("select scname,scid from subcatogory where cid='"+ str(catid)+"'")
  print("iiiiiiiiiiiiiiiiii")
  print("select * from subcatogory where cid='"+ str(catid)+"'")
  data2=c.fetchall()
#   for d in data2:
#     sublist.append(d[2])
  return HttpResponse(json.dumps(data2),content_type="application/json")

def brandcat(request):
  brandcatlist=[]
  catid=request.GET.get("dataid")
  c.execute("select bname from brand where cid in(select cname from catogory where cid='"+ str(catid)+"')")
  data2=c.fetchall()
  for d in data2:
    brandcatlist.append(d[0])
  return HttpResponse(json.dumps(brandcatlist),content_type="application/json")

def MerchantViewMyProduct(Request):
    mi = Request.session["mid"]
    s="select * from model where merchid = '"+str(mi)+"'"
    c.execute(s)
    data=c.fetchall()
    return render(Request,'MerchantViewMyProduct.html',{"data":data})
def reviewViewMyProduct(Request):
    mi = Request.session["mid"]
    s="select * from model where merchid = '"+str(mi)+"'"
    c.execute(s)
    data=c.fetchall()
    return render(Request,'reviewViewMyProduct.html',{"data":data})
def reviewViewMyProductadmin(Request):
    mi = Request.session["mid"]
    s="select * from model "
    c.execute(s)
    data=c.fetchall()
    return render(Request,'adminreview.html',{"data":data})
def ViewWarning(Request):
    mi = Request.session["mid"]
    s="select * from warning where mid = '"+str(mi)+"'"
    c.execute(s)
    data=c.fetchall()
    return render(Request,'ViewWarning.html',{"data":data})

def cus(Request):
    return render(Request,'cus.html')

def CustomerProductSearch(request):
    c.execute("select * from catogory")
    data = c.fetchall()
    if request.POST:
        scname = request.POST.get("scname")
        print(scname)
        request.session["scname"] = scname
        return HttpResponseRedirect("/viewproductbym")
    return render(request,'CustomerProductSearch.html',{"data":data})

def viewproductbym(Request):
    sc =  Request.session["scname"]
    c.execute("select scid from subcatogory where scid = '"+sc+"'")
    print("select scid from subcatogory where scid = '"+sc+"'")
    d = c.fetchone()
    
    s="select * from model where scid = '"+str(d[0])+"'"
    c.execute(s)
    data=c.fetchall()
    t="select * from catogory"
    c.execute(t)
    data1=c.fetchall()
    u="select * from subcatogory"
    c.execute(u)
    data2=c.fetchall()
    v="select * from brand"
    c.execute(v)
    data3=c.fetchall()
    return render(Request,'CustomerShop.html',{"data":data,"data1":data1,"data2":data2,"data3":data3})

def CustomerViewProCategory(Request):
    cname=Request.GET.get("id")
    r="select cid from catogory where cname='"+str(cname)+"'"
    c.execute(r)
    data=c.fetchone()
    ci= data[0]
    s="select * from model where cid = '"+str(ci)+"'"
    c.execute(s)
    data=c.fetchall()
    t="select * from catogory"
    c.execute(t)
    data1=c.fetchall()
    u="select * from subcatogory"
    c.execute(u)
    data2=c.fetchall()
    v="select * from brand"
    c.execute(v)
    data3=c.fetchall()
    return render(Request,'CustomerShop.html',{"data":data,"data1":data1,"data2":data2,"data3":data3})

def CustomerViewProSubCategory(Request):
    sid=Request.GET.get("id")
    s="select * from model where scid = '"+str(sid)+"'"
    c.execute(s)
    data=c.fetchall()
    t="select * from catogory"
    c.execute(t)
    data1=c.fetchall()
    u="select * from subcatogory"
    c.execute(u)
    data2=c.fetchall()
    v="select * from brand"
    c.execute(v)
    data3=c.fetchall()
    return render(Request,'CustomerShop.html',{"data":data,"data1":data1,"data2":data2,"data3":data3})

def CustomerViewProBrand(Request):
    bid=Request.GET.get("id")
    s="select * from model where bid = '"+str(bid)+"'"
    c.execute(s)
    data=c.fetchall()
    t="select * from catogory"
    c.execute(t)
    data1=c.fetchall()
    u="select * from subcatogory"
    c.execute(u)
    data2=c.fetchall()
    v="select * from brand"
    c.execute(v)
    data3=c.fetchall()
    return render(Request,'CustomerShop.html',{"data":data,"data1":data1,"data2":data2,"data3":data3})

def CustomerViewProDetails(Request):
    pid=Request.GET.get("id")
    s="select * from model where mid = '"+str(pid)+"'"
    c.execute(s)
    data=c.fetchall()
    t="select * from catogory"
    c.execute(t)
    data1=c.fetchall()
    u="select * from subcatogory"
    c.execute(u)
    data2=c.fetchall()
    v="select * from brand"
    c.execute(v)
    data3=c.fetchall()
    return render(Request,'CustomerViewProDetails.html',{"data":data,"data1":data1,"data2":data2,"data3":data3})

def CustomerOrderProduct(Request):
    pid=Request.GET.get("id")
    s="select * from model where mid = '"+str(pid)+"'"
    c.execute(s)
    data=c.fetchall()
    cid = Request.session["cid"]
    merid = data[0][9]
    price = data[0][6]
    c.execute("insert into cart (cid,mid,pid,amount,qty)values('"+str(cid)+"','"+str(merid)+"','"+str(pid)+"','"+str(price)+"','1')")
    con.commit()
    t="select * from catogory"
    c.execute(t)
    data1=c.fetchall()
    u="select * from subcatogory"
    c.execute(u)
    data2=c.fetchall()
    v="select * from brand"
    c.execute(v)
    data3=c.fetchall()
    msg="Add to cart"
    return render(Request,'CustomerViewProDetails.html',{"data":data,"data1":data1,"data2":data2,"data3":data3,"msg":msg})
def deletecart(request):
    id=request.GET.get("id")
    d="delete from cart where cartid='"+str(id)+"'"
    print(d)
    c.execute(d)
    con.commit()
    return HttpResponseRedirect("CustomerViewCart")
def CustomerViewCart(Request):
    try:

        cid = Request.session["cid"]
        s="select * from cart inner join model on cart.pid = model.mid where cart.cid = '"+str(cid)+"'"
        c.execute(s)
        data=c.fetchall()
        merid = data[0][9]
        price = data[0][6]
        pid = data[0][3]
        qty = data[0][5]
        t="select count(*) from cart where cid = '"+str(cid)+"'"
        c.execute(t)
        data1=c.fetchone()
        u="select sum(amount) from cart where cid = '"+str(cid)+"'"
        c.execute(u)
        data2=c.fetchone()
        totalamount = data2[0]
        tot = totalamount
        Request.session["pay"] = str(tot)
        if(Request.POST):
            
            c.execute("select * from cart where cid = '"+str(cid)+"'")
            data3 = c.fetchall()
            for d3 in data3:
                
                custid = d3[1]
                meid = d3[2]
                proid = d3[3]
                amot = d3[4]
                quty = d3[5]
                carid = d3[0]
               
                name=Request.POST.get("name")
                print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
                mob=Request.POST.get("mob")
                loc=Request.POST.get("land")
                atype=Request.POST.get("atype")
                
                print("insert into cust_order (cid,mid,pid,amount,qty,name,mob,loc,atype)values('"+str(custid)+"','"+str(meid)+"','"+str(proid)+"','"+str(amot)+"','"+str(quty)+"','"+str(name)+"','"+str(mob)+"','"+str(loc)+"','"+str(atype)+"')")
                c.execute("insert into cust_order (cid,mid,pid,amount,qty,name,mob,loc,atype)values('"+str(custid)+"','"+str(meid)+"','"+str(proid)+"','"+str(amot)+"','"+str(quty)+"','"+str(name)+"','"+str(mob)+"','"+str(loc)+"','"+str(atype)+"')")
                con.commit()
                c.execute("select  qty from model where mid='"+str(proid)+"'")
                
                dd=c.fetchone()
                qty=dd[0]-qty
                c.execute("update model set qty='"+str(qty)+"' where mid='"+str(proid)+"'")
                con.commit()

                c.execute("delete from cart where cartid = '"+str(carid)+"'")
                con.commit()
                
            return HttpResponseRedirect("/payment1")
        return render(Request,'CustomerViewCart.html',{"data":data,"data1":data1[0],"data2":data2[0]})
    except:
        msg="ok"

    return render(Request,'CustomerViewCart.html')

def payment1(request):
    
    if request.POST:
        card=request.POST.get("test")
        cardno=request.POST.get("cardno")
        request.session["card_no"]=cardno
        pinno=request.POST.get("pinno")
        return HttpResponseRedirect("/payment2")
    return render(request,"payment1.html")

def payment2(request):
    cno=request.session["card_no"]
    amount=request.session["pay"]
    if request.POST:
        # name=request.POST.get("t1")
        # request.session["m"]=name
        # address=request.POST.get("t2")
        # email=request.POST.get("t3")
        # phno=request.POST.get("t4")
        # n="insert into delivery values('"+str(cno)+"','"+str(name)+"','"+str(address)+"','"+str(email)+"','"+str(phno)+"','"+str(amount)+"')"
        # print(n)
        # c.execute(n)
        # con.commit()
        return HttpResponseRedirect("/payment3")
    return render(request,"payment2.html",{"cno":cno,"amount":amount})

def payment3(request):
    return render(request,"payment3.html")

def payment4(request):
    return render(request,"payment4.html")

def payment5(request):
    cno=request.session["card_no"]
    today = date.today()
    name =  request.session['NAME'] 
    amount = request.session["pay"]
    print(amount)
    # n="select * from delivery where card='"+str(cno)+"'"
    # c.execute(n)
    # data=c.fetchall()
    return render(request,"payment5.html",{"cno":cno,"today":today,"name":name,"amount":amount})


def orderproduct(Request):
    name=request.GET.get("name")
    s="select m.mname,m.spec,m.price,c.cname,b.bname from model m join catogory c on(c.cid=m.cid) join brand b on (b.bid=m.bid) where m.name='"+name+"'"
    c.execute(s)
    data=c.fetchall()
    return render(Request,'orderproduct.html',{"data":data})

def viewcommentbasedproduct(Request):
    name=request.GET.get("name")
    s="select m.mname,m.spec,m.price,c.cname,b.bname,r.comment from model m join catogory c on(c.cid=m.cid) join brand b on (b.bid=m.bid) join review r on(m.mid=r.mid)"
    c.execute(s)
    data=c.fetchall()
    if request.POST :
        mname=request.POST.get("mname")
        price=request.POST.get("price")
        cname=request.session["uname"]
        s="insert into order(name,price,custname) values('"+manme+"','"+price+"','"+cname+"')"
    return render(Request,'viewcommentbasedproduct.html',{"data":data})
def adminviewcommentbasedproduct(Request):
    name=request.GET.get("name")
    s="select m.mname,m.spec,m.price,c.cname,b.bname,r.comment from model m join catogory c on(c.cid=m.cid) join brand b on (b.bid=m.bid) join review r on(m.mid=r.mid)"
    c.execute(s)
    data=c.fetchall()
    if request.POST :
        mname=request.POST.get("mname")
        price=request.POST.get("price")
        cname=request.session["uname"]
        s="insert into order(name,price,custname) values('"+manme+"','"+price+"','"+cname+"')"
    return render(Request,'adminviewcommentbasedproduct.html',{"data":data})


def demo_piechart(request):
    """
    pieChart page
    """
    name=request.GET.get("name")
    data=print_sentiment_scores(name)
    # s="select  count(comment),mid from review group by mid,comment"
    # c.execute(s)
    # data=c.fetchall()
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    print(data)
    d1=data[0]
    d2=data[1]
    d3=data[2]
    
    # xdata=[]
    # ydata=[]
    # for d in data:

    #     xdata .append(d[1])
    #     ydata .append(d[0])

    # extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    # chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    # charttype = "pieChart"

   
    return render(request,'chart.html',{"d1":d1,"d2":d2,"d3":d3})  

def demo_piechart2(request):
    """
    pieChart page
    """
    name=request.GET.get("name")
    data=sujection(name)
    # s="select  count(comment),mid from review group by mid,comment"
    # c.execute(s)
    # data=c.fetchall()
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    print(data)
    d1=data[0]
    d2=data[1]
    d3=data[2]
    d4=data[3]
    
    # xdata=[]
    # ydata=[]
    # for d in data:

    #     xdata .append(d[1])
    #     ydata .append(d[0])

    # extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    # chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    # charttype = "pieChart"

   
    return render(request,'chart2.html',{"d1":d1,"d2":d2,"d3":d3,"d4":d4})
    

def mar(Request):
    return render(Request,'mar.html')
    
def comment(Request):
    if(Request.POST):
        cid=Request.POST.get("catogory")
        scid=Request.POST.get("subcatogry")
        bid=Request.POST.get("brand")
        mid=Request.POST.get("model")
        com=Request.POST.get("review")
        qry="insert into review(cus_id,cid,scid,bid,mid,comment) values('"+cus_id+"','"+cid+"','"+scid+"','"+bid+"','"+mid+"','"+com+"')"
        c.execute(qry)
        con.commit()
    return render(Request,'comment.html')  
def vproduct(Request):
    sc =  Request.GET.get("dataid")
   
    s="select * from model where scid = '"+str(sc)+"'"
    c.execute(s)
    data=c.fetchall()
   
    return HttpResponse(json.dumps(data),content_type="application/json")
    
def addproduct(Request):
    c.execute("select * from catogory")
    data = c.fetchall()
    msg=""
    if(Request.POST):
        cid=Request.POST.get("catname")
        scid=Request.POST.get("scname")
        
        mid=Request.POST.get("pname")
        se="select mname from model where mid='"+str(mid)+"'"
        c.execute(se)
        dd=c.fetchall()
        com=Request.POST.get("review")
        cus_id= Request.session["cid"]
        s1="select count(*) from cust_order where cid='"+str(cus_id)+"' and pid='"+str(mid)+"'"

        c.execute(s1)
        cnt=c.fetchall()
        if(cnt[0][0]!=0):

            lines=str(mid)+" ,"+dd[0][0]+" ,"+"  ,"+"  ,"+cid+"  ,"+"  ,"+"  ,"+"  ,"+"  ,"+"  ,"+"   ,"+"  ,"+"  ,"+"  ,"+"  ,"+"  ,"+com+","+"  ,"
            with open('1429_1.csv', 'a') as writeFile:
                #writer = csv.writer(writeFile)
                #writer.writerows(lines)
                writeFile.write("\n")
                writeFile.write(lines)
            writeFile.close()
            qry="insert into review(cus_id,cid,scid,mid,comment) values('"+str(cus_id)+"','"+str(cid)+"','"+str(scid)+"','"+str(mid)+"','"+str(com)+"')"
            c.execute(qry)
            con.commit()
        else:
            msg="you not purchase the product"
    return render(Request,'addproduct.html',{"data":data,"msg":msg})

def customervieworders(request):
    cid=request.session["cid"]
    ss="select cust_order.pid, model.mname,cusreg.fname,cust_order.qty,cust_order.amount from cust_order join model on(cust_order.pid=model.mid) join cusreg on(cusreg.cus_id=cust_order.cid) where cusreg.cus_id='"+str(cid)+"'"
    c.execute(ss)
    data=c.fetchall()
    return render(request,'customervieworders.html',{"data":data})
def marchentvieworder(request):
    mid=request.session["mid"]
    ss="select cust_order.pid, model.mname,cusreg.fname,cust_order.qty,cust_order.amount,cust_order.name,cust_order.mob,cust_order.loc,cust_order.atype from cust_order join model on(cust_order.pid=model.mid) join cusreg on(cusreg.cus_id=cust_order.cid) where cust_order.mid='"+str(mid)+"'"
    c.execute(ss)
    data=c.fetchall()
    return render(request,'MerchantViewOrder.html',{"data":data})

