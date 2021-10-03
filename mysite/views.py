from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text','analyze')
    rmpunc = request.POST.get('rmpunc','off')
    fullcap = request.POST.get('fullcap','off')
    newlinerm = request.POST.get('newlinerm', 'off')
    extraspc = request.POST.get('extraspc', 'off')
    charcount = request.POST.get('charcount','off')

    print(djtext)
    print(rmpunc)

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

    if rmpunc == "on":
        punctuations = '''!#$%&'()*+,-./:;<=>?@[\]^_"`{|}~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if fullcap == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitilze all', 'analyzed_text': analyzed}
        djtext = analyzed
    #    return render(request,'analyze.html',params)

    if newlinerm == "on":
        analyzed = ""
        for char in djtext:
            if newlinerm != '\n':
                analyzed = analyzed + char
        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        djtext = analyzed
    #    return render(request,'analyze.html',params)

    if extraspc == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove extra space', 'analyzed_text': analyzed}
        djtext = analyzed
    #    return render(request, 'analyze.html', params)

    if charcount == "on":
        analyzed = ""
        analyzed = analyzed + str(len(djtext.replace(" ", "")))
        params = {'purpose': 'Total Number of characters in text', 'analyzed_text': analyzed}
    #    return render(request, 'analyze.html', params)

    if rmpunc == "on" and fullcap == "on" and charcount == "on" and extraspc == "on" and newlinerm == "on":
        return HttpResponse("Error!, Please select any operation ")
        return render(request, 'analyze.html', params)