from django.shortcuts import render
from django.views import generic
from .models import Video, OtherPacket, ChapterPacket
# Create your views here.

class Index(generic.ListView):
    model = ChapterPacket
    context_object_name = 'chapter_list'
    template_name = 'index.html'
    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(*args, **kwargs) #keep the base context normal
        context['other_list'] = OtherPacket.objects.all()
        context['home'] = True
        return context


class ChapterView(generic.ListView):

    model = ChapterPacket
    context_object_name = 'chapter_list'
    template_name = 'chapter_view.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ChapterView, self).get_context_data(*args, **kwargs) #keep the base context normal
        context['other_list'] = OtherPacket.objects.all()
        context['packet'] = True
        try:
            context['current_packet'] = ChapterPacket.objects.get(number=self.kwargs['pk'])
            context['video_list'] = Video.objects.filter(chapterPacket__number=self.kwargs['pk']) #add in our second video context
        except:
            context['attempted_num'] = self.kwargs['pk']
        return context
#there is an error where the otherPackets and ChapterPackets video contents are mixed up
class OtherView(generic.ListView):
    model = OtherPacket
    context_object_name = 'other_list'
    template_name = 'chapter_view.html'
    def get_context_data(self, *args, **kwargs):
        context = super(OtherView, self).get_context_data(*args, **kwargs) #keep the base context normal
        context['chapter_list'] = ChapterPacket.objects.all()
        context['packet'] = True
        try:
            context['current_packet'] = OtherPacket.objects.get(id=self.kwargs['pk'])
            context['video_list'] = Video.objects.filter(otherPacket__id=self.kwargs['pk']) #add in our second video context
        except:
            context['attempted_num'] = self.kwargs['pk']
        return context

class AddUserView(generic.ListView):
    model = ChapterPacket
    context_object_name = 'chapter_list'
    template_name = 'add_user_view.html'
    def get_context_data(self, *args, **kwargs):
        context = super(AddUserView, self).get_context_data(*args, **kwargs) #keep the base context normal
        context['other_list'] = OtherPacket.objects.all()
        context['add_users'] = True
        return context
class AddVideoView(generic.ListView):
    model = ChapterPacket
    context_object_name = 'chapter_list'
    template_name = 'add_video_view.html'
    def get_context_data(self, *args, **kwargs):
        context = super(AddVideoView, self).get_context_data(*args, **kwargs) #keep the base context normal
        context['other_list'] = OtherPacket.objects.all()
        context['add_video'] = True
        return context
class AdvancedView(generic.ListView):
    model = ChapterPacket
    context_object_name = 'chapter_list'
    template_name = 'advanced_editing_view.html'
    def get_context_data(self, *args, **kwargs):
        context = super(AdvancedView, self).get_context_data(*args, **kwargs) #keep the base context normal
        context['other_list'] = OtherPacket.objects.all()
        context['advanced'] = True
        return context
