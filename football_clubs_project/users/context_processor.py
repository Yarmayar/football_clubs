from clubs.utils import menu


def get_clubs_context(request):
    return {'mainmenu': menu}