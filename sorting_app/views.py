from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm

def selectionSort(nts):
    print("Just used selection sort")
    nts_len = len(nts)
    for i in range(nts_len - 1):
        min_index = i
        for j in range(i + 1, nts_len):
            if nts[j] < nts[min_index]:  # change to > for descending
                min_index = j
        nts[i], nts[min_index] = nts[min_index], nts[i]
    return nts

def insertionSort(nts):
    print("Just used insertion sort")
    for i in range(1, len(nts)):
        current_num = nts[i]
        p = i - 1
        while p >= 0 and nts[p] > current_num:
            nts[p + 1] = nts[p]
            p -= 1
        nts[p + 1] = current_num
    return nts

def bubbleSort(nts):
    print("Just used bubble sort")
    nts_len = len(nts)
    for i in range(nts_len):
        for p in range(nts_len - i - 1):
            if nts[p] > nts[p + 1]: # change to < for descending
                nts[p], nts[p + 1] = nts[p + 1], nts[p]
    return nts

def home(request):
    form = NameForm()
    return render(request, 'sorting_app/index.html', {'form': form})

def submitted(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            x = request.POST['your_name']
            algorithm_key = request.POST['algorithm']
            # Map algorithm keys to names
            algorithm_names = {
                'bubbleSort': 'Bubble Sort',
                'insertionSort': 'Insertion Sort',
                'selectionSort': 'Selection Sort',}
            # Get the algorithm name from the key
            algorithm_name = algorithm_names.get(algorithm_key, 'Unknown Algorithm')
            y = x.split()
            list_of_integers = list(map(int, y))
            sorted_list = globals()[algorithm_key](list_of_integers)
            return render(request, "sorting_app/processed.html", {'nts': sorted_list, 'algorithm_name': algorithm_name})
    else:
        return HttpResponseRedirect('/')
