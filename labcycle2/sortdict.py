dict={"name":"Sandra","age":17,"college":"CET","place":"Sunflower/Shine"}
print("Dictionary:",dict)
val=list(dict.keys())
sorted_list = sorted(val)

sorted_dict = {}
for key in sorted_list:
    sorted_dict[key]=dict[key]

print("Sorted Dict",sorted_dict)





