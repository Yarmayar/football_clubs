menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add club', 'url_name': 'add_club'},
        {'title': 'Feedback', 'url_name': 'feedback'},
        {'title': 'Login', 'url_name': 'login'}
        ]


class DataMixin:
    page_title = None
    cntr_selected = None
    extra_context = {}

    def __init__(self):
        if self.page_title:
            self.extra_context['title'] = self.page_title
        if self.cntr_selected is not None:
            self.extra_context['cntr_selected'] = self.cntr_selected
        if 'menu' not in self.extra_context:
            self.extra_context['menu'] = menu

    def get_mixin_context(self, context, **kwargs):
        context['menu'] = menu
        context['cntr_selected'] = None
        context.update(**kwargs)
        return context
