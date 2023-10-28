from django.shortcuts import render

class TreeMenuViews:

    def BaseMenu(self):
        return render(self, 'base.html')