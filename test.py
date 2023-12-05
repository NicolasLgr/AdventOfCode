tab = [1,2,3,4,5,6,10]
# tab.insert(0,4) #[4, 1, 2, 3, 4, 5, 6]
tp_pop = tab.index(1)
tab.pop(tp_pop)
print(tab)
tab_copy = tab.copy()
if tab_copy == tab:
    print("C'est les même")

# tab2 = ''.join(tab)
# print(tab2)

