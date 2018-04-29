from django.shortcuts import render
from django.views import generic
from .models import Video, ChapterPacket, OtherPacket
# Create your views here.
def index(request):
    return render(
        request,
        'packets.html',
    )

class ChapterView(generic.ListView):
    model = ChapterPacket
    context_object_name = 'chapter_list'
    template = 'chapterpacket_list.html' #note I can't seem to change this
    def get_context_data(self, *args, **kwargs):
        context = super(ChapterView, self).get_context_data(*args, **kwargs) #keep the base context normal
        context['video_list'] = Video.objects.filter(chapterPacket__number=self.kwargs['pk']) #add in our second video context
        context['current_chapter'] = ChapterPacket.objects.get(number=self.kwargs['pk'])
        return context
