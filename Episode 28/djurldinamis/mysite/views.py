from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Halaman Beranda</h1>")


def thn_arsip(request, tahun):
    headLine = "<h1>Tahun arsip</h1>"
    thnArsip = "Tahun : " + tahun
    return HttpResponse(headLine + thnArsip)


def detail_arsip(request, kategori):
    headLine = "<h1>Detail Arsip</h1>"
    kat = kategori
    return HttpResponse(headLine + kat)


def arsip(request, input):
    headline = "<h1>Nomor arsip</h1>"
    noArsip = input
    return HttpResponse(headline + "Nomor %d " % noArsip)


def tgl_arsip(request, **input):
    print(input)
    headline = "<h1>Penanggalan arsip</h1>"
    tglAr = input['tgl']
    blnAr = input['bln']
    thnAr = input['thn']
    return HttpResponse(headline + "<h3>Tanggal: %d/%d/%d</h3>" % (tglAr, blnAr, thnAr))

# def tgl_arsip(request, tgl, bln, thn):
#     headline = "<h1>Penanggalan arsip</h1>"
#     tglArsip = tgl
#     blnArsip = bln
#     thnArsip = thn
#     return HttpResponse(headline + "<h3>Tanggal: %d / %d / %d</h3>" % (tglArsip, blnArsip, thnArsip))
