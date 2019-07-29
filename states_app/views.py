from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from states_app import models
from django.views.generic.base import TemplateView
from django.shortcuts import redirect


class Municipality(TemplateView):

    template_name = "../templates/municipality.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request):
        
        instance = models.Municipality.objects.create(name=request.POST.get('name'), code=request.POST.get('code'))
        instance.save()
        return redirect('/states')

    def get_municipality(request):

        template_name = "../templates/municipality_show.html"

        municipality = models.Municipality.objects.all()
        return render(request, template_name,
            {'municipality': municipality})

    def get_edit(request, **kwargs):
        template_name = "../templates/municipality_edit.html"
        municipality = models.Municipality.objects.get(id=kwargs.get('pk'))
        return render(request, template_name,
            {'municipality': municipality})  

    def update(request):

        instance = models.Municipality.objects.get(pk=request.POST.get('municipality_id'))
        instance.name = request.POST.get('name')
        instance.code = request.POST.get('code')
        instance.save()
        return redirect('/states/municipaly/show')

    def delete(request, **kwargs):
        
        instance = models.Municipality.objects.get(pk=kwargs.get('pk'))
        if instance.status:
            instance.status = 0
        else:
            instance.status = 1
        instance.save()
        return redirect('/states/municipaly/show')


class Region(TemplateView):

    template_name = "../templates/state.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['municipality'] = models.Municipality.objects.all()
        return context

    def post(self, request):

        municipality = models.Municipality.objects.filter(pk__in=request.POST.getlist('municipality'))
        instance = models.Region.objects.create(name=request.POST.get('name'), code=request.POST.get('code'))
        for val in municipality:
            instance.municipality_id.add(val.id)
            instance.save()
        return redirect('/states/states')

    def get_edit(request, **kwargs):

        template_name = "../templates/state_edit.html"
        data = models.Region.objects.filter(id=kwargs.get('pk'))
        municipality = models.Municipality.objects.exclude(pk=data[0].municipality_id.all)
        return render(request, template_name,
            {'data': data, 'municipality': municipality})  

    def update(request):

        instance = models.Region.objects.get(pk=request.POST.get('region'))
        municipality = models.Municipality.objects.filter(pk__in=request.POST.getlist('municipality'))
        instance.name = request.POST.get('name')
        instance.code = request.POST.get('code')
        instance.municipality_id.clear()
        for val in municipality:

            instance.municipality_id.add(val.id)
            instance.save()
        return redirect('/states/states/show')

    def delete(request, **kwargs):

        instance = models.Region.objects.get(pk=kwargs.get('pk'))
        if instance.status:
            instance.status = 0
        else:
            instance.status = 1
        instance.save()
        return redirect('/states/states/show')

    def get_region(request):
        template_name = "../templates/state_show.html"

        data = models.Region.objects.all()
        return render(request, template_name,
            {'data': data})