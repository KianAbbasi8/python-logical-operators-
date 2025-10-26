"""
check karega kiy ya value data main exist krte ha "/?
but ya number k vaid ni ha
ya do kism k hoty ha ak 
1:in
2: not in 

"""
#suppose we have a bag with copy ball pen 

bag= ["copy","ball","pen"]
print("copy" in bag)
print("rubber" in bag) # false 
print("rubber" not in bag) # same but ture 
print("========================= its seprate  concept of dictionary ")

person={ "name":"ali ","asad":"abbasi"}
print( person["name"])
print(person["asad"])
person ["job"] = "engineering" # add into disctionary 
print(person["job"])