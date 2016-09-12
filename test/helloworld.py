#this is a test

import urllib.request

    
#print ("url=", url, " page=", page)

# enclosedQuote
# input: string which might contain a quoted phrase
# output: q,p
#  if a single or double quoted string is found
#       p = position in str just past the quoted string
#       q = the quoted string
#  if no quoted string is found
#       p = -1, q = ""


def enclosedQuote(str,start) :
    sqc = "'"
    dqc = '"'
    qc = dqc
    sq = str[start:].find(sqc)
    dq = str[start:].find(dqc)
    p1,p2 = 0,0
    q = ""
    p = -1

    if sq == -1 :           # no single quote
        if dq != -1 :       
            p1 = dq          # only double quote exists
            qc = dqc
        else:
            return p,q
    else:                   # there is a single quote
        if dq == -1 :       # but not double quote, 
            p1 = sq          # single quote only
            qc = sqc
        else:               # both quote styles exist
            if sq < dq :
                p1 = sq
                qc = sqc
            else:
                p1 = dq
                qc = dqc
    p1 += start
    p2 = str[p1+1:].find(qc) + p1 + 1
    q =  str[p1+1:p2]
    p = p2+1
    return p,q
    


    
def getNextLink(pg,p) :
    hf = pg[p:].find("href=")
    if hf != -1 :
        p,q = (enclosedQuote(pg,hf+p))
        print ("Results of enclosedQuote",p,q)
        return p,q
    else :
        return -1
        
def get_Links(page) :
    q = ""
    pg = "".join(map(chr,page))
    p = 0
    p,q = getNextLink(pg,p)
    if p != -1 :
        p,q = getNextLink(pg,p)  
    if p != -1 :
        p,q = getNextLink(pg,p)    



#get_Links(page)

# parceByteArray(ray,list)
#   parces the byte array looking for any delimiter in list
#   returns f,bray,pos
#       f is boolean True if a substring was found
#       where bray (a byte array of bytes between delimiters
#       pos is the position just past where the substring was found

def parceByteArray(ray,list) :
    flist = []  # a list of found delimiters
    i = 0
    while i < len(list) :
        a = list[i]
        b = ray.find(a)
        if b != -1 :
            print ("a:",a," found at:", b)
            flist.append([a,i])
        i += 1
    print (flist)
    
parceByteArray(['"','h','e','l','l','o','"',"'"],['"',"'"])    

def getPage(url) :
    print (url)
    with urllib.request.urlopen(url) as f :
        page = (f.read())
    return page
    
def test() :    
    url = 'http://udacity.com/cs101x/urank/index.html'
    page = getPage(url)
    print (page)
    
#test()    