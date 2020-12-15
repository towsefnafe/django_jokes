from django.shortcuts import render
import pyjokes

# Create your views here.
def main(request):
	jokes = []
	for x in range(10):
		jokes.append(pyjokes.get_joke())
	context = {
		'jokes': jokes,
	}
	return render(request, 'index.html', context)