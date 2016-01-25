from django import template
from blogsederhana.models import Post, AboutUs
from taggit.models import Tag

register = template.Library()

@register.simple_tag
def about_us():
    about = AboutUs.objects.all()
    output = []
    for aboutus in about:
        output.append('%s' % aboutus.description)
    return ''.join(output)

@register.assignment_tag
def latest_post():
	latest = Post.objects.published()[:4]
	output = {}
	for latest_p in latest:
		output.update({latest_p.id:latest_p.title})
	return output

@register.assignment_tag
def tags():
	latest = Tag.objects.all()[:4]
	return latest