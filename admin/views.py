from app.models import Post
import settings
from bottle_neck import BaseHandler, WSResponse, route_method


class ModelAdminViewSet(BaseHandler):
    """Admin app Model ViewSet.
    """

    template_dir = ''

    model = None

    @classmethod
    def model_cls(cls):
        return cls.model.__name__.lower()

    @classmethod
    def get_template(cls, prefix=None):
        if prefix is None:
            return '/'.join([cls.template_dir, cls.model_cls()]) + '.html'

        return '{}_{}.html'.format('/'.join([cls.template_dir, cls.model_cls()]), prefix)


class PostAdminViewSet(ModelAdminViewSet):
    """Post model Admin views.
    """

    template_dir = 'admin/pages'

    model = Post

    def get(self):
        post_list = Post.manager.list(limit=None, offset=None, fields=[])
        template = self.get_template()
        return self.render(template, {'posts': post_list})

    def post(self):
        post_image = self.request.files.get('img')

        form_data = {
            'title': self.request.forms.get('title'),
            'body': self.request.forms.get('body')
        }

        if post_image:
            save_path = '{}/static/uploads/post/{}'.format(settings.STATIC_ROOT, post_image.filename)
            post_image.save(save_path)
            form_data['img'] = save_path.replace(settings.STATIC_ROOT, '')

        new_post = Post(**form_data)

        resp = Post.manager.create(new_post, [])

        return WSResponse.ok(data=resp)

    @route_method('GET', extra_part=True)
    def new(self):

        return self.render('admin/pages/post_create.html')
