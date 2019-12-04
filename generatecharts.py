import math
import numpy as np
import matplotlib.pyplot as plt
import pprint


def one_is_zero(i):
    if i==1:
        return 0
    return i

def commas_for_int(i):
    s = str(i)
    groups = s[::-3]

def power(data, label, filename, log=False):
    fig1, ax1 = plt.subplots()
    ax1.set_title(label)
    plt.xlim(-1,len(data)+1)
    if log: 
        maxvalue = max(data)
        exponent = math.log10(maxvalue)
        top = math.ceil(exponent+1) 
        plt.yticks(np.arange(top), [0]+['{:,}'.format(10**i) for i in range(1,top)]) 
        logs = [math.log10(max(x,1)) for x in data] 
        data = [x for x in map(one_is_zero,logs)] 
        bottom, computedtop = plt.ylim()
        print(bottom,computedtop,top)
        plt.ylim(bottom=0,top=top)
    else:
        maxvalue = max(data)
        bottom, computedtop = plt.ylim() 
        plt.ylim(bottom=0,top=maxvalue)
        ax1.ticklabel_format(style='plain')
        #plt.yticks(np.arange(top), [0]+['{:,}'.format(i) for i in range(1,top)]) 
        #maxvalue = max(data)
        #plt.yticks(np.arange(7), [10**i for i in range(maxvalue)]) 
    data.sort(reverse=True)
    ax1.scatter([i for i,x in enumerate(data)],data,marker='x',s=3) 
    ax1.tick_params(labelsize=8)
    fig1.show()
    fig1.savefig(filename)
    
def crubadan():
    with open("Crubadan-corpussizes.csv") as crubadan:  
        lines = crubadan.readlines()
        crubvalues = [int(line.strip()) for line in lines] 
        zeros = [0.1 for x in range(7459-len(crubvalues))]
        values = crubvalues + zeros        
        power(sorted(values), "corpus sizes for languages", "corpussizes.png")
        power(sorted(values), "Sizes of available corpora for languages (log scale)", "corpussizes_log.png", log=True)
    
def wikistats():    
    with open("wikstats.csv") as wikstats:  
        lines = wikstats.readlines()
        tuples = [l.split(', ') for l in lines]
        lgs = [x[0].strip() for x in tuples]
        wiktionaryvalues = [int(x[1].strip()) for x in tuples]
        zeros = [0.1 for x in range(7459-len(wiktionaryvalues))]
        values = wiktionaryvalues + zeros        
        power(sorted(values), "lemmas in wiktionaries", "wiktionary.png")
        power(sorted(values), "lemmas in wiktionaries (log)", "wiktionary_log.png", log=True)     
        
def olachtml():    
    with open("olachtml.csv") as olach:  
        lines = olach.readlines()
        tuples = [l.split(', ') for l in lines]
        lgs = [x[0].strip() for x in tuples]
        olachvalues = [max(0,int(x[1].strip())-3) for x in tuples] #decrement value by 3 for Glottolog, LingList, SIL, which are not real resources
        #zeros = [0.1 for x in range(7459-len(wiktionaryvalues))]
        values = olachvalues # + zeros        
        power(sorted(values), "Resources listed on OLAC web page", "olachtml.png")
        power(sorted(values), "Resources listed on OLAC web page (log)", "olachtml_log.png", log=True)       
        
def olacprimarytexts():    
    with open("olacprimarytexts.csv") as olac:  
        lines = olac.readlines()
        olacvalues = [int(line.strip()) for line in lines] 
        zeros = [0.1 for x in range(7459-len(olacvalues))]
        values = olacvalues + zeros            
        power(sorted(values), "# primary texts listed in OLAC", "olacprimarytexts.png")
        power(sorted(values), "# primary texts listed in OLAC (log)", "olacprimarytexts_log.png", log=True)    
        
def glottorefs():    
    with open("glottorefs.csv") as glottorefs:  
        lines = glottorefs.readlines()
        glottorefvalues = [int(line.strip()) for line in lines] 
        #zeros = [0.1 for x in range(7459-len(glottorefvalues))]
        values = glottorefvalues #+ zeros            
        power(sorted(values), "# references in Glottolog", "glottorefs.png")
        power(sorted(values), "# primary texts listed in OLAC (log)", "glottorefs_log.png", log=True)            

def aclwiki():    
    with open("aclwiki.csv") as acl:  
        lines = acl.readlines()
        aclvalues = [int(line.strip()) for line in lines] 
        zeros = [0.1 for x in range(7459-len(aclvalues))]
        values = aclvalues + zeros            
        power(sorted(values), "# resources listed in ACL wiki", "aclwiki.png")
        #power(sorted(values), "# primary texts listed in OLAC (log)", "glottorefs_log.png", log=True)    
        
def audioduration():    
    with open("audioduration.csv") as audio:  
        lines = audio.readlines()
        audiovalues = [float(line.strip()) for line in lines] 
        zeros = [0.1 for x in range(7459-len(audiovalues))]
        values = audiovalues + zeros            
        power(sorted(values), "# total length of archived audio in hours", "audio.png")
        power(sorted(values), "# total length of archived audio in hours (log)", "audio_log.png", log=True)  
        power(sorted(values)[:-10], "# total length of archived audio in hours (excluding top 10 lgs)", "audio_cropped.png")
        power(sorted(values)[:-10], "# total length of archived audio in hours (excluding top 10 lgs, log)", "audio_cropped_log.png", log=True)           
        
def audioduration_delaman():    
    with open("audioduration_delaman.csv") as audiodelaman:  
        lines = audiodelaman.readlines()
        audiodelamanvalues = [float(line.strip()) for line in lines] 
        zeros = [0.1 for x in range(7459-len(audiodelamanvalues))]
        values = audiodelamanvalues + zeros            
        power(sorted(values), "# total length of archived audio in hours in DELAMAN archives", "audio_delaman.png")
        power(sorted(values), "# total length of archived audio in hours in DELAMAN archives (log)", "audio_delaman_log.png", log=True)  
        power(sorted(values)[:-10], "# total length of archived audio in hours in DELAMAN archives(excluding top 10 lgs)", "audio_delaman_cropped.png")
        power(sorted(values)[:-10], "# total length of archived audio in hours in DELAMAN archives (excluding top 10 lgs, log)", "audio_delaman_cropped_log.png", log=True)   
        
def videoduration_delaman():    
    with open("videoduration_delaman.csv") as videodelaman:  
        lines = videodelaman.readlines()
        videodelamanvalues = [float(line.strip()) for line in lines] 
        zeros = [0.1 for x in range(7459-len(videodelamanvalues))]
        values = videodelamanvalues + zeros            
        power(sorted(values), "# total length of archived video in hours in DELAMAN archives", "video_delaman.png")
        power(sorted(values), "# total length of archived video in hours in DELAMAN archives (log)", "video_delaman_log.png", log=True)  
        power(sorted(values)[:-10], "# total length of archived video in hours in DELAMAN archives(excluding top 10 lgs)", "video_delaman_cropped.png")
        power(sorted(values)[:-10], "# total length of archived video in hours in DELAMAN archives (excluding top 10 lgs, log)", "video_delaman_cropped_log.png", log=True)   
        
def videoduration():    
    with open("videoduration.csv") as video:  
        lines = video.readlines()
        videovalues = [float(line.strip()) for line in lines] 
        zeros = [0.1 for x in range(7459-len(videovalues))]
        values = videovalues + zeros            
        power(sorted(values), "# total length of archived video in hours", "video.png")
        power(sorted(values), "# total length of archived video in hours (log)", "video_log.png", log=True)  
        power(sorted(values)[:-10], "# total length of archived video in hours (excluding top 10 lgs)", "video_cropped.png")
        power(sorted(values)[:-10], "# total length of archived video in hours (excluding top 10 lgs, log)", "video_cropped_log.png", log=True)          
        
                
def transcriptions():    
    with open("transcriptions.csv") as transcription:  
        lines = transcription.readlines()
        transcriptionvalues = [float(line.strip()) for line in lines] 
        zeros = [0.1 for x in range(7459-len(transcriptionvalues))]
        values = transcriptionvalues + zeros            
        power(sorted(values), "# archived transcription", "transcription.png")
        power(sorted(values), "# archived transcription (log)", "transcription_log.png", log=True)  
        power(sorted(values)[:-10], "# archived transcription (excluding top 10 lgs)", "transcription_cropped.png")
        power(sorted(values)[:-10], "# archived transcription (excluding top 10 lgs, log)", "transcription_cropped_log.png", log=True)          
        
if __name__ == "__main__":
    crubadan()
    wikistats()
    olacprimarytexts()
    audioduration()
    audioduration_delaman()
    videoduration()
    videoduration_delaman()
    transcriptions()
    glottorefs()
    aclwiki()
    olachtml()


            
