from collections import namedtuple

Worker = namedtuple("Worker", ["job", "salary", "workplace"])

Mike = Worker("Engineer", 65000, "Taiwan")
print(type[Mike])  # <class 'collections.Worker'>
print(Mike)  # Worker(job='Engineer', salary=65000, workplace='Taiwan')
print(Mike[0])  
print(Mike.job)  # Engineer
