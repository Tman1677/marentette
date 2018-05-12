from django.db import models

# Create your models here.

class OtherPacket(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name()

class ChapterPacket(models.Model):
    pass
    number = models.IntegerField(unique=True)
    def name(self):
        return "Chapter " + str(self.number)
    def __str__(self):
        return self.name()
    class Meta:
        ordering = ["number"]


class Video(models.Model):
    chapterPacket = models.ForeignKey('ChapterPacket', on_delete=models.SET_NULL,blank=True, null=True)
    otherPacket = models.ForeignKey('OtherPacket', on_delete=models.SET_NULL,blank=True, null=True)
    url = models.URLField(max_length=200)
    firstProblem = models.IntegerField()
    lastProblem = models.IntegerField()
    firstProblemSubProblems = models.CharField(max_length=5,blank=True,help_text="This is for if the problem range starts with a sub like 15a")
    lastProblemSubProblems = models.CharField(max_length=5,blank=True,help_text="This is for if the problem range ends with a sub like 15b")
    def checkPlural(self):
        if self.firstProblem == self.lastProblem and self.firstProblemSubProblems == self.lastProblemSubProblems and len(self.firstProblemSubProblems) < 2:
            return " Problem "
        elif self.firstProblem == self.lastProblem:
            return " Problems "
        else:
            return " Problems "
    def name(self):
        problemString = self.checkPlural()
        try:
            return self.chapterPacket.name() + problemString + self.problems()
        except:
            try:
                return self.otherPacket.name() + problemString + self.problems()
            except:
                return "Error there is no packet assigned to this problem"
    def problems(self):
        if self.firstProblem == self.lastProblem and self.firstProblemSubProblems == self.lastProblemSubProblems:
            return str(self.firstProblem) + str(self.firstProblemSubProblems)
        elif self.firstProblem == self.lastProblem:
            return str(self.firstProblem) + str(self.firstProblemSubProblems) + "-" + str(self.lastProblemSubProblems)
        else:
            return str(self.firstProblem) + str(self.firstProblemSubProblems) + "-" + str(self.lastProblem) + str(self.lastProblemSubProblems)
    class Meta:
        ordering = ["firstProblem"]
    def __str__(self):
        return self.name()
