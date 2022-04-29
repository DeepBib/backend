import ir_datasets
dataset = ir_datasets.load("antique")
i = 0
for doc in dataset.docs_iter():
    print(doc)
    i+=1
    if i>10 : break
