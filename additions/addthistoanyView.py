    # microsurveys
    ev = Event.objects.filter(position=request.user.profile.position)
    evcounter = 0
    html = ""
    for e in ev:
        html = e.template.html
        MinAns = e.template.MinAns
        MaxAns = e.template.MaxAns
        delay = e.SecAfter *1000
        html = html.replace("%id%","mic"+str(evcounter))
        html = html.replace("%question%",str(e.question.Title))
        ansHtml=""
        ansemojies = ["😑","🙂","😊","😍"]
        for a in range(MinAns,MaxAns+1):
            ansHtml+='<input  type="radio" id="a'+str(a)+'" name="'+str(e.id)+'" value="'+str(a)+'" onclick="sendFeedback('+str(e.id)+','+str(a)+','+str(evcounter)+')"/><label  for="a'+str(a)+'">'+ansemojies[a]+'</label>'
        html = html.replace("%choices%",ansHtml)
        scr = "<script> span"+str(evcounter)+"=document.getElementsByClassName('micclose')["+str(evcounter)+"]; span"+str(evcounter)+".onclick = function() {document.getElementById('mic"+str(evcounter)+"').style.display = 'none';};setTimeout(function() {document.getElementById('mic"+str(evcounter)+"').style.display='block';}, "+str(delay)+");</script>"
        html+=scr
        evcounter+=1
