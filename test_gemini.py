import google.generativeai as genai
genai.configure(api_key="AIzaSyA_u9hnrvBLvRmFwM6zGURIvkvOpWr1wG0")

for m in genai.list_models():
    print(m.name)
