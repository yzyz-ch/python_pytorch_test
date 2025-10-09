import os
print(os.name)
print(os.getcwd())
print(os.listdir())
os.mkdir('test')
print(os.listdir())
os.rmdir('test')
print(os.listdir())


#py file set env par
str = os.getcwd()
os.environ["TEST_PATH"] = str

print(os.getenv("TEST_PATH"))
